#!/local/bin/python3
# カレントディレクトリのファイル名からブランクを無くしてリネーム
# ...Python3

import os
import sys
import re
import shutil

def yes_no_input(s):
    while True:
        choice = input(s).lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False

def print_entry(entry):
    print(entry)

def print_nobrank_entry(entry):
    print(re.sub(r"\s+","",entry))

def rename_entry(entry):
    print_nobrank_entry(entry)
    shutil.move(entry,re.sub(r"\s+","",entry))

def list_handler(d_list,func):
    for entry in d_list:
        func(entry)
    
def before_disp(dir_list):
    print("* ファイル名をブランク除去変換 *")
    print("-- 変換前 -------------------------------")
    list_handler(dir_list,print_entry)

def after_disp(dir_list):
    print("-- 変換後 -------------------------------")
    list_handler(dir_list,print_nobrank_entry)
    print("----------------------------------------")

def file_rename(dir_list):
    if yes_no_input("\nファイル名を変換して良いですか? [y/N]: "):
        list_handler(dir_list,rename_entry)
        print("\n** 変換を終了しました**")

    else:
        print("\n!! 変換を中止しました!!")
        sys.exit(1)
#
# Main
#

if (len(sys.argv) != 2):
    print("usage : rename.py 検索文字列")
    exit(1)

s = sys.argv[1]
dir_list = os.listdir()
new_d_list = [l for l in dir_list if s in l]

before_disp(new_d_list)
after_disp(new_d_list)

file_rename(new_d_list)
