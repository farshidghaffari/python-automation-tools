# Usage Guide

This guide explains how to run the automation tools in this repository.

## 1. Install Dependencies

From the project root:

```bash
pip install -r requirements.txt
```

## 2. Run File Organizer

```bash
python tools/file_organizer/file_organizer.py
```

### What it does

The file organizer groups files by extension.

Example:

```text
downloads/
├── invoice.pdf
├── image.jpg
├── notes.txt
```

After running the script:

```text
downloads/
├── pdf/
│   └── invoice.pdf
├── jpg/
│   └── image.jpg
└── txt/
    └── notes.txt
```

## 3. Run CSV Cleaner

```bash
python tools/csv_cleaner/csv_cleaner.py sample_data/sales_data.csv cleaned_sales_data.csv
```

### What it does

The CSV cleaner:

- Removes empty rows
- Normalizes column names
- Trims text values
- Exports a cleaned CSV file

### Example output

```text
cleaned_sales_data.csv
```

## 4. Run Report Generator

```bash
python tools/excel_report_automation/report_generator.py sample_data/sales_data.csv sales_report.csv
```

### What it does

The report generator reads sales data and creates a simple report with:

- Total orders
- Total revenue
- Average order value
- Revenue by category

### Example output

```text
sales_report.csv
```

## 5. Recommended Client Workflow

For real client work, the process usually looks like this:

1. Review the current manual workflow
2. Check the input files and expected output
3. Create a Python script for the repeated task
4. Test the script with sample files
5. Deliver the script with instructions
6. Improve the script after real usage feedback

## 6. Suggested Improvements

- Add logging
- Add configuration files
- Add unit tests
- Add sample output files
- Add error handling for missing columns
- Add scheduled execution
- Add GUI or dashboard support
