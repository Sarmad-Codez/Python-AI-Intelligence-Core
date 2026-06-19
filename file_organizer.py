import os
import shutil

def organize_folder(target_folder):
    # Mapping of extensions to folder names
    EXTENSION_MAP = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Media': ['.mp3', '.mp4', '.mkv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Programs': ['.exe', '.msi', '.apk']
    }

    if not os.path.exists(target_folder):
        print("❌ Error: Specified folder does not exist!")
        return

    print(f"🔄 Scanning folder: {target_folder}...\n")
    files_moved = 0

    # Read all files in the directory
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # Skip directories, process only files
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_ext = os.path.splitext(filename)
        file_ext = file_ext.lower()

        # Find the correct category folder
        destination_folder = "Others"
        for folder_name, extensions in EXTENSION_MAP.items():
            if file_ext in extensions:
                destination_folder = folder_name
                break

        # Create destination folder if it doesn't exist
        dest_dir_path = os.path.join(target_folder, destination_folder)
        if not os.path.exists(dest_dir_path):
            os.makedirs(dest_dir_path)

        # Move file
        try:
            shutil.move(file_path, os.path.join(dest_dir_path, filename))
            print(f"📁 Moved: {filename} ➡️ {destination_folder}/")
            files_moved += 1
        except Exception as e:
            print(f"❌ Could not move {filename}: {e}")

    print("\n" + "="*40)
    print(f"✅ Success! Total files organized: {files_moved}")
    print("="*40)

if __name__ == "__main__":
    print("="*40)
    print("      AUTOMATED FILE ORGANIZER      ")
    print("="*40)
    
    # You can change this path to test on any folder
    path_to_clean = input("Enter full path of the folder to organize: ").strip()
    
    # Remove quotes if user dragged and dropped the folder into terminal
    path_to_clean = path_to_clean.strip("'\"")
    
    if path_to_clean:
        organize_folder(path_to_clean)
    else:
        print("❌ Path cannot be empty.")