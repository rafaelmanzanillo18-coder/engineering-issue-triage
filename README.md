# Engineering Issue Triage Automation (AI-001)

An original educational Python project for classifying **fictional** engineering issue reports. This first version uses simple keyword rules, **not artificial intelligence**. It generates suggested priorities and explicitly requires human review. A future version will compare an AI-assisted classifier against this baseline.

## Features
- Reads engineering issue descriptions from a CSV file
- Suggests Critical, High, Medium, or Low priority using illustrative keyword rules
- Exports results to CSV with a `Needs human review` status
- Includes automated tests using Python's built-in `unittest`
- Uses only Python's standard library (no packages to install)

## Requirements
Python 3.9 or newer.

## Run
Open a terminal in the repository folder and execute:

```bash
python triage.py --input data/sample_issues.csv --output output/triaged_issues.csv
```

On Windows, `py` may be used instead of `python`.

## Test

```bash
python -m unittest discover -s tests -v
```

## Example
Input: `Communication lost while reading telemetry`

Output: `High` / `Needs human review`

## Project status
Version 0.1: rule-based baseline. Future milestones: input validation, better test coverage, evaluation dataset, and optional AI-assisted triage with human oversight.

## Safety and limitations
This project uses synthetic data only. Keyword matching is not a validated risk assessment and must never be used as an autonomous safety decision or a replacement for engineering procedures. No employer data, confidential test reports, or proprietary code is included.
