import function
import csv
from collections import defaultdict
context_info = defaultdict(list)
csv.field_size_limit(1000000000)


with open('final_replication_dataset_v2 2.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  # セミコロンでデータを分割

    count = 0
    for row in reader:

        # コード内のコメントはjava parserのエラーの原因になるため削除
        # submit_code=function.remove_comments(row[19])
        # refund_code=function.remove_comments(row[20])

        satd_comment = row[17]
        above_code = row[19]
        under_block = row[20]

        # インデントや改行を削除
        satd_comment = function.remove_indentation_and_newlines(satd_comment)
        above_code = function.remove_indentation_and_newlines(above_code)
        under_block = function.remove_indentation_and_newlines(under_block)

        context_info["satd_comment"].append(satd_comment)
        context_info["above_code"].append(above_code)
        context_info["under_block"].append(under_block)


# 重複削除のための格納変数
tmp = ""
# ノイズデータを除いたリスト番号を格納するリスト
lists = []

# ファイルを書き込みモードで開く
with open('./output_file/under_block_line.txt', 'w') as f:
    # ファイルにテキストを書き込む
    for i in range(context_info['under_block'].__len__()):

        # 一個前のデータと同じでないかつ、文字数が10文字以上の場合
        if tmp != context_info['under_block'][i] and len(context_info['under_block'][i]) > 10:
            f.write(context_info['under_block'][i] + "\n")
            lists.append(i)
            tmp = context_info['under_block'][i]

with open('./output_file/satd_comment_line.txt', 'w') as f:
    # ファイルにテキストを書き込む
    for i in lists:
        f.write(context_info['satd_comment'][i] + "\n")


with open('./output_file/above_code_line.txt', 'w') as f:
    # ファイルにテキストを書き込む
    for i in lists:
        f.write(context_info['above_code'][i] + "\n")
