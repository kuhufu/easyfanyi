import sys
import os
import shutil

def alias_conf(filepath, line):
    with open(filepath, 'at') as out:
        out.write('\n# easyfanyi')
        out.write('\n' + line)

def copy_dir(src, dest):
    is_exist = os.path.exists(dest)
    if is_exist:
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

if __name__ == '__main__':
    src = 'dic'
    dest = '/opt/easyfanyi'
    copy_dir(src, dest)

    user = sys.argv[1] 
    file_path = '/home/' + user + '/.bashrc'
    line = "alias dic='python3 /opt/easyfanyi/dic-youdao.py'"
    alias_conf(file_path, line)
