# Bisoprolol PADER-Style Safety Report

Generated: 2026-08-16T21:30:20Z

## Reporting Period

- Product: Bisoprolol
- Report type: PADER-style annual report
- Reporting period: 2024-12-27 to 2025-12-26
- Date field used for period: `receivedate`
- Source file analyzed at runtime: `Bisoprolol_icsr_sample_1068rows.xlsx`
- Source rows: 1068; unique case count: 1024

## Methodology and Data Interpretation

Case-level metrics are calculated after deduplicating records using `safetyreportid`. Therefore, source-row counts and unique-case counts are treated as separate measures.

Reaction-frequency metrics are calculated from MedDRA Preferred Term occurrences in `patient_reaction_reactionmeddrapt`. A single safety case may contain multiple reaction terms, so reaction counts are not interpreted as unique-case counts.

Reaction outcome counts are also reaction-level because a case may contain multiple reactions and corresponding outcomes.

Country analysis uses `occurcountry`. Reporting-period dates are derived from `receivedate`.

No System Organ Class field was supplied, so reaction analysis is limited to MedDRA Preferred Term level. No product label or CCDS was supplied, so expectedness is out of scope. No safety-action history was supplied, so labeling changes, regulatory actions, studies, or risk-minimization activities are not inferred.

## Narrative Summary and Analysis

During the reporting period, 1024 unique safety cases were identified from 1068 source rows. Of these, 1023 (99.9%) were classified as serious and 1 was classified as non-serious.

1023 cases (99.9%) met `fulfillexpeditecriteria` and were treated as the 15-day alert population for this exercise. The most frequently reported reaction Preferred Term was Acute kidney injury (81 reaction occurrences). These observations are descriptive only; the dataset does not include product exposure, comparator incidence, label expectedness, or medical review conclusions.

## Summary Analysis of Cases

### Case Volume

| metric | value |
| --- | --- |
| Total unique cases | 1024 |
| Serious cases | 1023 (99.9%) |
| Non-serious cases | 1 |
| 15-day alert / expedited cases | 1023 (99.9%) |

### Age Group

| age_group | count | percent |
| --- | --- | --- |
| 75+ | 407 | 39.7% |
| 65-74 | 266 | 26.0% |
| 45-64 | 204 | 19.9% |
| Missing | 84 | 8.2% |
| 18-44 | 44 | 4.3% |
| 0-17 | 19 | 1.9% |

### Sex

| value | count | percent |
| --- | --- | --- |
| female | 503 | 49.1% |
| male | 493 | 48.1% |
| missing | 28 | 2.7% |

### Country of Occurrence

Country analysis uses `occurcountry`, not reporter country.

| value | count | percent |
| --- | --- | --- |
| eu | 325 | 31.7% |
| united kingdom | 278 | 27.1% |
| france | 187 | 18.3% |
| canada | 55 | 5.4% |
| italy | 52 | 5.1% |
| germany | 39 | 3.8% |
| spain | 26 | 2.5% |
| poland | 21 | 2.1% |
| portugal | 9 | 0.9% |
| missing | 7 | 0.7% |
| united states | 4 | 0.4% |
| belgium | 4 | 0.4% |
| IE | 3 | 0.3% |
| RO | 2 | 0.2% |
| SA | 2 | 0.2% |

### Reporter Qualification

| value | count | percent |
| --- | --- | --- |
| physician | 493 | 48.1% |
| pharmacist | 255 | 24.9% |
| other health professional | 161 | 15.7% |
| consumer or non-health professional | 115 | 11.2% |

### Reaction Outcomes

Outcome counts are reaction-level because a case can list multiple reaction outcomes.

| outcome | count | percent_of_reaction_outcomes |
| --- | --- | --- |
| recovered/resolved | 1347 | 37.0% |
| unknown | 1135 | 31.2% |
| not recovered/not resolved/ongoing | 569 | 15.6% |
| recovering/resolving | 420 | 11.5% |
| fatal | 137 | 3.8% |
| recovered/resolved with sequelae | 34 | 0.9% |

## Reaction / Adverse Event Analysis

Reaction analysis is performed at MedDRA Preferred Term level. SOC-level analysis is not performed because no SOC field was supplied. Reaction counts below represent Preferred Term occurrences and are not unique-case counts.

### Most Common Reaction Occurrences

| reaction | count | percent_of_reactions |
| --- | --- | --- |
| Acute kidney injury | 81 | 2.2% |
| Drug ineffective | 60 | 1.6% |
| Hypotension | 48 | 1.3% |
| Drug interaction | 45 | 1.2% |
| Dizziness | 40 | 1.1% |
| Bradycardia | 39 | 1.1% |
| Dyspnoea | 39 | 1.1% |
| Fatigue | 35 | 1.0% |
| Off label use | 34 | 0.9% |
| Diarrhoea | 33 | 0.9% |
| Fall | 32 | 0.9% |
| Condition aggravated | 30 | 0.8% |
| Asthenia | 28 | 0.8% |
| Hypokalaemia | 27 | 0.7% |
| Medication error | 27 | 0.7% |

### Most Common Serious Reaction Occurrences

| reaction | count | percent_of_reactions |
| --- | --- | --- |
| Acute kidney injury | 81 | 2.2% |
| Drug ineffective | 59 | 1.6% |
| Hypotension | 48 | 1.3% |
| Drug interaction | 45 | 1.2% |
| Dizziness | 40 | 1.1% |
| Bradycardia | 39 | 1.1% |
| Dyspnoea | 39 | 1.1% |
| Fatigue | 35 | 1.0% |
| Off label use | 34 | 0.9% |
| Diarrhoea | 33 | 0.9% |
| Fall | 32 | 0.9% |
| Condition aggravated | 30 | 0.8% |
| Asthenia | 28 | 0.8% |
| Hypokalaemia | 27 | 0.7% |
| Medication error | 27 | 0.7% |

## Serious Cases / 15-Day Alerts

The serious case population consisted of 1023 cases. The expedited/alert population consisted of 1023 cases. Because these populations are nearly identical in this dataset, the serious and alert reaction-occurrence profiles are also similar.

### Seriousness Criteria

| criterion | cases |
| --- | --- |
| seriousnessdeath | 67 |
| seriousnesslifethreatening | 105 |
| seriousnesshospitalization | 480 |
| seriousnessdisabling | 43 |
| seriousnesscongenitalanomali | 7 |
| seriousnessother | 905 |

### Most Common Alert Reaction Occurrences

| reaction | count | percent_of_reactions |
| --- | --- | --- |
| Acute kidney injury | 81 | 2.2% |
| Drug ineffective | 59 | 1.6% |
| Hypotension | 48 | 1.3% |
| Drug interaction | 45 | 1.2% |
| Dizziness | 40 | 1.1% |
| Bradycardia | 39 | 1.1% |
| Dyspnoea | 39 | 1.1% |
| Fatigue | 35 | 1.0% |
| Off label use | 34 | 0.9% |
| Diarrhoea | 33 | 0.9% |
| Fall | 32 | 0.9% |
| Condition aggravated | 30 | 0.8% |
| Asthenia | 28 | 0.8% |
| Hypokalaemia | 27 | 0.7% |
| Medication error | 27 | 0.7% |

## Trends and Important Observations

Monthly case volume ranged from 21 cases in 2024-12 to 109 cases in 2025-07. These are reporting-volume observations only and are not interpreted as evidence of incidence or risk.

| month | cases |
| --- | --- |
| 2024-12 | 21 |
| 2025-01 | 75 |
| 2025-02 | 94 |
| 2025-03 | 83 |
| 2025-04 | 78 |
| 2025-05 | 80 |
| 2025-06 | 84 |
| 2025-07 | 109 |
| 2025-08 | 64 |
| 2025-09 | 76 |
| 2025-10 | 102 |
| 2025-11 | 75 |
| 2025-12 | 83 |

## History of Actions

No safety-related action history was supplied with the assessment dataset. No labeling changes, regulatory communications, studies, or risk-minimization actions are inferred.

## Case Index / Listing

The listing below provides traceability from aggregate findings back to case-level records.

