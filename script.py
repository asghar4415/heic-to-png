import os
from datetime import datetime
from pillow_heif import register_heif_opener
from PIL import Image
from tqdm import tqdm

register_heif_opener()

input_folder = "heic"
output_folder = "png"

if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"'{input_folder}' folder created. Please add HEIC images inside it and run the script again.")
    exit()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"'{output_folder}' folder created to store converted PNGs.")

heic_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".heic")]

if not heic_files:
    print(f"No .heic files found in '{input_folder}'. Nothing to convert.")
    exit()

log_file_path = os.path.join(output_folder, "conversion_log.txt")
log_file = open(log_file_path, "a", encoding="utf-8")

for filename in tqdm(heic_files, desc="Converting HEIC to PNG"):
    try:
        heic_path = os.path.join(input_folder, filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.splitext(filename)[0]
        png_name = f"{base_name}_{timestamp}.png"
        png_path = os.path.join(output_folder, png_name)

        if os.path.exists(png_path):
            print(f"Skipped (already exists): {png_name}")
            continue

        image = Image.open(heic_path)
        image.save(png_path, "PNG")

        log_file.write(f"{filename} -> {png_name}\n")
        print(f"Converted: {filename} ➜ {png_name}")

    except Exception as e:
        print(f"Error converting {filename}: {e}")
        log_file.write(f"Error: {filename} - {str(e)}\n")

log_file.close()
print(f"All done. Log saved to: {log_file_path}")
