# FileRenamer
Basic file renamer, made with python

This script provides various options for renaming files, such as prefixing, suffixing, replacing parts of filenames, changing extensions, and more.

### How to Use This Script

1. **Save the script** to a file, for example, `file_renamer.py`.

2. **Run the script** from the command line, providing the necessary arguments. Here are some examples:

    - To add a prefix to all files in a directory:
      ```sh
      python file_renamer.py /path/to/directory --prefix "new_"
      ```

    - To add a suffix to all files in a directory:
      ```sh
      python file_renamer.py /path/to/directory --suffix "_backup"
      ```

    - To replace a part of the filename:
      ```sh
      python file_renamer.py /path/to/directory --replace "old" --replacement "new"
      ```

    - To change the file extensions:
      ```sh
      python file_renamer.py /path/to/directory --change-ext --new-ext ".txt"
      ```

### Arguments Explained

- `directory`: The directory containing the files to rename.
- `--prefix`: Add this prefix to the beginning of each file name.
- `--suffix`: Add this suffix to the end of each file name.
- `--replace`: The substring to find in the filenames.
- `--replacement`: The substring to replace the found string with.
- `--change-ext`: Flag to indicate if you want to change the file extensions.
- `--new-ext`: The new extension to use if `--change-ext` is specified.

This script provides flexibility in renaming files with various options and can be extended further based on additional requirements.
