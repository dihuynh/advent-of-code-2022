import re
from file_system import Directory, File, Item

def is_command(line: str):
    return line.startswith("$")


# returns directory name
def is_cd_command(line: str):
    return line.startswith('$ cd')


# assumes that line is a cd command
def get_directory(line: str):
    return line[5:]


def is_ls_command(line: str):
    return line == '$ ls'


def parse_ls_output(line: str, current_dir: Directory):
    if line.startswith("dir"):
        dir_name = line[4:]
        current_dir.add_item(Directory(dir_name, current_dir))
    else:
        regex = re.compile(r'(\d*)\s*(.*)')
        result = regex.match(line)
        # print(f"file: {result.group(1)} {result.group(2)}")
        current_dir.add_item(
            File(name=result.group(2), size=int(result.group(1)))
        )


def dir_not_in_parent(new_dir_name, items):
    return new_dir_name not in set([item.name for item in items])


def build_directory_structure():
    input_lines.reverse()
    root: Directory = Directory(ROOT, None)
    current_dir: Directory = None
    line = input_lines.pop()

    while len(input_lines) > 0:
        if is_cd_command(line):
            new_dir_name = get_directory(line)
            if new_dir_name == ROOT:
                current_dir = root
            if new_dir_name == '..':
                current_dir = current_dir.get_parent()
            elif dir_not_in_parent(new_dir_name, current_dir.items):
                current_dir.add_item(Directory(new_dir_name, current_dir))
            else:
                current_dir = current_dir.get_item(new_dir_name)
            print(f"current dir: {current_dir}")
            if len(input_lines) > 0:
                line = input_lines.pop()
        elif is_ls_command(line):
            line = input_lines.pop()
            while line and not is_command(line):
                parse_ls_output(line, current_dir)
                if len(input_lines) > 0:
                    line = input_lines.pop()
                else:
                    line = None
            print(f"after ls: {current_dir}")

    return root



def find_dirs_under_size(directory, size_limit):
    dirs = []
    for item in directory.items:
        if item.is_directory and item.name != ROOT:
            if item.size < size_limit:
                dirs.append(item)
            dirs.extend(find_dirs_under_size(item, size_limit))
    return dirs


def find_dirs_over_size(directory, size_limit):
    dirs = set()
    if directory.size > size_limit:
        dirs.add(directory)
    for item in directory.items:
        if item.is_directory:
            if item.size >= size_limit:
                dirs.add(item)
            dirs.union(find_dirs_over_size(item, size_limit))
    return dirs


def find_smallest_dir_to_delete(directory, unused_space_needed, total_space_on_disk):
    total_space_taken = directory.size
    if total_space_taken + unused_space_needed < total_space_on_disk:
        # plenty of space left
        return None
    else:
        target_size = unused_space_needed + total_space_taken - total_space_on_disk
        dirs = find_dirs_over_size(directory, target_size)
        print(f'Directories over size: {dirs}')
        return min([d.size for d in dirs])



input_lines = open('input.txt').read().splitlines()
# input_lines = open('test_input.txt').read().splitlines()
PARENT_DIR = ".."
ROOT = "/"
size_limit = 100000
total_space_on_disk = 70000000
unused_space_needed = 30000000
directory: Directory = build_directory_structure()
all_dirs_under_size = find_dirs_under_size(directory, size_limit)
print(f'Result for part 1: {sum([dir.size for dir in all_dirs_under_size])}')
smallest_dir_to_delete = find_smallest_dir_to_delete(directory, unused_space_needed, total_space_on_disk)
print(f'Result for part 2: {smallest_dir_to_delete}')






