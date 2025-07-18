# HEIC to PNG Converter

A simple Python script to batch convert `.heic` images (commonly from iPhones) to lossless `.png` format.  
Perfect for photographers who want to retain original image quality.

## Features

- Converts all `.heic` images in the `heic/` folder to `.png` format
- Saves output images in the `png/` folder
- Automatically creates folders if they don’t exist
- Skips already converted files
- Logs all conversions to `conversion_log.txt`
- Adds timestamps to output filenames to avoid overwriting
- Progress bar for visual feedback

## Requirements

Install required libraries:

```bash
pip install pillow pillow-heif tqdm
```

## Usage

- Place all your `.heic` images inside the `heic/` folder.
- Run the script:

```bash
python script.py
```

- Converted `.png` images will appear in the `png/` folder.
- A `conversion_log.txt` file will be generated inside the `png/` folder with the conversion history.