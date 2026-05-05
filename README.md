# Python Automation Tools

A practical Python automation repository by **Farshid Ghaffari**.

This repository contains small automation tools that solve common repetitive tasks such as organizing files, cleaning CSV data, and generating simple report outputs from structured data.

It is designed as a portfolio-ready example for clients who need practical Python scripts to reduce manual work and improve daily workflows.

## What This Repository Demonstrates

- Python scripting for real workflow problems
- File and folder automation
- CSV data cleaning
- Simple report generation
- Command-line tool usage
- Clean documentation and project structure
- Beginner-friendly automation examples

## Included Tools

| Tool | Path | Description |
|---|---|---|
| File Organizer | `tools/file_organizer/` | Organizes files into folders by extension |
| CSV Cleaner | `tools/csv_cleaner/` | Cleans CSV files by removing empty rows and normalizing column names |
| Excel Report Automation | `tools/excel_report_automation/` | Generates a simple report from CSV sales data |

## Repository Structure

```text
python-automation-tools/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── sample_data/
│   └── sales_data.csv
├── tools/
│   ├── file_organizer/
│   │   ├── file_organizer.py
│   │   └── README.md
│   ├── csv_cleaner/
│   │   ├── csv_cleaner.py
│   │   └── README.md
│   └── excel_report_automation/
│       ├── report_generator.py
│       └── README.md
└── docs/
    └── usage.md
```

## Quick Start

Clone the repository:

```bash
git clone https://github.com/farshidghaffari/python-automation-tools.git
cd python-automation-tools
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Tools

### 1. File Organizer

```bash
python tools/file_organizer/file_organizer.py
```

Use case:

```text
Before:
downloads/
├── invoice.pdf
├── image.jpg
├── notes.txt

After:
downloads/
├── pdf/
│   └── invoice.pdf
├── jpg/
│   └── image.jpg
└── txt/
    └── notes.txt
```

### 2. CSV Cleaner

```bash
python tools/csv_cleaner/csv_cleaner.py sample_data/sales_data.csv cleaned_sales_data.csv
```

What it does:

- Removes empty rows
- Normalizes column names
- Trims extra spaces from text values
- Exports a cleaned CSV file

### 3. Excel Report Automation

```bash
python tools/excel_report_automation/report_generator.py sample_data/sales_data.csv sales_report.csv
```

Report includes:

- Total orders
- Total revenue
- Average order value
- Revenue by category

## Business Use Cases

These tools can be adapted for:

- Organizing downloaded files
- Cleaning exported CSV reports
- Preparing data before import
- Creating weekly or monthly summaries
- Reducing repetitive spreadsheet work
- Building small internal business utilities
- Creating first versions of automation workflows

## Freelance Service Angle

This repository demonstrates the type of small automation work I can build for clients:

> I can create Python scripts that automate repetitive tasks, clean messy CSV/Excel files, generate reports, and make daily workflows faster and more reliable.

## Related Portfolio Pages

- Portfolio: https://farshidghaffari.net
- Services: https://farshidghaffari.net/services/
- Excel / CSV Automation Service: https://farshidghaffari.net/services/excel-csv-automation/
- Projects: https://farshidghaffari.net/projects/
- Blog: https://farshidghaffari.net/blog/
- Excel / CSV Report Automation Project: https://github.com/farshidghaffari/excel-csv-report-automation

## Suggested Next Improvements

- Add screenshots or terminal output examples
- Add unit tests for each tool
- Add logging
- Add configuration files
- Add sample input/output folders
- Add scheduled execution examples
- Add a small GUI or web dashboard

## Author

**Farshid Ghaffari**  
Python Developer focused on automation, backend APIs, data tools, and practical problem solving.

Website: https://farshidghaffari.net  
GitHub: https://github.com/farshidghaffari
