import argparse
import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List

import pandas as pd


DEFAULT_DATA_PATH = (
    r"C:\Users\miray\OneDrive\Desktop\assessment"
    r"\Bisoprolol_icsr_sample_1068rows.xlsx"
)


REQUIRED_COLUMNS = [
    "safetyreportid",
    "receivedate",
    "occurcountry",
    "serious",
    "fulfillexpeditecriteria",
    "patient_patientonsetage",
    "patient_patientonsetageunit",
    "patient_patientsex",
    "patient_reaction_reactionmeddrapt",
    "patient_reaction_reactionoutcome",
    "primarysource_qualification",
    "seriousnessdeath",
    "seriousnesslifethreatening",
    "seriousnesshospitalization",
    "seriousnessdisabling",
    "seriousnesscongenitalanomali",
    "seriousnessother",
]


REQUIRED_REPORT_SECTIONS = [
    "## Reporting Period",
    "## Methodology and Data Interpretation",
    "## Narrative Summary and Analysis",
    "## Summary Analysis of Cases",
    "## Reaction / Adverse Event Analysis",
    "## Serious Cases / 15-Day Alerts",
    "## Trends and Important Observations",
    "## History of Actions",
    "## Case Index / Listing",
]

def yes_count(series: pd.Series) -> int:
    """
    Count values equal to 'yes', ignoring capitalization and whitespace.
    """
    return int(
        series.astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .sum()
    )


def pct(numerator: int, denominator: int) -> str:
    """
    Return a percentage formatted to one decimal place.
    """
    if denominator == 0:
        return "0.0%"

    return f"{(numerator / denominator) * 100:.1f}%"


def split_terms(series: pd.Series) -> pd.Series:
    """
    Split comma-separated reaction/outcome terms into individual values.

    Example:
        "Dizziness,Fall"

    becomes:

        Dizziness
        Fall
    """
    return (
        series.fillna("missing")
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .replace("", "missing")
    )


def parse_yyyymmdd(series: pd.Series) -> pd.Series:
    """
    Parse dates stored as YYYYMMDD.
    """
    return pd.to_datetime(
        series.astype(str),
        format="%Y%m%d",
        errors="coerce",
    )


def validate_input_df(df: pd.DataFrame) -> None:
    """
    Validate the minimum structure required by the analysis.
    """
    missing = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            "Input file is missing required columns: "
            + ", ".join(missing)
        )

    if df["safetyreportid"].isna().any():
        raise ValueError(
            "Input file contains rows without safetyreportid."
        )

    received_dates = parse_yyyymmdd(df["receivedate"])

    if received_dates.isna().any():
        raise ValueError(
            "Input file contains receivedate values "
            "that could not be parsed as YYYYMMDD."
        )


def value_counts_table(
    series: pd.Series,
    top_n: int | None = None,
) -> List[Dict[str, Any]]:
    """
    Produce a value/count/percentage table from a column.
    """
    counts = (
        series.fillna("missing")
        .astype(str)
        .str.strip()
        .replace("", "missing")
        .value_counts()
    )

    total = int(counts.sum())

    if top_n:
        counts = counts.head(top_n)

    return [
        {
            "value": str(index),
            "count": int(count),
            "percent": pct(int(count), total),
        }
        for index, count in counts.items()
    ]


def reaction_counts(
    series: pd.Series,
    top_n: int = 15,
) -> List[Dict[str, Any]]:
    """
    Count MedDRA Preferred Term occurrences.

    IMPORTANT:
    This function counts reaction occurrences, not unique safety cases.

    A single case may contain multiple reaction terms.
    """
    terms = split_terms(series)

    counts = terms.value_counts().head(top_n)

    total = int(terms.shape[0])

    return [
        {
            "reaction": str(index),
            "count": int(count),
            "percent_of_reactions": pct(
                int(count),
                total,
            ),
        }
        for index, count in counts.items()
    ]


def md_table(
    rows: Iterable[Dict[str, Any]],
    headers: List[str],
) -> str:
    """
    Convert structured rows into a Markdown table.
    """
    rows = list(rows)

    if not rows:
        return "_No rows available._"

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for row in rows:
        cells = [
            str(row.get(header, ""))
            .replace("|", "\\|")
            .replace("\n", " ")
            for header in headers
        ]

        lines.append(
            "| " + " | ".join(cells) + " |"
        )

    return "\n".join(lines)


