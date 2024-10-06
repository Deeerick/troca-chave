import os
from tqdm import tqdm


def replace_code_in_file(file_path, old_codes, new_code):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            file_data = file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return

    original_data = file_data

    for old_code in old_codes:
        if old_code in file_data:
            print(f"Found '{old_code}' in {file_path}")
        file_data = file_data.replace(old_code, new_code)

    if file_data != original_data:
        try:
            with open(file_path, 'w', encoding='latin-1') as file:
                file.write(file_data)
            print(f"Replaced code in {file_path}")
        except Exception as e:
            print(f"Error writing file {file_path}: {e}")
    else:
        print(f"No changes made to {file_path}")
        pass


def replace_code_in_directory(directory, old_codes, new_code):
    total_files = sum(
        [len(files) for r, d, files in os.walk(directory)
         if any(f.endswith('.txt') for f in files)]
    )

    with tqdm(total=total_files, desc="Processing files", unit="file") as pbar:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    replace_code_in_file(file_path, old_codes, new_code)
                    pbar.update(1)


directory_path = 'C:\\arquivos\\'
old_codes = ['abc', 'ABC']
new_code = 'FFF'

replace_code_in_directory(directory_path, old_codes, new_code)
