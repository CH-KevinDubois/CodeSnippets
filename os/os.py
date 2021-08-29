import os

# print(dict(os.environ).keys())
# print(os.environ["OS"])
# print(os.environ["PATH"])
# print(os.environ.get('PATH'))

# print(os.getcwd()) # Get current dir
# os.chdir('./os') # Change dir 
# print(os.listdir())

# os.mkdir('dir') # Create one dir
# os.makedirs('dir/subdir') # Create dir with subdir


# file = os.open('file.txt', os.O_RDWR|os.O_CREAT)
# os.close(file)


# os.rename('file.txt', 'renamed_file')

# os.stat('renamed_file')
# os.stat('renamed_file').st_mtime

# for dirpath, dirnames, filesnames in os.walk('.'):
#     print(f'Current path: {dirpath}')
#     print(f'Directories: {dirnames}')
#     print(f'Files: {filesnames}')

# os.rmdir('dir')
# os.removedirs('dir/subdir')
# os.remove('renamed_file')

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

base_name = os.path.dirname(file_path)
dir_name = os.path.dirname(file_path)
both = os.path.split(file_path)
path_exist = os.path.exists(file_path)
path_isdir = os.path.isdir(file_path)
path_isfile = os.path.isfile('../codesnippets/text.txt')
split_ext = os.path.splitext(file_path)

print(path_isfile, split_ext)