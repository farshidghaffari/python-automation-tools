# Python Automation Tools

A practical Python automation repository by **Farshid Ghaffari**.

This repository contains small automation tools that solve common repetitive tasks such as organizing files, cleaning CSV data, and generating simple Excel-style reports.

## Purpose

The goal of this repository is to demonstrate how Python can be used to reduce manual work and build practical workflow tools.

## Included Tools

| Tool | Path | Description |
|---|---|---|
| File Organizer | `tools/file_organizer/` | Organizes files into folders by extension |
| CSV Cleaner | `tools/csv_cleaner/` | Cleans CSV files by removing empty rows and normalizing column names |
| Excel Report Automation | `tools/excel_report_automation/` | Generates a simple report from CSV data |

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

Run a tool:

```bash
python tools/file_organizer/file_organizer.py
```

or:

```bash
python tools/csv_cleaner/csv_cleaner.py sample_data/sales_data.csv cleaned_sales_data.csv
```

or:

```bash
python tools/excel_report_automation/report_generator.py sample_data/sales_data.csv sales_report.csv
```

## Tools Overview

### 1. File Organizer

Organizes files inside a folder based on their extension.

Example:
- `invoice.pdf` goes to `pdf/`
- `photo.jpg` goes to `jpg/`
- `notes.txt` goes to `txt/`

### 2. CSV Cleaner

Cleans CSV files by:
- Removing empty rows
- Normalizing column names
- Trimming extra spaces
- Exporting a cleaned CSV file

### 3. Report Generator

Creates a simple summary report from CSV sales data.

It calculates:
- Total rows
- Total revenue
- Average order value
- Revenue by category

## Related Links

- Portfolio: https://farshidghaffari.net
- Services: https://farshidghaffari.net/services/
- Projects: https://farshidghaffari.net/projects/
- Blog: https://farshidghaffari.net/blog/

## Author

**Farshid Ghaffari**  
Python Developer focused on automation, backend APIs, data tools, and practical problem solving.
