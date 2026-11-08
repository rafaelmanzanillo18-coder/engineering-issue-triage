"""Educational rule-based triage of fictional engineering issues."""
import argparse
import csv
from pathlib import Path

RULES = (
    ("Critical", ("smoke", "fire", "electric shock")),
    ("High", ("communication lost", "power failure", "overvoltage")),
    ("Medium", ("timeout", "intermittent", "unexpected reset")),
)


def classify(description: str) -> str:
    """Suggest a priority from illustrative keywords; human review is required."""
    text = description.lower()
    for priority, keywords in RULES:
        if any(keyword in text for keyword in keywords):
            return priority
    return "Low"


def process(input_path: str, output_path: str) -> int:
    """Read input CSV and export suggested priorities. Return number of issues."""
    with open(input_path, newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames or "description" not in reader.fieldnames:
            raise ValueError("Input CSV must contain a 'description' column")
        rows = list(reader)
        fieldnames = list(reader.fieldnames)
    for column in ("suggested_priority", "review_status"):
        if column not in fieldnames:
            fieldnames.append(column)
    for row in rows:
        row["suggested_priority"] = classify(row["description"] or "")
        row["review_status"] = "Needs human review"
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rule-based engineering issue triage demo")
    parser.add_argument("--input", default="data/sample_issues.csv")
    parser.add_argument("--output", default="output/triaged_issues.csv")
    args = parser.parse_args()
    count = process(args.input, args.output)
    print(f"Processed {count} fictional issues. Output: {args.output}")
