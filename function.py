import re
import csv
from collections import defaultdict
submit_satd_refund = defaultdict(list)
csv.field_size_limit(1000000000)


def remove_comments(java_code):
    # 単一行のコメントを削除
    java_code = re.sub("//.*", "", java_code)
    # 複数行のコメントを削除
    java_code = re.sub("/\*.*?\*/", "", java_code, flags=re.DOTALL)

    return java_code

#インデントと空白だけ削除
def remove_indentation(code):
    return code.replace('    ', '')  

def remove_indentation_and_newlines(code):
    return ''.join(code.splitlines()).replace('    ', '')  # 4 spaces indent assumed