def normalize_age_years(
    age: Any,
    unit: Any,
) -> float | None:
    """
    Convert age values to years where possible.
    """
    if pd.isna(age):
        return None

    try:
        value = float(age)
    except (TypeError, ValueError):
        return None

    unit_value = str(unit).strip().lower()

    if unit_value.startswith("month"):
        return value / 12

    if unit_value.startswith("day"):
        return value / 365.25

    if unit_value.startswith("week"):
        return value / 52.1775

    return value


def build_evidence(
    df: pd.DataFrame,
) -> Dict[str, Any]:
    """
    Perform deterministic analysis and return the evidence packet.

    Case-level metrics are calculated after deduplicating on
    safetyreportid.

    Reaction metrics are calculated separately as reaction occurrences.
    """
    validate_input_df(df)

    # ------------------------------------------------------------
    # Case-level population
    # ------------------------------------------------------------

    case_df = (
        df.sort_values(
            ["receivedate", "safetyreportid"]
        )
        .drop_duplicates("safetyreportid")
    )

    received_dates = parse_yyyymmdd(
        case_df["receivedate"]
    )

    report_start = (
        received_dates.min()
        .date()
        .isoformat()
    )

    report_end = (
        received_dates.max()
        .date()
        .isoformat()
    )

    total_cases = int(
        case_df["safetyreportid"].nunique()
    )

    serious_cases = int(
        case_df["serious"]
        .astype(str)
        .str.lower()
        .eq("serious")
        .sum()
    )

    non_serious_cases = (
        total_cases - serious_cases
    )

    alert_cases = yes_count(
        case_df["fulfillexpeditecriteria"]
    )

    # ------------------------------------------------------------
    # Age analysis
    # ------------------------------------------------------------

    age_years = [
        normalize_age_years(age, unit)
        for age, unit in zip(
            case_df["patient_patientonsetage"],
            case_df[
                "patient_patientonsetageunit"
            ],
        )
    ]

    age_series = pd.Series(age_years)

    bins = [
        -0.01,
        17,
        44,
        64,
        74,
        200,
    ]

    labels = [
        "0-17",
        "18-44",
        "45-64",
        "65-74",
        "75+",
    ]

    age_groups = (
        pd.cut(
            age_series,
            bins=bins,
            labels=labels,
        )
        .astype("object")
        .fillna("Missing")
    )

    # ------------------------------------------------------------
    # Monthly reporting trend
    # ------------------------------------------------------------

    monthly = (
        received_dates
        .dt.to_period("M")
        .value_counts()
        .sort_index()
    )

    monthly_cases = [
        {
            "month": str(month),
            "cases": int(count),
        }
        for month, count in monthly.items()
    ]

    # ------------------------------------------------------------
    # Serious / alert populations
    # ------------------------------------------------------------

    serious_ids = set(
        case_df.loc[
            case_df["serious"]
            .astype(str)
            .str.lower()
            .eq("serious"),
            "safetyreportid",
        ]
    )

    alert_ids = set(
        case_df.loc[
            case_df[
                "fulfillexpeditecriteria"
            ]
            .astype(str)
            .str.lower()
            .eq("yes"),
            "safetyreportid",
        ]
    )

    # ------------------------------------------------------------
    # Reaction-level outcomes
    # ------------------------------------------------------------

    outcome_terms = split_terms(
        df[
            "patient_reaction_reactionoutcome"
        ]
    )

    outcome_counts = (
        outcome_terms.value_counts()
    )

    outcome_rows = [
        {
            "outcome": str(index),
            "count": int(count),
            "percent_of_reaction_outcomes": pct(
                int(count),
                int(outcome_counts.sum()),
            ),
        }
        for index, count
        in outcome_counts.items()
    ]

    # ------------------------------------------------------------
    # Seriousness criteria
    # ------------------------------------------------------------

    flags = [
        "seriousnessdeath",
        "seriousnesslifethreatening",
        "seriousnesshospitalization",
        "seriousnessdisabling",
        "seriousnesscongenitalanomali",
        "seriousnessother",
    ]

    seriousness_flags = {
        flag: yes_count(case_df[flag])
        for flag in flags
    }

    # ------------------------------------------------------------
    # Case listing
    # ------------------------------------------------------------

    case_listing_cols = [
        "safetyreportid",
        "receivedate",
        "occurcountry",
        "patient_patientsex",
        "patient_patientonsetage",
        "patient_reaction_reactionmeddrapt",
        "serious",
        "fulfillexpeditecriteria",
        "patient_reaction_reactionoutcome",
    ]

    listing = (
        case_df[
            case_listing_cols
        ]
        .copy()
    )

    listing["receivedate"] = (
        parse_yyyymmdd(
            listing["receivedate"]
        )
        .dt.date
        .astype(str)
    )

    listing = listing.fillna("missing")

    listing = listing.rename(
        columns={
            "safetyreportid": "case_id",
            "receivedate": "received_date",
            "occurcountry": "country",
            "patient_patientsex": "sex",
            "patient_patientonsetage": "age",
            "patient_reaction_reactionmeddrapt": (
                "reaction"
            ),
            "fulfillexpeditecriteria": "alert",
            "patient_reaction_reactionoutcome": (
                "outcome"
            ),
        }
    )

    # ------------------------------------------------------------
    # Reporting-period extrema
    # ------------------------------------------------------------

    top_month = max(
        monthly_cases,
        key=lambda row: row["cases"],
    )

    low_month = min(
        monthly_cases,
        key=lambda row: row["cases"],
    )

    # ------------------------------------------------------------
    # Structured evidence
    # ------------------------------------------------------------

    return {
        "product": "Bisoprolol",

        "report_type": (
            "PADER-style annual report"
        ),

        "data_source": (
            "Bisoprolol_icsr_sample_1068rows.xlsx"
        ),

        "row_count": int(len(df)),

        "unique_cases": total_cases,

        # Explicit methodology information.
        "case_counting_methodology": {
            "unit": "unique_case",
            "deduplication_key": (
                "safetyreportid"
            ),
            "description": (
                "Case-level metrics are calculated "
                "after deduplicating records using "
                "safetyreportid."
            ),
        },

        "reaction_counting_methodology": {
            "unit": "reaction_occurrence",
            "source_field": (
                "patient_reaction_"
                "reactionmeddrapt"
            ),
            "description": (
                "Reaction-frequency metrics count "
                "MedDRA Preferred Term occurrences "
                "from the source reaction field. "
                "These counts are not unique-case "
                "counts."
            ),
        },

        "outcome_counting_methodology": {
            "unit": "reaction_outcome_occurrence",
            "source_field": (
                "patient_reaction_"
                "reactionoutcome"
            ),
            "description": (
                "Outcome metrics are reaction-level "
                "because a safety case can contain "
                "multiple reactions and outcomes."
            ),
        },

        "reporting_period": {
            "start": report_start,
            "end": report_end,
            "date_field": "receivedate",
        },

        "serious_cases": serious_cases,

        "non_serious_cases": (
            non_serious_cases
        ),

        "serious_percent": pct(
            serious_cases,
            total_cases,
        ),

        "alert_cases": alert_cases,

        "alert_percent": pct(
            alert_cases,
            total_cases,
        ),

        "age_groups": [
            {
                "age_group": str(index),
                "count": int(count),
                "percent": pct(
                    int(count),
                    total_cases,
                ),
            }
            for index, count
            in age_groups.value_counts().items()
        ],

        "sex": value_counts_table(
            case_df[
                "patient_patientsex"
            ]
        ),

        "countries": value_counts_table(
            case_df["occurcountry"],
            top_n=15,
        ),

        "reporters": value_counts_table(
            case_df[
                "primarysource_qualification"
            ]
        ),

        "outcomes": outcome_rows,

        "top_reactions": reaction_counts(
            df[
                "patient_reaction_"
                "reactionmeddrapt"
            ],
            top_n=15,
        ),

        "top_serious_reactions": (
            reaction_counts(
                df[
                    df["safetyreportid"].isin(
                        serious_ids
                    )
                ][
                    "patient_reaction_"
                    "reactionmeddrapt"
                ],
                top_n=15,
            )
        ),

        "top_alert_reactions": (
            reaction_counts(
                df[
                    df["safetyreportid"].isin(
                        alert_ids
                    )
                ][
                    "patient_reaction_"
                    "reactionmeddrapt"
                ],
                top_n=15,
            )
        ),

        "monthly_cases": monthly_cases,

        "highest_month": top_month,

        "lowest_month": low_month,

        "seriousness_flags": (
            seriousness_flags
        ),

        "case_listing": (
            listing.to_dict(
                orient="records"
            )
        ),

        "known_gaps": [
            (
                "No product label or CCDS was "
                "supplied; expectedness is out "
                "of scope."
            ),
            (
                "No System Organ Class field was "
                "supplied; reaction analysis is "
                "limited to MedDRA Preferred Term."
            ),
            (
                "No safety action history was "
                "supplied; no labeling, study, "
                "or regulatory actions are inferred."
            ),
        ],

        "quality_checks": {
            "required_columns_present": True,

            "case_level_deduplication_key": (
                "safetyreportid"
            ),

            "case_listing_rows": int(
                len(listing)
            ),

            "case_listing_matches_unique_cases": (
                int(len(listing))
                == total_cases
            ),

            "serious_plus_non_serious_matches_total": (
                serious_cases
                + non_serious_cases
                == total_cases
            ),

            "receivedate_parseable": bool(
                received_dates
                .notna()
                .all()
            ),
        },
    }


