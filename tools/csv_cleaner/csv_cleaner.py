"""
CSV Cleaner Automation Tool

This tool reads a CSV file, removes empty rows, normalizes column names,
trims text values, and exports a cleaned CSV file.

Usage:
    python tools/csv_cleaner/csv_cleaner.py input.csv output.csv
"""

from pathlib import Path
import sys
import pandas as pd


def normalize_column_name(column_name: str) -> str:
    """Normalize a column name for cleaner data processing."""
    return (
        column_name.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )


def clean_csv(input_path: Path, output_path: Path) -> None:
    """Clean a CSV file and export the result."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)

    # Remove rows that are fully empty
    df = df.dropna(how="all")

    # Normalize column names
    df.columns = [normalize_column_name(column) for column in df.columns]

    # Trim text cells
    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].astype(str).str.strip()

    df.to_csv(output_path, index=False)
    print(f"Cleaned CSV saved to: {output_path}")


def main() -> None:
    """Run the CSV cleaner tool."""
    if len(sys.argv) != 3:
        print("Usage: python tools/csv_cleaner/csv_cleaner.py input.csv output.csv")
        return

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    try:
        clean_csv(input_path, output_path)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
