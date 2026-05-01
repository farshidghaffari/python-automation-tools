"""
Excel-Style Report Automation Tool

This tool reads CSV sales data and generates a simple summary report.

Expected CSV columns:
    date, category, product, quantity, price

Usage:
    python tools/excel_report_automation/report_generator.py input.csv report.csv
"""

from pathlib import Path
import sys
import pandas as pd


def generate_report(input_path: Path, output_path: Path) -> None:
    """Generate a summary report from sales data."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)

    required_columns = {"date", "category", "product", "quantity", "price"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    df["revenue"] = df["quantity"] * df["price"]

    total_orders = len(df)
    total_revenue = df["revenue"].sum()
    average_order_value = df["revenue"].mean()

    category_report = (
        df.groupby("category", as_index=False)
        .agg(
            total_quantity=("quantity", "sum"),
            total_revenue=("revenue", "sum"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    summary = pd.DataFrame(
        [
            {"metric": "total_orders", "value": total_orders},
            {"metric": "total_revenue", "value": round(total_revenue, 2)},
            {"metric": "average_order_value", "value": round(average_order_value, 2)},
        ]
    )

    with open(output_path, "w", encoding="utf-8") as report_file:
        report_file.write("SUMMARY\n")
        summary.to_csv(report_file, index=False)
        report_file.write("\nCATEGORY REPORT\n")
        category_report.to_csv(report_file, index=False)

    print(f"Report saved to: {output_path}")


def main() -> None:
    """Run the report generator."""
    if len(sys.argv) != 3:
        print(
            "Usage: python tools/excel_report_automation/report_generator.py "
            "input.csv report.csv"
        )
        return

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    try:
        generate_report(input_path, output_path)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
