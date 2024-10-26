import os
import shutil

# Define folder structure and file extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh"]
}

def organize_files(directory_path):
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return

    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move files based on their extensions
        moved = False
        for category, extensions in file_categories.items():
            if any(file_name.lower().endswith(ext) for ext in extensions):
                category_path = os.path.join(directory_path, category)

                # Create category folder if it doesn't exist
                os.makedirs(category_path, exist_ok=True)

                # Move file to category folder
                shutil.move(file_path, os.path.join(category_path, file_name))
                print(f"Moved: {file_name} -> {category}")
                moved = True
                break

        # Move unclassified files to "Others"
        if not moved:
            other_path = os.path.join(directory_path, "Others")
            os.makedirs(other_path, exist_ok=True)
            shutil.move(file_path, os.path.join(other_path, file_name))
            print(f"Moved: {file_name} -> Others")

# Run the file organizer on a specific directory
organize_files("C:/Users/HP/Desktop/BSSE-5A")
