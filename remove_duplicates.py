import os
import hashlib

def hash_file(filepath):
    """تولید هش SHA256 برای محتوای فایل"""
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def find_and_remove_duplicates(folder_path):
    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = hash_file(filepath)

            if file_hash in hashes:
                print(f"🔁 Duplicate found: {filepath} (same as {hashes[file_hash]})")
                os.remove(filepath)
                duplicates.append(filepath)
            else:
                hashes[file_hash] = filepath

    print(f"\n✅ Done! {len(duplicates)} duplicate files removed.")

# مسیر فولدر را اینجا وارد کن:
folder_path = "/path/to/your/folder"
find_and_remove_duplicates(folder_path)
