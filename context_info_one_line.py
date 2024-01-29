import csv
from collections import defaultdict
csv.field_size_limit(1000000000)

context_info = []

with open('final_replication_dataset_v2 2.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        under_block = row[20]
        context_info.append(under_block)

# 重複削除のための格納変数
tmp = ""
# ノイズデータを除いたリスト番号を格納するリスト
lists = []

# under_blockの最初の行を保存するファイルを開く
with open('./output_file/one_under_block.txt', 'w') as f_under:
    for i in range(len(context_info)):
        if tmp != context_info[i] and len(context_info[i]) > 10:
            # under_blockの最初の行を抽出して保存
            f_under.write(context_info[i].split('\n')[0] + "\n")
            lists.append(i)
            tmp = context_info[i]

# 既存のコードでファイルを作成
# with open('./output_file/under_block.txt', 'w') as f:
#     for i in lists:
#         f.write(context_info[i] + "\n")