@dataclass
class PromptPacket:
    """
    A section-specific context packet that could be sent to an LLM.
    """

    section: str

    system_instruction: str

    evidence: Dict[str, Any]

    task: str

    def to_markdown(self) -> str:
        return (
            f"## {self.section}\n\n"
            f"### System Instruction\n"
            f"{self.system_instruction}\n\n"
            f"### Approved Evidence\n"
            f"```json\n"
            f"{json.dumps(self.evidence, indent=2)}"
            f"\n```\n\n"
            f"### Section Task\n"
            f"{self.task}\n"
        )


SYSTEM_INSTRUCTION = (
    "You are drafting a simplified PADER-style "
    "regulatory safety report. Use only the approved "
    "evidence provided for the section. Do not compute "
    "new numbers, infer causality, declare safety "
    "signals, or invent missing regulatory context. "
    "Write in a neutral regulatory tone and clearly "
    "identify data limitations. Respect the supplied "
    "counting methodology and do not treat reaction "
    "occurrences as unique safety cases."
)


def build_prompt_packets(
    evidence: Dict[str, Any],
) -> List[PromptPacket]:
    """
    Assemble section-specific prompt/context packets.

    Each section receives only the evidence needed for
    that task rather than the complete raw dataset.
    """
    return [
        PromptPacket(
            "Narrative Summary and Analysis",

            SYSTEM_INSTRUCTION,

            {
                k: evidence[k]
                for k in [
                    "product",
                    "report_type",
                    "reporting_period",
                    "unique_cases",
                    "case_counting_methodology",
                    "reaction_counting_methodology",
                    "serious_cases",
                    "non_serious_cases",
                    "serious_percent",
                    "alert_cases",
                    "alert_percent",
                    "top_reactions",
                    "highest_month",
                    "lowest_month",
                    "known_gaps",
                ]
            },

            (
                "Summarize the reporting-period "
                "safety data using only the supplied "
                "counts, methodologies, and "
                "limitations."
            ),
        ),

        PromptPacket(
            "Trends and Important Observations",

            SYSTEM_INSTRUCTION,

            {
                "monthly_cases": (
                    evidence["monthly_cases"]
                ),

                "highest_month": (
                    evidence["highest_month"]
                ),

                "lowest_month": (
                    evidence["lowest_month"]
                ),

                "reaction_counting_methodology": (
                    evidence[
                        "reaction_counting_methodology"
                    ]
                ),

                "top_reactions": (
                    evidence["top_reactions"][:5]
                ),
            },

            (
                "Describe numerical trends only. "
                "Do not characterize any trend as "
                "a confirmed safety signal. Treat "
                "reaction counts as reaction "
                "occurrences rather than unique-case "
                "counts."
            ),
        ),
    ]