| case_id | received_date | country | sex | age | reaction | serious | alert | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24780403 | 2024-12-27 | italy | female | 85.0 | Rectal haemorrhage,Deficiency anaemia | serious | yes | unknown,unknown |
| 24780599 | 2024-12-27 | france | female | 69.0 | Coma | serious | yes | recovered/resolved |
| 24780680 | 2024-12-27 | france | male | 85.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 24784771 | 2024-12-28 | united kingdom | female | 86.0 | Muscle spasms | serious | yes | recovered/resolved |
| 24784845 | 2024-12-28 | united kingdom | male | 35.0 | Chest pain,Anxiety,Panic attack | serious | yes | not recovered/not resolved/ongoing,recovering/resolving,recovering/resolving |
| 24784920 | 2024-12-28 | united kingdom | female | 60.0 | Genital burning sensation | serious | yes | not recovered/not resolved/ongoing |
| 24784985 | 2024-12-28 | united kingdom | male | 78.0 | Pemphigoid | serious | yes | unknown |
| 24784989 | 2024-12-28 | united kingdom | male | 59.0 | Drug interaction,Hypersensitivity | serious | yes | unknown,unknown |
| 24787006 | 2024-12-30 | united kingdom | male | 59.0 | Bradycardia,Medication error | serious | yes | not recovered/not resolved/ongoing,unknown |
| 24787240 | 2024-12-30 | united kingdom | male | 45.0 | Muscle twitching,Muscle spasms | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 24787307 | 2024-12-30 | united kingdom | female | 64.0 | Cardiac arrest | serious | yes | recovering/resolving |
| 24787627 | 2024-12-30 | italy | female | 88.0 | Hypoglycaemia,Acidosis | serious | yes | recovering/resolving,recovering/resolving |
| 24788122 | 2024-12-30 | italy | male | 63.0 | Erectile dysfunction,Condition aggravated,Drug ineffective | serious | yes | recovering/resolving,recovering/resolving,unknown |
| 24791327 | 2024-12-31 | france | female | 81.0 | Cardiac failure | serious | yes | not recovered/not resolved/ongoing |
| 24791598 | 2024-12-31 | france | female | 72.0 | Hepatic cytolysis | serious | yes | recovering/resolving |
| 24791831 | 2024-12-31 | united kingdom | missing | missing | Cardiogenic shock | serious | yes | unknown |
| 24792345 | 2024-12-31 | united kingdom | missing | missing | Atrioventricular block | serious | yes | unknown |
| 24792691 | 2024-12-31 | france | male | 77.0 | Pseudoporphyria | serious | yes | recovering/resolving |
| 24792889 | 2024-12-31 | spain | male | 87.0 | Hyponatraemia,Hypervolaemia,Cardiac failure | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 24793431 | 2024-12-31 | france | female | 70.0 | Dyskinesia | serious | yes | not recovered/not resolved/ongoing |
| 24795574 | 2024-12-31 | united kingdom | female | 62.0 | Oxygen saturation decreased,Cardiac failure congestive,Dyspnoea | serious | yes | unknown,recovered/resolved with sequelae,recovered/resolved with sequelae |
| 24795755 | 2025-01-01 | united kingdom | male | 78.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 24796067 | 2025-01-01 | united kingdom | male | 77.0 | Leg amputation | serious | yes | recovered/resolved |
| 24796224 | 2025-01-01 | france | male | 70.0 | Dyskinesia | serious | yes | not recovered/not resolved/ongoing |
| 24798336 | 2025-01-02 | spain | male | 72.0 | Inappropriate antidiuretic hormone secretion,Hyponatraemia,Craniocerebral injury,Haemorrhage intracranial | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24802877 | 2025-01-03 | france | male | 63.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 24803041 | 2025-01-03 | spain | female | missing | Hyponatraemia | serious | yes | recovered/resolved |
| 24803117 | 2025-01-03 | united kingdom | female | 81.0 | Hepatic enzyme increased | serious | yes | unknown |
| 24803128 | 2025-01-03 | spain | female | missing | Haematemesis | serious | yes | recovered/resolved |
| 24803463 | 2025-01-03 | france | male | 52.0 | Hepatic cytolysis | serious | yes | recovered/resolved with sequelae |
| 24806665 | 2025-01-04 | france | male | missing | Foetal growth restriction,Medically induced preterm birth,Maternal exposure during pregnancy | serious | yes | not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved |
| 24806776 | 2025-01-04 | poland | female | 86.0 | Sinus bradycardia,Drug ineffective | serious | yes | unknown,unknown |
| 24806812 | 2025-01-04 | germany | female | missing | Sudden onset of sleep,Sleep disorder,Somnolence,Disturbance in attention,General physical health deterioration,Gamma-glutamyltransferase increased | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown |
| 24806832 | 2025-01-04 | portugal | female | 90.0 | Cardio-respiratory arrest | serious | yes | recovered/resolved |
| 24807274 | 2025-01-05 | portugal | female | 89.0 | BRASH syndrome | serious | yes | recovered/resolved |
| 24809124 | 2025-01-06 | italy | male | 59.0 | Cough,Chest discomfort,Dyspnoea | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 24812900 | 2025-01-07 | france | female | 71.0 | Dilated cardiomyopathy | serious | yes | not recovered/not resolved/ongoing |
| 24812977 | 2025-01-07 | germany | female | 56.0 | Suicide attempt,Intentional overdose | serious | yes | unknown,unknown |
| 24813208 | 2025-01-07 | germany | female | 66.0 | Urostomy complication | serious | yes | recovered/resolved |
| 24813219 | 2025-01-07 | france | male | 78.0 | Pancytopenia | serious | yes | fatal |
| 24813415 | 2025-01-07 | france | male | 91.0 | Cutaneous vasculitis,Vascular purpura | serious | yes | recovering/resolving,recovering/resolving |
| 24815412 | 2025-01-07 | france | female | missing | Bradycardia foetal,Neonatal respiratory distress,Microencephaly,Neonatal behavioural syndrome,Maternal exposure during pregnancy,Foetal growth restriction | serious | yes | recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing,recovered/resolved,not recovered/not resolved/ongoing,recovered/resolved |
| 24816890 | 2025-01-07 | france | male | 67.0 | Hepatic cytolysis | serious | yes | recovering/resolving |
| 24822547 | 2025-01-09 | united kingdom | male | 80.0 | Symptom masked | serious | yes | unknown |
| 24823024 | 2025-01-09 | germany | female | 66.0 | Gastric ulcer | serious | yes | recovered/resolved |
| 24828530 | 2025-01-10 | france | female | 62.0 | Altered state of consciousness,Cognitive disorder,Asthenia,Salivary hypersecretion,Overdose | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24828871 | 2025-01-10 | spain | female | 104.0 | Syncope,Hyponatraemia,Asthenia,Dizziness,Fall | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 24833163 | 2025-01-11 | france | male | 71.0 | Hypoglycaemia | serious | yes | recovered/resolved |
| 24833191 | 2025-01-11 | united kingdom | female | 66.0 | Mobility decreased,Hypertonia,Parkinsonism,Cognitive disorder,Hyperreflexia,Reduced facial expression,Tardive dyskinesia,Tremor,Fall,Reflexes abnormal | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 24833204 | 2025-01-11 | germany | female | 58.0 | Chest pain,Dizziness,Blood pressure systolic decreased,Right ventricular failure,Pleural effusion,Pulmonary congestion,Pneumonia,Pericardial effusion,Renal injury,Cardiorenal syndrome,Lymphadenopathy mediastinal,Pain,Arthralgia,Cystitis escherichia | serious | yes | unknown,recovered/resolved,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 24833425 | 2025-01-12 | italy | male | missing | Pseudomonas infection,Septic shock,Respiratory failure,Pyrexia,Diarrhoea | serious | yes | fatal,fatal,fatal,unknown,unknown |
| 24834918 | 2025-01-13 | germany | male | 56.0 | Cerebral haemorrhage | serious | yes | unknown |
| 24835358 | 2025-01-13 | germany | male | 56.0 | Cerebral haemorrhage | serious | yes | unknown |
| 24843792 | 2025-01-15 | italy | male | 83.0 | Cerebral haemorrhage | serious | yes | fatal |
| 24847678 | 2025-01-16 | united kingdom | female | 89.0 | Confusional state,Fatigue | serious | yes | unknown,unknown |
| 24847955 | 2025-01-16 | france | male | 81.0 | Coma,Confusional state | serious | yes | recovered/resolved,recovered/resolved |
| 24853075 | 2025-01-16 | united kingdom | female | 64.0 | Muscular weakness,Muscle spasms,Paraesthesia,Muscle twitching,Restless legs syndrome | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovering/resolving |
| 24853349 | 2025-01-17 | france | female | 84.0 | Respiratory distress,Lactic acidosis,Atrioventricular block complete,Acute kidney injury,Drug interaction,Overdose | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24855113 | 2025-01-17 | france | female | 83.0 | Acute kidney injury,Hyperkalaemia | serious | yes | recovering/resolving,recovered/resolved |
| 24858691 | 2025-01-18 | united kingdom | male | 92.0 | Joint swelling,Dizziness,Oedema peripheral | serious | yes | unknown,recovered/resolved,recovered/resolved |
| 24858708 | 2025-01-18 | united kingdom | female | 17.0 | Menstruation delayed,Intermenstrual bleeding,Menstruation irregular | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 24858723 | 2025-01-18 | france | female | 74.0 | Ischaemic stroke | serious | yes | recovered/resolved |
| 24858756 | 2025-01-18 | RO | male | 40.0 | Acute kidney injury,Cardiac arrest,Hyperkalaemia,Lactic acidosis,Hypoxia,Hypotension,Altered state of consciousness,Agitation,Respiratory disorder,Pallor,Peripheral coldness,Renal impairment,Campylobacter gastroenteritis,Bradycardia,Dyskinesia,Muscular weakness | serious | yes | unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,unknown,unknown,unknown |
| 24860343 | 2025-01-20 | france | male | missing | Neuropathy peripheral | serious | yes | not recovered/not resolved/ongoing |
| 24860802 | 2025-01-20 | italy | male | 82.0 | Purpura,Face oedema,Dermatitis exfoliative generalised | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 24860813 | 2025-01-20 | canada | female | 53.0 | Drug ineffective | serious | yes | unknown |
| 24861349 | 2025-01-20 | france | female | 53.0 | Cholestasis | serious | yes | not recovered/not resolved/ongoing |
| 24864994 | 2025-01-21 | united kingdom | missing | 86.0 | Orthostatic hypotension | serious | yes | recovered/resolved |
| 24865163 | 2025-01-21 | united kingdom | male | 71.0 | Atrioventricular block complete | serious | yes | unknown |
| 24865641 | 2025-01-21 | france | female | 78.0 | Hypotension,Malaise,Fall | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving |
| 24865801 | 2025-01-21 | united kingdom | female | 89.0 | Chronic obstructive pulmonary disease,Dyspnoea | serious | yes | unknown,recovered/resolved |
| 24866816 | 2025-01-21 | united kingdom | male | 58.0 | Pulmonary embolism | serious | yes | not recovered/not resolved/ongoing |
| 24871166 | 2025-01-22 | united kingdom | male | 66.0 | Hypocalcaemia | serious | yes | recovered/resolved |
| 24871216 | 2025-01-22 | france | male | 66.0 | Atrial fibrillation,Hypokalaemia | serious | yes | recovered/resolved,recovered/resolved |
| 24872990 | 2025-01-22 | belgium | female | 74.0 | Enterococcal infection,Neutropenia,Pancytopenia,Thrombocytopenia,Leukopenia,Anaemia,Normochromic normocytic anaemia,Escherichia infection,Pyrexia | serious | yes | unknown,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,recovered/resolved |
| 24876245 | 2025-01-23 | united kingdom | female | missing | Sleep paralysis,Skin irritation,Alopecia,Fatigue,Nightmare | serious | yes | recovered/resolved,recovering/resolving,recovering/resolving,recovering/resolving,recovered/resolved |
| 24887289 | 2025-01-27 | united kingdom | female | 81.0 | Hyperkalaemia | serious | yes | recovering/resolving |
| 24887406 | 2025-01-27 | france | male | 71.0 | Lung disorder,Thrombocytopenia,Pneumonitis,Bronchopulmonary aspergillosis | serious | yes | fatal,unknown,unknown,unknown |
| 24887784 | 2025-01-27 | france | female | 72.0 | Poisoning deliberate,Altered state of consciousness,Hypoxia,Hypothermia,Bradycardia | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24888230 | 2025-01-27 | france | male | 85.0 | Hypotension | serious | yes | recovering/resolving |
| 24888268 | 2025-01-27 | france | female | 79.0 | Clostridium difficile colitis | serious | yes | recovered/resolved |
| 24888443 | 2025-01-27 | united kingdom | missing | 44.0 | Hypoacusis,Ototoxicity | serious | yes | unknown,unknown |
| 24892198 | 2025-01-28 | france | male | 70.0 | Haematemesis,Gastric ischaemia,Intestinal ischaemia,Oesophageal stenosis | serious | yes | fatal,fatal,fatal,fatal |
| 24893439 | 2025-01-28 | united kingdom | missing | 69.0 | Acute kidney injury | serious | yes | unknown |
| 24898140 | 2025-01-29 | united kingdom | female | 22.0 | Confusional state | serious | yes | not recovered/not resolved/ongoing |
| 24898322 | 2025-01-29 | united kingdom | male | 70.0 | Gouty arthritis,Medication error | serious | yes | not recovered/not resolved/ongoing,unknown |
| 24902753 | 2025-01-30 | germany | male | missing | Small for dates baby,Foetal exposure during pregnancy | serious | yes | recovering/resolving,unknown |
| 24902758 | 2025-01-30 | united kingdom | female | 75.0 | Pharyngeal swelling,Anaphylactic reaction | serious | yes | fatal,not recovered/not resolved/ongoing |
| 24907505 | 2025-01-31 | france | female | 65.0 | Lactic acidosis,Acute kidney injury | serious | yes | fatal,fatal |
| 24907834 | 2025-01-31 | united kingdom | female | 75.0 | Urinary incontinence | serious | yes | recovered/resolved |
| 24908264 | 2025-01-31 | france | female | 96.0 | Acute kidney injury,Hyponatraemia,Atrioventricular block,Drug interaction | serious | yes | recovered/resolved,recovered/resolved,recovering/resolving,recovering/resolving |
| 24908454 | 2025-01-31 | france | female | 75.0 | Gastrointestinal ulcer haemorrhage,Pancreatitis acute,Hepatitis cholestatic,Congenital aplasia | serious | yes | recovered/resolved,recovering/resolving,recovering/resolving,recovered/resolved |
| 24908666 | 2025-01-31 | italy | female | 72.0 | Melaena | serious | yes | recovered/resolved |
| 24908919 | 2025-01-31 | italy | female | 68.0 | Melaena,Rectal haemorrhage,Anaemia | serious | yes | unknown,unknown,recovering/resolving |
| 24909030 | 2025-01-31 | italy | female | 71.0 | Palpitations,Atrial fibrillation,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 24909055 | 2025-01-31 | france | female | 77.0 | Acute kidney injury | serious | yes | recovering/resolving |
| 24913162 | 2025-02-01 | france | male | 50.0 | Subarachnoid haemorrhage | serious | yes | recovered/resolved |
| 24913316 | 2025-02-01 | france | female | 84.0 | Cardiac failure,Acute kidney injury,Drug interaction | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 24913394 | 2025-02-01 | spain | male | 58.0 | Erythema,Swelling,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 24915088 | 2025-02-03 | spain | female | 83.0 | Atrial fibrillation,Acute myocardial infarction,Cellulitis,COVID-19,Neutropenia,Urinary tract infection | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24915494 | 2025-02-03 | united kingdom | female | 7.0 | Sinus arrest | serious | yes | unknown |
| 24919026 | 2025-02-04 | spain | male | 72.0 | Hallucination,Tongue erythema,Dysarthria,Disturbance in attention,Urinary tract infection,Swollen tongue,Disorientation,Cognitive disorder,Somnolence,Emotional disorder | serious | yes | recovered/resolved,unknown,unknown,recovered/resolved,recovered/resolved,unknown,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 24919227 | 2025-02-04 | france | male | 88.0 | Stevens-Johnson syndrome,Asthenia,Somnolence,Decreased appetite | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24920583 | 2025-02-04 | france | female | 56.0 | Electrocardiogram QT prolonged | serious | yes | recovered/resolved |
| 24921420 | 2025-02-04 | france | male | 74.0 | Stevens-Johnson syndrome,Febrile bone marrow aplasia | serious | yes | fatal,fatal |
| 24921475 | 2025-02-04 | france | female | 88.0 | Autoimmune myositis | serious | yes | recovering/resolving |
| 24925730 | 2025-02-04 | france | male | 90.0 | Orthostatic hypotension | serious | yes | recovering/resolving |
| 24927026 | 2025-02-05 | spain | male | 58.0 | Erythema,Swelling,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,unknown |
| 24928144 | 2025-02-05 | united kingdom | female | 94.0 | Ankle fracture | serious | yes | recovering/resolving |
| 24935168 | 2025-02-06 | france | male | 74.0 | Acute kidney injury,Lactic acidosis,Anaemia | serious | yes | recovered/resolved with sequelae,recovered/resolved,recovered/resolved |
| 24935540 | 2025-02-06 | united kingdom | male | 53.0 | Blood glucose abnormal,Hyperglycaemia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 24939529 | 2025-02-06 | united kingdom | female | missing | Blood glucose decreased | serious | yes | recovered/resolved |
| 24939539 | 2025-02-06 | france | male | 67.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 24940500 | 2025-02-07 | united kingdom | female | 93.0 | Femur fracture | serious | yes | recovering/resolving |
| 24940531 | 2025-02-07 | canada | female | 84.0 | Delirium | serious | yes | recovered/resolved |
| 24940601 | 2025-02-07 | canada | male | 71.0 | Upper gastrointestinal haemorrhage,Gastrointestinal injury | serious | yes | fatal,fatal |
| 24940932 | 2025-02-07 | canada | female | 56.0 | Back pain,Cardiac disorder,Carditis,Dental restoration failure,Gastrooesophageal reflux disease | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 24940938 | 2025-02-07 | united kingdom | male | 78.0 | Swelling face,Dizziness,Nausea | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 24944728 | 2025-02-08 | canada | missing | missing | Blindness transient,Epistaxis,Drug effective for unapproved indication,Off label use | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24946649 | 2025-02-10 | italy | female | 15.0 | Kounis syndrome,Stress cardiomyopathy,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,unknown |
| 24947625 | 2025-02-10 | spain | male | 88.0 | Musculoskeletal stiffness,Decreased appetite,Gait disturbance | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 24952766 | 2025-02-11 | canada | female | 59.0 | Alanine aminotransferase increased,Allergic sinusitis,Antinuclear antibody positive,Arthralgia,Arthritis,Arthropathy,Blood iron decreased,Blood uric acid increased,C-reactive protein increased,Condition aggravated,Cyst,Hepatic enzyme increased,Injection site pain,Injection site warmth,Joint effusion,Joint swelling,Nephrolithiasis,Oedema,Osteoarthritis,Pain,Pain in extremity,Psoriasis,Pyrexia,Rash,Renal disorder,Sepsis,Synovial disorder,Synovitis,Tendonitis,Urinary tract infection,Vitamin B12 decreased,Incorrect dose administered,Drug ineffective,Device issue,Wrong technique in device usage process | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 24952834 | 2025-02-11 | france | female | missing | Foetal growth restriction,Normal newborn,Term birth,Maternal exposure during pregnancy | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24953039 | 2025-02-11 | united kingdom | male | 60.0 | Wheezing | serious | yes | recovered/resolved |
| 24959215 | 2025-02-12 | canada | female | 56.0 | Nephrolithiasis,Allergic sinusitis,Alanine aminotransferase increased,Antinuclear antibody positive,Arthralgia,Arthritis,Arthropathy,Blood iron decreased,Blood uric acid increased,C-reactive protein increased,Condition aggravated,Cyst,Hepatic enzyme increased,Injection site pain,Injection site warmth,Joint effusion,Joint swelling,Oedema,Osteoarthritis,Pain,Pain in extremity,Psoriasis,Pyrexia,Rash,Renal disorder,Sepsis,Synovial disorder,Synovitis,Tendonitis,Urinary tract infection,Vitamin B12 decreased,Drug ineffective,Incorrect dose administered | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 24963584 | 2025-02-13 | france | female | 89.0 | Subdural haematoma | serious | yes | recovered/resolved |
| 24963620 | 2025-02-13 | united kingdom | female | 52.0 | Nocturia,Insomnia,Bradycardia,Hypotension,Suicidal ideation,Hallucination,Depression | serious | yes | not recovered/not resolved/ongoing,recovering/resolving,recovered/resolved with sequelae,recovered/resolved with sequelae,recovered/resolved,recovered/resolved,recovered/resolved |
| 24963798 | 2025-02-13 | poland | male | 70.0 | Condition aggravated,Drug intolerance | serious | yes | unknown,unknown |
| 24964204 | 2025-02-13 | france | male | 83.0 | Hypokalaemia,Tonic clonic movements,Hypomagnesaemia,Hypocalcaemia,Hypophosphataemia | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovering/resolving,recovering/resolving |
| 24964501 | 2025-02-13 | france | male | 67.0 | Bicytopenia | serious | yes | recovered/resolved |
| 24964514 | 2025-02-13 | france | male | 91.0 | Angioedema,Drug interaction | serious | yes | recovered/resolved,recovered/resolved |
| 24964515 | 2025-02-13 | france | female | 86.0 | Acute kidney injury,Cholestasis | serious | yes | recovering/resolving,recovering/resolving |
| 24964530 | 2025-02-13 | united kingdom | female | 82.0 | Femoral neck fracture | serious | yes | recovering/resolving |
| 24964537 | 2025-02-13 | united kingdom | female | 76.0 | Palpitations,Dizziness,Abnormal dreams | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 24964648 | 2025-02-13 | united kingdom | female | 71.0 | Face oedema,Skin oedema,Epistaxis,Cough | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown |
| 24965125 | 2025-02-13 | france | female | 83.0 | Fall,Hypotension | serious | yes | recovered/resolved,recovered/resolved |
| 24965157 | 2025-02-13 | france | male | 73.0 | Acute kidney injury,Off label use | serious | yes | recovering/resolving,unknown |
| 24968368 | 2025-02-14 | france | male | 49.0 | Myalgia | serious | yes | recovered/resolved |
| 24968502 | 2025-02-14 | france | female | 71.0 | Eosinophilia | serious | yes | recovering/resolving |
| 24969537 | 2025-02-14 | poland | female | 70.0 | Atrioventricular block complete,Bradycardia,Bradyarrhythmia,Left ventricular end-diastolic pressure increased,Diastolic dysfunction,Atrioventricular block second degree,Supraventricular extrasystoles,Atrioventricular block,Asthenia,Dizziness | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24969561 | 2025-02-14 | united kingdom | female | missing | Myalgia,Chest pain,Bradycardia,Heart rate abnormal,Chest discomfort,Diarrhoea | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown,recovering/resolving |
| 24969964 | 2025-02-14 | poland | male | 66.0 | Thrombocytopenia,Febrile neutropenia | serious | yes | recovered/resolved,recovered/resolved |
| 24973030 | 2025-02-16 | france | female | 79.0 | Fall | serious | yes | recovering/resolving |
| 24973067 | 2025-02-16 | france | male | 78.0 | Hypotension | serious | yes | recovered/resolved |
| 24974307 | 2025-02-17 | united kingdom | female | 57.0 | Cardiac arrest,Medication error | serious | yes | recovered/resolved,unknown |
| 24979403 | 2025-02-18 | germany | male | 69.0 | Cancer pain,Immune-mediated hepatitis | serious | yes | recovered/resolved,not recovered/not resolved/ongoing |
| 24983830 | 2025-02-19 | france | female | 65.0 | Depressed level of consciousness,Tremor,Antipsychotic drug level above therapeutic,Potentiating drug interaction | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24984238 | 2025-02-19 | france | male | 71.0 | Lactic acidosis,Drug level above therapeutic | serious | yes | fatal,fatal |
| 24984747 | 2025-02-19 | france | male | 75.0 | Lactic acidosis,Drug level above therapeutic | serious | yes | recovered/resolved,recovered/resolved |
| 24988517 | 2025-02-20 | united kingdom | female | 86.0 | Pulmonary embolism,Treatment failure | serious | yes | recovered/resolved,unknown |
| 24988692 | 2025-02-20 | IE | female | 75.0 | Liver injury | serious | yes | recovered/resolved |
| 24989004 | 2025-02-20 | france | female | 80.0 | Rash,Face oedema | serious | yes | recovering/resolving,recovering/resolving |
| 24989105 | 2025-02-20 | united kingdom | male | 68.0 | Abdominal distension,Intrusive thoughts,Urinary retention,Back pain,Gastrointestinal pain,Hyperhidrosis,Tremor,Insomnia,Panic attack | serious | yes | not recovered/not resolved/ongoing,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24989291 | 2025-02-20 | france | male | 78.0 | Eosinophilia,Rash | serious | yes | not recovered/not resolved/ongoing,recovering/resolving |
| 24989348 | 2025-02-20 | italy | male | 86.0 | Cerebrovascular accident | serious | yes | unknown |
| 24989439 | 2025-02-20 | france | female | 79.0 | Colitis microscopic | serious | yes | not recovered/not resolved/ongoing |
| 24989454 | 2025-02-20 | france | male | 40.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 24989546 | 2025-02-20 | france | female | 83.0 | Hypercalcaemia | serious | yes | recovering/resolving |
| 24990334 | 2025-02-20 | eu | female | 79.0 | Otitis media acute,Colitis,Diarrhoea | serious | yes | unknown,recovered/resolved,recovered/resolved |
| 24993273 | 2025-02-21 | france | male | 86.0 | Tendon rupture,Labelled drug-drug interaction issue | serious | yes | recovering/resolving,recovered/resolved |
| 24997724 | 2025-02-22 | italy | female | 86.0 | Intestinal haemorrhage,Anaemia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 24997826 | 2025-02-22 | italy | female | 27.0 | Drug abuse,Intentional self-injury,Suicide attempt,Abdominal pain upper | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 24997999 | 2025-02-22 | france | female | 92.0 | Hypokalaemia,Orthostatic hypotension,Potentiating drug interaction | serious | yes | recovering/resolving,recovered/resolved,recovered/resolved |
| 24998163 | 2025-02-22 | italy | male | missing | Syncope,Electrocardiogram QT prolonged,Sinus bradycardia | serious | yes | unknown,unknown,unknown |
| 25006602 | 2025-02-25 | portugal | male | 78.0 | Hypertensive emergency,Renal sympathetic nerve ablation,Chronic kidney disease,Heart failure with preserved ejection fraction,Atrial fibrillation,Hypertension,Headache,Sigmoid-shaped ventricular septum,Cardiac hypertrophy,Aortic dilatation,Blood creatinine increased,Left ventricular hypertrophy,QRS axis abnormal,Diastolic dysfunction,Multiple-drug resistance,Drug resistance,Drug ineffective | serious | yes | not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown,recovering/resolving,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,recovering/resolving,unknown,unknown |
| 25007035 | 2025-02-25 | italy | male | 56.0 | Drug abuse,Intentional self-injury,Vomiting,Aggression,Agitation | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25007823 | 2025-02-25 | france | male | 71.0 | Anti factor V antibody,Shock haemorrhagic,Intra-abdominal haemorrhage,Hypoxia,Hepatic failure,Cell death,Benign recurrent intrahepatic cholestasis,Hypoglycaemia,Coagulopathy,Device related infection | serious | yes | not recovered/not resolved/ongoing,recovering/resolving,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25007836 | 2025-02-25 | france | male | 77.0 | Acquired haemophilia | serious | yes | recovering/resolving |
| 25008577 | 2025-02-25 | italy | male | 77.0 | Cerebral haemorrhage | serious | yes | not recovered/not resolved/ongoing |
| 25008610 | 2025-02-25 | portugal | male | 78.0 | Hypertension,Hypertensive emergency,Renal sympathetic nerve ablation | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown |
| 25008670 | 2025-02-25 | spain | male | 63.0 | Febrile neutropenia | serious | yes | recovered/resolved |
| 25008814 | 2025-02-25 | italy | male | 54.0 | Electrocardiogram QT prolonged,Dilated cardiomyopathy,Condition aggravated,Hypocalcaemia,Trousseau^s sign | serious | yes | recovered/resolved,recovering/resolving,recovering/resolving,recovered/resolved,recovered/resolved |
| 25008822 | 2025-02-25 | france | female | 73.0 | Acute kidney injury | serious | yes | recovering/resolving |
| 25008902 | 2025-02-25 | united kingdom | female | 72.0 | Hypokalaemia,Drug ineffective,Blood albumin decreased | serious | yes | recovered/resolved,unknown,unknown |
| 25012228 | 2025-02-26 | united kingdom | female | 77.0 | Vertigo,Headache,Nausea | serious | yes | recovering/resolving,recovered/resolved,recovered/resolved |
| 25012604 | 2025-02-26 | france | male | missing | Hypoglycaemia neonatal,Foetal growth restriction,Foetal heart rate disorder,Maternal exposure during pregnancy,Caesarean section,Term birth,Low birth weight baby,Normal newborn | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,recovered/resolved |
| 25013092 | 2025-02-26 | united kingdom | male | 87.0 | Ventricular tachycardia,Blood magnesium decreased,Blood potassium decreased | serious | yes | unknown,unknown,unknown |
| 25013240 | 2025-02-26 | france | female | 61.0 | Cholestasis | serious | yes | recovering/resolving |
| 25013867 | 2025-02-26 | germany | female | 71.0 | Generalised tonic-clonic seizure | serious | yes | recovering/resolving |
| 25013886 | 2025-02-26 | italy | male | 76.0 | Subdural haematoma,Subarachnoid haemorrhage,Muscular weakness | serious | yes | recovering/resolving,unknown,unknown |
| 25014028 | 2025-02-26 | united kingdom | male | 59.0 | Drug interaction | serious | yes | unknown |
| 25015944 | 2025-02-27 | united kingdom | female | 57.0 | Blister,Joint swelling,Swelling face | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving |
| 25016073 | 2025-02-27 | france | female | 91.0 | Hypokalaemia | serious | yes | recovered/resolved |
| 25017552 | 2025-02-27 | france | female | 85.0 | Toxic encephalopathy,Hyperammonaemia,White matter lesion,Facial paralysis,Dysarthria,Confusional state,Amnesia,Disorientation,Electroencephalogram abnormal,Electrocardiogram T wave peaked,Electrocardiogram abnormal,Encephalopathy,Cognitive disorder,Memory impairment,Ammonia increased,Neurological symptom,Altered state of consciousness | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25017714 | 2025-02-27 | germany | female | 74.0 | Hypertension,Pruritus,Back pain,Eye irritation,Lymphadenopathy,Scratch,Lymphadenitis,Head injury,Eye pruritus,Abdominal pain upper,Chest pain,Wrong technique in product usage process | serious | yes | unknown,not recovered/not resolved/ongoing,recovered/resolved,unknown,unknown,unknown,unknown,unknown,unknown,recovered/resolved,recovered/resolved,unknown |
| 25017911 | 2025-02-27 | united kingdom | male | 91.0 | Treatment failure | serious | yes | unknown |
| 25023087 | 2025-02-28 | italy | male | 85.0 | Traumatic intracranial haemorrhage | serious | yes | recovering/resolving |
| 25023514 | 2025-02-28 | italy | female | 86.0 | Loss of consciousness,Orthostatic hypotension | serious | yes | recovering/resolving,recovering/resolving |
| 25023607 | 2025-02-28 | france | male | 73.0 | Cardiogenic shock,Wrong patient | serious | yes | recovered/resolved,recovered/resolved |
| 25023658 | 2025-02-28 | france | male | 63.0 | Troponin increased | serious | yes | not recovered/not resolved/ongoing |
| 25026227 | 2025-03-01 | germany | male | 66.0 | Death,Respiratory depression,Polyneuropathy | serious | yes | fatal,unknown,unknown |
| 25028609 | 2025-03-02 | poland | female | 69.0 | Asthenia | serious | yes | fatal |
| 25036112 | 2025-03-04 | united kingdom | female | 19.0 | Drug ineffective | serious | yes | unknown |
| 25039361 | 2025-03-05 | poland | male | 76.0 | Anal haemorrhage | serious | yes | recovering/resolving |
| 25039953 | 2025-03-05 | france | male | 78.0 | Rhabdomyolysis | serious | yes | recovering/resolving |
| 25039963 | 2025-03-05 | france | male | 67.0 | Pemphigus | serious | yes | recovering/resolving |
| 25040847 | 2025-03-05 | france | female | 68.0 | Encephalopathy,Anticholinergic syndrome | serious | yes | recovered/resolved,recovered/resolved |
| 25040902 | 2025-03-05 | spain | male | 44.0 | Asthmatic crisis,Asthma,Condition aggravated | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25041239 | 2025-03-05 | united kingdom | missing | missing | Loss of libido,Erectile dysfunction,Ejaculation delayed | serious | yes | not recovered/not resolved/ongoing,unknown,unknown |
| 25043816 | 2025-03-06 | spain | male | 50.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 25044279 | 2025-03-06 | france | female | 93.0 | Pancreatitis acute,Blood potassium increased,Blood creatinine increased | serious | yes | recovered/resolved,unknown,unknown |
| 25044335 | 2025-03-06 | france | female | 78.0 | Renal failure | serious | yes | recovering/resolving |
| 25048586 | 2025-03-07 | united kingdom | female | 66.0 | Blood pressure systolic increased,Nausea,Vision blurred,Headache,Malaise,Product dispensing error | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown |
| 25049865 | 2025-03-07 | france | male | 80.0 | Acute kidney injury,Clostridium difficile colitis | serious | yes | recovered/resolved,recovered/resolved |
| 25055048 | 2025-03-08 | italy | male | 80.0 | Renal impairment,Weight decreased,Feeding disorder,Decreased appetite,Diarrhoea,Vomiting | serious | yes | unknown,unknown,unknown,recovering/resolving,recovering/resolving,recovered/resolved |
| 25055082 | 2025-03-08 | united kingdom | female | 67.0 | Swollen tongue,Pharyngeal swelling | serious | yes | recovered/resolved,recovered/resolved |
| 25055088 | 2025-03-08 | united kingdom | male | 71.0 | Dry eye | serious | yes | recovered/resolved |
| 25055162 | 2025-03-08 | united kingdom | female | 91.0 | Drug interaction | serious | yes | unknown |
| 25055194 | 2025-03-08 | IE | male | 79.0 | Cellulitis,Catheter site warmth,Catheter site pain,Catheter site swelling,Rectal haemorrhage,Haemoglobin abnormal,C-reactive protein increased,Red blood cell sedimentation rate increased | serious | yes | recovering/resolving,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovering/resolving,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25055215 | 2025-03-08 | united kingdom | female | 91.0 | Drug interaction | serious | yes | unknown |
| 25055227 | 2025-03-08 | united kingdom | female | 20.0 | Photosensitivity reaction,Miliaria | serious | yes | recovered/resolved,recovered/resolved |
| 25062832 | 2025-03-11 | united kingdom | male | 79.0 | Ageusia,Dry mouth,Decreased appetite | serious | yes | unknown,unknown,unknown |
| 25063322 | 2025-03-11 | united kingdom | female | 91.0 | Drug interaction | serious | yes | unknown |
| 25063910 | 2025-03-11 | eu | male | 76.0 | Rhabdomyolysis,Drug interaction,Cardiac failure congestive,Renal impairment,Acute kidney injury,Hypokalaemia,Myopathy toxic | serious | yes | recovered/resolved,recovered/resolved,unknown,unknown,recovering/resolving,recovered/resolved,recovering/resolving |
| 25063935 | 2025-03-11 | germany | male | 83.0 | Dyspnoea,Pulmonary oedema,Hypoacusis,Tendon rupture,Inappropriate schedule of product administration | serious | yes | unknown,recovered/resolved,not recovered/not resolved/ongoing,unknown,not recovered/not resolved/ongoing |
| 25066459 | 2025-03-12 | germany | female | 69.0 | Immune-mediated lung disease,Off label use | serious | yes | recovering/resolving,unknown |
| 25066645 | 2025-03-12 | united kingdom | male | 75.0 | Duodenal ulcer haemorrhage | serious | yes | recovering/resolving |
| 25067040 | 2025-03-12 | united kingdom | female | 84.0 | Hyponatraemia | serious | yes | unknown |
| 25067414 | 2025-03-12 | germany | female | 84.0 | Syncope,Bladder disorder,Exostosis,General physical health deterioration | serious | yes | recovered/resolved,unknown,unknown,unknown |
| 25067529 | 2025-03-12 | germany | male | 51.0 | Cardiac failure acute | serious | yes | unknown |
| 25067889 | 2025-03-12 | poland | female | 62.0 | Neuropathy peripheral,Hyponatraemia,Underdose | serious | yes | not recovered/not resolved/ongoing,unknown,unknown |
| 25077217 | 2025-03-14 | italy | male | 84.0 | Loss of consciousness,Syncope | serious | yes | recovering/resolving,recovering/resolving |
| 25078744 | 2025-03-14 | france | female | 79.0 | Acute kidney injury,Fall | serious | yes | recovering/resolving,recovering/resolving |
| 25080666 | 2025-03-15 | united kingdom | female | 68.0 | Hemiparesis,Paraesthesia | serious | yes | recovered/resolved,recovered/resolved |
| 25080914 | 2025-03-15 | france | male | 80.0 | Atrioventricular block complete,Hyperkalaemia | serious | yes | recovered/resolved,recovered/resolved |
| 25080935 | 2025-03-15 | france | male | 89.0 | Fall,Haematoma | serious | yes | fatal,fatal |
| 25081317 | 2025-03-16 | spain | male | 80.0 | Cutaneous vasculitis,Anuria,Acute pulmonary oedema,Dyspnoea,Hyperkalaemia,Renal failure | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown |
| 25087457 | 2025-03-18 | portugal | male | missing | Drug ineffective,Bradycardia | serious | yes | unknown,unknown |
| 25088417 | 2025-03-18 | france | female | 68.0 | Lactic acidosis,Drug level increased | serious | yes | recovered/resolved,recovered/resolved |
| 25088953 | 2025-03-18 | france | female | 71.0 | Leukopenia,Renal abscess | serious | yes | recovered/resolved,unknown |
| 25093452 | 2025-03-19 | france | female | 78.0 | Vomiting,Tremor,Overdose | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25093622 | 2025-03-19 | france | male | 55.0 | Erectile dysfunction,Sexual dysfunction | serious | yes | recovered/resolved,unknown |
| 25097898 | 2025-03-20 | france | male | 75.0 | Cardiac disorder,Labelled drug-drug interaction issue,Drug interaction | serious | yes | unknown,unknown,unknown |
| 25098189 | 2025-03-20 | italy | male | 76.0 | Acute kidney injury,Confusional state,Dysstasia,Vomiting,Metabolic acidosis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25099895 | 2025-03-20 | france | female | 3.0 | Foetal heart rate disorder,Neonatal respiratory depression,Foetal growth restriction,Maternal exposure during pregnancy,Neonatal gastrointestinal disorder,Premature baby,Neonatal hyperglycaemia,Hospitalisation,Transfusion | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25100240 | 2025-03-20 | france | female | missing | Foetal growth restriction,Neonatal respiratory depression,Maternal exposure during pregnancy,Premature baby,Neonatal gastrointestinal disorder,Hospitalisation | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25103643 | 2025-03-21 | germany | male | 69.0 | Electrocardiogram QT prolonged,Sinus bradycardia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25103650 | 2025-03-21 | germany | female | 69.0 | Delirium,Aggression | serious | yes | recovered/resolved,recovered/resolved |
| 25103779 | 2025-03-21 | france | male | 72.0 | Thrombotic microangiopathy,Bronchial obstruction,Herpes virus infection,Neoplasm progression | serious | yes | unknown,unknown,unknown,unknown |
| 25104878 | 2025-03-21 | united kingdom | female | 69.0 | Swollen tongue,Pruritus | serious | yes | recovered/resolved,recovered/resolved |
| 25108310 | 2025-03-22 | france | male | 55.0 | Extremity necrosis | serious | yes | unknown |
| 25108470 | 2025-03-22 | france | male | 84.0 | Acute kidney injury | serious | yes | recovering/resolving |
| 25108665 | 2025-03-22 | germany | male | 90.0 | Chest pain,Dyspnoea,Hypotension,Bundle branch block right | serious | yes | unknown,unknown,unknown,unknown |
| 25117025 | 2025-03-25 | united kingdom | female | 44.0 | Ototoxicity | serious | yes | unknown |
| 25117268 | 2025-03-25 | france | female | 86.0 | Pulmonary alveolar haemorrhage | serious | yes | not recovered/not resolved/ongoing |
| 25117300 | 2025-03-25 | italy | female | 73.0 | Acute kidney injury | serious | yes | recovering/resolving |
| 25121537 | 2025-03-26 | france | female | 88.0 | Sinus node dysfunction | serious | yes | recovering/resolving |
| 25122724 | 2025-03-26 | united kingdom | female | 65.0 | Dyspnoea,Cough,Wheezing | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25123019 | 2025-03-26 | france | female | missing | Microcephaly,Maternal exposure during pregnancy,Foetal growth restriction,Foetal heart rate disorder,Term birth,Low birth weight baby,Transposition of the great vessels | serious | yes | unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25123074 | 2025-03-26 | united kingdom | female | 79.0 | Loss of consciousness,Abdominal pain upper | serious | yes | recovered/resolved,recovered/resolved |
| 25123104 | 2025-03-26 | france | male | 65.0 | Pemphigoid | serious | yes | not recovered/not resolved/ongoing |
| 25123726 | 2025-03-26 | portugal | male | 76.0 | Acute kidney injury,Atrial fibrillation,Cardiac failure,Respiratory failure,Haemorrhoidal haemorrhage,Hyperglycaemia,Rectal haemorrhage,Neuropathy peripheral,Neutropenia,Dry skin,Skin exfoliation,Erythema,Decreased appetite,Weight decreased | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25128211 | 2025-03-27 | united kingdom | female | 79.0 | Melaena | serious | yes | recovered/resolved |
| 25128264 | 2025-03-27 | united kingdom | female | 79.0 | Treatment failure | serious | yes | recovering/resolving |
| 25132371 | 2025-03-28 | germany | female | 74.0 | Hypercapnic coma,Acute kidney injury,Drug abuse,Neurological decompensation,Respiratory acidosis,Toxicity to various agents,Drug interaction | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25132695 | 2025-03-28 | france | female | 80.0 | Thrombocytopenia,Haematoma muscle,Condition aggravated,Anaemia | serious | yes | recovered/resolved,recovering/resolving,recovering/resolving,recovered/resolved |
| 25133337 | 2025-03-28 | france | male | 78.0 | Cardiac failure acute,Sinus bradycardia | serious | yes | recovered/resolved,recovered/resolved |
| 25134409 | 2025-03-28 | italy | female | 89.0 | Transient ischaemic attack,Dysarthria | serious | yes | recovering/resolving,recovering/resolving |
| 25134451 | 2025-03-28 | france | female | 73.0 | Pemphigoid | serious | yes | not recovered/not resolved/ongoing |
| 25134452 | 2025-03-28 | italy | male | 55.0 | Infusion related reaction | serious | yes | recovered/resolved |
| 25134771 | 2025-03-28 | united kingdom | female | 75.0 | Muscle spasms | serious | yes | recovered/resolved |
| 25134870 | 2025-03-28 | france | male | 71.0 | Hepatic cytolysis,Hepatitis,Epistaxis,Paraesthesia oral,Dry mouth,Weight decreased,Decreased appetite | serious | yes | recovering/resolving,recovered/resolved,not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown |
| 25137541 | 2025-03-29 | france | male | 72.0 | Cardiogenic shock | serious | yes | recovering/resolving |
| 25137551 | 2025-03-29 | france | female | 78.0 | Thrombocytopenia,Autoimmune haemolytic anaemia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25137573 | 2025-03-29 | france | female | 91.0 | Immune thrombocytopenia | serious | yes | not recovered/not resolved/ongoing |
| 25137580 | 2025-03-29 | france | female | 57.0 | Sinus tachycardia,Syncope,Somnolence,Malaise | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25137726 | 2025-03-29 | italy | male | 76.0 | Sepsis,Nephrotic syndrome | serious | yes | recovered/resolved,recovered/resolved |
| 25137754 | 2025-03-29 | france | male | 83.0 | Endocarditis staphylococcal | serious | yes | fatal |
| 25137777 | 2025-03-29 | italy | male | 69.0 | Clostridium difficile colitis | serious | yes | recovered/resolved |
| 25137866 | 2025-03-29 | italy | male | 57.0 | Renal failure,Drug reaction with eosinophilia and systemic symptoms,Rash morbilliform,Periorbital oedema,Lymphadenopathy,Eosinophilia | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25139255 | 2025-03-31 | france | female | 93.0 | Confusional state,Hypotension | serious | yes | recovered/resolved,recovered/resolved |
| 25139308 | 2025-03-31 | united kingdom | female | 81.0 | Joint swelling | serious | yes | recovered/resolved |
| 25139563 | 2025-03-31 | united kingdom | male | 76.0 | Subdural haematoma | serious | yes | recovered/resolved |
| 25143695 | 2025-04-01 | italy | male | 86.0 | Lactic acidosis | serious | yes | recovered/resolved |
| 25143922 | 2025-04-01 | united kingdom | male | 76.0 | Cardiac amyloidosis,Loss of consciousness,Orthostatic hypotension,Dyspnoea,Chest pain,Hypokalaemia,Circulatory collapse | serious | yes | unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25143930 | 2025-04-01 | united kingdom | male | 79.0 | Hepatitis | serious | yes | recovered/resolved |
| 25144761 | 2025-04-01 | france | male | 29.0 | Lactic acidosis,Shock,Acute kidney injury,Poisoning deliberate | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25144939 | 2025-04-01 | belgium | female | 65.0 | Pyrexia | serious | yes | recovered/resolved |
| 25148867 | 2025-04-02 | germany | male | 74.0 | Immune-mediated lung disease,Dysphagia,Hypotension | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25149267 | 2025-04-02 | italy | female | 88.0 | Hyperkalaemia | serious | yes | recovered/resolved |
| 25149308 | 2025-04-02 | france | male | 63.0 | Neuroleptic malignant syndrome,Drug interaction | serious | yes | recovered/resolved,recovered/resolved |
| 25153169 | 2025-04-03 | france | female | missing | Foetal growth restriction,Maternal exposure during pregnancy,Term birth,Normal newborn | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25154394 | 2025-04-03 | united kingdom | female | 80.0 | Haemorrhage intracranial,Thrombocytopenia | serious | yes | not recovered/not resolved/ongoing,recovered/resolved |
| 25159299 | 2025-04-04 | germany | male | 76.0 | Syncope,Fall,Gait disturbance,Dizziness | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25163535 | 2025-04-05 | poland | male | 55.0 | Renal impairment,Gastrointestinal haemorrhage | serious | yes | recovering/resolving,recovering/resolving |
| 25163868 | 2025-04-05 | germany | female | missing | Hyperthyroidism,Blood thyroid stimulating hormone abnormal,Muscle spasms,Oedema peripheral | serious | yes | unknown,not recovered/not resolved/ongoing,unknown,unknown |
| 25164028 | 2025-04-05 | france | female | missing | Fournier^s gangrene,Septic shock | serious | yes | fatal,fatal |
| 25164055 | 2025-04-05 | france | male | 71.0 | Pancreatitis acute | serious | yes | recovered/resolved |
| 25165561 | 2025-04-07 | france | female | 78.0 | Agranulocytosis,Cholestatic liver injury | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25166634 | 2025-04-07 | france | female | 89.0 | Hypokalaemia | serious | yes | recovered/resolved |
| 25166741 | 2025-04-07 | france | male | 76.0 | Gynaecomastia | serious | yes | recovered/resolved |
| 25166932 | 2025-04-07 | united kingdom | female | 58.0 | Migraine | serious | yes | not recovered/not resolved/ongoing |
| 25170438 | 2025-04-08 | FI | female | 74.0 | Seizure,Arthralgia,Discomfort,Skin burning sensation,Joint effusion,Dyspnoea,Anxiety,Tremor,Nausea,Paraesthesia,Myalgia,Chills,Hypoaesthesia,Blood pressure increased,Reaction to excipient,Exposure via partner,Adverse drug reaction,Exposure via inhalation,Accidental exposure to product,Product complaint,Product formulation issue,Product substitution issue | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown,not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown,unknown |
| 25170910 | 2025-04-08 | france | male | 62.0 | Hypotension | serious | yes | recovered/resolved |
| 25171388 | 2025-04-08 | france | male | missing | Maternal exposure during pregnancy,Premature baby,Low birth weight baby | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25171693 | 2025-04-08 | france | male | 85.0 | Acute kidney injury,Sinus bradycardia,Hypotension,Disturbance in attention,Wrong patient received product | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25172780 | 2025-04-08 | france | male | 98.0 | Rash morbilliform | serious | yes | recovering/resolving |
| 25176112 | 2025-04-09 | france | male | 66.0 | Lip oedema | serious | yes | recovered/resolved |
| 25176655 | 2025-04-09 | united kingdom | female | 77.0 | Atrial fibrillation,Heart rate increased | serious | yes | recovered/resolved,recovered/resolved |
| 25177139 | 2025-04-09 | france | male | 79.0 | Acute kidney injury,Dysphagia,General physical health deterioration | serious | yes | fatal,fatal,fatal |
| 25181463 | 2025-04-10 | united kingdom | female | 76.0 | Chest pain,Condition aggravated,Orthostatic hypotension | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25181557 | 2025-04-10 | france | female | 82.0 | Acute kidney injury,Hypotension,Atrioventricular block | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving |
| 25181724 | 2025-04-10 | germany | female | 61.0 | Ileus,Abdominal pain | serious | yes | recovering/resolving,recovering/resolving |
| 25182125 | 2025-04-10 | italy | female | 89.0 | Syncope | serious | yes | recovered/resolved |
| 25187835 | 2025-04-11 | germany | male | 81.0 | Suicide attempt,Loss of consciousness,Suicidal ideation,Hallucination, auditory,Cerebral infarction,Drug interaction | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown |
| 25191358 | 2025-04-11 | france | male | 85.0 | Tubulointerstitial nephritis | serious | yes | not recovered/not resolved/ongoing |
| 25191362 | 2025-04-11 | spain | male | 86.0 | Chronic kidney disease,Lactic acidosis | serious | yes | recovered/resolved,recovered/resolved |
| 25191366 | 2025-04-11 | france | male | 51.0 | Intestinal haematoma,Renal haematoma,Pyelonephritis acute,Haematuria | serious | yes | recovering/resolving,recovering/resolving,recovered/resolved,recovered/resolved |
| 25191370 | 2025-04-11 | france | female | 73.0 | Amaurosis | serious | yes | recovered/resolved |
| 25191382 | 2025-04-11 | france | male | 78.0 | Acute kidney injury | serious | yes | not recovered/not resolved/ongoing |
| 25197782 | 2025-04-15 | united kingdom | female | 79.0 | Vertigo,Visual impairment,Diplopia,Drug monitoring procedure not performed,Aura,Balance disorder,Gait disturbance,Dizziness | serious | yes | not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25198763 | 2025-04-15 | france | male | 74.0 | Respiratory syncytial virus infection,Drug interaction,Overdose | serious | yes | unknown,unknown,unknown |
| 25202021 | 2025-04-16 | france | male | 75.0 | Bone marrow failure | serious | yes | recovered/resolved |
| 25202610 | 2025-04-16 | france | female | 70.0 | Erythema | serious | yes | recovering/resolving |
| 25206298 | 2025-04-17 | germany | female | 48.0 | Therapeutic response changed | serious | yes | recovered/resolved |
| 25206340 | 2025-04-17 | france | male | 67.0 | Pancytopenia,Acute kidney injury | serious | yes | recovered/resolved,recovered/resolved |
| 25206481 | 2025-04-17 | france | male | 77.0 | Linear IgA disease | serious | yes | recovered/resolved |
| 25206508 | 2025-04-17 | eu | female | 75.0 | Myasthenia gravis,Faeces discoloured,Respiratory failure,Death,Toxicity to various agents | serious | yes | fatal,fatal,fatal,fatal,fatal |
| 25211549 | 2025-04-18 | united kingdom | male | 72.0 | Liver injury | serious | yes | not recovered/not resolved/ongoing |
| 25213392 | 2025-04-18 | united kingdom | male | 83.0 | Wheezing,Dyspnoea,Fatigue,Malaise | serious | yes | recovered/resolved,unknown,unknown,unknown |
| 25216918 | 2025-04-19 | france | male | 66.0 | Skin erosion | serious | yes | not recovered/not resolved/ongoing |
| 25217031 | 2025-04-19 | eu | male | 79.0 | IVth nerve paralysis,IgA nephropathy,Drug ineffective,COVID-19 | serious | yes | unknown,unknown,unknown,unknown |
| 25217359 | 2025-04-20 | france | female | 86.0 | Interstitial lung disease | serious | yes | not recovered/not resolved/ongoing |
| 25218216 | 2025-04-21 | united kingdom | missing | missing | Dry mouth | serious | yes | not recovered/not resolved/ongoing |
| 25223687 | 2025-04-22 | italy | female | 39.0 | Oedema peripheral,Drug ineffective,Drug effective for unapproved indication | serious | yes | not recovered/not resolved/ongoing,unknown,recovered/resolved |
| 25224052 | 2025-04-22 | italy | female | 44.0 | Hyperthyroidism,Neutropenia,Heart rate increased,Sinus tachycardia,Therapeutic response decreased | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 25229228 | 2025-04-23 | united kingdom | missing | 69.0 | Swelling,Rash,Back pain | serious | yes | recovered/resolved,recovered/resolved,recovering/resolving |
| 25229565 | 2025-04-23 | france | female | missing | Hypoglycaemia neonatal,Neonatal respiratory distress,Maternal exposure during pregnancy | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25229672 | 2025-04-23 | germany | male | 58.0 | Hypotension,Respiratory failure,Bradycardia,Intentional product misuse | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25229871 | 2025-04-23 | france | female | 81.0 | Renal tubular disorder | serious | yes | not recovered/not resolved/ongoing |
| 25233240 | 2025-04-24 | france | female | 82.0 | Thrombocytopenia | serious | yes | unknown |
| 25234657 | 2025-04-24 | france | female | 81.0 | Shock haemorrhagic,Retroperitoneal haematoma,Blood creatinine increased,Abdominal rigidity,Abdominal distension,Activated partial thromboplastin time shortened,Haemoglobin decreased,International normalised ratio increased,Overdose | serious | yes | unknown,not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown,unknown,recovered/resolved,recovered/resolved |
| 25238700 | 2025-04-25 | germany | male | 66.0 | Hypothyroidism | serious | yes | not recovered/not resolved/ongoing |
| 25239144 | 2025-04-25 | united kingdom | female | 75.0 | Chronic obstructive pulmonary disease,Alanine aminotransferase increased | serious | yes | unknown,unknown |
| 25239246 | 2025-04-25 | united kingdom | male | 85.0 | Cerebrovascular accident,Cerebral haemorrhage | serious | yes | fatal,not recovered/not resolved/ongoing |
| 25239411 | 2025-04-25 | germany | male | 66.0 | Hypothyroidism,Neutropenia,Fatigue,Abdominal pain,Diarrhoea,Nausea,Rash,Intentional product use issue | serious | yes | recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25241950 | 2025-04-26 | IE | female | 33.0 | Sleep disorder,Hypnopompic hallucination | serious | yes | recovering/resolving,recovered/resolved |
| 25242442 | 2025-04-27 | spain | female | 73.0 | Hepatotoxicity,Acute kidney injury,Rhabdomyolysis,Drug interaction,Myopathy | serious | yes | unknown,recovering/resolving,recovering/resolving,unknown,unknown |
| 25242443 | 2025-04-27 | spain | female | 39.0 | Therapy partial responder | serious | yes | unknown |
| 25243162 | 2025-04-28 | italy | male | 77.0 | Syncope | serious | yes | recovering/resolving |
| 25243204 | 2025-04-28 | united kingdom | female | missing | Arthritis reactive,Rash | serious | yes | recovered/resolved,recovered/resolved |
| 25243486 | 2025-04-28 | poland | female | 73.0 | Ventricular tachycardia,Torsade de pointes,Long QT syndrome,Electrocardiogram QT prolonged,Hypokalaemia,Syncope,Dizziness,Asthenia,Sinus rhythm,Ventricular arrhythmia | serious | yes | recovered/resolved with sequelae,recovered/resolved with sequelae,recovering/resolving,recovered/resolved with sequelae,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovered/resolved with sequelae,recovered/resolved with sequelae |
| 25243980 | 2025-04-28 | france | female | 68.0 | Somnolence,Disturbance in attention,Hyperglycaemia,Wrong patient received product | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25244377 | 2025-04-28 | poland | female | 54.0 | Suicide attempt,Hypotonia,Toxicity to various agents | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving |
| 25248790 | 2025-04-29 | spain | female | 72.0 | Cerebrovascular accident,Oedema peripheral,Pain,Micturition disorder,Sleep disorder,Fluid retention,Dizziness,Hypoaesthesia,Peripheral swelling,Joint swelling,Abdominal distension | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25249931 | 2025-04-29 | germany | female | 68.0 | Toxicity to various agents,Interstitial lung disease,Respiratory failure,Oedema peripheral,Bronchitis,Adverse drug reaction | serious | yes | not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25250858 | 2025-04-29 | france | male | 65.0 | Factor X deficiency,Drug ineffective | serious | yes | unknown,unknown |
| 25250922 | 2025-04-29 | germany | male | missing | Alcoholism,Drug dependence,Somnolence,Sleep disorder,Speech disorder,Feeling drunk,Labelled drug-disease interaction issue,Product substitution issue | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25251152 | 2025-04-29 | italy | male | 77.0 | Chest discomfort,Chills,Hyperhidrosis,Headache | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25254595 | 2025-04-30 | poland | male | 38.0 | Suicide attempt,Toxicity to various agents | serious | yes | unknown,unknown |
| 25256153 | 2025-04-30 | HR | female | missing | Electrocardiogram QRS complex shortened,Suicide attempt,Intentional overdose | serious | yes | unknown,unknown,unknown |
| 25258556 | 2025-05-01 | united kingdom | male | 60.0 | Angioedema | serious | yes | recovering/resolving |
| 25258834 | 2025-05-01 | eu | male | 73.0 | Septic shock,Atrial fibrillation,Renal failure,Respiratory failure,Thrombocytopenia,Hypokalaemia,Sepsis,Seizure,Malignant neoplasm progression,Anaemia | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,recovered/resolved,unknown,unknown |
| 25258902 | 2025-05-01 | france | female | 83.0 | Electrocardiogram QT prolonged,Diarrhoea | serious | yes | recovered/resolved,recovered/resolved |
| 25259138 | 2025-05-01 | united kingdom | female | missing | Hyponatraemia,Confusional state,Fatigue,Nausea | serious | yes | not recovered/not resolved/ongoing,recovered/resolved with sequelae,not recovered/not resolved/ongoing,recovering/resolving |
| 25259190 | 2025-05-01 | france | male | 88.0 | Hypotension,Bradycardia | serious | yes | recovered/resolved,recovered/resolved |
| 25262968 | 2025-05-02 | united kingdom | male | 64.0 | Erectile dysfunction,Hot flush | serious | yes | recovered/resolved,recovered/resolved |
| 25263047 | 2025-05-02 | italy | female | 95.0 | Dyspnoea,Hypotension | serious | yes | fatal,fatal |
| 25263173 | 2025-05-02 | germany | female | 86.0 | Craniofacial fracture,Inappropriate antidiuretic hormone secretion,Immobile,Fatigue,Dizziness,Fall,Mobility decreased,Constipation,Dysphagia,Contusion,Fear of falling,Wrong dose,Incorrect dose administered | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25265598 | 2025-05-03 | germany | female | 82.0 | Sudden death | serious | yes | fatal |
| 25265690 | 2025-05-03 | portugal | female | 61.0 | Rash macular,Pruritus,Throat irritation | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25265786 | 2025-05-03 | united kingdom | male | 82.0 | Heart rate decreased,Sudden hearing loss,Fatigue,Peripheral coldness,Pruritus | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25265801 | 2025-05-03 | united kingdom | male | 79.0 | IgA nephropathy,IVth nerve paralysis,Drug ineffective,COVID-19 | serious | yes | unknown,unknown,unknown,unknown |
| 25271690 | 2025-05-06 | united kingdom | female | 83.0 | Myositis | serious | yes | not recovered/not resolved/ongoing |
| 25272045 | 2025-05-06 | united kingdom | male | 72.0 | Medication error,Asthenia | serious | yes | unknown,not recovered/not resolved/ongoing |
| 25277387 | 2025-05-07 | united kingdom | female | 66.0 | Gastrooesophageal reflux disease,Paraesthesia | serious | yes | recovering/resolving,recovering/resolving |
| 25278828 | 2025-05-07 | italy | male | 79.0 | Cardiac failure congestive,Sepsis,Acute myeloid leukaemia,Multiple organ dysfunction syndrome,Disease progression,Thrombocytopenia | serious | yes | fatal,fatal,fatal,fatal,fatal,not recovered/not resolved/ongoing |
| 25282363 | 2025-05-08 | france | male | 66.0 | Hepatic cytolysis | serious | yes | recovering/resolving |
| 25282743 | 2025-05-08 | france | male | 83.0 | Nightmare,Acute kidney injury,Hallucination, visual | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovered/resolved |
| 25282819 | 2025-05-08 | united kingdom | female | 79.0 | Haemorrhage intracranial,Thrombocytopenia | serious | yes | not recovered/not resolved/ongoing,recovered/resolved |
| 25282914 | 2025-05-08 | france | female | 66.0 | Colitis,Febrile bone marrow aplasia | serious | yes | recovered/resolved,recovered/resolved |
| 25282958 | 2025-05-08 | united kingdom | missing | 55.0 | Agranulocytosis,Neutropenic sepsis,Abdominal pain,Nausea | serious | yes | recovered/resolved,unknown,unknown,unknown |
| 25286328 | 2025-05-09 | italy | male | 94.0 | Loss of consciousness | serious | yes | recovering/resolving |
| 25286488 | 2025-05-09 | france | female | 74.0 | Acute kidney injury,Anaemia | serious | yes | recovered/resolved,recovered/resolved |
| 25286888 | 2025-05-09 | united kingdom | female | 67.0 | Hypokalaemia,Hyponatraemia,Osmotic demyelination syndrome,Confusional state,Electrolyte imbalance,Somnolence | serious | yes | recovered/resolved with sequelae,recovered/resolved with sequelae,unknown,unknown,unknown,unknown |
| 25286895 | 2025-05-09 | france | female | 69.0 | Herpes zoster | serious | yes | recovered/resolved with sequelae |
| 25287192 | 2025-05-09 | united kingdom | female | missing | Hypertension,Heart rate irregular,Hyperhidrosis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25287381 | 2025-05-09 | united kingdom | missing | 81.0 | Transaminases abnormal,Liver function test abnormal | serious | yes | unknown,unknown |
| 25287571 | 2025-05-09 | united kingdom | female | 68.0 | Hyponatraemia | serious | yes | recovered/resolved |
| 25287807 | 2025-05-09 | france | male | 73.0 | Hypomagnesaemia,Hypocalcaemia,Electrocardiogram QT prolonged | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25298788 | 2025-05-12 | eu | male | 84.0 | Fall,Acute kidney injury,Hypotension,Dysarthria,Diarrhoea,Hallucination,Hypokalaemia,Syncope,Electrolyte imbalance,Hyponatraemia,Restlessness | serious | yes | recovered/resolved,unknown,unknown,unknown,unknown,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25299031 | 2025-05-12 | spain | male | 59.0 | Erectile dysfunction | serious | yes | recovering/resolving |
| 25299145 | 2025-05-12 | france | male | 63.0 | Rash maculo-papular,Hepatic cytolysis,Acute kidney injury | serious | yes | recovering/resolving,recovering/resolving,recovered/resolved |
| 25307220 | 2025-05-13 | france | female | 87.0 | Cardiac failure,Angina pectoris,Hypokalaemia,Pelvic organ prolapse,Heart rate decreased,Peripheral coldness,Insomnia,Fatigue,Asthenia,Polyuria,Diarrhoea,Urinary incontinence,Intentional product use issue,Intentional product misuse | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown,unknown |
| 25310411 | 2025-05-14 | poland | female | 45.0 | Asthenia | serious | yes | not recovered/not resolved/ongoing |
| 25310526 | 2025-05-14 | united kingdom | male | 71.0 | Depression,Nausea,Dyspnoea,Panic attack | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovered/resolved |
| 25317988 | 2025-05-15 | italy | male | 65.0 | Somnolence,Drug ineffective | serious | yes | recovered/resolved,unknown |
| 25318310 | 2025-05-15 | italy | female | 82.0 | Acidosis,Oliguria,Vomiting,Diarrhoea | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25318420 | 2025-05-15 | united kingdom | male | 64.0 | Acute myocardial infarction,Acute coronary syndrome | serious | yes | unknown,recovered/resolved |
| 25318424 | 2025-05-15 | united kingdom | female | 71.0 | Diplopia | serious | yes | recovered/resolved |
| 25318484 | 2025-05-15 | united kingdom | missing | 68.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 25318568 | 2025-05-15 | france | male | missing | Premature baby,Low birth weight baby,Maternal exposure during pregnancy | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25321874 | 2025-05-16 | united kingdom | male | 79.0 | IVth nerve paralysis | serious | yes | unknown |
| 25323837 | 2025-05-16 | germany | female | 66.0 | Pancreatitis | serious | yes | recovered/resolved |
| 25327402 | 2025-05-17 | eu | female | 86.0 | Fall,Contusion,Craniofacial fracture,Mobility decreased,Renal impairment,Inappropriate antidiuretic hormone secretion,Medication error,Immobile,Blood pressure decreased,Dizziness,Constipation,Fatigue,Lethargy,Dysphagia,Hyponatraemia,Prescribed overdose,Fear of falling,Incorrect dose administered | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,recovered/resolved,recovered/resolved,unknown,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,recovered/resolved,unknown,unknown |
| 25327503 | 2025-05-17 | france | female | 89.0 | Agranulocytosis | serious | yes | recovered/resolved |
| 25327507 | 2025-05-17 | france | female | 87.0 | Cardiac failure,Angina pectoris,Hypokalaemia,Urinary incontinence,Pelvic organ prolapse,Polyuria,Heart rate decreased,Peripheral coldness,Insomnia,Fatigue,Asthenia,Diarrhoea | serious | yes | unknown,unknown,unknown,unknown,unknown,not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown,unknown,not recovered/not resolved/ongoing |
| 25333893 | 2025-05-20 | france | female | 82.0 | Urinary retention,Dysuria,Oedema peripheral,Product substitution,Weight increased,Oxygen saturation decreased | serious | yes | unknown,recovered/resolved,recovered/resolved,unknown,recovered/resolved,recovered/resolved |
| 25333958 | 2025-05-20 | italy | male | 73.0 | Motor dysfunction,Myalgia | serious | yes | recovering/resolving,recovering/resolving |
| 25335387 | 2025-05-20 | france | male | 79.0 | Angioedema,Drug interaction,Diarrhoea | serious | yes | unknown,unknown,unknown |
| 25336030 | 2025-05-20 | france | male | 62.0 | Acute generalised exanthematous pustulosis | serious | yes | recovered/resolved |
| 25336046 | 2025-05-20 | france | male | 85.0 | Oesophageal candidiasis,Oral candidiasis | serious | yes | recovered/resolved,recovered/resolved |
| 25339473 | 2025-05-21 | united kingdom | female | 86.0 | Peripheral swelling | serious | yes | unknown |
| 25339477 | 2025-05-21 | france | male | 73.0 | Calculus urinary | serious | yes | not recovered/not resolved/ongoing |
| 25340570 | 2025-05-21 | united kingdom | female | 47.0 | Tinnitus,Tachycardia | serious | yes | not recovered/not resolved/ongoing,unknown |
| 25340982 | 2025-05-21 | portugal | male | 68.0 | Renal impairment | serious | yes | recovering/resolving |
| 25341255 | 2025-05-21 | eu | female | 48.0 | Arrhythmia,Serotonin syndrome,Ventricular arrhythmia,Disease risk factor,Drug interaction,Drug-disease interaction,Nausea,Vomiting,Dehydration,Electrolyte imbalance,No adverse event | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25345749 | 2025-05-22 | italy | female | 99.0 | Loss of consciousness | serious | yes | recovering/resolving |
| 25346246 | 2025-05-22 | united kingdom | male | 87.0 | Hypomagnesaemia,Hypokalaemia | serious | yes | recovered/resolved,recovered/resolved |
| 25350246 | 2025-05-23 | france | male | 46.0 | Anaphylactic reaction | serious | yes | recovered/resolved |
| 25351249 | 2025-05-23 | france | female | 76.0 | Sinoatrial block,Accidental overdose,Hypotension | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving |
| 25351254 | 2025-05-23 | france | female | 81.0 | Haemorrhagic stroke,Urinary retention,Hypertension | serious | yes | recovered/resolved with sequelae,recovered/resolved,recovered/resolved with sequelae |
| 25351450 | 2025-05-23 | france | female | 84.0 | Eyelid injury,Rash scarlatiniform,Pruritus | serious | yes | not recovered/not resolved/ongoing,recovering/resolving,recovering/resolving |
| 25352070 | 2025-05-23 | united kingdom | female | 77.0 | Drug interaction | serious | yes | unknown |
| 25355021 | 2025-05-24 | united kingdom | female | 84.0 | Sepsis,Poisoning | serious | yes | fatal,recovered/resolved |
| 25355679 | 2025-05-25 | spain | male | 66.0 | Melaena,Abdominal pain,Malaise | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25355693 | 2025-05-25 | HR | female | missing | Electrocardiogram QRS complex shortened,Suicide attempt,Intentional overdose | serious | yes | unknown,unknown,unknown |
| 25356717 | 2025-05-26 | italy | male | 71.0 | Motor dysfunction,Myalgia | serious | yes | recovering/resolving,recovering/resolving |
| 25357821 | 2025-05-26 | poland | female | 57.0 | Labelled drug-drug interaction issue,Central nervous system haemorrhage,Drug interaction | serious | yes | unknown,unknown,unknown |
| 25358018 | 2025-05-26 | france | female | 68.0 | Polyarthritis | serious | yes | recovering/resolving |
| 25358067 | 2025-05-26 | france | female | 92.0 | Atrioventricular block,Bradycardia,Overdose | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25358250 | 2025-05-26 | UA | female | 93.0 | Off label use | serious | yes | unknown |
| 25362159 | 2025-05-27 | france | male | 79.0 | Acute kidney injury,Oedema peripheral | serious | yes | recovered/resolved,recovered/resolved |
| 25366264 | 2025-05-28 | united kingdom | missing | missing | Cyanopsia | serious | yes | recovering/resolving |
| 25367757 | 2025-05-28 | poland | male | 60.0 | Myocardial infarction,Atrial fibrillation,Cardiac failure chronic,Dyslipidaemia,Cardiac failure,Drug abuse,Off label use | serious | yes | unknown,unknown,unknown,unknown,recovering/resolving,unknown,unknown |
| 25372181 | 2025-05-29 | belgium | female | 64.0 | Acute kidney injury,Rhabdomyolysis,Hyperkalaemia,Blood thyroid stimulating hormone increased,Hepatic function abnormal,Metabolic acidosis,Decreased appetite,Diarrhoea,Labelled drug-drug interaction issue | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25376854 | 2025-05-30 | united kingdom | female | 53.0 | Serotonin syndrome,Neuroleptic malignant syndrome | serious | yes | recovered/resolved,recovered/resolved |
| 25378495 | 2025-05-30 | france | female | 57.0 | Hepatitis acute | serious | yes | recovering/resolving |
| 25381810 | 2025-05-31 | poland | female | 48.0 | Ventricular arrhythmia,Drug interaction | serious | yes | unknown,unknown |
| 25381915 | 2025-05-31 | united kingdom | female | 64.0 | Femoral neck fracture,Dizziness,Fall | serious | yes | unknown,unknown,recovered/resolved |
| 25381958 | 2025-05-31 | united kingdom | male | 66.0 | Haemoptysis,Contusion | serious | yes | recovered/resolved,recovered/resolved |
| 25382381 | 2025-06-01 | germany | male | 87.0 | Drug ineffective | serious | yes | unknown |
| 25388281 | 2025-06-03 | portugal | male | 71.0 | Diarrhoea,Renal pain,Anaemia,Pruritus,Rash | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25388525 | 2025-06-03 | united kingdom | male | 60.0 | Extrasystoles,Heart rate decreased,Peripheral coldness,Fatigue,Sleep disorder,Alopecia,Dizziness,Abdominal distension | serious | yes | not recovered/not resolved/ongoing,unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown |
| 25388850 | 2025-06-03 | united kingdom | female | 68.0 | Clostridium difficile infection | serious | yes | recovering/resolving |
| 25389249 | 2025-06-03 | france | male | 60.0 | Drug ineffective,Therapy non-responder,Intentional product use issue,Off label use | serious | yes | unknown,unknown,unknown,unknown |
| 25389536 | 2025-06-03 | spain | female | 76.0 | Vomiting,Nausea,Drug ineffective | serious | yes | unknown,unknown,unknown |
| 25389670 | 2025-06-03 | united states | male | 46.0 | Atrial fibrillation,Hyperthyroidism,Ventricular tachycardia,Mitral valve incompetence | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25393094 | 2025-06-04 | italy | female | 6.0 | Hypertriglyceridaemia,Off label use | serious | yes | unknown,unknown |
| 25393833 | 2025-06-04 | sweden | male | 60.0 | Multiple acyl-coenzyme A dehydrogenase deficiency,Wheelchair user,Muscular weakness,Dysphagia | serious | yes | unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown |
| 25393936 | 2025-06-04 | italy | male | 77.0 | Acute kidney injury | serious | yes | fatal |
| 25394964 | 2025-06-04 | france | female | 65.0 | Gastrointestinal disorder,Acute kidney injury,Lactic acidosis,Hyperkalaemia,Shock | serious | yes | fatal,fatal,fatal,fatal,fatal |
| 25395270 | 2025-06-04 | united kingdom | female | 71.0 | Liver function test abnormal | serious | yes | recovered/resolved |
| 25400327 | 2025-06-05 | united kingdom | male | 67.0 | Haematochezia | serious | yes | recovered/resolved |
| 25400397 | 2025-06-05 | united kingdom | female | 85.0 | Acute kidney injury | serious | yes | unknown |
| 25400812 | 2025-06-05 | united kingdom | male | 82.0 | Fatigue,Lethargy | serious | yes | recovered/resolved,recovered/resolved |
| 25401071 | 2025-06-05 | poland | female | 68.0 | Suicide attempt,Toxicity to various agents,Bradycardia | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25404945 | 2025-06-06 | france | female | 57.0 | Cardiogenic shock,Poisoning,Overdose | serious | yes | unknown,unknown,unknown |
| 25405117 | 2025-06-06 | france | female | 85.0 | Diplegia | serious | yes | recovering/resolving |
| 25406074 | 2025-06-06 | france | male | 48.0 | Drug reaction with eosinophilia and systemic symptoms | serious | yes | recovered/resolved |
| 25409056 | 2025-06-07 | france | male | 15.0 | Atrial fibrillation,Bradycardia,Sinus node dysfunction,Overdose,Drug ineffective,Chronotropic incompetence,Intentional product use issue,Product use issue,Off label use | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25409237 | 2025-06-07 | france | male | 63.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 25409243 | 2025-06-07 | france | male | 85.0 | Subacute cutaneous lupus erythematosus | serious | yes | recovered/resolved |
| 25409374 | 2025-06-07 | united kingdom | male | missing | Brain fog,Medication error | serious | yes | not recovered/not resolved/ongoing,unknown |
| 25409428 | 2025-06-07 | united kingdom | male | 72.0 | Dyspnoea,Medication error | serious | yes | recovered/resolved,unknown |
| 25410761 | 2025-06-09 | united kingdom | male | missing | Acute kidney injury | serious | yes | not recovered/not resolved/ongoing |
| 25411668 | 2025-06-09 | united kingdom | female | 67.0 | Hypertensive crisis,Dizziness | serious | yes | recovering/resolving,unknown |
| 25412577 | 2025-06-09 | italy | missing | 90.0 | Drug ineffective | serious | yes | unknown |
| 25422712 | 2025-06-11 | italy | male | 37.0 | Drug resistance,Blood pressure increased,Drug ineffective,Off label use | serious | yes | unknown,unknown,recovering/resolving,unknown |
| 25428113 | 2025-06-12 | united kingdom | male | missing | Walking aid user,Arthralgia,Muscle tightness,Pain in extremity,Off label use | serious | yes | recovering/resolving,recovering/resolving,recovered/resolved,recovering/resolving,unknown |
| 25428644 | 2025-06-12 | poland | female | 76.0 | Drug ineffective | serious | yes | unknown |
| 25428646 | 2025-06-12 | united kingdom | male | 68.0 | Fluid retention,Hypertension,Osteoporosis,Ocular hyperaemia,Weight increased,Arthralgia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25432209 | 2025-06-13 | united kingdom | female | 86.0 | Delirium | serious | yes | recovered/resolved |
| 25432749 | 2025-06-13 | germany | male | 61.0 | Syncope,Fatigue,Fibrin D dimer increased | serious | yes | recovered/resolved,not recovered/not resolved/ongoing,unknown |
| 25432788 | 2025-06-13 | united kingdom | male | 64.0 | Chest discomfort | serious | yes | recovered/resolved |
| 25437825 | 2025-06-16 | poland | male | 69.0 | Leriche syndrome,Peripheral artery occlusion,Infarction,Peripheral ischaemia,Peripheral arterial occlusive disease,Splenic infarction,Renal infarct | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25438412 | 2025-06-16 | france | female | 87.0 | Fall,Epistaxis | serious | yes | fatal,fatal |
| 25439832 | 2025-06-16 | italy | male | 65.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 25442830 | 2025-06-17 | united kingdom | female | 67.0 | Supraventricular tachycardia,Condition aggravated | serious | yes | recovered/resolved,recovered/resolved |
| 25443131 | 2025-06-17 | france | female | 93.0 | Asthenia,Gait disturbance,Speech disorder,Sinus bradycardia,Hypotension,Product administration error | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25443354 | 2025-06-17 | france | female | missing | Mixed liver injury,Condition aggravated | serious | yes | recovering/resolving,recovering/resolving |
| 25444366 | 2025-06-17 | france | male | 71.0 | Myositis,Liver disorder | serious | yes | recovering/resolving,recovered/resolved |
| 25444430 | 2025-06-17 | belgium | female | 90.0 | Vertebrobasilar stroke,Urinary tract infection,Confusional state,Hyponatraemia | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing |
| 25445448 | 2025-06-17 | france | male | 82.0 | Cholestasis,Rash maculo-papular | serious | yes | recovering/resolving,recovering/resolving |
| 25448818 | 2025-06-18 | united kingdom | female | 83.0 | Disorientation,Confusional state,Palpitations,Sedation | serious | yes | unknown,unknown,unknown,unknown |
| 25450050 | 2025-06-18 | france | male | 82.0 | Hypotension,Bradycardia,Renal failure,Toxicity to various agents,Intentional overdose,Suicide attempt,Shock,Somnolence | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25453501 | 2025-06-19 | eu | female | 67.0 | Intestinal villi atrophy,Intestinal intraepithelial lymphocytes increased,Gastrointestinal disorder,Enterocolitis,Diarrhoea,Weight decreased | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25453723 | 2025-06-19 | united kingdom | male | 62.0 | Joint swelling | serious | yes | recovering/resolving |
| 25453725 | 2025-06-19 | united kingdom | female | 75.0 | Duodenal ulcer | serious | yes | not recovered/not resolved/ongoing |
| 25453820 | 2025-06-19 | united kingdom | missing | 76.0 | Bradycardia | serious | yes | recovered/resolved |
| 25453840 | 2025-06-19 | poland | female | 70.0 | Suicide attempt,Bradycardia,Toxicity to various agents | serious | yes | unknown,recovering/resolving,recovering/resolving |
| 25454348 | 2025-06-19 | united kingdom | male | 73.0 | Neuropathy peripheral | serious | yes | unknown |
| 25454410 | 2025-06-19 | italy | female | 50.0 | Alanine aminotransferase increased,Pain,Pyrexia,Transaminases increased,Condition aggravated | serious | yes | recovered/resolved with sequelae,recovered/resolved,recovered/resolved,recovered/resolved with sequelae,recovered/resolved with sequelae |
| 25454690 | 2025-06-19 | germany | missing | missing | Cleft palate,Atrial septal defect,Cardiac hypertrophy,Large for dates baby,Foetal exposure during pregnancy | serious | yes | unknown,recovered/resolved,unknown,unknown,unknown |
| 25455490 | 2025-06-19 | poland | male | 66.0 | Hypotony of eye,Seizure,Myocardial infarction,Hyporeflexia,Musculoskeletal stiffness,Asthenia,Muscular weakness | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25455510 | 2025-06-19 | canada | female | 43.0 | Therapy non-responder | serious | yes | unknown |
| 25459553 | 2025-06-20 | spain | female | 64.0 | Pneumonitis | serious | yes | not recovered/not resolved/ongoing |
| 25459633 | 2025-06-20 | france | male | 27.0 | Dyslipidaemia | serious | yes | not recovered/not resolved/ongoing |
| 25459724 | 2025-06-20 | germany | male | 68.0 | Neuroleptic malignant syndrome,Hallucinations, mixed,Hypokalaemia,Serotonin syndrome,Disorientation,Agitation,Cold sweat,Pyrexia,Apraxia,Resting tremor,Intention tremor,Postural tremor,Dysarthria,Chills,Blood creatine phosphokinase increased,Hypernatraemia | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25460310 | 2025-06-20 | RO | missing | 46.0 | Condition aggravated,Ventricle rupture | serious | yes | unknown,unknown |
| 25461380 | 2025-06-20 | france | male | 77.0 | Febrile bone marrow aplasia,Septic shock | serious | yes | fatal,fatal |
| 25461442 | 2025-06-20 | italy | male | 73.0 | Spontaneous haematoma,Off label use | serious | yes | recovered/resolved,recovered/resolved |
| 25461487 | 2025-06-20 | france | female | 69.0 | Serotonin syndrome | serious | yes | not recovered/not resolved/ongoing |
| 25463792 | 2025-06-21 | germany | female | 82.0 | Polyneuropathy | serious | yes | not recovered/not resolved/ongoing |
| 25463940 | 2025-06-21 | eu | male | 87.0 | Anaemia,Haemarthrosis,Pain | serious | yes | recovering/resolving,recovered/resolved,recovered/resolved |
| 25464187 | 2025-06-21 | SA | female | 39.0 | Premature delivery,Exposure during pregnancy | serious | yes | unknown,unknown |
| 25464227 | 2025-06-21 | poland | male | 69.0 | Leriche syndrome,Ischaemic nephropathy,Spleen ischaemia,Peripheral arterial occlusive disease,Ulnar nerve injury,Peripheral artery bypass | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown |
| 25464251 | 2025-06-21 | united kingdom | male | missing | Cerebrovascular accident,Disability,Hyperkalaemia,Nervous system disorder,Vomiting,Therapy cessation,Drug dose titration not performed,Product prescribing issue | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25464386 | 2025-06-21 | SA | female | 2.0 | Premature baby,Foetal exposure during pregnancy,Underweight,Respiratory disorder neonatal,Multiple congenital abnormalities,Heart rate decreased,Teratogenicity | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25464802 | 2025-06-22 | spain | male | 66.0 | Renal impairment,Neoplasm progression | serious | yes | unknown,unknown |
| 25465662 | 2025-06-23 | france | male | 79.0 | Angioedema,Oedema,Respiratory disorder,Diarrhoea | serious | yes | unknown,unknown,unknown,unknown |
| 25470506 | 2025-06-24 | france | female | 72.0 | Acute hepatic failure | serious | yes | recovered/resolved |
| 25474438 | 2025-06-24 | eu | male | 54.0 | Ileus paralytic,Anaemia | serious | yes | recovered/resolved,recovered/resolved |
| 25477178 | 2025-06-25 | spain | male | 79.0 | Acute myocardial infarction | serious | yes | recovered/resolved |
| 25482289 | 2025-06-26 | united kingdom | male | missing | Skin reaction | serious | yes | recovering/resolving |
| 25483112 | 2025-06-26 | sweden | male | 72.0 | Asthenia,Cough,Dyspnoea,Muscular weakness,Myositis,Pneumonia,Visual impairment | serious | yes | fatal,fatal,fatal,fatal,fatal,fatal,fatal |
| 25483406 | 2025-06-26 | france | female | 83.0 | Encephalopathy,Acute kidney injury,Overdose | serious | yes | fatal,fatal,fatal |
| 25484278 | 2025-06-26 | spain | male | 87.0 | Acute kidney injury,Disorientation,Hypotension | serious | yes | recovering/resolving,recovered/resolved,recovered/resolved |
| 25486746 | 2025-06-27 | eu | male | missing | Device related infection,Osteoarthritis,Knee arthroplasty,Anaemia postoperative | serious | yes | unknown,unknown,unknown,unknown |
| 25487893 | 2025-06-27 | france | male | missing | Hyperkalaemia,Drug interaction | serious | yes | unknown,unknown |
| 25487953 | 2025-06-27 | united kingdom | male | 50.0 | Rash papular,Dyspnoea | serious | yes | recovered/resolved,recovered/resolved |
| 25490087 | 2025-06-28 | united kingdom | female | 72.0 | Pain in extremity,Peripheral coldness | serious | yes | recovered/resolved,recovered/resolved |
| 25493751 | 2025-06-30 | united kingdom | male | 71.0 | Eye injury | serious | yes | not recovered/not resolved/ongoing |
| 25493912 | 2025-06-30 | spain | male | 61.0 | Sinus bradycardia | serious | yes | recovered/resolved |
| 25496565 | 2025-06-30 | france | male | 87.0 | Lip oedema,Tongue oedema,Dysphonia,Dyspnoea | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25496720 | 2025-07-01 | eu | male | 84.0 | Asthenia,Toxicity to various agents | serious | yes | recovering/resolving,recovering/resolving |
| 25497099 | 2025-07-01 | eu | female | 88.0 | Renal failure,Drug reaction with eosinophilia and systemic symptoms,Hepatic failure,Eosinophilia,Pyrexia | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 25497984 | 2025-07-01 | united kingdom | male | 87.0 | Diarrhoea,Colitis microscopic,Anxiety | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25497986 | 2025-07-01 | united kingdom | female | 67.0 | Joint swelling | serious | yes | recovered/resolved |
| 25497997 | 2025-07-01 | eu | female | 63.0 | Chronic cutaneous lupus erythematosus,Morphoea,Dermatitis psoriasiform,Sinus bradycardia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown |
| 25498826 | 2025-07-01 | eu | female | 80.0 | Anaphylactic reaction | serious | yes | recovered/resolved |
| 25499429 | 2025-07-01 | eu | male | 54.0 | Generalised tonic-clonic seizure,Hypomagnesaemia,Supraventricular tachycardia | serious | yes | unknown,recovered/resolved,recovered/resolved |
| 25500305 | 2025-07-01 | eu | male | 57.0 | Superinfection,Chronic inflammatory response syndrome,Mouth ulceration,Odynophagia,Pain,Pyrexia,Chronic kidney disease,Mononeuropathy,Off label use | serious | yes | unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,not recovered/not resolved/ongoing,unknown |
| 25502017 | 2025-07-02 | eu | male | 72.0 | Neutropenia,Rash maculo-papular,Pyrexia,Asthenia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25502579 | 2025-07-02 | eu | female | 1.0 | Poland^s syndrome,Maternal exposure during pregnancy | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25502657 | 2025-07-02 | eu | female | 60.0 | Cardiogenic shock | serious | yes | not recovered/not resolved/ongoing |
| 25502688 | 2025-07-02 | eu | female | missing | Blood cholesterol increased,Low density lipoprotein increased,Drug intolerance,Blood triglycerides increased,Drug ineffective | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown,unknown |
| 25502988 | 2025-07-02 | united kingdom | female | 55.0 | Blood potassium decreased,Mouth ulceration,Fatigue,Paraesthesia | serious | yes | recovering/resolving,not recovered/not resolved/ongoing,recovering/resolving,not recovered/not resolved/ongoing |
| 25503311 | 2025-07-02 | united states | male | 73.0 | Drug ineffective,Therapy change,Product substitution issue | not serious | no | unknown,unknown,unknown |
| 25508155 | 2025-07-03 | eu | female | 54.0 | Superficial vein thrombosis | serious | yes | recovered/resolved |
| 25509197 | 2025-07-03 | eu | female | 64.0 | Cholestatic liver injury,Hypothyroidism | serious | yes | recovered/resolved,recovering/resolving |
| 25516706 | 2025-07-04 | united kingdom | female | 71.0 | Gastritis | serious | yes | not recovered/not resolved/ongoing |
| 25517207 | 2025-07-04 | eu | male | 75.0 | Pneumonia,Fall,Sleep apnoea syndrome,Hallucination, visual,Abnormal dreams,Cognitive disorder,Chills,Constipation,Depressed mood,Dysphagia,General physical health deterioration,Memory impairment,Mobility decreased,Musculoskeletal disorder,Nocturia,Parkinsonism,Pollakiuria,Rapid eye movement sleep behaviour disorder | serious | yes | not recovered/not resolved/ongoing,unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,not recovered/not resolved/ongoing |
| 25518899 | 2025-07-04 | united kingdom | female | 79.0 | Hip fracture,Fall,Joint arthroplasty,Cataract,Joint injury,Abdominal discomfort,Balance disorder,Pharyngeal swelling,Arthralgia,Arterial thrombosis,Pain,Blood iron decreased | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,not recovered/not resolved/ongoing,recovered/resolved |
| 25520827 | 2025-07-05 | united kingdom | female | 69.0 | Fatigue,Asthenia,Weight increased,Dyspnoea,Neuropathy peripheral,Pain in extremity,Dyspepsia,Arthralgia,Tinnitus,Amnesia,Eye pain | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25520863 | 2025-07-05 | eu | female | 83.0 | Presyncope,Bradycardia | serious | yes | recovered/resolved,recovered/resolved |
| 25521160 | 2025-07-05 | eu | male | 61.0 | Gastrointestinal haemorrhage,Drug interaction | serious | yes | recovered/resolved,recovered/resolved |
| 25521499 | 2025-07-06 | eu | female | 80.0 | Urticaria papular | serious | yes | recovered/resolved |
| 25521504 | 2025-07-06 | eu | male | 73.0 | Mucosal inflammation,Malignant neoplasm progression | serious | yes | not recovered/not resolved/ongoing,unknown |
| 25521507 | 2025-07-06 | eu | male | 33.0 | Epilepsy,Product administration error | serious | yes | recovered/resolved,recovered/resolved |
| 25523170 | 2025-07-07 | united kingdom | male | 76.0 | Urinary retention | serious | yes | recovered/resolved |
| 25523210 | 2025-07-07 | eu | female | 79.0 | Respiratory failure | serious | yes | fatal |
| 25523238 | 2025-07-07 | united kingdom | female | missing | Vasculitis | serious | yes | not recovered/not resolved/ongoing |
| 25523341 | 2025-07-07 | united kingdom | male | missing | Toxicity to various agents | serious | yes | recovered/resolved |
| 25528355 | 2025-07-08 | eu | male | 60.0 | Polyneuropathy,Metastases to liver,Arteriosclerosis coronary artery,Hypomagnesaemia,Therapy partial responder | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 25528383 | 2025-07-08 | eu | male | 60.0 | Ejection fraction decreased | serious | yes | not recovered/not resolved/ongoing |
| 25528810 | 2025-07-08 | eu | male | 72.0 | Encephalitis,Polyneuropathy,Malignant neoplasm progression,Atrial fibrillation,Hypokalaemia,Immune-mediated lung disease,Aphasia,Disorientation,Dyspnoea,Mucosal inflammation,Osteolysis | serious | yes | recovered/resolved,not recovered/not resolved/ongoing,unknown,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,recovered/resolved,recovered/resolved,unknown |
| 25531830 | 2025-07-09 | eu | female | 67.0 | Inappropriate antidiuretic hormone secretion | serious | yes | recovering/resolving |
| 25532154 | 2025-07-09 | eu | male | 99.0 | Wrong patient | serious | yes | fatal |
| 25532201 | 2025-07-09 | united kingdom | male | 85.0 | Psoriasis | serious | yes | not recovered/not resolved/ongoing |
| 25532382 | 2025-07-09 | eu | female | 75.0 | Calciphylaxis,Pain of skin,Skin lesion,Skin ulcer,Skin necrosis,Erythema,Cutaneous calcification,Renal impairment,Superinfection bacterial,Sepsis,Off label use | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25533151 | 2025-07-09 | eu | male | 74.0 | Acquired haemophilia | serious | yes | recovered/resolved |
| 25533545 | 2025-07-09 | eu | male | 51.0 | Autoimmune myositis | serious | yes | recovered/resolved |
| 25533807 | 2025-07-09 | united kingdom | male | 54.0 | Peyronie^s disease,Medication error | serious | yes | unknown,unknown |
| 25534452 | 2025-07-09 | united kingdom | male | 70.0 | Atrial fibrillation,Anxiety,Fatigue,Dizziness | serious | yes | recovered/resolved,recovering/resolving,recovering/resolving,recovering/resolving |
| 25539035 | 2025-07-10 | eu | female | 62.0 | Drug ineffective,Asthenia,Somnolence,Drug interaction,Medication error | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 25539068 | 2025-07-10 | united kingdom | male | 68.0 | Mouth swelling | serious | yes | recovered/resolved |
| 25539296 | 2025-07-10 | eu | male | 84.0 | Hyperbilirubinaemia | serious | yes | not recovered/not resolved/ongoing |
| 25541512 | 2025-07-11 | united kingdom | missing | missing | Pain in extremity,Oedema peripheral,Abdominal distension | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25542374 | 2025-07-11 | eu | female | 82.0 | Bradycardia,Atrioventricular block | serious | yes | recovered/resolved,recovered/resolved |
| 25542615 | 2025-07-11 | eu | male | 50.0 | Blood thyroid stimulating hormone decreased | serious | yes | recovered/resolved with sequelae |
| 25542675 | 2025-07-11 | united kingdom | female | 52.0 | Vaginal haemorrhage,Dizziness | serious | yes | recovered/resolved,recovered/resolved |
| 25543687 | 2025-07-11 | eu | male | 73.0 | Hyperbilirubinaemia,Condition aggravated | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25546158 | 2025-07-13 | united kingdom | male | 62.0 | Malignant neoplasm progression,Syncope,Blister,Toxicity to various agents,Off label use,Product dose omission issue,Product distribution issue | serious | yes | unknown,recovered/resolved,recovered/resolved,unknown,unknown,unknown,unknown |
| 25547806 | 2025-07-14 | eu | female | 70.0 | Hepatic cytolysis | serious | yes | not recovered/not resolved/ongoing |
| 25548024 | 2025-07-14 | eu | male | 82.0 | Atrioventricular block | serious | yes | recovering/resolving |
| 25552003 | 2025-07-14 | united kingdom | female | 75.0 | Vomiting,Malaise | serious | yes | recovered/resolved,unknown |
| 25552485 | 2025-07-15 | eu | male | 55.0 | High density lipoprotein decreased,Hypercholesterolaemia,Stomatocytes present,Red blood cell abnormality,Drug interaction | serious | yes | recovered/resolved,unknown,recovered/resolved,recovered/resolved,recovered/resolved |
| 25552852 | 2025-07-15 | eu | male | 78.0 | Acute generalised exanthematous pustulosis | serious | yes | recovered/resolved |
| 25553656 | 2025-07-15 | eu | male | 65.0 | Acute myocardial infarction,Arteriospasm coronary,Atrial fibrillation,Left ventricular dysfunction,Ventricular arrhythmia,Cardiac arrest,Akinesia,Cardiac failure,Ventricular tachycardia,Myocarditis,Arrhythmia,Drug ineffective,Chest pain,Blood pressure increased | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25553731 | 2025-07-15 | eu | female | 77.0 | Febrile bone marrow aplasia,Septic shock,Cardiac failure acute,Acute kidney injury,Drug reaction with eosinophilia and systemic symptoms,Medication error,Drug monitoring procedure not performed | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25553978 | 2025-07-15 | eu | male | 61.0 | Gastrointestinal haemorrhage | serious | yes | recovered/resolved |
| 25563974 | 2025-07-16 | eu | male | missing | Pancytopenia,Leukopenia,Anaemia,Thrombocytosis,Fatigue,Diarrhoea | serious | yes | recovering/resolving,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovered/resolved |
| 25564765 | 2025-07-16 | united kingdom | male | 52.0 | Sinus bradycardia | serious | yes | recovered/resolved |
| 25565161 | 2025-07-16 | eu | male | 54.0 | Cerebellar syndrome,Generalised tonic-clonic seizure,Hypokalaemia,Hypomagnesaemia,Supraventricular tachycardia,Sleep disorder,Tetany | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25565299 | 2025-07-16 | eu | male | 73.0 | Mycobacterial infection,Cytopenia | serious | yes | recovered/resolved,recovered/resolved |
| 25565564 | 2025-07-16 | eu | male | 72.0 | Drug interaction,Myalgia,Malaise | serious | yes | unknown,unknown,unknown |
| 25570132 | 2025-07-17 | united kingdom | male | missing | Aura | serious | yes | recovered/resolved |
| 25570254 | 2025-07-17 | eu | male | 63.0 | Macroglossia,Dysphonia,Dyspnoea | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25570823 | 2025-07-17 | united kingdom | male | 59.0 | Subarachnoid haemorrhage | serious | yes | recovering/resolving |
| 25571526 | 2025-07-17 | australia | female | 60.0 | Gastrointestinal tract mucosal pigmentation | serious | yes | unknown |
| 25571733 | 2025-07-17 | eu | male | 56.0 | Acute kidney injury,Abdominal pain,Diarrhoea,C-reactive protein increased | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25571836 | 2025-07-17 | eu | female | missing | Hepatotoxicity | serious | yes | recovered/resolved |
| 25575675 | 2025-07-18 | united kingdom | male | 72.0 | Suicidal ideation | serious | yes | recovered/resolved |
| 25575856 | 2025-07-18 | eu | male | missing | Syncope,Bradycardia,Wrong patient received product | serious | yes | unknown,unknown,recovered/resolved |
| 25576229 | 2025-07-18 | eu | female | 53.0 | Rash pruritic,Oropharyngeal discomfort,Oedema peripheral | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25576857 | 2025-07-18 | eu | male | 66.0 | Polyneuropathy,Condition aggravated,Glomerular filtration rate decreased,Diarrhoea | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved |
| 25581884 | 2025-07-19 | united kingdom | male | 39.0 | Alopecia | serious | yes | not recovered/not resolved/ongoing |
| 25581942 | 2025-07-19 | eu | male | 66.0 | Death,Toxic epidermal necrolysis | serious | yes | fatal,unknown |
| 25582038 | 2025-07-19 | eu | female | 89.0 | Bradycardia,Syncope | serious | yes | recovered/resolved,recovering/resolving |
| 25582293 | 2025-07-20 | united kingdom | female | 81.0 | Muscle spasms | serious | yes | recovered/resolved |
| 25582496 | 2025-07-20 | eu | male | 80.0 | Toxic epidermal necrolysis,Stevens-Johnson syndrome,Septic shock,Skin reaction | serious | yes | fatal,fatal,fatal,unknown |
| 25584646 | 2025-07-21 | united kingdom | female | 23.0 | Drug ineffective | serious | yes | recovered/resolved |
| 25585570 | 2025-07-21 | eu | male | 32.0 | Cardiac failure,Ejection fraction decreased,Condition aggravated | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving |
| 25588310 | 2025-07-22 | eu | male | 56.0 | Acute kidney injury,Abdominal pain,Diarrhoea,C-reactive protein increased,Intentional product use issue,Off label use | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25588314 | 2025-07-22 | eu | female | 93.0 | Bradycardia,Hypotension,Product administration error,Wrong patient received product | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25588869 | 2025-07-22 | eu | male | 85.0 | Syncope | serious | yes | recovered/resolved |
| 25589993 | 2025-07-22 | eu | female | 74.0 | Hypoxia,Melaena,Nausea,Pyrexia,Diarrhoea | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved with sequelae,recovered/resolved,recovered/resolved |
| 25595247 | 2025-07-23 | eu | female | 64.0 | Raynaud^s phenomenon | serious | yes | recovering/resolving |
| 25595339 | 2025-07-23 | eu | male | 88.0 | Ischaemic stroke | serious | yes | not recovered/not resolved/ongoing |
| 25595841 | 2025-07-23 | eu | female | 79.0 | Atrioventricular block complete,Syncope | serious | yes | recovered/resolved,recovered/resolved |
| 25595958 | 2025-07-23 | eu | female | missing | Hepatotoxicity | serious | yes | recovering/resolving |
| 25595977 | 2025-07-23 | united kingdom | male | missing | Atrioventricular block | serious | yes | recovered/resolved |
| 25599214 | 2025-07-24 | eu | female | 82.0 | Gastric ulcer,Melaena,Haemorrhage,Malaise,Labelled drug-drug interaction medication error | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 25599366 | 2025-07-24 | eu | male | 9.0 | Type 2 diabetes mellitus,Weight decreased,Idiopathic interstitial pneumonia,Hepatitis acute | serious | yes | unknown,unknown,recovering/resolving,recovered/resolved |
| 25604532 | 2025-07-25 | eu | female | 77.0 | Tubulointerstitial nephritis | serious | yes | recovered/resolved |
| 25608501 | 2025-07-26 | eu | female | 64.0 | Raynaud^s phenomenon,Skin necrosis,Pain in extremity,Paraesthesia,Oedema peripheral,Pallor,Cyanosis,Dry skin,Condition aggravated,Carpal tunnel syndrome,Arthralgia,Skin ulcer,Erythema | serious | yes | recovered/resolved,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25611114 | 2025-07-28 | eu | female | 66.0 | Syncope,Adverse drug reaction | serious | yes | recovering/resolving,recovering/resolving |
| 25611176 | 2025-07-28 | united kingdom | female | 88.0 | Musculoskeletal stiffness,Nightmare,Peripheral swelling | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25615880 | 2025-07-29 | eu | male | 94.0 | Dehydration,Hypotension,Hyponatraemia | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving |
| 25615980 | 2025-07-29 | united kingdom | male | 82.0 | Stevens-Johnson syndrome,Toxic epidermal necrolysis,Rash papular,Mouth ulceration,Genital ulceration | serious | yes | fatal,not recovered/not resolved/ongoing,unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25616798 | 2025-07-29 | eu | female | 90.0 | Rhabdomyolysis,Cholestasis,Hepatic cytolysis | serious | yes | recovered/resolved,recovering/resolving,recovered/resolved |
| 25616836 | 2025-07-29 | eu | male | 75.0 | Basal cell carcinoma | serious | yes | not recovered/not resolved/ongoing |
| 25616903 | 2025-07-29 | eu | male | 56.0 | Acute kidney injury,Abdominal pain,Diarrhoea,Intentional product use issue,Off label use,C-reactive protein increased | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,recovered/resolved |
| 25616932 | 2025-07-29 | eu | male | 65.0 | Eyelid oedema | serious | yes | recovered/resolved |
| 25620389 | 2025-07-30 | eu | female | 83.0 | Cardio-respiratory arrest | serious | yes | fatal |
| 25620624 | 2025-07-30 | eu | female | 73.0 | Melaena,Rash,Herpes zoster,Polyp,Off label use | serious | yes | unknown,recovered/resolved,recovered/resolved,unknown,unknown |
| 25620719 | 2025-07-30 | eu | female | 46.0 | Suicide attempt,Hypotension,Toxicity to various agents,Alcohol interaction | serious | yes | unknown,recovering/resolving,recovering/resolving,recovering/resolving |
| 25621964 | 2025-07-30 | eu | female | 67.0 | Agranulocytosis | serious | yes | recovered/resolved |
| 25622114 | 2025-07-30 | eu | female | 74.0 | Cardiogenic shock | serious | yes | fatal |
| 25625581 | 2025-07-31 | united kingdom | male | 88.0 | Pulmonary embolism,Accidental overdose,Sedation,Mobility decreased,Device use error | serious | yes | fatal,unknown,unknown,unknown,unknown |
| 25626610 | 2025-07-31 | united kingdom | male | 55.0 | Drug ineffective | serious | yes | unknown |
| 25626868 | 2025-07-31 | eu | male | 77.0 | Urinary tract infection,Therapeutic product effect increased,Glycosuria,Drug interaction | serious | yes | unknown,unknown,unknown,unknown |
| 25627510 | 2025-07-31 | eu | female | 90.0 | Acute myocardial infarction,Product administration error,Wrong patient,Wrong product administered | serious | yes | fatal,fatal,fatal,fatal |
| 25631192 | 2025-08-01 | united kingdom | male | 64.0 | Muscle spasticity,Neuropathy peripheral,Fatigue,Sexual dysfunction,Constipation,Brain fog,Tendonitis,Neurogenic bladder,Polyneuropathy,Hypersensitivity,Vertigo,Small fibre neuropathy,Stiff leg syndrome,Muscle atrophy,Taste disorder,Anxiety,Neurogenic bowel,Myoclonus,Muscular weakness,Paralysis,Medication error | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovering/resolving,unknown |
| 25635934 | 2025-08-03 | eu | male | 39.0 | Hypertriglyceridaemia,Cough | serious | yes | recovered/resolved,unknown |
| 25637229 | 2025-08-04 | united kingdom | female | 76.0 | Decreased appetite,Hypotension,Nausea | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25638178 | 2025-08-04 | united kingdom | female | 64.0 | Hyperglycaemia | serious | yes | recovered/resolved |
| 25638316 | 2025-08-04 | united kingdom | male | 60.0 | Vision blurred,Muscle rigidity | serious | yes | not recovered/not resolved/ongoing,recovered/resolved |
| 25642621 | 2025-08-05 | united kingdom | male | 75.0 | Arthralgia,Myalgia,Fatigue,Brain fog,Depressed level of consciousness,Memory impairment,Pain in extremity,Tendonitis | serious | yes | recovered/resolved with sequelae,recovered/resolved,recovered/resolved,recovered/resolved,recovering/resolving,not recovered/not resolved/ongoing,recovered/resolved,unknown |
| 25642687 | 2025-08-05 | united kingdom | male | 75.0 | Tremor,Balance disorder,Feeling abnormal | serious | yes | unknown,recovered/resolved,unknown |
| 25642951 | 2025-08-05 | united kingdom | male | 66.0 | Diarrhoea | serious | yes | not recovered/not resolved/ongoing |
| 25643008 | 2025-08-05 | eu | male | 61.0 | Adverse event,Epistaxis,Pruritus,Alopecia,White blood cell count decreased | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25643903 | 2025-08-05 | eu | male | 34.0 | Therapy non-responder | serious | yes | unknown |
| 25643954 | 2025-08-05 | eu | female | missing | Pancytopenia,Tongue discolouration,Tooth discolouration | serious | yes | unknown,recovering/resolving,recovering/resolving |
| 25644154 | 2025-08-05 | united kingdom | female | 89.0 | Epistaxis,Product prescribing issue | serious | yes | unknown,unknown |
| 25647220 | 2025-08-06 | eu | male | 76.0 | BRASH syndrome,Hyperkalaemia,Bradycardia,Gastrointestinal haemorrhage,Toxicity to various agents,Condition aggravated,Renal failure,Haemoglobin decreased,Acute kidney injury,Melaena,Fatigue,Dyspnoea,Hypotension,Pallor,Blood creatinine increased,Glomerular filtration rate decreased,Blood urea increased | serious | yes | recovered/resolved,unknown,unknown,recovered/resolved,unknown,unknown,unknown,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,unknown,unknown,recovering/resolving,recovering/resolving,recovering/resolving |
| 25647682 | 2025-08-06 | eu | female | 65.0 | Cardiogenic shock,Distributive shock,Altered state of consciousness,Multiple organ dysfunction syndrome,Respiratory failure,Acute kidney injury,Hypoxia,Liver injury,Electrocardiogram QT prolonged,Hepatic function abnormal,Renal impairment,Hypotension,Bradycardia,Asthenia,Intentional overdose,Toxicity to various agents,Drug ineffective,Depressed level of consciousness,Overdose | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,recovered/resolved |
| 25649473 | 2025-08-06 | united kingdom | missing | 74.0 | Hypothyroidism,Abnormal weight gain,Blood glucose increased,Dizziness,Dyspnoea | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovered/resolved with sequelae,recovered/resolved with sequelae |
| 25654415 | 2025-08-07 | eu | male | 54.0 | Hyperkalaemia,Acute kidney injury,Hypoglycaemia,Metabolic acidosis | serious | yes | unknown,unknown,unknown,unknown |
| 25654484 | 2025-08-07 | eu | male | 78.0 | Acute kidney injury,Bradycardia,Fall | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25658366 | 2025-08-08 | united kingdom | male | 70.0 | Anal fissure | serious | yes | not recovered/not resolved/ongoing |
| 25658721 | 2025-08-08 | united kingdom | female | 84.0 | Joint swelling | serious | yes | recovering/resolving |
| 25658941 | 2025-08-08 | eu | female | 93.0 | Lip oedema | serious | yes | recovering/resolving |
| 25658980 | 2025-08-08 | eu | female | 22.0 | Bradycardia,Psychomotor skills impaired,Hypotension,Toxicity to various agents | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25669701 | 2025-08-12 | eu | female | 91.0 | Renal impairment,Hyperkalaemia | serious | yes | unknown,unknown |
| 25674938 | 2025-08-13 | eu | male | 84.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 25678941 | 2025-08-14 | eu | female | 82.0 | Transaminases increased,Drug interaction | serious | yes | recovered/resolved,recovered/resolved |
| 25679791 | 2025-08-14 | united kingdom | male | 38.0 | Cardiac arrest,Brain injury,Overdose | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25679800 | 2025-08-14 | eu | male | 42.0 | Bradyarrhythmia | serious | yes | recovered/resolved |
| 25684646 | 2025-08-15 | united kingdom | female | 76.0 | Epistaxis | serious | yes | not recovered/not resolved/ongoing |
| 25684730 | 2025-08-15 | eu | female | 61.0 | Hyperkalaemia,Acute kidney injury,Poisoning deliberate,Metabolic acidosis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25686817 | 2025-08-16 | eu | female | 77.0 | Atrioventricular block,Asthenia | serious | yes | recovered/resolved,recovered/resolved |
| 25686979 | 2025-08-16 | eu | female | 68.0 | Hypotension,Vertigo,Tachycardia,Fatigue,Chest pain,Erythema,Contusion,Peripheral swelling,Pain,Arteriosclerosis,Cardiomegaly,Arterial occlusive disease | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovering/resolving,recovering/resolving,unknown,unknown,unknown |
| 25686995 | 2025-08-16 | eu | male | missing | Hypospadias,Foetal exposure during pregnancy | serious | yes | not recovered/not resolved/ongoing,unknown |
| 25687004 | 2025-08-16 | eu | male | 15.0 | Drug ineffective | serious | yes | unknown |
| 25687520 | 2025-08-17 | eu | male | 41.0 | Drug ineffective | serious | yes | unknown |
| 25687522 | 2025-08-17 | eu | male | 49.0 | Dizziness,Discomfort,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,recovering/resolving |
| 25687523 | 2025-08-17 | united kingdom | female | 79.0 | Pharyngeal paraesthesia,Paraesthesia oral | serious | yes | recovered/resolved,unknown |
| 25688713 | 2025-08-18 | eu | female | 76.0 | Swollen tongue,Asphyxia,Drug hypersensitivity | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25689422 | 2025-08-18 | eu | female | 83.0 | Dermatitis bullous | serious | yes | recovering/resolving |
| 25698103 | 2025-08-19 | united kingdom | female | 76.0 | Hypomagnesaemia | serious | yes | recovered/resolved |
| 25698371 | 2025-08-19 | united kingdom | female | 90.0 | Hyponatraemia,Cough | serious | yes | recovered/resolved with sequelae,unknown |
| 25698586 | 2025-08-19 | eu | female | 78.0 | Gastrointestinal haemorrhage,Drug interaction,Coagulation factor deficiency | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25704866 | 2025-08-20 | eu | female | 88.0 | Bradycardia,Hyponatraemia,Melaena,Acute kidney injury | serious | yes | recovering/resolving,recovering/resolving,recovered/resolved,recovered/resolved |
| 25705220 | 2025-08-20 | united kingdom | missing | 77.0 | Atrioventricular block,Bradycardia | serious | yes | recovered/resolved,recovered/resolved |
| 25709907 | 2025-08-21 | eu | female | 76.0 | Acute kidney injury,Chronic kidney disease,Gastrointestinal disorder,Hypotension,Weight decreased,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25715605 | 2025-08-22 | eu | male | 66.0 | Sepsis,Pancytopenia | serious | yes | fatal,fatal |
| 25718300 | 2025-08-23 | united kingdom | male | missing | Dyspnoea,Heart rate irregular | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25721209 | 2025-08-25 | eu | male | 80.0 | Hypotension | serious | yes | recovered/resolved |
| 25721285 | 2025-08-25 | eu | male | 78.0 | Drug ineffective | serious | yes | unknown |
| 25722723 | 2025-08-25 | eu | male | 70.0 | Toxic skin eruption,Eye infection gonococcal,Rash macular,Rash,Conjunctivitis,Cheilitis,Urethritis,Skin exfoliation | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25724308 | 2025-08-26 | eu | female | 74.0 | Myelitis,Condition aggravated,Insomnia,Tremor,Drug ineffective | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovered/resolved,unknown |
| 25724320 | 2025-08-26 | eu | female | 73.0 | Medication error,Haematoma,Anticholinergic effect,Patient elopement,Fall,Confusional state,Dizziness,Daydreaming,Drug interaction,Drug ineffective | serious | yes | unknown,unknown,unknown,unknown,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25724984 | 2025-08-26 | eu | male | 49.0 | Discomfort,Dizziness,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,recovering/resolving |
| 25725402 | 2025-08-26 | united kingdom | male | 74.0 | Hiccups | serious | yes | not recovered/not resolved/ongoing |
| 25733394 | 2025-08-28 | united kingdom | female | 87.0 | Bradycardia,Confusional state,Hallucination,Lethargy | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25733972 | 2025-08-28 | eu | male | 72.0 | Haematoma | serious | yes | not recovered/not resolved/ongoing |
| 25734619 | 2025-08-28 | united kingdom | female | 79.0 | Headache,Dyspnoea,Cough,Fatigue,Balance disorder,Diarrhoea,Hyperhidrosis | serious | yes | recovered/resolved,recovering/resolving,recovering/resolving,recovering/resolving,recovered/resolved,recovered/resolved,recovering/resolving |
| 25734623 | 2025-08-28 | united kingdom | male | 72.0 | Dyspnoea | serious | yes | recovered/resolved |
| 25734654 | 2025-08-28 | eu | missing | 78.0 | Cardiovascular disorder,Acute kidney injury,Hyperkalaemia,Dyspnoea,Hypotension | serious | yes | unknown,unknown,unknown,recovering/resolving,unknown |
| 25734921 | 2025-08-28 | eu | female | 72.0 | Hepatic cytolysis,Dyskinesia | serious | yes | recovering/resolving,recovered/resolved |
| 25735161 | 2025-08-28 | eu | female | 77.0 | Dizziness,Gastrooesophageal reflux disease,Injection site erythema,Dry mouth,Depressed mood,Abdominal pain upper,Hyperhidrosis,Headache,Decreased appetite,Apathy,Hiatus hernia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown |
| 25738427 | 2025-08-29 | eu | female | 39.0 | Agranulocytosis | serious | yes | recovered/resolved |
| 25738433 | 2025-08-29 | eu | male | 15.0 | Condition aggravated,Hypoprothrombinaemia | serious | yes | recovered/resolved,recovered/resolved |
| 25739941 | 2025-08-29 | eu | female | 13.0 | Pericardial effusion,Mitral valve incompetence,Myocarditis,Pericarditis,Drug ineffective,Weight increased | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovering/resolving,recovered/resolved,unknown |
| 25740041 | 2025-08-29 | eu | male | 73.0 | Progressive multifocal leukoencephalopathy,Encephalitis | serious | yes | fatal,not recovered/not resolved/ongoing |
| 25740087 | 2025-08-29 | united kingdom | female | 75.0 | Joint swelling,Peripheral swelling | serious | yes | unknown,recovered/resolved |
| 25744485 | 2025-09-01 | united kingdom | female | 72.0 | Lip swelling | serious | yes | recovered/resolved |
| 25744500 | 2025-09-01 | united kingdom | female | 79.0 | Acute generalised exanthematous pustulosis | serious | yes | recovered/resolved |
| 25745093 | 2025-09-01 | eu | female | 75.0 | Spontaneous haematoma | serious | yes | recovering/resolving |
| 25745094 | 2025-09-01 | united kingdom | missing | 93.0 | Atrioventricular block first degree | serious | yes | unknown |
| 25745112 | 2025-09-01 | eu | male | 67.0 | Epidural lipomatosis | serious | yes | not recovered/not resolved/ongoing |
| 25745734 | 2025-09-01 | united kingdom | female | 76.0 | Hypomagnesaemia | serious | yes | recovered/resolved |
| 25745939 | 2025-09-01 | eu | female | missing | Deafness,Palpitations,Heart rate abnormal,Tinnitus,Autonomic nervous system imbalance,Blood pressure decreased | serious | yes | not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved |
| 25745996 | 2025-09-01 | eu | female | 93.0 | Fall | serious | yes | fatal |
| 25749000 | 2025-09-02 | eu | female | 73.0 | Medication error,Haematoma,Anticholinergic effect,Patient elopement,Fall,Confusional state,Dizziness,Daydreaming,Disturbance in attention,Drug interaction,Drug ineffective | serious | yes | unknown,unknown,recovered/resolved,recovered/resolved,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 25749459 | 2025-09-02 | eu | female | 60.0 | Pancytopenia,Febrile neutropenia,Pneumonitis,Intestinal perforation | serious | yes | fatal,fatal,fatal,fatal |
| 25749606 | 2025-09-02 | eu | male | 68.0 | Angina unstable,Apnoea,Arthrodesis,Loss of personal independence in daily activities,Respiratory disorder,Articular disc disorder,Ill-defined disorder,Emphysema,Breath sounds abnormal,Back pain,Neck pain,Hyporeflexia,Arthralgia,Chest pain,Spinal pain,Fatigue,Obstructive sleep apnoea syndrome | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25750061 | 2025-09-02 | eu | male | 66.0 | Arteriospasm coronary | serious | yes | recovered/resolved |
| 25750372 | 2025-09-02 | united kingdom | male | 61.0 | Myalgia,Joint swelling,Confusional state,Hyperhidrosis,Burning sensation | serious | yes | unknown,unknown,unknown,recovered/resolved,unknown |
| 25753756 | 2025-09-03 | eu | female | 70.0 | Multiple drug therapy,Acute kidney injury,Hyperkalaemia,Renal impairment | serious | yes | recovering/resolving,recovered/resolved,recovered/resolved,recovered/resolved |
| 25754449 | 2025-09-03 | united kingdom | male | 52.0 | Hepatic function abnormal | serious | yes | recovering/resolving |
| 25754453 | 2025-09-03 | united kingdom | male | 68.0 | Interstitial lung disease | serious | yes | unknown |
| 25754545 | 2025-09-03 | eu | male | 83.0 | Haemorrhage,Distributive shock | serious | yes | recovering/resolving,recovering/resolving |
| 25773137 | 2025-09-08 | canada | male | 3.0 | Myocarditis,Drug interaction,Tachycardia | serious | yes | recovered/resolved,unknown,unknown |
| 25776917 | 2025-09-09 | eu | female | 68.0 | Dilated cardiomyopathy | serious | yes | unknown |
| 25784665 | 2025-09-10 | canada | male | 67.0 | Acute kidney injury,Haemofiltration,Tubulointerstitial nephritis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25784897 | 2025-09-10 | canada | female | 85.0 | COVID-19,Throat irritation,Cough,Fatigue,Pharyngeal paraesthesia,Pneumonia,Pyrexia,Off label use,Circumstance or information capable of leading to medication error | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25785032 | 2025-09-10 | canada | female | 69.0 | Pruritus,Skin exfoliation,Skin reaction | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25785041 | 2025-09-10 | eu | female | 70.0 | Cholestatic liver injury,Eosinophilia | serious | yes | recovered/resolved,recovered/resolved |
| 25785294 | 2025-09-10 | eu | male | 79.0 | Plasma cell myeloma | serious | yes | unknown |
| 25785418 | 2025-09-10 | eu | male | 67.0 | Epidural lipomatosis | serious | yes | not recovered/not resolved/ongoing |
| 25789067 | 2025-09-11 | canada | female | 48.0 | Food allergy,Arthralgia,Arthritis | serious | yes | unknown,unknown,unknown |
| 25789513 | 2025-09-11 | canada | female | 85.0 | Throat irritation,COVID-19,Circumstance or information capable of leading to medication error,Cough,Fatigue,Pharyngeal paraesthesia,Pneumonia,Pyrexia,Off label use | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25789916 | 2025-09-11 | eu | male | 68.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 25789952 | 2025-09-11 | eu | female | 77.0 | Dyspnoea,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved |
| 25790552 | 2025-09-11 | canada | male | 75.0 | Dermatitis atopic,Drug eruption | serious | yes | recovering/resolving,recovering/resolving |
| 25798718 | 2025-09-13 | eu | female | 74.0 | Bradycardia,Conduction disorder,Condition aggravated | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25798751 | 2025-09-13 | eu | female | 83.0 | Pneumocystis jirovecii pneumonia,Acute respiratory distress syndrome | serious | yes | fatal,fatal |
| 25798821 | 2025-09-13 | eu | female | 69.0 | Hypothyroidism,Condition aggravated | serious | yes | recovering/resolving,recovering/resolving |
| 25799020 | 2025-09-13 | united kingdom | female | 70.0 | Self-injurious ideation,Anxiety | serious | yes | recovering/resolving,recovering/resolving |
| 25799135 | 2025-09-13 | eu | female | 60.0 | Drug ineffective,Dyspnoea,Atrioventricular block complete,Hypotension,Anaemia,Off label use | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown |
| 25799610 | 2025-09-14 | eu | male | 65.0 | Orthostatic hypotension,Fall,Malaise,Drug interaction | serious | yes | recovered/resolved with sequelae,recovered/resolved with sequelae,recovered/resolved with sequelae,not recovered/not resolved/ongoing |
| 25799644 | 2025-09-14 | united kingdom | female | 86.0 | Gout | serious | yes | unknown |
| 25801607 | 2025-09-15 | eu | male | 64.0 | Pelvic pain,Vomiting | serious | yes | unknown,unknown |
| 25801745 | 2025-09-15 | canada | female | 75.0 | Seizure,Metabolic acidosis | serious | yes | recovering/resolving,recovering/resolving |
| 25801815 | 2025-09-15 | united kingdom | male | 59.0 | Gingival hypoplasia,Gingival hypertrophy | serious | yes | unknown,unknown |
| 25802218 | 2025-09-15 | united kingdom | male | 59.0 | Hypokalaemia | serious | yes | unknown |
| 25805062 | 2025-09-16 | eu | missing | 48.0 | Renal impairment,Hypotension,Drug intolerance | serious | yes | recovering/resolving,recovered/resolved,recovering/resolving |
| 25805267 | 2025-09-16 | united kingdom | missing | 69.0 | Pneumonitis | serious | yes | fatal |
| 25805853 | 2025-09-16 | eu | male | 76.0 | Hospitalisation,Fall,Tooth loss | serious | yes | unknown,unknown,unknown |
| 25807053 | 2025-09-16 | eu | male | 82.0 | Hypotension,Malaise,Potentiating drug interaction | serious | yes | not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved |
| 25815498 | 2025-09-18 | eu | female | 63.0 | Death,Coma scale abnormal,Hypokalaemia,Confusional state | serious | yes | fatal,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25815504 | 2025-09-18 | united kingdom | female | 64.0 | Somnolence,Dry mouth,Dysarthria,Confusional state | serious | yes | not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved,recovered/resolved |
| 25816331 | 2025-09-18 | united kingdom | male | 77.0 | Confusional state | serious | yes | not recovered/not resolved/ongoing |
| 25816737 | 2025-09-18 | united kingdom | female | 73.0 | Oral lichenoid reaction,Glossitis,Mouth ulceration | serious | yes | recovered/resolved,unknown,unknown |
| 25817340 | 2025-09-18 | eu | male | 79.0 | Acute kidney injury,Pneumonia,Neurogenic bladder,Tooth disorder,Off label use | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 25817510 | 2025-09-18 | eu | male | missing | Dyspnoea,Anaemia | serious | yes | fatal,recovering/resolving |
| 25817526 | 2025-09-18 | eu | female | 74.0 | Respiratory failure,Hypercapnia,Chronic inflammatory demyelinating polyradiculoneuropathy,Infection,Pneumonia aspiration,Somnolence,Epilepsy,Malaise,Fall,Delirium,Neurological decompensation,Drug ineffective,Encephalopathy | serious | yes | fatal,fatal,not recovered/not resolved/ongoing,unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown |
| 25818402 | 2025-09-18 | eu | female | 82.0 | Hyponatraemia,Dizziness | serious | yes | recovered/resolved,recovered/resolved |
| 25818451 | 2025-09-18 | eu | male | 77.0 | Angina pectoris | serious | yes | recovered/resolved |
| 25820563 | 2025-09-19 | eu | male | missing | Hypertension,Product size issue | serious | yes | unknown,unknown |
| 25821892 | 2025-09-19 | canada | male | 91.0 | Blood loss anaemia neonatal | serious | yes | recovered/resolved |
| 25826878 | 2025-09-20 | united kingdom | male | 75.0 | Pneumonitis,Pneumonia,Respiratory failure | serious | yes | fatal,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25829019 | 2025-09-22 | eu | male | missing | Hypotension,Wrong patient received product,Wrong drug | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25829287 | 2025-09-22 | united kingdom | female | 82.0 | Neurological symptom | serious | yes | recovered/resolved |
| 25829610 | 2025-09-22 | canada | male | 74.0 | Contusion,Dyspnoea exertional,Presyncope,Swelling,Tenderness | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25829806 | 2025-09-22 | canada | female | 88.0 | Thrombosis,Haematuria | serious | yes | recovered/resolved,recovered/resolved |
| 25829975 | 2025-09-22 | eu | female | 78.0 | Rash,Oral mucosa erosion,Lip erosion | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving |
| 25830841 | 2025-09-22 | united kingdom | female | 67.0 | Arthralgia,Nightmare | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25831123 | 2025-09-22 | eu | male | 79.0 | Cerebral haematoma | serious | yes | recovered/resolved with sequelae |
| 25835995 | 2025-09-23 | eu | male | 65.0 | Inappropriate antidiuretic hormone secretion,Hyponatraemia,Chest pain,Pulmonary mass,Paraneoplastic syndrome,Dry mouth | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown |
| 25839297 | 2025-09-24 | indonesia | male | 56.0 | Drug ineffective | serious | yes | unknown |
| 25839565 | 2025-09-24 | united kingdom | female | 65.0 | Gastrointestinal haemorrhage,Oesophageal intramural haematoma,Upper gastrointestinal haemorrhage | serious | yes | unknown,recovered/resolved,recovered/resolved |
| 25847005 | 2025-09-25 | canada | female | 72.0 | Seizure,Coma scale abnormal,Cyanosis,Postictal state,Endotracheal intubation | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25852510 | 2025-09-26 | eu | male | 87.0 | Hepatitis acute | serious | yes | recovered/resolved |
| 25857209 | 2025-09-29 | united kingdom | male | 60.0 | Chest pain,Angina pectoris,Paraesthesia,Dyspnoea | serious | yes | not recovered/not resolved/ongoing,unknown,unknown,unknown |
| 25857694 | 2025-09-29 | canada | male | 68.0 | Pericardial effusion,Pulmonary embolism | serious | yes | fatal,fatal |
| 25857706 | 2025-09-29 | eu | female | 78.0 | Cardiogenic shock,Hyperkalaemia,Bradycardia | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25858087 | 2025-09-29 | eu | female | 61.0 | Acute kidney injury,Distributive shock,Diarrhoea | serious | yes | recovered/resolved,recovered/resolved,recovering/resolving |
| 25858101 | 2025-09-29 | eu | male | 59.0 | Myocardial ischaemia,Carotid artery occlusion,Drug ineffective | serious | yes | unknown,unknown,recovering/resolving |
| 25862410 | 2025-09-30 | canada | male | 69.0 | Aortic arteriosclerosis,Hepatic cancer stage IV,Hepatic cirrhosis,Hepatic steatosis,Malignant neoplasm progression,Portal hypertension,Metastases to spine | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25862611 | 2025-09-30 | eu | male | 75.0 | Colitis microscopic | serious | yes | not recovered/not resolved/ongoing |
| 25867406 | 2025-10-01 | united kingdom | female | 63.0 | Pruritus,Rash | serious | yes | unknown,recovered/resolved |
| 25868162 | 2025-10-01 | united kingdom | male | 83.0 | Acute kidney injury | serious | yes | recovered/resolved |
| 25872465 | 2025-10-02 | canada | female | 61.0 | Wheezing,Aphonia,Arthralgia,Body temperature decreased,Cough,Drug hypersensitivity,Ear infection,Hypoventilation,Limb discomfort,Middle ear effusion,Nasopharyngitis,Pneumonia,Productive cough,Rash,Sinusitis,Tendonitis,Tissue injury,Weight decreased,Road traffic accident,Off label use,Accident,Product use issue,Wrong technique in product usage process | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25872501 | 2025-10-02 | eu | male | 92.0 | Toxic encephalopathy,Accidental overdose | serious | yes | recovered/resolved,recovered/resolved |
| 25872586 | 2025-10-02 | eu | female | 64.0 | Pancreatitis necrotising | serious | yes | recovering/resolving |
| 25872668 | 2025-10-02 | eu | male | 42.0 | Conjunctival irritation | serious | yes | recovered/resolved |
| 25875603 | 2025-10-03 | eu | male | 50.0 | Thrombosis mesenteric vessel,Product communication issue,Product administration error | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25877069 | 2025-10-03 | eu | female | 81.0 | Hypotension,Ulcer haemorrhage | serious | yes | recovering/resolving,recovering/resolving |
| 25880211 | 2025-10-04 | united kingdom | female | 54.0 | Behaviour disorder,Irritability,Anger,Impatience,Tearfulness,Apathy,Social avoidant behaviour | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25880636 | 2025-10-04 | united kingdom | female | 68.0 | Migraine with aura | serious | yes | not recovered/not resolved/ongoing |
| 25883655 | 2025-10-06 | eu | female | 2.0 | Foetal growth restriction,Premature baby,Maternal exposure during pregnancy | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25883849 | 2025-10-06 | united kingdom | female | 41.0 | Diarrhoea haemorrhagic | serious | yes | not recovered/not resolved/ongoing |
| 25883946 | 2025-10-06 | eu | male | 57.0 | Hepatitis cholestatic,Hyperbilirubinaemia | serious | yes | recovered/resolved,recovered/resolved |
| 25884142 | 2025-10-06 | eu | female | 90.0 | Presyncope,Hypotension,Bradycardia | serious | yes | unknown,unknown,unknown |
| 25884306 | 2025-10-06 | united kingdom | female | 64.0 | Haematuria | serious | yes | unknown |
| 25884439 | 2025-10-06 | eu | female | 64.0 | Atrial fibrillation,Vomiting,Oral candidiasis,Constipation,Alopecia,White blood cell count decreased | serious | yes | recovered/resolved,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved,recovered/resolved |
| 25884461 | 2025-10-06 | eu | male | 24.0 | Euglycaemic diabetic ketoacidosis | serious | yes | recovered/resolved |
| 25888115 | 2025-10-07 | united kingdom | male | 76.0 | Aggression | serious | yes | recovered/resolved |
| 25888753 | 2025-10-07 | eu | male | 84.0 | Pancytopenia | serious | yes | recovered/resolved |
| 25888756 | 2025-10-07 | eu | female | 68.0 | Rhabdomyolysis,Lung disorder | serious | yes | recovered/resolved,recovered/resolved |
| 25889670 | 2025-10-07 | united kingdom | female | missing | Medication error,Toxicity to various agents | serious | yes | unknown,recovering/resolving |
| 25889823 | 2025-10-07 | eu | male | 79.0 | Treatment failure | serious | yes | unknown |
| 25889979 | 2025-10-07 | eu | female | 44.0 | Arrhythmia,Chest pain,Malaise,Palpitations,Asthenia,Electrocardiogram QT prolonged,Long QT syndrome,Syncope,Presyncope | serious | yes | recovering/resolving,unknown,unknown,unknown,unknown,recovering/resolving,recovering/resolving,unknown,unknown |
| 25890142 | 2025-10-07 | united kingdom | male | missing | Renal haemorrhage,Rectal haemorrhage,Epistaxis,Medication error | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,unknown |
| 25893210 | 2025-10-08 | eu | female | 93.0 | Atrioventricular block | serious | yes | unknown |
| 25893794 | 2025-10-08 | united kingdom | female | 56.0 | Nausea,Atrial fibrillation,Pain,Medication error | serious | yes | not recovered/not resolved/ongoing,recovering/resolving,not recovered/not resolved/ongoing,unknown |
| 25895271 | 2025-10-08 | eu | male | 59.0 | Pneumonitis | serious | yes | recovered/resolved |
| 25895575 | 2025-10-08 | eu | female | 79.0 | Electrocardiogram QT prolonged,Hypomagnesaemia,Hypocalcaemia,Hypoparathyroidism,Vomiting,Vertigo | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25899124 | 2025-10-09 | eu | male | 70.0 | Therapeutic product effect incomplete | serious | yes | unknown |
| 25899198 | 2025-10-09 | eu | male | 72.0 | Hallucination,Dopamine supersensitivity psychosis,Intestinal obstruction,Infusion site infection,Cognitive disorder,Paradoxical drug reaction,Neurogenic bowel,Aggression,Disorientation,On and off phenomenon,Parkinsonism,Anxiety,Restlessness,Tremor,Executive dysfunction,Mental disorder,Constipation | serious | yes | recovered/resolved,unknown,unknown,unknown,unknown,unknown,unknown,recovered/resolved,unknown,unknown,recovered/resolved,recovered/resolved,unknown,recovered/resolved,unknown,unknown,unknown |
| 25899203 | 2025-10-09 | eu | male | 67.0 | Rhabdomyolysis,Hepatic cytolysis,Drug interaction | serious | yes | recovering/resolving,recovering/resolving,recovered/resolved |
| 25900475 | 2025-10-09 | united kingdom | male | 84.0 | Mood altered,Depressed mood | serious | yes | recovered/resolved,recovered/resolved |
| 25903938 | 2025-10-10 | united kingdom | female | 73.0 | Blood glucose decreased,Dizziness,Dyspepsia,Abdominal pain | serious | yes | not recovered/not resolved/ongoing,unknown,unknown,unknown |
| 25904938 | 2025-10-10 | eu | female | 73.0 | Febrile bone marrow aplasia | serious | yes | fatal |
| 25905431 | 2025-10-10 | eu | male | 54.0 | Toxicity to various agents,Bradycardia,Atrioventricular block second degree | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25905773 | 2025-10-10 | eu | male | 61.0 | Acute kidney injury,Hypovolaemic shock | serious | yes | fatal,fatal |
| 25905855 | 2025-10-10 | eu | female | 84.0 | Cerebellar haemorrhage | serious | yes | fatal |
| 25912915 | 2025-10-13 | united kingdom | female | 60.0 | Plantar fasciitis | serious | yes | recovered/resolved |
| 25913053 | 2025-10-13 | eu | female | 86.0 | Dyspnoea | serious | yes | unknown |
| 25916674 | 2025-10-14 | united kingdom | female | 82.0 | Gastrooesophageal reflux disease | serious | yes | not recovered/not resolved/ongoing |
| 25917511 | 2025-10-14 | united kingdom | male | missing | Immune-mediated encephalitis,Antiphospholipid syndrome,Immune thrombocytopenia | serious | yes | fatal,unknown,unknown |
| 25917764 | 2025-10-14 | eu | female | 79.0 | Anaemia,Drug interaction | serious | yes | recovered/resolved,recovered/resolved |
| 25918547 | 2025-10-14 | eu | male | 66.0 | Cutaneous vasculitis | serious | yes | recovering/resolving |
| 25918660 | 2025-10-14 | eu | female | 75.0 | Cholestasis | serious | yes | recovering/resolving |
| 25922795 | 2025-10-15 | eu | female | 58.0 | Neuropathy peripheral | serious | yes | not recovered/not resolved/ongoing |
| 25922962 | 2025-10-15 | eu | female | 71.0 | Cholestasis | serious | yes | recovering/resolving |
| 25923080 | 2025-10-15 | eu | female | 78.0 | Dizziness,Vitamin B12 deficiency,Diabetes mellitus inadequate control,Acute kidney injury | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25923212 | 2025-10-15 | eu | female | 84.0 | Drug abuse,Presyncope | serious | yes | unknown,unknown |
| 25923213 | 2025-10-15 | eu | male | 76.0 | Hyponatraemia | serious | yes | recovering/resolving |
| 25923395 | 2025-10-15 | eu | female | 89.0 | Acute kidney injury,Hypokalaemia | serious | yes | recovering/resolving,recovering/resolving |
| 25924279 | 2025-10-15 | eu | male | 66.0 | Renal failure | serious | yes | recovering/resolving |
| 25927859 | 2025-10-16 | eu | male | 93.0 | Toxic encephalopathy,Generalised tonic-clonic seizure,Myoclonic epilepsy | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25929827 | 2025-10-16 | united kingdom | male | 91.0 | Haematemesis,Haematochezia,Medication error | serious | yes | recovering/resolving,recovering/resolving,unknown |
| 25933055 | 2025-10-17 | eu | female | 80.0 | Disease progression,Hyponatraemia | serious | yes | fatal,recovered/resolved |
| 25933899 | 2025-10-17 | united kingdom | male | 74.0 | Nightmare | serious | yes | not recovered/not resolved/ongoing |
| 25934171 | 2025-10-17 | eu | male | 80.0 | Subdural haematoma | serious | yes | recovered/resolved |
| 25934202 | 2025-10-17 | united kingdom | missing | 52.0 | Suicidal ideation | serious | yes | recovered/resolved |
| 25934251 | 2025-10-17 | eu | female | 86.0 | Pancreatitis chronic | serious | yes | recovered/resolved |
| 25934532 | 2025-10-17 | united kingdom | male | 46.0 | Atrioventricular block complete | serious | yes | unknown |
| 25937530 | 2025-10-18 | eu | female | missing | Liver function test increased,Hepatic enzyme increased,Gamma-glutamyltransferase increased,Aspartate aminotransferase increased,Alanine aminotransferase increased,Blood alkaline phosphatase increased | serious | yes | recovered/resolved,recovered/resolved,unknown,unknown,unknown,unknown |
| 25937620 | 2025-10-18 | united kingdom | female | 81.0 | Cognitive disorder,Tremor | serious | yes | recovered/resolved,recovered/resolved |
| 25937648 | 2025-10-18 | eu | male | 43.0 | Cardiac arrest,Electrocardiogram ST segment abnormal,Myositis,Myopathy,Acute myocardial infarction,Rheumatic disorder,Myalgia,Fatigue,Dysphagia,Rhabdomyolysis,Acute coronary syndrome,Psoriatic arthropathy,Asthenia,Depression,Drug intolerance,Blood creatine phosphokinase increased,Hypoaesthesia,Paraesthesia,Arthralgia,Pustular psoriasis,Stenosis,Arterial occlusive disease,Chest pain,Angioplasty,Dyspnoea exertional,Skin lesion,Claustrophobia,Pruritus,Pain,Psoriasis,Back pain,Hyperuricaemia | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 25937867 | 2025-10-18 | eu | male | 63.0 | General physical health deterioration,Dyspnoea,Swelling,Drug ineffective,Treatment failure,Laboratory test abnormal,Clostridium difficile infection,Pain,Inflammatory marker increased,Oedema,Condition aggravated,Serratia infection,Clostridium difficile colitis,Anaemia,Hypervolaemia,Nephrotic syndrome,Oedema peripheral,Pleural effusion,Respiratory failure | serious | yes | unknown,recovering/resolving,recovering/resolving,recovered/resolved,unknown,unknown,recovered/resolved,unknown,recovering/resolving,unknown,unknown,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25942521 | 2025-10-21 | eu | male | 70.0 | International normalised ratio increased,Toxicity to various agents | serious | yes | unknown,unknown |
| 25943997 | 2025-10-21 | united kingdom | male | 73.0 | Brain fog,Morose | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25944056 | 2025-10-21 | united kingdom | male | 68.0 | Swollen tongue | serious | yes | recovering/resolving |
| 25946799 | 2025-10-22 | united states | female | 69.0 | Rhabdomyolysis,Hypokalaemia,Fall,Device programming error | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25952436 | 2025-10-23 | eu | female | 86.0 | Pancreatitis acute | serious | yes | recovered/resolved |
| 25954580 | 2025-10-24 | eu | male | 66.0 | Nightmare,Condition aggravated | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25955018 | 2025-10-24 | canada | male | 65.0 | Aortic dilatation,Bronchitis,Cardiac septal hypertrophy,Dilatation atrial,Mitral valve incompetence,Hyperhidrosis | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown |
| 25955228 | 2025-10-24 | united kingdom | female | 72.0 | Abdominal discomfort | serious | yes | unknown |
| 25955235 | 2025-10-24 | canada | female | 78.0 | Dizziness,Haematochezia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25955465 | 2025-10-24 | united kingdom | female | missing | Swollen tongue | serious | yes | recovered/resolved |
| 25955466 | 2025-10-24 | eu | female | 4.0 | Bone metabolism disorder,Myocardial injury,Blood creatinine decreased,Blood phosphorus decreased,Blood lactate dehydrogenase increased,Accidental exposure to product by child,Accidental overdose,Cardiotoxicity,Overdose,Accidental exposure to product | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,unknown |
| 25955530 | 2025-10-24 | eu | male | 81.0 | Haematuria | serious | yes | unknown |
| 25955552 | 2025-10-24 | united kingdom | female | 89.0 | Aphasia,Muscular weakness,Balance disorder | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25956016 | 2025-10-24 | united kingdom | male | 58.0 | Thrombocytopenia,Sepsis,Pyrexia | serious | yes | not recovered/not resolved/ongoing,unknown,unknown |
| 25956595 | 2025-10-24 | united kingdom | male | 74.0 | Wheezing | serious | yes | recovering/resolving |
| 25960740 | 2025-10-27 | eu | female | 29.0 | Trisomy 21,Foetal growth restriction,Premature baby,Maternal exposure during pregnancy | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovered/resolved |
| 25960741 | 2025-10-27 | eu | female | 69.0 | Acute respiratory distress syndrome | serious | yes | recovered/resolved |
| 25966305 | 2025-10-28 | eu | female | missing | Asthma,Infective exacerbation of asthma,Dyspnoea exertional,Infection | serious | yes | recovered/resolved,recovered/resolved,unknown,unknown |
| 25966344 | 2025-10-28 | eu | male | 63.0 | Device related thrombosis,Dyspepsia,Rash | serious | yes | unknown,recovered/resolved,recovered/resolved |
| 25967352 | 2025-10-28 | canada | female | 85.0 | Asthenia,Blood pressure increased,Dysarthria,Neoplasm malignant,Head and neck cancer metastatic,Tooth extraction,Feeding disorder,Heart rate increased,Hypersomnia,Respiratory rate increased,Expired product administered | serious | yes | fatal,fatal,fatal,fatal,fatal,fatal,fatal,fatal,fatal,fatal,fatal |
| 25967612 | 2025-10-28 | canada | female | 82.0 | Frequent bowel movements,Abdominal tenderness,Dizziness,Crohn^s disease | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25968033 | 2025-10-28 | eu | male | 74.0 | Syncope | serious | yes | recovered/resolved |
| 25968069 | 2025-10-28 | eu | male | 84.0 | Balance disorder,Fatigue,Decreased appetite,Aphonia,Dyspnoea,Thirst,Ketoacidosis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25968179 | 2025-10-28 | eu | female | 75.0 | Colitis microscopic | serious | yes | recovered/resolved |
| 25968362 | 2025-10-28 | eu | male | 89.0 | Subdural haematoma,Fall | serious | yes | fatal,fatal |
| 25968486 | 2025-10-28 | eu | female | 77.0 | Acute kidney injury,Drug interaction | serious | yes | fatal,fatal |
| 25968545 | 2025-10-28 | canada | female | 82.0 | Eosinophil count increased,Immunoglobulins increased,Petechiae,Rash maculo-papular | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25969138 | 2025-10-28 | united kingdom | female | 71.0 | Malaise | serious | yes | recovering/resolving |
| 25972607 | 2025-10-29 | eu | male | 76.0 | Respiratory failure,Interstitial lung disease | serious | yes | fatal,not recovered/not resolved/ongoing |
| 25973353 | 2025-10-29 | eu | female | 72.0 | Renal tubular necrosis,Acute kidney injury | serious | yes | recovered/resolved,recovered/resolved |
| 25973398 | 2025-10-29 | eu | male | 65.0 | Anaphylactic shock,Shock | serious | yes | recovered/resolved,recovered/resolved |
| 25974465 | 2025-10-29 | eu | male | 76.0 | Dyspnoea,Tubulointerstitial nephritis,Toxicity to various agents,Nephritis,Metabolic acidosis,Hypoglycaemia,Lethargy,Hyperlactacidaemia,Acute kidney injury,Clostridium difficile colitis,Disorientation,Blood creatinine increased,Enterococcal sepsis,Mitochondrial toxicity,Escherichia urinary tract infection | serious | yes | unknown,recovered/resolved,recovered/resolved,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,unknown,unknown,recovered/resolved,unknown,unknown,unknown |
| 25978327 | 2025-10-30 | eu | female | 90.0 | Renal failure,Hypotension | serious | yes | fatal,recovered/resolved |
| 25978488 | 2025-10-30 | eu | female | 74.0 | Erythema,Dyspnoea,Dysphagia,Pruritus | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25979265 | 2025-10-30 | eu | female | 4.0 | Myocardial injury,Heart rate decreased,Bone metabolism disorder,Accidental overdose | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25979408 | 2025-10-30 | eu | female | 59.0 | Loss of consciousness,Malaise,Hyperhidrosis,Urge incontinence | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25979414 | 2025-10-30 | eu | female | 74.0 | Death,Acute myocardial infarction,Breast cancer,Malignant neoplasm progression,Cardiogenic shock,Atrioventricular block complete | serious | yes | fatal,recovered/resolved,unknown,unknown,unknown,unknown |
| 25982005 | 2025-10-31 | eu | female | 85.0 | Pneumonia,Bronchopulmonary aspergillosis,Interstitial lung disease | serious | yes | recovering/resolving,recovering/resolving,not recovered/not resolved/ongoing |
| 25982363 | 2025-10-31 | eu | female | 78.0 | Subacute cutaneous lupus erythematosus | serious | yes | not recovered/not resolved/ongoing |
| 25985644 | 2025-11-01 | canada | female | 55.0 | Anaphylactic reaction,Cataract,Colitis ulcerative,Intervertebral disc protrusion,Multiple allergies,Drug ineffective,Off label use | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 25985696 | 2025-11-01 | united kingdom | female | 61.0 | Tachycardia | serious | yes | unknown |
| 25986361 | 2025-11-01 | united kingdom | male | 84.0 | Kidney infection,Lactic acidosis | serious | yes | unknown,unknown |
| 25986750 | 2025-11-01 | UA | male | missing | Off label use | serious | yes | unknown |
| 25988676 | 2025-11-03 | eu | male | 50.0 | Dermatitis acneiform,Neutropenia | serious | yes | recovered/resolved,recovered/resolved |
| 25988690 | 2025-11-03 | united kingdom | male | missing | Fournier^s gangrene | serious | yes | recovered/resolved |
| 25994857 | 2025-11-04 | canada | male | 70.0 | Activated partial thromboplastin time prolonged,Drug interaction,Treatment delayed | serious | yes | unknown,unknown,unknown |
| 25994875 | 2025-11-04 | canada | male | 53.0 | Abdominal discomfort,Alcohol poisoning,Adverse drug reaction,Arthritis,Bronchiectasis,Burns second degree,Catarrh,Cardiac murmur,COVID-19,Cerebrovascular accident,Colitis ulcerative,Condition aggravated,Confusional state,Deep vein thrombosis,Depression,Dysgeusia,Eczema,Fatigue,Frequent bowel movements,Gingival pain,Haematochezia,Headache,Hypopnoea,Impaired quality of life,Impaired work ability,Loss of personal independence in daily activities,Migraine,Nightmare,Pain,Pain in extremity,Parosmia,Palpitations,Product use in unapproved indication,Pulmonary embolism,Pyrexia,Rash,Rectal haemorrhage,Rhinitis,Somnolence,Steroid dependence,Stress,Swollen tongue,Systemic lupus erythematosus,Tinnitus,Tubulointerstitial nephritis,Vertigo,Weight decreased,Accidental overdose,Drug ineffective,Off label use,Inappropriate schedule of product administration,Intentional product use issue,Medication error | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25995167 | 2025-11-04 | canada | male | 77.0 | Blood potassium increased,Blood electrolytes increased,Cardiovascular function test abnormal,Cerebrovascular accident,Drug effect less than expected,Fatigue | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown |
| 25995338 | 2025-11-04 | united kingdom | male | missing | Muscle rupture | serious | yes | not recovered/not resolved/ongoing |
| 25995402 | 2025-11-04 | canada | female | 80.0 | Blood pressure diastolic decreased,Blood pressure fluctuation,Blood pressure systolic decreased,Constipation,Dizziness,Dyspepsia,Dyspnoea,Feeling abnormal,Food refusal,Haemorrhage,Heart rate decreased,Hypotension,Illness,Joint swelling,Limb injury,Malaise,Nausea,Oxygen saturation abnormal,Peripheral swelling,Pollakiuria,Productive cough,Vomiting,Weight decreased | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 25997993 | 2025-11-05 | eu | male | 73.0 | Chronic kidney disease | serious | yes | recovered/resolved with sequelae |
| 25998241 | 2025-11-05 | canada | female | 76.0 | Angiodysplasia,Gastrointestinal haemorrhage | serious | yes | fatal,fatal |
| 25998516 | 2025-11-05 | canada | male | 95.0 | Upper gastrointestinal haemorrhage,Gastric haemorrhage | serious | yes | fatal,unknown |
| 25999126 | 2025-11-05 | canada | female | 51.0 | Eczema,Haemorrhage,Nephrolithiasis,Psoriasis,Weight increased,Off label use | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown |
| 25999164 | 2025-11-05 | eu | female | 68.0 | Hypothyroidism | serious | yes | recovering/resolving |
| 25999218 | 2025-11-05 | canada | female | 57.0 | Anxiety,Arthritis,Circadian rhythm sleep disorder,Drug hypersensitivity,Dry throat,Fatigue,Flushing,Headache,Feeling cold,Joint swelling,Pruritus,Somnolence,Symptom recurrence,Urticaria,Product use issue,Inappropriate schedule of product administration,Off label use,Therapeutic response delayed,Wrong technique in product usage process | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 25999687 | 2025-11-05 | canada | female | 90.0 | Hypokalaemia,Acute kidney injury,Clostridium difficile colitis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 25999849 | 2025-11-05 | canada | female | 41.0 | Clostridium difficile colitis,Sepsis | serious | yes | recovering/resolving,recovering/resolving |
| 25999864 | 2025-11-05 | canada | male | 90.0 | Clostridium difficile colitis,Sepsis | serious | yes | recovered/resolved,recovered/resolved |
| 26002837 | 2025-11-06 | canada | male | 74.0 | Clostridium difficile infection,Clostridium test positive | serious | yes | unknown,unknown |
| 26003429 | 2025-11-06 | united kingdom | male | 66.0 | Medication error,Pain | serious | yes | unknown,recovering/resolving |
| 26003435 | 2025-11-06 | eu | female | 84.0 | Pneumonia aspiration | serious | yes | recovering/resolving |
| 26006197 | 2025-11-06 | canada | female | 63.0 | Vomiting,Abdominal pain,Adverse event,Alanine aminotransferase increased,Alopecia,Arthralgia,Arthritis,Arthropathy,Aspartate aminotransferase increased,Basal cell carcinoma,Blood parathyroid hormone decreased,Breath sounds abnormal,C-reactive protein increased,Condition aggravated,Deafness,Drug eruption,Drug hypersensitivity,Erythema,Fatigue,Granuloma skin,Headache,Hepatic enzyme increased,Hepatitis,Hypercalcaemia,Hypersensitivity,Hypertension,Inflammation,Infusion related reaction,Insomnia,Joint swelling,Musculoskeletal stiffness,Nausea,Pain,Panniculitis,Peripheral swelling,Pneumonia,Pruritus,Pulmonary fibrosis,Rash,Rash pruritic,Red blood cell sedimentation rate increased,Rheumatoid arthritis,Rheumatoid nodule,Skin necrosis,Skin ulcer,Ulcer,Synovitis,Loss of personal independence in daily activities,Drug intolerance,Drug tolerance decreased,Therapeutic product effect decreased,Product use issue,Prescribed underdose,Therapeutic product effect incomplete,Therapeutic response decreased,Treatment failure,Product use in unapproved indication,Contraindicated product administered,Drug ineffective,Off label use | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 26006245 | 2025-11-06 | eu | male | 91.0 | Malaise,Loss of consciousness,Hypotension,Somnolence,Bradycardia,Hyperkalaemia,Accidental poisoning,Wrong patient | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26013967 | 2025-11-08 | eu | male | 70.0 | Pancreatitis acute | serious | yes | recovering/resolving |
| 26013968 | 2025-11-08 | eu | female | 53.0 | Arrhythmia,Bradycardia | serious | yes | recovering/resolving,recovering/resolving |
| 26016360 | 2025-11-10 | canada | female | 70.0 | Blood pressure inadequately controlled,Headache,Concomitant disease aggravated,Migraine,Product substitution issue | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26017794 | 2025-11-10 | eu | male | 83.0 | International normalised ratio increased | serious | yes | recovering/resolving |
| 26019451 | 2025-11-10 | eu | female | 33.0 | Maternal exposure during pregnancy,Abortion spontaneous | serious | yes | recovered/resolved,recovered/resolved |
| 26024642 | 2025-11-11 | eu | male | 63.0 | Thyrotoxic crisis,Hyperthyroidism,Cardiac dysfunction,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,recovering/resolving,unknown |
| 26029134 | 2025-11-12 | united kingdom | female | 70.0 | Myalgia,Muscular weakness | serious | yes | recovered/resolved,recovered/resolved |
| 26029811 | 2025-11-12 | eu | male | 71.0 | Pseudocellulitis,Erysipelas,Cardiac failure,Oedema,Pyrexia,Cellulitis,Oedema peripheral,Erythema,Pain,Drug interaction,C-reactive protein increased,Tissue infiltration,Skin fibrosis | serious | yes | recovered/resolved,unknown,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26030772 | 2025-11-12 | united kingdom | female | 73.0 | Eczema | serious | yes | recovered/resolved |
| 26030778 | 2025-11-12 | united kingdom | female | 91.0 | Glaucoma,Tachycardia,Hypertension,Fall,Skin laceration,Blood pressure increased,Weight decreased,Skin discolouration,Pain in extremity,Skin fragility,Oedema peripheral,Condition aggravated,Contusion,Erythema,Malaise,Peripheral swelling,Therapy interrupted | serious | yes | unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,recovering/resolving,unknown,unknown,unknown,unknown,unknown,unknown,unknown,recovering/resolving,recovering/resolving,recovering/resolving,unknown,unknown |
| 26031817 | 2025-11-12 | united kingdom | male | 64.0 | Jaundice,Hepatitis | serious | yes | recovered/resolved,recovering/resolving |
| 26032679 | 2025-11-12 | united kingdom | male | 89.0 | Hypotension,Loss of consciousness,Circulatory collapse,Medication error | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,unknown |
| 26032731 | 2025-11-12 | eu | female | 68.0 | Atrial fibrillation,Febrile neutropenia,Pancreatic atrophy,Renal failure,Large intestine infection,Tachycardia,Escherichia urinary tract infection,Urinary tract infection bacterial,Weight decreased | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing |
| 26032735 | 2025-11-12 | eu | female | 83.0 | Hyponatraemia | serious | yes | recovering/resolving |
| 26034227 | 2025-11-12 | eu | male | 67.0 | Chest pain,Tachycardia,Off label use | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26034345 | 2025-11-12 | eu | male | 28.0 | Atrioventricular block complete | serious | yes | recovered/resolved |
| 26038706 | 2025-11-13 | eu | male | 83.0 | Loss of consciousness,Toxicity to various agents,Hallucination,Urinary tract infection,Loss of personal independence in daily activities,Disorientation | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing,recovered/resolved |
| 26039356 | 2025-11-13 | eu | male | 95.0 | Cholestasis,Hepatic cytolysis,Accidental overdose,Wrong schedule | serious | yes | not recovered/not resolved/ongoing,recovering/resolving,recovered/resolved,recovered/resolved |
| 26044504 | 2025-11-14 | united kingdom | female | missing | Thrombocytopenia | serious | yes | fatal |
| 26048949 | 2025-11-15 | united kingdom | female | 54.0 | Arthralgia,Joint swelling,Myalgia | serious | yes | unknown,recovered/resolved,recovered/resolved |
| 26048967 | 2025-11-15 | eu | male | 75.0 | Cardiac failure,Chronic obstructive pulmonary disease,Atrial fibrillation,Oedema peripheral,Visual acuity reduced | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 26058398 | 2025-11-18 | eu | female | missing | Renal impairment,Fatigue,Constipation,Cough,Diarrhoea,Dry mouth,Influenza like illness,Nightmare,Hypoaesthesia,Rhinorrhoea,Myalgia,Arthralgia,Sleep disorder,Peripheral swelling,Visual impairment,Asthenia | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 26059255 | 2025-11-18 | eu | female | 73.0 | Pemphigoid | serious | yes | recovering/resolving |
| 26061711 | 2025-11-18 | eu | male | 67.0 | Pneumocystis jirovecii pneumonia,Secondary immunodeficiency | serious | yes | fatal,fatal |
| 26061723 | 2025-11-18 | canada | female | 70.0 | Anxiety,Depression,Polyuria | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26068196 | 2025-11-20 | united kingdom | male | missing | Drug hypersensitivity,Contraindicated product prescribed,Product prescribing issue,Seizure,Epistaxis,Aggression,Headache,Allergic reaction to excipient | serious | yes | not recovered/not resolved/ongoing,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 26068890 | 2025-11-20 | eu | male | 68.0 | Cerebellar syndrome | serious | yes | recovered/resolved |
| 26068904 | 2025-11-20 | canada | female | 84.0 | Vomiting,Abdominal distension,Arthralgia,Calcium deficiency,Cognitive disorder,Constipation,Decreased appetite,Depressed mood,Dizziness,Dry mouth,Eye pruritus,Fall,Fatigue,Gait disturbance,General physical health deterioration,Head injury,Hypotension,Insomnia,Lacrimation decreased,Loss of personal independence in daily activities,Nausea,Parkinson^s disease,Psychiatric symptom,Vitamin B12 deficiency | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 26068967 | 2025-11-20 | canada | male | 72.0 | Blood cholesterol increased,Blood pressure increased,Chordae tendinae rupture,Diarrhoea,Hypotension,Mitral valve incompetence | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 26069696 | 2025-11-20 | eu | male | 67.0 | Hypokalaemia | serious | yes | recovering/resolving |
| 26073225 | 2025-11-21 | united kingdom | male | 88.0 | Paranoia,Emotional distress,Delusion,Aggression | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26073757 | 2025-11-21 | united kingdom | male | 82.0 | Atrial flutter,Hallucination,Memory impairment,Depression,Anal incontinence,Blood triglycerides increased | serious | yes | unknown,recovering/resolving,recovering/resolving,recovering/resolving,unknown,unknown |
| 26073988 | 2025-11-21 | eu | female | 89.0 | Cholestasis | serious | yes | recovering/resolving |
| 26078483 | 2025-11-23 | canada | female | 91.0 | Abdominal discomfort,Asthenia,Cholecystitis,Dizziness,Dyspnoea,Laryngitis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26086713 | 2025-11-25 | eu | male | missing | Philadelphia chromosome positive,Aspartate aminotransferase increased,Hypertriglyceridaemia,Headache,Abdominal pain upper,Blood creatine phosphokinase increased,Alanine aminotransferase increased,Drug ineffective | serious | yes | recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing,recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,recovered/resolved |
| 26086717 | 2025-11-25 | canada | male | 64.0 | Abdominal pain,Abdominal wall haematoma,Haemoglobin decreased,Retroperitoneal haemorrhage | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovering/resolving |
| 26086924 | 2025-11-25 | canada | male | 93.0 | Gastric ulcer,Upper gastrointestinal haemorrhage,Transfusion | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26090652 | 2025-11-26 | eu | female | 80.0 | Bradycardia,Wrong product administered,Product prescribing error | serious | yes | unknown,unknown,unknown |
| 26090986 | 2025-11-26 | missing | female | 41.0 | Ectopic pregnancy | serious | yes | unknown |
| 26091135 | 2025-11-26 | eu | male | 58.0 | Acute kidney injury,Hypotension | serious | yes | recovered/resolved,recovered/resolved |
| 26091142 | 2025-11-26 | eu | female | 93.0 | Fall,Orthostatic hypotension | serious | yes | recovering/resolving,recovering/resolving |
| 26091803 | 2025-11-26 | eu | missing | 59.0 | Hyperkalaemia,Off label use | serious | yes | unknown,unknown |
| 26091944 | 2025-11-26 | eu | female | 62.0 | Pancytopenia,Mucosal inflammation,Skin exfoliation,Alopecia,Medication error | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26095046 | 2025-11-27 | eu | female | 85.0 | Pneumonia,Pleuritic pain,Bronchitis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26095769 | 2025-11-27 | united kingdom | female | 62.0 | Oral mucosal blistering,Burning sensation,Swelling | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26096759 | 2025-11-27 | eu | male | 52.0 | Embolism | serious | yes | recovered/resolved |
| 26097095 | 2025-11-27 | eu | female | 89.0 | Neuropathy peripheral,Cellulitis | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 26099986 | 2025-11-28 | eu | male | 42.0 | Therapy non-responder | serious | yes | unknown |
| 26100980 | 2025-11-28 | united kingdom | male | 60.0 | Muscle fatigue | serious | yes | recovering/resolving |
| 26103693 | 2025-11-29 | missing | female | 82.0 | Fistula,Osteonecrosis of jaw | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 26105609 | 2025-12-01 | eu | female | 55.0 | Eosinophilia | serious | yes | recovering/resolving |
| 26105664 | 2025-12-01 | eu | female | 72.0 | Drug interaction,International normalised ratio increased,Anaemia | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26106064 | 2025-12-01 | eu | female | missing | International normalised ratio fluctuation,Drug interaction | serious | yes | unknown,unknown |
| 26115443 | 2025-12-03 | united kingdom | male | missing | Aggression | serious | yes | not recovered/not resolved/ongoing |
| 26115569 | 2025-12-03 | united kingdom | female | 74.0 | Swelling face,Swollen tongue | serious | yes | recovered/resolved,recovered/resolved |
| 26115696 | 2025-12-03 | eu | female | 77.0 | Gastrointestinal haemorrhage,Anaemia | serious | yes | recovering/resolving,recovering/resolving |
| 26115793 | 2025-12-03 | canada | male | 74.0 | Delirium,Hallucination, visual,Abdominal pain upper,Confusional state,Fall,Somnolence | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing |
| 26116128 | 2025-12-03 | eu | female | 60.0 | Pneumonia,Aortic thrombosis,Supraventricular tachycardia | serious | yes | unknown,recovering/resolving,unknown |
| 26116333 | 2025-12-03 | missing | male | missing | Cerebrovascular accident,Confusional state,Headache,Seizure | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26119618 | 2025-12-04 | eu | male | 53.0 | Shock haemorrhagic | serious | yes | recovered/resolved |
| 26119634 | 2025-12-04 | eu | male | 93.0 | Cardiac failure | serious | yes | unknown |
| 26119660 | 2025-12-04 | missing | female | 85.0 | Atypical femur fracture,Colitis,Diarrhoea | serious | yes | unknown,unknown,unknown |
| 26119674 | 2025-12-04 | eu | male | 80.0 | Rhabdomyolysis,Urinary retention,Poisoning deliberate,Miosis | serious | yes | recovering/resolving,recovered/resolved with sequelae,recovered/resolved,recovered/resolved |
| 26120650 | 2025-12-04 | eu | female | 80.0 | Arrhythmia | serious | yes | recovering/resolving |
| 26120681 | 2025-12-04 | united kingdom | male | 78.0 | BRASH syndrome | serious | yes | recovering/resolving |
| 26124757 | 2025-12-05 | missing | male | 65.0 | Suicide attempt,Intentional overdose,No adverse event | serious | yes | unknown,unknown,unknown |
| 26125807 | 2025-12-05 | eu | male | 53.0 | Mania | serious | yes | recovered/resolved |
| 26128203 | 2025-12-07 | united kingdom | female | 71.0 | Arthralgia,Medication error | serious | yes | not recovered/not resolved/ongoing,unknown |
| 26128233 | 2025-12-07 | canada | female | 74.0 | Febrile neutropenia,Colitis,Neutrophil count abnormal | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26129227 | 2025-12-08 | united kingdom | male | 73.0 | Joint swelling | serious | yes | recovered/resolved |
| 26129228 | 2025-12-08 | missing | female | missing | Dizziness,Coordination abnormal,Hypoaesthesia,Asthenia,Palpitations,Medication error | serious | yes | not recovered/not resolved/ongoing,recovering/resolving,recovered/resolved,recovering/resolving,not recovered/not resolved/ongoing,unknown |
| 26129452 | 2025-12-08 | united kingdom | female | 88.0 | Hypokalaemia,Hypomagnesaemia,Hypocalcaemia,Muscle spasms | serious | yes | recovering/resolving,recovered/resolved,recovered/resolved,unknown |
| 26133873 | 2025-12-09 | united kingdom | male | 36.0 | Priapism | serious | yes | unknown |
| 26134287 | 2025-12-09 | eu | female | 37.0 | Pruritus,Throat tightness,Urticaria | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26134289 | 2025-12-09 | eu | female | 68.0 | Pneumothorax,Depersonalisation/derealisation disorder,Asthma,Depression | serious | yes | unknown,unknown,not recovered/not resolved/ongoing,recovered/resolved |
| 26134485 | 2025-12-09 | eu | female | 79.0 | Ischaemic stroke | serious | yes | recovered/resolved |
| 26134590 | 2025-12-09 | eu | female | 87.0 | Hyponatraemia | serious | yes | recovering/resolving |
| 26134776 | 2025-12-09 | eu | female | 67.0 | Drug-induced liver injury,Accidental overdose | serious | yes | recovered/resolved,recovered/resolved |
| 26135051 | 2025-12-09 | united kingdom | female | 88.0 | Toxicity to various agents | serious | yes | recovering/resolving |
| 26138560 | 2025-12-10 | eu | male | missing | Carotid arteriosclerosis,Lipoprotein (a) increased,Arteriosclerosis,Coronary artery disease,Peripheral arterial occlusive disease | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 26138789 | 2025-12-10 | eu | female | 54.0 | Intentional self-injury,Drug abuse | serious | yes | unknown,unknown |
| 26138825 | 2025-12-10 | united kingdom | missing | 91.0 | Fall | serious | yes | recovered/resolved |
| 26139427 | 2025-12-10 | united states | female | 31.0 | Bradycardia,Condition aggravated | serious | yes | unknown,unknown |
| 26143609 | 2025-12-11 | eu | male | 86.0 | Acute kidney injury,Bradycardia | serious | yes | recovering/resolving,recovered/resolved |
| 26144428 | 2025-12-11 | eu | female | 64.0 | Dyspnoea,Pruritus,Erythema | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26144528 | 2025-12-11 | eu | female | 66.0 | Hallucination, visual,Delirium,Psychomotor hyperactivity | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26148598 | 2025-12-12 | eu | female | 61.0 | Liver disorder | serious | yes | recovered/resolved |
| 26148703 | 2025-12-12 | eu | missing | 79.0 | Diabetic ketoacidosis,Type 1 diabetes mellitus,Pancreatic failure | serious | yes | unknown,unknown,unknown |
| 26148939 | 2025-12-12 | eu | male | missing | Idiopathic pulmonary fibrosis,Liver function test abnormal,Diarrhoea,Weight decreased,Photosensitivity reaction | serious | yes | unknown,unknown,unknown,unknown,unknown |
| 26149269 | 2025-12-12 | eu | male | 61.0 | Poisoning deliberate,Sopor,Bradycardia,Vomiting,Toxicity to various agents | serious | yes | recovering/resolving,recovering/resolving,recovering/resolving,recovered/resolved,recovering/resolving |
| 26152300 | 2025-12-14 | united kingdom | female | 81.0 | Hypokalaemia | serious | yes | not recovered/not resolved/ongoing |
| 26152417 | 2025-12-14 | united kingdom | female | 54.0 | Arthralgia,Joint swelling,Myalgia | serious | yes | unknown,recovered/resolved,recovered/resolved |
| 26153118 | 2025-12-14 | united kingdom | male | 61.0 | Death | serious | yes | fatal |
| 26153496 | 2025-12-14 | canada | female | 85.0 | Freezing phenomenon,Movement disorder,Muscle rigidity | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved |
| 26154927 | 2025-12-15 | eu | male | 60.0 | Epilepsy | serious | yes | recovered/resolved |
| 26159073 | 2025-12-16 | united kingdom | male | 78.0 | Abnormal weight gain | serious | yes | not recovered/not resolved/ongoing |
| 26160330 | 2025-12-16 | eu | female | 90.0 | Thrombocytopenia,Anaemia,Mucosal inflammation | serious | yes | recovered/resolved,not recovered/not resolved/ongoing,recovered/resolved |
| 26160801 | 2025-12-16 | eu | female | 67.0 | Cholestasis | serious | yes | recovered/resolved |
| 26160824 | 2025-12-16 | united kingdom | male | 83.0 | Skin exfoliation,Pruritus | serious | yes | recovering/resolving,recovering/resolving |
| 26166592 | 2025-12-17 | eu | female | 93.0 | Fall,Orthostatic hypotension,Chest injury,Musculoskeletal chest pain | serious | yes | recovering/resolving,recovering/resolving,unknown,unknown |
| 26168076 | 2025-12-17 | eu | male | 64.0 | Pneumonia | serious | yes | fatal |
| 26168521 | 2025-12-17 | eu | female | 62.0 | Retroperitoneal haematoma,Shock haemorrhagic | serious | yes | recovering/resolving,recovered/resolved |
| 26168629 | 2025-12-17 | eu | female | 73.0 | Interstitial lung disease | serious | yes | recovered/resolved |
| 26168760 | 2025-12-17 | eu | male | 75.0 | Jaundice cholestatic | serious | yes | recovering/resolving |
| 26172584 | 2025-12-18 | china | male | 56.0 | Drug level decreased,False positive investigation result,Therapeutic product effect decreased,Drug interaction,Hypertension | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26172911 | 2025-12-18 | united kingdom | female | 74.0 | Nightmare | serious | yes | not recovered/not resolved/ongoing |
| 26172919 | 2025-12-18 | united kingdom | female | 53.0 | Atrial fibrillation,Drug ineffective | serious | yes | unknown,unknown |
| 26173526 | 2025-12-18 | missing | male | 60.0 | Erectile dysfunction | serious | yes | recovered/resolved |
| 26174489 | 2025-12-18 | eu | male | 83.0 | Pericardial haemorrhage,Drug interaction | serious | yes | recovered/resolved,recovered/resolved |
| 26178177 | 2025-12-19 | eu | male | 84.0 | Confusional state,Hallucination,Somnolence | serious | yes | recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing |
| 26178704 | 2025-12-19 | eu | female | 59.0 | Idiopathic interstitial pneumonia | serious | yes | recovering/resolving |
| 26179438 | 2025-12-19 | eu | female | 70.0 | Erythema,Palmar erythema | serious | yes | unknown,unknown |
| 26179555 | 2025-12-19 | eu | female | 73.0 | Acute kidney injury,Urinary tract infection,Dysstasia,General physical health deterioration | serious | yes | not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,unknown |
| 26179782 | 2025-12-19 | eu | female | 74.0 | Neuralgia | serious | yes | recovered/resolved with sequelae |
| 26180072 | 2025-12-19 | eu | male | 77.0 | Atrial fibrillation,Pneumothorax,Cardiac disorder,Dyspnoea exertional,Increased upper airway secretion,Dysphonia,Cough,Secretion discharge,Chest discomfort,Obstructive airways disorder,Fractional exhaled nitric oxide increased,Dyspnoea,Nasopharyngitis,Eosinophilia,Exostosis,Coronary artery disease,Plantar fasciitis,Obstructive sleep apnoea syndrome,Bronchospasm,Myoglobin blood increased,Sensation of foreign body,Muscle spasms,Brain natriuretic peptide increased,Wheezing | serious | yes | recovered/resolved,not recovered/not resolved/ongoing,unknown,unknown,unknown,not recovered/not resolved/ongoing,not recovered/not resolved/ongoing,unknown,not recovered/not resolved/ongoing,unknown,recovered/resolved,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 26183187 | 2025-12-21 | eu | female | missing | Hypotension,Medication error | serious | yes | recovered/resolved,recovered/resolved |
| 26183191 | 2025-12-21 | eu | male | 54.0 | Muscle spasms | serious | yes | recovering/resolving |
| 26183404 | 2025-12-21 | eu | male | 63.0 | Acute kidney injury | serious | yes | recovered/resolved with sequelae |
| 26193595 | 2025-12-24 | canada | female | 82.0 | Acute kidney injury,Clostridium test positive,Colitis,Generalised oedema,Sepsis | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26196758 | 2025-12-24 | eu | male | 70.0 | Arrhythmic storm,Rebound effect | serious | yes | fatal,fatal |
| 26196949 | 2025-12-24 | eu | male | 87.0 | Haemorrhage,Anaemia | serious | yes | recovered/resolved,recovered/resolved |
| 26198785 | 2025-12-25 | eu | male | missing | Cardiac arrest | serious | yes | fatal |
| 26198835 | 2025-12-25 | eu | female | 61.0 | Blood pressure increased,Drug interaction,Malaise,Toxicity to various agents,Nasopharyngitis,Headache,Hyperhidrosis,Vomiting,Dizziness | serious | yes | unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown,unknown |
| 26198856 | 2025-12-25 | eu | male | 67.0 | Hyponatraemia,Inappropriate antidiuretic hormone secretion | serious | yes | recovered/resolved,recovered/resolved |
| 26198861 | 2025-12-25 | eu | male | 76.0 | Renal failure | serious | yes | not recovered/not resolved/ongoing |
| 26199166 | 2025-12-25 | eu | male | 87.0 | Hypokalaemia | serious | yes | recovered/resolved |
| 26199224 | 2025-12-25 | united kingdom | male | missing | Gastritis,Crohn^s disease,Syncope,Dizziness | serious | yes | unknown,unknown,unknown,unknown |
| 26201254 | 2025-12-26 | canada | female | 80.0 | Atypical femur fracture | serious | yes | recovered/resolved |
| 26201786 | 2025-12-26 | eu | female | 56.0 | Periorbital swelling,Swelling face,Pruritus,Hypoaesthesia oral | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved |
| 26202851 | 2025-12-26 | eu | male | 63.0 | Pancytopenia | serious | yes | recovered/resolved |
| 26202882 | 2025-12-26 | united kingdom | male | missing | Rectal haemorrhage,Medication error | serious | yes | recovering/resolving,unknown |
| 26203219 | 2025-12-26 | eu | male | 74.0 | Shock haemorrhagic,Septic shock,Duodenal ulcer,Colitis,Acute kidney injury | serious | yes | recovered/resolved,recovered/resolved,recovered/resolved,recovered/resolved,not recovered/not resolved/ongoing |
| 26203300 | 2025-12-26 | canada | female | 81.0 | Blood test abnormal,Confusional state,Dizziness | serious | yes | unknown,unknown,unknown |
