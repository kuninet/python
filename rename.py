#!/local/bin/python3
# カレントディレクトリのファイル名からブランクを無くしてリネーム
# ...Python3

import os
import sys
import re
import shutil

def before_disp(dir_list,s):
    print("* ファイル名をブランク除去変換 *")
    print("-- 変換前 -------------------------------")
    for entry in dir_list:
        if entry.count(s):
            print(entry)

def after_disp(dir_list,s):
    print("-- 変換後 -------------------------------")
    for entry in dir_list:
        if entry.count(s):
            print(re.sub(r"\s+","",entry))
    print("----------------------------------------")

def yes_no_input(s):
    while True:
        choice = input(s).lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False

def file_rename(dir_list,s):
    if yes_no_input("\nファイル名を変換して良いですか? [y/N]: "):
        for entry in dir_list:
            if entry.count(s):
                print(re.sub(r"\s+","",entry))
                shutil.move(entry,re.sub(r"\s+","",entry))

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

before_disp(dir_list,s)
after_disp(dir_list,s)

file_rename(dir_list,s)
