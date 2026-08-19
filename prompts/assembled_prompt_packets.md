## Narrative Summary and Analysis

### System Instruction
You are drafting a simplified PADER-style regulatory safety report. Use only the approved evidence provided for the section. Do not compute new numbers, infer causality, declare safety signals, or invent missing regulatory context. Write in a neutral regulatory tone and clearly identify data limitations. Respect the supplied counting methodology and do not treat reaction occurrences as unique safety cases.

### Approved Evidence
```json
{
  "product": "Bisoprolol",
  "report_type": "PADER-style annual report",
  "reporting_period": {
    "start": "2024-12-27",
    "end": "2025-12-26",
    "date_field": "receivedate"
  },
  "unique_cases": 1024,
  "case_counting_methodology": {
    "unit": "unique_case",
    "deduplication_key": "safetyreportid",
    "description": "Case-level metrics are calculated after deduplicating records using safetyreportid."
  },
  "reaction_counting_methodology": {
    "unit": "reaction_occurrence",
    "source_field": "patient_reaction_reactionmeddrapt",
    "description": "Reaction-frequency metrics count MedDRA Preferred Term occurrences from the source reaction field. These counts are not unique-case counts."
  },
  "serious_cases": 1023,
  "non_serious_cases": 1,
  "serious_percent": "99.9%",
  "alert_cases": 1023,
  "alert_percent": "99.9%",
  "top_reactions": [
    {
      "reaction": "Acute kidney injury",
      "count": 81,
      "percent_of_reactions": "2.2%"
    },
    {
      "reaction": "Drug ineffective",
      "count": 60,
      "percent_of_reactions": "1.6%"
    },
    {
      "reaction": "Hypotension",
      "count": 48,
      "percent_of_reactions": "1.3%"
    },
    {
      "reaction": "Drug interaction",
      "count": 45,
      "percent_of_reactions": "1.2%"
    },
    {
      "reaction": "Dizziness",
      "count": 40,
      "percent_of_reactions": "1.1%"
    },
    {
      "reaction": "Bradycardia",
      "count": 39,
      "percent_of_reactions": "1.1%"
    },
    {
      "reaction": "Dyspnoea",
      "count": 39,
      "percent_of_reactions": "1.1%"
    },
    {
      "reaction": "Fatigue",
      "count": 35,
      "percent_of_reactions": "1.0%"
    },
    {
      "reaction": "Off label use",
      "count": 34,
      "percent_of_reactions": "0.9%"
    },
    {
      "reaction": "Diarrhoea",
      "count": 33,
      "percent_of_reactions": "0.9%"
    },
    {
      "reaction": "Fall",
      "count": 32,
      "percent_of_reactions": "0.9%"
    },
    {
      "reaction": "Condition aggravated",
      "count": 30,
      "percent_of_reactions": "0.8%"
    },
    {
      "reaction": "Asthenia",
      "count": 28,
      "percent_of_reactions": "0.8%"
    },
    {
      "reaction": "Hypokalaemia",
      "count": 27,
      "percent_of_reactions": "0.7%"
    },
    {
      "reaction": "Medication error",
      "count": 27,
      "percent_of_reactions": "0.7%"
    }
  ],
  "highest_month": {
    "month": "2025-07",
    "cases": 109
  },
  "lowest_month": {
    "month": "2024-12",
    "cases": 21
  },
  "known_gaps": [
    "No product label or CCDS was supplied; expectedness is out of scope.",
    "No System Organ Class field was supplied; reaction analysis is limited to MedDRA Preferred Term.",
    "No safety action history was supplied; no labeling, study, or regulatory actions are inferred."
  ]
}
```

### Section Task
Summarize the reporting-period safety data using only the supplied counts, methodologies, and limitations.


---

## Trends and Important Observations

### System Instruction
You are drafting a simplified PADER-style regulatory safety report. Use only the approved evidence provided for the section. Do not compute new numbers, infer causality, declare safety signals, or invent missing regulatory context. Write in a neutral regulatory tone and clearly identify data limitations. Respect the supplied counting methodology and do not treat reaction occurrences as unique safety cases.

### Approved Evidence
```json
{
  "monthly_cases": [
    {
      "month": "2024-12",
      "cases": 21
    },
    {
      "month": "2025-01",
      "cases": 75
    },
    {
      "month": "2025-02",
      "cases": 94
    },
    {
      "month": "2025-03",
      "cases": 83
    },
    {
      "month": "2025-04",
      "cases": 78
    },
    {
      "month": "2025-05",
      "cases": 80
    },
    {
      "month": "2025-06",
      "cases": 84
    },
    {
      "month": "2025-07",
      "cases": 109
    },
    {
      "month": "2025-08",
      "cases": 64
    },
    {
      "month": "2025-09",
      "cases": 76
    },
    {
      "month": "2025-10",
      "cases": 102
    },
    {
      "month": "2025-11",
      "cases": 75
    },
    {
      "month": "2025-12",
      "cases": 83
    }
  ],
  "highest_month": {
    "month": "2025-07",
    "cases": 109
  },
  "lowest_month": {
    "month": "2024-12",
    "cases": 21
  },
  "reaction_counting_methodology": {
    "unit": "reaction_occurrence",
    "source_field": "patient_reaction_reactionmeddrapt",
    "description": "Reaction-frequency metrics count MedDRA Preferred Term occurrences from the source reaction field. These counts are not unique-case counts."
  },
  "top_reactions": [
    {
      "reaction": "Acute kidney injury",
      "count": 81,
      "percent_of_reactions": "2.2%"
    },
    {
      "reaction": "Drug ineffective",
      "count": 60,
      "percent_of_reactions": "1.6%"
    },
    {
      "reaction": "Hypotension",
      "count": 48,
      "percent_of_reactions": "1.3%"
    },
    {
      "reaction": "Drug interaction",
      "count": 45,
      "percent_of_reactions": "1.2%"
    },
    {
      "reaction": "Dizziness",
      "count": 40,
      "percent_of_reactions": "1.1%"
    }
  ]
}
```

### Section Task
Describe numerical trends only. Do not characterize any trend as a confirmed safety signal. Treat reaction counts as reaction occurrences rather than unique-case counts.
