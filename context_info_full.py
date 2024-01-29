import function
import csv
from collections import defaultdict
context_info = defaultdict(list)
csv.field_size_limit(1000000000)

with open('final_replication_dataset_v2 2.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  # セミコロンでデータを分割

    for row in reader:
        satd_comment = row[17]
        above_code = row[19]
        under_block = row[20]
        label = row[18]  # 正解ラベル

        # インデントや改行を削除
        satd_comment = function.remove_indentation_and_newlines(satd_comment)
        above_code = function.remove_indentation_and_newlines(above_code)
        default_under_block = under_block
        under_block = function.remove_indentation_and_newlines(under_block)

        context_info["satd_comment"].append(satd_comment)
        context_info["above_code"].append(above_code)
        context_info["default_under_block"].append(default_under_block)
        context_info["under_block"].append(under_block)
        context_info["label"].append(label)

# 重複削除のための格納変数
tmp = ""
lists = []  # ノイズデータを除いたリスト番号を格納するリスト

with open('./output_file/all_under_block.txt', 'w') as f:
    for i in range(len(context_info['under_block'])):
        if tmp != context_info['under_block'][i] and len(context_info['under_block'][i]) > 10:
            f.write(context_info['under_block'][i] + "\n")
            lists.append(i)
            tmp = context_info['under_block'][i]

with open('./output_file/satd_comment_line.txt', 'w') as f:
    for i in lists:
        f.write(context_info['satd_comment'][i] + "\n")

with open('./output_file/above_code_line.txt', 'w') as f:
    for i in lists:
        f.write(context_info['above_code'][i] + "\n")

with open('./output_file/label.txt', 'w') as f:
    count = {}
    for i in lists:
        if context_info['label'][i] == 'WITHOUT_CLASSIFICATION':
            f.write('0' + "\n")
            count['0'] = count.get('0', 0) + 1
        else:
            f.write('1' + "\n")
            count['1'] = count.get('1', 0) + 1
    print(count)

# ブロックの1行目、2行目、および3行目をそれぞれファイルに保存
with open('./output_file/one_under_block.txt', 'w') as f:
    for i in lists:
        f.write(context_info['default_under_block'][i].split('\n')[0] + "\n")

with open('./output_file/two_under_block.txt', 'w') as f:
    for i in lists:
        lines = context_info['default_under_block'][i].split('\n')
        to_write = lines[0] if len(lines) > 0 else ""
        if len(lines) > 1:
            to_write += lines[1]
        f.write(to_write + "\n")

with open('./output_file/three_under_block.txt', 'w') as f:
    for i in lists:
        lines = context_info['default_under_block'][i].split('\n')
        to_write = lines[0] if len(lines) > 0 else ""
        if len(lines) > 1:
            to_write += lines[1]
        if len(lines) > 2:
            to_write += lines[2]
        f.write(to_write + "\n")
