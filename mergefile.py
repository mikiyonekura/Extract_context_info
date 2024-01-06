import os
import re
from natsort import natsorted

# ソースコードが存在するディレクトリ
source_directory = "./after_src2abs/abs_refund"

# 出力するテキストファイルのパス
output_file = "after_src2abs/merge_refund"

# 指定されたディレクトリ内のすべての.javaファイルを取得
java_files = [f for f in os.listdir(source_directory) if f.endswith(".java")]

# ファイル名内の数字部分でソート
print(java_files)
java_files=natsorted(java_files)
print(java_files)

# 出力ファイルを開き、すべての.javaファイルを書き込む
with open(output_file, 'w') as outfile:
    for java_file in java_files:
        with open(os.path.join(source_directory, java_file), 'r') as infile:
            outfile.write(infile.read() + '\n')
