
# Baselight Path Frame Mapper

This script processes a Baselight export text file and maps each frame number to a corrected file path based on predefined path rules. It then outputs a CSV that summarizes the frame ranges for each path.

## 📋 What It Does

1. **Reads a Baselight export file** (`Baselight_export_spring2025.txt`) containing paths and frame numbers.
2. **Parses each line** to identify the base path and frame numbers.
3. **Normalizes paths** for sequences related to the project `dogman`, replacing the base path with a corrected path from a mapping.
4. **Groups frames into ranges** for each path (e.g., `1001-1005`, `1006`, etc.).
5. **Outputs results** to a CSV file named `output.csv` containing two columns: `Path` and `Frames`.

Example output:

```
Path,Frames
/hpsans13/production/dogman/reel1/partA/1920x1080,1001-1004
/hpsans14/production/dogman/reel1/VFX/AnimalLogic,2000
...
```

## 📁 Input File Format

Each line in the `Baselight_export_spring2025.txt` file should follow this format:

```
/some/path/dogman/reel1/partA/1920x1080 1001 1002 1003
```

- The first token is the full path.
- The rest are frame numbers associated with that path.

## 🧩 How It Works

- The script looks for any path containing `dogman`.
- It extracts the sub-path (e.g., `reel1/partA/1920x1080`) and matches it against a list of known locations.
- If a match is found, it uses a corrected path from a dictionary.
- It aggregates frame numbers for each corrected path and compresses consecutive numbers into ranges.

## 🚀 How to Run

### Requirements

- Python 3

### Steps

1. Place your `Baselight_export_spring2025.txt` in the same directory as the script.
2. Run the script:

```bash
python import_parse.py
```

3. After running, you'll find `output.csv` in the same directory.

## 🛠 Configuration

To update paths or add new ones:

- Modify the `xytech_locations` list and `path_update` dictionary in the script accordingly.
