# MIT License
# Aahnik 2021
# a script to organize the files in loconotion output
# also updates html and css files
# unix (linux / mac) style file paths are used in the program,
# will fail inevitably if run on windows
# ditch windows

import logging
import os

structure = {'assets/images': ['png', 'jpg', 'jpeg','bmp','gif','ico'],
             'assets/fonts': ['woff','ttf'],
             'assets/css': ['css'],
             'assets/js': ['js']}
# !! changing this structure, may break other stuff.

logging.info(structure)

mapping = {}
for folder, extensions in structure.items():
    for ext in extensions:
        mapping[ext] = folder

logging.info(mapping)

all_files = [file for file in os.listdir() if os.path.isfile(file)]

logging.info(all_files)

old_to_new = {}


def rename():
    for file in all_files:
        ext = file.split('.')[-1]
        new_parent_dir = mapping.get(ext)

        if new_parent_dir:
            new_file = os.path.join(new_parent_dir, file)

            if not os.path.isdir(new_parent_dir):
                os.makedirs(new_parent_dir)

            os.rename(file, new_file)
            old_to_new[file] = new_file
            logging.info('%s renamed to %s', file, new_file)


def update_code(file_name, old_to_new):

    with open(file_name, 'r') as file:
        content = file.read()

    for old, new in old_to_new.items():
        if file_name.endswith('.css'):
            new = new.replace('assets', '..')
            # relative position of files related to css files
        content = content.replace(old, new)

    with open(file_name, 'w') as file:
        file.write(content)


def main():
    rename()
    print(old_to_new)
    for file in os.listdir():
        if file.endswith('.html'):
            logging.info(file)
            update_code(file, old_to_new)
    for file in os.listdir('assets/css'):
        if file.endswith('.css'):
            logging.info(file)
            update_code(f'assets/css/{file}', old_to_new)


if __name__ == '__main__':
    print('loconotion organizer')
    main()