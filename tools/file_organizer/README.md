# File Organizer

Organizes files inside a folder based on their file extensions.

## Example

Before:

```text
downloads/
├── invoice.pdf
├── image.jpg
├── notes.txt
```

After:

```text
downloads/
├── pdf/
│   └── invoice.pdf
├── jpg/
│   └── image.jpg
└── txt/
    └── notes.txt
```

## Run

```bash
python tools/file_organizer/file_organizer.py
```
