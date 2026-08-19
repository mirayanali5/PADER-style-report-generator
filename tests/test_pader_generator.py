import os
import unittest
from pathlib import Path

import pandas as pd

from src.pader_generator import (
    build_evidence,
    build_prompt_packets,
    render_report,
    validate_report,
)


# ---------------------------------------------------------------------------
# Real assessment dataset
#
# You can optionally override the path with:
#
#   set GENAR_DATA_PATH=C:\path\to\Bisoprolol_icsr_sample_1068rows.xlsx
#
# This makes the test suite easier to run on another machine later.
# ---------------------------------------------------------------------------

REAL_DATA = Path(
    os.environ.get(
        "GENAR_DATA_PATH",
        (
            r"C:\Users\miray\OneDrive\Desktop\assessment"
            r"\Bisoprolol_icsr_sample_1068rows.xlsx"
        ),
    )
)


def sample_df():
    """
    Small synthetic dataset for fast unit tests.

    This lets us test core logic without depending on the full
    assessment spreadsheet for every basic test.
    """
    rows = [
        {
            "safetyreportid": "CASE-1",
            "receivedate": "20250101",
            "occurcountry": "GB",
            "serious": "serious",
            "fulfillexpeditecriteria": "yes",
            "patient_patientonsetage": 70,
            "patient_patientonsetageunit": "year",
            "patient_patientsex": "male",
            "patient_reaction_reactionmeddrapt": "Dizziness",
            "patient_reaction_reactionoutcome": "recovered",
            "primarysource_qualification": "Physician",
            "seriousnessdeath": "no",
            "seriousnesslifethreatening": "no",
            "seriousnesshospitalization": "yes",
            "seriousnessdisabling": "no",
            "seriousnesscongenitalanomali": "no",
            "seriousnessother": "no",
        },
        {
            "safetyreportid": "CASE-2",
            "receivedate": "20250102",
            "occurcountry": "US",
            "serious": "non-serious",
            "fulfillexpeditecriteria": "no",
            "patient_patientonsetage": 40,
            "patient_patientonsetageunit": "year",
            "patient_patientsex": "female",
            "patient_reaction_reactionmeddrapt": "Headache",
            "patient_reaction_reactionoutcome": "recovering",
            "primarysource_qualification": "Consumer",
            "seriousnessdeath": "no",
            "seriousnesslifethreatening": "no",
            "seriousnesshospitalization": "no",
            "seriousnessdisabling": "no",
            "seriousnesscongenitalanomali": "no",
            "seriousnessother": "no",
        },
    ]

    return pd.DataFrame(rows)


class PaderGeneratorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Load the real dataset once for the whole test suite.

        Loading once is faster than reading the Excel file separately
        for every test.
        """
        if not REAL_DATA.exists():
            raise FileNotFoundError(
                "Assessment dataset was not found.\n"
                f"Expected path: {REAL_DATA}\n\n"
                "Either place the dataset there or set GENAR_DATA_PATH "
                "to the correct XLSX file."
            )

        cls.real_df = pd.read_excel(REAL_DATA)

        cls.real_evidence = build_evidence(
            cls.real_df
        )

        cls.real_packets = build_prompt_packets(
            cls.real_evidence
        )

        cls.real_report = render_report(
            cls.real_evidence,
            cls.real_packets,
        )

    # =======================================================================
    # 1. BASIC UNIT TESTS
    # =======================================================================

    def test_case_counts_and_validation(self):
        """
        Basic synthetic-data calculation and report validation.
        """
        evidence = build_evidence(
            sample_df()
        )

        self.assertEqual(
            evidence["unique_cases"],
            2,
        )

        self.assertEqual(
            evidence["serious_cases"],
            1,
        )

        self.assertEqual(
            evidence["non_serious_cases"],
            1,
        )

        self.assertEqual(
            evidence["alert_cases"],
            1,
        )

        self.assertTrue(
            evidence[
                "quality_checks"
            ][
                "case_listing_matches_unique_cases"
            ]
        )

        report = render_report(
            evidence,
            build_prompt_packets(evidence),
        )

        validation = validate_report(
            report,
            evidence,
        )

        self.assertTrue(
            validation["passed"],
            validation,
        )

    def test_missing_required_column_fails_fast(self):
        """
        Missing required columns must stop processing.
        """
        df = sample_df().drop(
            columns=["serious"]
        )

        with self.assertRaises(ValueError):
            build_evidence(df)

    # =======================================================================
    # 2. REAL-DATA REGRESSION TESTS
    # =======================================================================

    def test_real_bisoprolol_dataset_reference_results(self):
        """
        Verify known deterministic case-level results.
        """
        evidence = self.real_evidence

        self.assertEqual(
            evidence["row_count"],
            1068,
        )

        self.assertEqual(
            evidence["unique_cases"],
            1024,
        )

        self.assertEqual(
            evidence["serious_cases"],
            1023,
        )

        self.assertEqual(
            evidence["non_serious_cases"],
            1,
        )

        self.assertEqual(
            evidence["alert_cases"],
            1023,
        )

        self.assertEqual(
            evidence["serious_percent"],
            "99.9%",
        )

        self.assertEqual(
            evidence["alert_percent"],
            "99.9%",
        )

        self.assertEqual(
            evidence[
                "reporting_period"
            ]["start"],
            "2024-12-27",
        )

        self.assertEqual(
            evidence[
                "reporting_period"
            ]["end"],
            "2025-12-26",
        )

    def test_real_dataset_case_level_invariants(self):
        """
        Check relationships that should always remain true.
        """
        evidence = self.real_evidence

        total = evidence["unique_cases"]

        serious = evidence[
            "serious_cases"
        ]

        non_serious = evidence[
            "non_serious_cases"
        ]

        alerts = evidence[
            "alert_cases"
        ]

        # Serious and non-serious populations must
        # account for all unique cases.
        self.assertEqual(
            serious + non_serious,
            total,
        )

        # Alert cases cannot exceed total cases.
        self.assertLessEqual(
            alerts,
            total,
        )

        # Unique cases cannot exceed source rows.
        self.assertLessEqual(
            total,
            evidence["row_count"],
        )

        # Case listing must contain one row per
        # deduplicated safety case.
        self.assertEqual(
            len(
                evidence[
                    "case_listing"
                ]
            ),
            total,
        )

        self.assertTrue(
            evidence[
                "quality_checks"
            ][
                "case_listing_matches_unique_cases"
            ]
        )

        self.assertTrue(
            evidence[
                "quality_checks"
            ][
                "serious_plus_non_serious_matches_total"
            ]
        )

        self.assertTrue(
            evidence[
                "quality_checks"
            ][
                "receivedate_parseable"
            ]
        )

    # =======================================================================
    # 3. REACTION ANALYSIS TESTS
    # =======================================================================

    def test_real_dataset_top_reactions_are_deterministic(self):
        """
        Verify current reaction-occurrence methodology.
        """
        top = self.real_evidence[
            "top_reactions"
        ]

        self.assertGreaterEqual(
            len(top),
            3,
        )

        self.assertEqual(
            top[0]["reaction"],
            "Acute kidney injury",
        )

        self.assertEqual(
            top[0]["count"],
            81,
        )

        self.assertEqual(
            top[1]["reaction"],
            "Drug ineffective",
        )

        self.assertEqual(
            top[1]["count"],
            60,
        )

        self.assertEqual(
            top[2]["reaction"],
            "Hypotension",
        )

        self.assertEqual(
            top[2]["count"],
            48,
        )

    def test_top_reactions_are_sorted_descending(self):
        """
        Reaction frequencies must be ranked highest to lowest.
        """
        counts = [
            item["count"]
            for item
            in self.real_evidence[
                "top_reactions"
            ]
        ]

        self.assertEqual(
            counts,
            sorted(
                counts,
                reverse=True,
            ),
        )

    def test_top_reactions_have_positive_counts(self):
        """
        Reaction-frequency entries cannot have zero or negative counts.
        """
        for item in self.real_evidence[
            "top_reactions"
        ]:
            self.assertGreater(
                item["count"],
                0,
                msg=(
                    "Invalid reaction "
                    f"count: {item}"
                ),
            )

    # =======================================================================
    # 4. METHODOLOGY / DATA-SEMANTICS TESTS
    # =======================================================================

    def test_counting_methodologies_are_explicit(self):
        """
        Evidence must distinguish case counts from reaction counts.
        """
        evidence = self.real_evidence

        case_method = evidence[
            "case_counting_methodology"
        ]

        reaction_method = evidence[
            "reaction_counting_methodology"
        ]

        outcome_method = evidence[
            "outcome_counting_methodology"
        ]

        self.assertEqual(
            case_method["unit"],
            "unique_case",
        )

        self.assertEqual(
            case_method[
                "deduplication_key"
            ],
            "safetyreportid",
        )

        self.assertEqual(
            reaction_method["unit"],
            "reaction_occurrence",
        )

        self.assertEqual(
            reaction_method[
                "source_field"
            ],
            (
                "patient_reaction_"
                "reactionmeddrapt"
            ),
        )

        self.assertEqual(
            outcome_method["unit"],
            (
                "reaction_outcome_"
                "occurrence"
            ),
        )

    def test_report_contains_methodology_section(self):
        """
        The report itself must explain important counting semantics.
        """
        report = self.real_report

        self.assertIn(
            "## Methodology and Data Interpretation",
            report,
        )

        self.assertIn(
            (
                "Case-level metrics are calculated "
                "after deduplicating"
            ),
            report,
        )

        self.assertIn(
            (
                "Reaction counts below represent "
                "Preferred Term occurrences and are "
                "not unique-case counts."
            ),
            report,
        )

    # =======================================================================
    # 5. REPORT GENERATION / GROUNDING TESTS
    # =======================================================================

    def test_real_dataset_report_passes_validation(self):
        """
        The correctly generated report must pass every validator check.
        """
        validation = validate_report(
            self.real_report,
            self.real_evidence,
        )

        self.assertTrue(
            validation["passed"],
            validation,
        )

        self.assertEqual(
            validation[
                "missing_required_evidence"
            ],
            [],
        )

        self.assertEqual(
            validation[
                "missing_required_sections"
            ],
            [],
        )

        self.assertEqual(
            validation[
                "missing_required_claims"
            ],
            [],
        )

        self.assertEqual(
            validation[
                "mismatched_core_claims"
            ],
            [],
        )

        self.assertEqual(
            validation[
                "banned_phrases_found"
            ],
            [],
        )

        self.assertEqual(
            validation[
                "failed_quality_checks"
            ],
            [],
        )

    def test_report_contains_core_case_claims(self):
        """
        Important case-level facts must reach the report.
        """
        evidence = self.real_evidence

        report = self.real_report

        self.assertIn(
            (
                f"{evidence['unique_cases']} "
                "unique safety cases"
            ),
            report,
        )

        self.assertIn(
            (
                f"{evidence['serious_cases']} "
                f"({evidence['serious_percent']}) "
                "were classified as serious"
            ),
            report,
        )

        self.assertIn(
            (
                f"{evidence['alert_cases']} cases "
                f"({evidence['alert_percent']}) met "
                "`fulfillexpeditecriteria`"
            ),
            report,
        )

        self.assertIn(
            "Acute kidney injury",
            report,
        )

    def test_report_contains_evidence_case_counts(self):
        """
        Core evidence values must propagate into the report.
        """
        evidence = self.real_evidence

        report = self.real_report

        self.assertIn(
            str(
                evidence[
                    "unique_cases"
                ]
            ),
            report,
        )

        self.assertIn(
            str(
                evidence[
                    "row_count"
                ]
            ),
            report,
        )

        self.assertIn(
            str(
                evidence[
                    "serious_cases"
                ]
            ),
            report,
        )

        self.assertIn(
            str(
                evidence[
                    "alert_cases"
                ]
            ),
            report,
        )

    def test_report_contains_evidence_reporting_period(self):
        """
        Exact deterministic reporting dates must reach the report.
        """
        evidence = self.real_evidence

        report = self.real_report

        start = evidence[
            "reporting_period"
        ]["start"]

        end = evidence[
            "reporting_period"
        ]["end"]

        self.assertIn(
            start,
            report,
        )

        self.assertIn(
            end,
            report,
        )

        self.assertIn(
            f"{start} to {end}",
            report,
        )

    # =======================================================================
    # 6. UNSUPPORTED-LANGUAGE NEGATIVE TESTS
    # =======================================================================

    def test_validator_rejects_confirmed_safety_signal_claim(self):
        """
        Unsupported signal declarations must be rejected.
        """
        bad_report = (
            self.real_report
            + "\nA confirmed safety signal "
            "was identified.\n"
        )

        validation = validate_report(
            bad_report,
            self.real_evidence,
        )

        self.assertFalse(
            validation["passed"]
        )

        self.assertIn(
            "confirmed safety signal",
            validation[
                "banned_phrases_found"
            ],
        )

    def test_validator_rejects_unsupported_causality_language(self):
        """
        Explicit causal conclusions must be rejected.
        """
        bad_report = (
            self.real_report
            + "\nThe adverse event was "
            "caused by bisoprolol.\n"
        )

        validation = validate_report(
            bad_report,
            self.real_evidence,
        )

        self.assertFalse(
            validation["passed"]
        )

        self.assertIn(
            "caused by bisoprolol",
            validation[
                "banned_phrases_found"
            ],
        )

    def test_validator_rejects_no_safety_concerns_claim(self):
        """
        Unsupported reassurance must be rejected.
        """
        bad_report = (
            self.real_report
            + "\nNo safety concerns were "
            "identified.\n"
        )

        validation = validate_report(
            bad_report,
            self.real_evidence,
        )

        self.assertFalse(
            validation["passed"]
        )

        self.assertIn(
            (
                "no safety concerns "
                "were identified"
            ),
            validation[
                "banned_phrases_found"
            ],
        )

    # =======================================================================
    # 7. CLAIM-LEVEL MISMATCH TESTS
    #
    # These tests are important because they prove the validator catches
    # a number that is VALID somewhere else but WRONG for the claim being
    # made.
    # =======================================================================

    def test_validator_rejects_wrong_serious_case_claim(self):
        """
        Example:

            Correct:
            1023 (99.9%) were classified as serious

            Corrupted:
            1024 (99.9%) were classified as serious

        1024 is a real number in the report, but it belongs to total
        unique cases, not serious cases.
        """
        evidence = self.real_evidence

        correct = (
            f"{evidence['serious_cases']} "
            f"({evidence['serious_percent']}) "
            "were classified as serious"
        )

        wrong = (
            f"{evidence['unique_cases']} "
            f"({evidence['serious_percent']}) "
            "were classified as serious"
        )

        self.assertIn(
            correct,
            self.real_report,
        )

        bad_report = self.real_report.replace(
            correct,
            wrong,
            1,
        )

        validation = validate_report(
            bad_report,
            evidence,
        )

        self.assertFalse(
            validation["passed"]
        )

        mismatches = validation[
            "mismatched_core_claims"
        ]

        self.assertTrue(
            any(
                item["claim_id"]
                == "serious_cases"
                and item["expected"]
                == 1023
                and item["found"]
                == 1024
                for item in mismatches
            ),
            mismatches,
        )

    def test_validator_rejects_wrong_case_volume_table_claim(self):
        """
        A wrong value in the deterministic case-volume table must fail.
        """
        evidence = self.real_evidence

        correct_row = (
            "| Serious cases | "
            f"{evidence['serious_cases']} "
            f"({evidence['serious_percent']}) |"
        )

        wrong_row = (
            "| Serious cases | "
            f"{evidence['unique_cases']} "
            f"({evidence['serious_percent']}) |"
        )

        self.assertIn(
            correct_row,
            self.real_report,
        )

        bad_report = self.real_report.replace(
            correct_row,
            wrong_row,
            1,
        )

        validation = validate_report(
            bad_report,
            evidence,
        )

        self.assertFalse(
            validation["passed"]
        )

        mismatches = validation[
            "mismatched_core_claims"
        ]

        self.assertTrue(
            any(
                item["claim_id"]
                == "table_serious_cases"
                and item["expected"]
                == 1023
                and item["found"]
                == 1024
                for item in mismatches
            ),
            mismatches,
        )

    def test_validator_rejects_wrong_top_reaction_claim(self):
        """
        The narrative must use the exact deterministic reaction result.
        """
        evidence = self.real_evidence

        top = evidence[
            "top_reactions"
        ][0]

        correct = (
            f"{top['reaction']} "
            f"({top['count']} "
            "reaction occurrences)"
        )

        wrong = (
            f"{top['reaction']} "
            f"({top['count'] - 1} "
            "reaction occurrences)"
        )

        self.assertIn(
            correct,
            self.real_report,
        )

        bad_report = self.real_report.replace(
            correct,
            wrong,
            1,
        )

        validation = validate_report(
            bad_report,
            evidence,
        )

        self.assertFalse(
            validation["passed"]
        )

        missing_claim_ids = {
            item["claim_id"]
            for item
            in validation[
                "missing_required_claims"
            ]
        }

        self.assertIn(
            "narrative_top_reaction",
            missing_claim_ids,
        )

    def test_validator_rejects_wrong_highest_month_claim(self):
        """
        A corrupted reporting-trend claim must fail validation.
        """
        evidence = self.real_evidence

        high = evidence[
            "highest_month"
        ]

        correct = (
            f"{high['cases']} cases in "
            f"{high['month']}"
        )

        wrong = (
            f"{high['cases'] + 1} cases in "
            f"{high['month']}"
        )

        self.assertIn(
            correct,
            self.real_report,
        )

        bad_report = self.real_report.replace(
            correct,
            wrong,
            1,
        )

        validation = validate_report(
            bad_report,
            evidence,
        )

        self.assertFalse(
            validation["passed"]
        )

        missing_claim_ids = {
            item["claim_id"]
            for item
            in validation[
                "missing_required_claims"
            ]
        }

        self.assertIn(
            "trend_high",
            missing_claim_ids,
        )


if __name__ == "__main__":
    unittest.main()