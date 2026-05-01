"""
File Organizer Automation Tool

This tool organizes files inside a target folder by moving them
into subfolders based on their file extensions.

Usage:
    python tools/file_organizer/file_organizer.py

Then enter the folder path when prompted.
"""

from pathlib import Path
import shutil


def organize_files(source_folder: Path) -> int:
    """Organize files in the given folder by extension and return moved file count."""
    if not source_folder.exists():
        raise FileNotFoundError(f"Folder not found: {source_folder}")

    if not source_folder.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {source_folder}")

    moved_count = 0

    for file_path in source_folder.iterdir():
        if not file_path.is_file():
            continue

        extension = file_path.suffix.lower().replace(".", "") or "no_extension"
        target_folder = source_folder / extension
        target_folder.mkdir(exist_ok=True)

        target_path = target_folder / file_path.name

        if target_path.exists():
            print(f"Skipped existing file: {target_path}")
            continue

        shutil.move(str(file_path), str(target_path))
        moved_count += 1
        print(f"Moved: {file_path.name} -> {target_folder.name}/")

    return moved_count


def main() -> None:
    """Run the file organizer tool."""
    folder_input = input("Enter folder path to organize: ").strip()

    if not folder_input:
        print("No folder path provided.")
        return

    try:
        moved_count = organize_files(Path(folder_input))
        print(f"Files organized successfully. Moved files: {moved_count}")
    except (FileNotFoundError, NotADirectoryError) as error:
        print(error)


if __name__ == "__main__":
    main()
