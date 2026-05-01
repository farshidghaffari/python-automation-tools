# Excel Report Automation

Generates a simple summary report from CSV sales data.

## Expected Columns

```text
date, category, product, quantity, price
```

## Run

```bash
python tools/excel_report_automation/report_generator.py sample_data/sales_data.csv sales_report.csv
```

## Report Includes

- Total orders
- Total revenue
- Average order value
- Revenue by category