def render_report(
    evidence: Dict[str, Any],
    prompt_packets: List[PromptPacket],
    max_listing: int | None = None,
) -> str:
    """
    Render the deterministic Version 0 Markdown report.
    """
    period = evidence[
        "reporting_period"
    ]

    listing = (
        evidence["case_listing"]
        if max_listing is None
        else evidence[
            "case_listing"
        ][:max_listing]
    )

    generated_at = (
        datetime.now(UTC)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )

    if evidence["non_serious_cases"] == 1:
        non_serious_phrase = (
            "1 was classified as non-serious"
        )
    else:
        non_serious_phrase = (
            f"{evidence['non_serious_cases']} "
            "were classified as non-serious"
        )

    lines = [
        "# Bisoprolol PADER-Style Safety Report",
        "",

        f"Generated: {generated_at}",
        "",

        "## Reporting Period",
        "",

        f"- Product: {evidence['product']}",

        (
            f"- Report type: "
            f"{evidence['report_type']}"
        ),

        (
            f"- Reporting period: "
            f"{period['start']} to "
            f"{period['end']}"
        ),

        (
            f"- Date field used for period: "
            f"`{period['date_field']}`"
        ),

        (
            f"- Source file analyzed at runtime: "
            f"`{evidence['data_source']}`"
        ),

        (
            f"- Source rows: "
            f"{evidence['row_count']}; "
            f"unique case count: "
            f"{evidence['unique_cases']}"
        ),

        "",

        "## Methodology and Data Interpretation",
        "",

        (
            "Case-level metrics are calculated after deduplicating "
            "records using `safetyreportid`. Therefore, source-row "
            "counts and unique-case counts are treated as separate "
            "measures."
        ),

        "",

        (
            "Reaction-frequency metrics are calculated from MedDRA "
            "Preferred Term occurrences in "
            "`patient_reaction_reactionmeddrapt`. A single safety "
            "case may contain multiple reaction terms, so reaction "
            "counts are not interpreted as unique-case counts."
        ),

        "",

        (
            "Reaction outcome counts are also reaction-level because "
            "a case may contain multiple reactions and corresponding "
            "outcomes."
        ),

        "",

        (
            "Country analysis uses `occurcountry`. Reporting-period "
            "dates are derived from `receivedate`."
        ),

        "",

        (
            "No System Organ Class field was supplied, so reaction "
            "analysis is limited to MedDRA Preferred Term level. "
            "No product label or CCDS was supplied, so expectedness "
            "is out of scope. No safety-action history was supplied, "
            "so labeling changes, regulatory actions, studies, or "
            "risk-minimization activities are not inferred."
        ),

        "",

        "## Narrative Summary and Analysis",
        "",

        (
            f"During the reporting period, "
            f"{evidence['unique_cases']} unique "
            f"safety cases were identified from "
            f"{evidence['row_count']} source rows. "
            f"Of these, "
            f"{evidence['serious_cases']} "
            f"({evidence['serious_percent']}) were "
            f"classified as serious and "
            f"{non_serious_phrase}."
        ),

        "",

        (
            f"{evidence['alert_cases']} cases "
            f"({evidence['alert_percent']}) met "
            "`fulfillexpeditecriteria` and were "
            "treated as the 15-day alert population "
            "for this exercise. The most frequently "
            "reported reaction Preferred Term was "
            f"{evidence['top_reactions'][0]['reaction']} "
            f"({evidence['top_reactions'][0]['count']} "
            "reaction occurrences). These observations "
            "are descriptive only; the dataset does "
            "not include product exposure, comparator "
            "incidence, label expectedness, or medical "
            "review conclusions."
        ),

        "",

        "## Summary Analysis of Cases",
        "",

        "### Case Volume",
        "",

        md_table(
            [
                {
                    "metric": (
                        "Total unique cases"
                    ),
                    "value": evidence[
                        "unique_cases"
                    ],
                },
                {
                    "metric": "Serious cases",
                    "value": (
                        f"{evidence['serious_cases']} "
                        f"({evidence['serious_percent']})"
                    ),
                },
                {
                    "metric": (
                        "Non-serious cases"
                    ),
                    "value": evidence[
                        "non_serious_cases"
                    ],
                },
                {
                    "metric": (
                        "15-day alert / expedited cases"
                    ),
                    "value": (
                        f"{evidence['alert_cases']} "
                        f"({evidence['alert_percent']})"
                    ),
                },
            ],
            ["metric", "value"],
        ),

        "",

        "### Age Group",
        "",

        md_table(
            evidence["age_groups"],
            [
                "age_group",
                "count",
                "percent",
            ],
        ),

        "",

        "### Sex",
        "",

        md_table(
            evidence["sex"],
            [
                "value",
                "count",
                "percent",
            ],
        ),

        "",

        "### Country of Occurrence",
        "",

        (
            "Country analysis uses "
            "`occurcountry`, not reporter country."
        ),

        "",

        md_table(
            evidence["countries"],
            [
                "value",
                "count",
                "percent",
            ],
        ),

        "",

        "### Reporter Qualification",
        "",

        md_table(
            evidence["reporters"],
            [
                "value",
                "count",
                "percent",
            ],
        ),

        "",

        "### Reaction Outcomes",
        "",

        (
            "Outcome counts are reaction-level "
            "because a case can list multiple "
            "reaction outcomes."
        ),

        "",

        md_table(
            evidence["outcomes"],
            [
                "outcome",
                "count",
                "percent_of_reaction_outcomes",
            ],
        ),

        "",

        "## Reaction / Adverse Event Analysis",
        "",

        (
            "Reaction analysis is performed at "
            "MedDRA Preferred Term level. SOC-level "
            "analysis is not performed because no "
            "SOC field was supplied. Reaction counts "
            "below represent Preferred Term "
            "occurrences and are not unique-case "
            "counts."
        ),

        "",

        "### Most Common Reaction Occurrences",
        "",

        md_table(
            evidence["top_reactions"],
            [
                "reaction",
                "count",
                "percent_of_reactions",
            ],
        ),

        "",

        "### Most Common Serious Reaction Occurrences",
        "",

        md_table(
            evidence[
                "top_serious_reactions"
            ],
            [
                "reaction",
                "count",
                "percent_of_reactions",
            ],
        ),

        "",

        "## Serious Cases / 15-Day Alerts",
        "",

        (
            f"The serious case population consisted "
            f"of {evidence['serious_cases']} cases. "
            f"The expedited/alert population "
            f"consisted of "
            f"{evidence['alert_cases']} cases. "
            "Because these populations are nearly "
            "identical in this dataset, the serious "
            "and alert reaction-occurrence profiles "
            "are also similar."
        ),

        "",

        "### Seriousness Criteria",
        "",

        md_table(
            [
                {
                    "criterion": key,
                    "cases": value,
                }
                for key, value
                in evidence[
                    "seriousness_flags"
                ].items()
            ],
            [
                "criterion",
                "cases",
            ],
        ),

        "",

        "### Most Common Alert Reaction Occurrences",
        "",

        md_table(
            evidence[
                "top_alert_reactions"
            ],
            [
                "reaction",
                "count",
                "percent_of_reactions",
            ],
        ),

        "",

        "## Trends and Important Observations",
        "",

        (
            f"Monthly case volume ranged from "
            f"{evidence['lowest_month']['cases']} "
            f"cases in "
            f"{evidence['lowest_month']['month']} "
            f"to "
            f"{evidence['highest_month']['cases']} "
            f"cases in "
            f"{evidence['highest_month']['month']}. "
            "These are reporting-volume observations "
            "only and are not interpreted as "
            "evidence of incidence or risk."
        ),

        "",

        md_table(
            evidence["monthly_cases"],
            [
                "month",
                "cases",
            ],
        ),

        "",

        "## History of Actions",
        "",

        (
            "No safety-related action history was "
            "supplied with the assessment dataset. "
            "No labeling changes, regulatory "
            "communications, studies, or "
            "risk-minimization actions are inferred."
        ),

        "",

        "## Case Index / Listing",
        "",

        (
            "The listing below provides traceability "
            "from aggregate findings back to "
            "case-level records."
        ),

        "",

        md_table(
            listing,
            [
                "case_id",
                "received_date",
                "country",
                "sex",
                "age",
                "reaction",
                "serious",
                "alert",
                "outcome",
            ],
        ),
    ]

    if (
        max_listing is not None
        and len(
            evidence["case_listing"]
        ) > max_listing
    ):
        lines.extend(
            [
                "",
                (
                    f"_Listing truncated to first "
                    f"{max_listing} cases for "
                    "readability._"
                ),
            ]
        )

    return "\n".join(lines) + "\n"


