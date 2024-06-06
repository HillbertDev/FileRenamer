import os
import argparse

def rename_files(directory, prefix="", suffix="", replace="", replacement="", change_ext=False, new_ext=""):
    try:
        files = os.listdir(directory)
        for file_name in files:
            old_file = os.path.join(directory, file_name)
            if os.path.isfile(old_file):
                base, ext = os.path.splitext(file_name)
                
                new_base = base
                if replace and replacement:
                    new_base = new_base.replace(replace, replacement)
                if prefix:
                    new_base = prefix + new_base
                if suffix:
                    new_base = new_base + suffix
                
                new_file_name = new_base + (new_ext if change_ext else ext)
                new_file = os.path.join(directory, new_file_name)
                
                os.rename(old_file, new_file)
                print(f'Renamed: {file_name} -> {new_file_name}')
        print("Renaming completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Rename files in a directory with various options.')
    parser.add_argument('directory', type=str, help='Directory containing the files to rename')
    parser.add_argument('--prefix', type=str, default='', help='Prefix to add to the files')
    parser.add_argument('--suffix', type=str, default='', help='Suffix to add to the files')
    parser.add_argument('--replace', type=str, default='', help='String to replace in the filenames')
    parser.add_argument('--replacement', type=str, default='', help='String to replace with in the filenames')
    parser.add_argument('--change-ext', action='store_true', help='Flag to change the file extensions')
    parser.add_argument('--new-ext', type=str, default='', help='New extension for the files if --change-ext is specified')
    
    args = parser.parse_args()
    rename_files(args.directory, args.prefix, args.suffix, args.replace, args.replacement, args.change_ext, args.new_ext)

if __name__ == '__main__':
    main()