def validate_report(
    report: str,
    evidence: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Validate report structure, required evidence, unsupported language,
    data-quality checks, and core claim-to-evidence consistency.

    This is still a lightweight engineering validator rather than a
    medical/regulatory approval mechanism. The important improvement is
    that core values are checked in the claims where they belong, rather
    than merely checking whether a number appears somewhere in the report.
    """

    # ------------------------------------------------------------
    # 1. Required evidence values must appear somewhere in the report.
    # ------------------------------------------------------------

    required_numbers = [
        str(evidence["unique_cases"]),
        str(evidence["row_count"]),
        str(evidence["serious_cases"]),
        str(evidence["non_serious_cases"]),
        str(evidence["alert_cases"]),
        evidence["reporting_period"]["start"],
        evidence["reporting_period"]["end"],
    ]

    missing = [
        value
        for value in required_numbers
        if value not in report
    ]

    # ------------------------------------------------------------
    # 2. Required report sections must exist.
    # ------------------------------------------------------------

    missing_sections = [
        section
        for section in REQUIRED_REPORT_SECTIONS
        if section not in report
    ]

    # ------------------------------------------------------------
    # 3. Unsupported / over-claiming language must not appear.
    # ------------------------------------------------------------

    banned_phrases = [
        "no safety concerns were identified",
        "confirmed safety signal",
        "caused by bisoprolol",
        "bisoprolol caused",
        "no new safety concerns",
        "safe and effective",
        "causally related",
        "causal relationship was established",
    ]

    report_lower = report.lower()

    found_banned = [
        phrase
        for phrase in banned_phrases
        if phrase in report_lower
    ]

    # ------------------------------------------------------------
    # 4. Deterministic evidence-quality checks must pass.
    # ------------------------------------------------------------

    failed_quality_checks = [
        name
        for name, passed
        in evidence.get(
            "quality_checks",
            {},
        ).items()
        if (
            isinstance(passed, bool)
            and not passed
        )
    ]

    # ------------------------------------------------------------
    # 5. Claim-level grounding checks.
    #
    # These checks verify that important facts appear in the correct
    # semantic context. This is stronger than merely checking that
    # "1024" or "1023" appears somewhere in the report.
    # ------------------------------------------------------------

    if evidence["non_serious_cases"] == 1:
        non_serious_narrative = (
            "1 was classified as non-serious"
        )
    else:
        non_serious_narrative = (
            f"{evidence['non_serious_cases']} "
            "were classified as non-serious"
        )

    top_reaction = evidence["top_reactions"][0]
    highest_month = evidence["highest_month"]
    lowest_month = evidence["lowest_month"]

    expected_claims = {
        "narrative_unique_cases": (
            f"{evidence['unique_cases']} unique safety cases"
        ),
        "narrative_source_rows": (
            f"{evidence['row_count']} source rows"
        ),
        "narrative_serious_cases": (
            f"{evidence['serious_cases']} "
            f"({evidence['serious_percent']}) were "
            "classified as serious"
        ),
        "narrative_non_serious_cases": (
            non_serious_narrative
        ),
        "narrative_alert_cases": (
            f"{evidence['alert_cases']} cases "
            f"({evidence['alert_percent']}) met "
            "`fulfillexpeditecriteria`"
        ),
        "narrative_top_reaction": (
            f"{top_reaction['reaction']} "
            f"({top_reaction['count']} reaction occurrences)"
        ),
        "case_volume_total": (
            f"| Total unique cases | "
            f"{evidence['unique_cases']} |"
        ),
        "case_volume_serious": (
            f"| Serious cases | "
            f"{evidence['serious_cases']} "
            f"({evidence['serious_percent']}) |"
        ),
        "case_volume_non_serious": (
            f"| Non-serious cases | "
            f"{evidence['non_serious_cases']} |"
        ),
        "case_volume_alert": (
            f"| 15-day alert / expedited cases | "
            f"{evidence['alert_cases']} "
            f"({evidence['alert_percent']}) |"
        ),
        "reporting_period": (
            f"{evidence['reporting_period']['start']} to "
            f"{evidence['reporting_period']['end']}"
        ),
        "trend_low": (
            f"{lowest_month['cases']} cases in "
            f"{lowest_month['month']}"
        ),
        "trend_high": (
            f"{highest_month['cases']} cases in "
            f"{highest_month['month']}"
        ),
        "reaction_methodology": (
            "Reaction counts below represent Preferred Term "
            "occurrences and are not unique-case counts."
        ),
    }

    missing_required_claims = [
        {
            "claim_id": claim_id,
            "expected_text": expected_text,
        }
        for claim_id, expected_text
        in expected_claims.items()
        if expected_text not in report
    ]

    # ------------------------------------------------------------
    # 6. Detect numerically incorrect core claims.
    #
    # This catches cases where a valid number exists elsewhere in the
    # report but is attached to the wrong concept.
    # ------------------------------------------------------------

    mismatched_core_claims: List[Dict[str, Any]] = []

    claim_patterns = [
        {
            "claim_id": "unique_cases",
            "pattern": r"(\d+)\s+unique safety cases",
            "expected": evidence["unique_cases"],
        },
        {
            "claim_id": "serious_cases",
            "pattern": (
                r"(\d+)(?:\s+\([^)]+\))?\s+were "
                r"classified as serious"
            ),
            "expected": evidence["serious_cases"],
        },
        {
            "claim_id": "non_serious_cases",
            "pattern": (
                r"(\d+)\s+(?:was|were)\s+classified "
                r"as non-serious"
            ),
            "expected": evidence["non_serious_cases"],
        },
        {
            "claim_id": "alert_cases",
            "pattern": (
                r"(\d+)\s+cases\s+\([^)]+\)\s+met "
                r"`fulfillexpeditecriteria`"
            ),
            "expected": evidence["alert_cases"],
        },
    ]

    for check in claim_patterns:
        matches = re.findall(
            check["pattern"],
            report,
            flags=re.IGNORECASE,
        )

        for match in matches:
            actual = int(match)

            if actual != check["expected"]:
                mismatched_core_claims.append(
                    {
                        "claim_id": check["claim_id"],
                        "expected": check["expected"],
                        "found": actual,
                    }
                )

    # Exact deterministic table rows give us an additional claim-level
    # check for the core case-volume metrics.
    table_claims = {
        "table_unique_cases": (
            r"\|\s*Total unique cases\s*\|\s*(\d+)\s*\|",
            evidence["unique_cases"],
        ),
        "table_serious_cases": (
            r"\|\s*Serious cases\s*\|\s*(\d+)",
            evidence["serious_cases"],
        ),
        "table_non_serious_cases": (
            r"\|\s*Non-serious cases\s*\|\s*(\d+)\s*\|",
            evidence["non_serious_cases"],
        ),
        "table_alert_cases": (
            r"\|\s*15-day alert / expedited cases\s*\|\s*(\d+)",
            evidence["alert_cases"],
        ),
    }

    for claim_id, (pattern, expected) in table_claims.items():
        match = re.search(
            pattern,
            report,
            flags=re.IGNORECASE,
        )

        if match:
            actual = int(match.group(1))

            if actual != expected:
                mismatched_core_claims.append(
                    {
                        "claim_id": claim_id,
                        "expected": expected,
                        "found": actual,
                    }
                )

    # ------------------------------------------------------------
    # Final result
    # ------------------------------------------------------------

    passed = (
        not missing
        and not missing_sections
        and not found_banned
        and not failed_quality_checks
        and not missing_required_claims
        and not mismatched_core_claims
    )

    return {
        "passed": passed,

        "missing_required_evidence": (
            missing
        ),

        "missing_required_sections": (
            missing_sections
        ),

        "missing_required_claims": (
            missing_required_claims
        ),

        "mismatched_core_claims": (
            mismatched_core_claims
        ),

        "banned_phrases_found": (
            found_banned
        ),

        "failed_quality_checks": (
            failed_quality_checks
        ),
    }


def main() -> None:
    """
    CLI entry point.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Generate a simplified PADER-style "
            "report from ICSR data."
        )
    )

    parser.add_argument(
        "--data",
        default=DEFAULT_DATA_PATH,
        help=(
            "Path to the source CSV or XLSX file."
        ),
    )

    parser.add_argument(
        "--out",
        default="report_output.md",
        help=(
            "Markdown report output path."
        ),
    )

    parser.add_argument(
        "--evidence-out",
        default="analysis_evidence.json",
        help=(
            "Evidence packet output path."
        ),
    )

    parser.add_argument(
        "--prompts-out",
        default=(
            "prompts/"
            "assembled_prompt_packets.md"
        ),
        help=(
            "Prompt packet output path."
        ),
    )

    parser.add_argument(
        "--review-out",
        default="human_review_status.json",
        help=(
            "Human review status output path."
        ),
    )

    parser.add_argument(
        "--approve",
        action="store_true",
        help=(
            "Mark generated report as approved "
            "by human reviewer."
        ),
    )

    parser.add_argument(
        "--max-listing",
        type=int,
        default=None,
        help=(
            "Limit case listing rows in the "
            "Markdown report."
        ),
    )

    args = parser.parse_args()

    data_path = Path(args.data)

    if data_path.suffix.lower() in {
        ".xlsx",
        ".xls",
    }:
        df = pd.read_excel(data_path)
    else:
        df = pd.read_csv(data_path)

    evidence = build_evidence(df)

    packets = build_prompt_packets(
        evidence
    )

    report = render_report(
        evidence,
        packets,
        max_listing=args.max_listing,
    )

    validation = validate_report(
        report,
        evidence,
    )

    out_path = Path(args.out)

    evidence_path = Path(
        args.evidence_out
    )

    prompts_path = Path(
        args.prompts_out
    )

    review_path = Path(
        args.review_out
    )

    for path in [
        out_path,
        evidence_path,
        prompts_path,
        review_path,
    ]:
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    out_path.write_text(
        report,
        encoding="utf-8",
    )

    evidence_path.write_text(
        json.dumps(
            evidence,
            indent=2,
        ),
        encoding="utf-8",
    )

    prompts_path.write_text(
        "\n\n---\n\n".join(
            packet.to_markdown()
            for packet in packets
        ),
        encoding="utf-8",
    )

    review_path.write_text(
        json.dumps(
            {
                "status": (
                    "approved"
                    if args.approve
                    else "pending_review"
                ),

                "review_gate": (
                    "Report is a draft until a "
                    "human reviewer sets --approve "
                    "or updates this status."
                ),

                "validation": validation,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        f"Wrote {out_path}"
    )

    print(
        f"Wrote {evidence_path}"
    )

    print(
        f"Wrote {prompts_path}"
    )

    print(
        f"Wrote {review_path}"
    )

    print(
        "Validation:",
        json.dumps(validation),
    )


if __name__ == "__main__":
    main()