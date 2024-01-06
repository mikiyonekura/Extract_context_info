import function
import csv
from collections import defaultdict
submit_satd_refund = defaultdict(list)
csv.field_size_limit(1000000000)


with open('final_replication_dataset_v2 2.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  # セミコロンでデータを分割

    count = 0
    for row in reader:

        # コード内のコメントはjava parserのエラーの原因になるため削除
        submit_code = function.remove_comments(row[19])
        refund_code = function.remove_comments(row[20])

        satd = row[17]
        submit_code = row[19]
        refund_code = row[20]

        # インデントや改行を削除
        satd = function.remove_indentation_and_newlines(satd)
        submit_code = function.remove_indentation_and_newlines(submit_code)
        refund_code = function.remove_indentation_and_newlines(refund_code)

        submit_satd_refund["satd"].append(satd)
        submit_satd_refund["submit"].append(submit_code)
        submit_satd_refund["refund"].append(refund_code)


# 重複削除のための格納変数
tmp = ""
# ノイズデータを除いたリスト番号を格納するリスト
lists = []

# ファイルを書き込みモードで開く
with open('./output_file/submit2.txt', 'w') as f:
    # ファイルにテキストを書き込む
    for i in range(submit_satd_refund['submit'].__len__()):

        # 一個前のデータと同じでないかつ、文字数が10文字以上の場合
        if tmp != submit_satd_refund['submit'][i] and len(submit_satd_refund['submit'][i]) > 10:
            f.write(submit_satd_refund['submit'][i] + "\n")
            lists.append(i)
            tmp = submit_satd_refund['submit'][i]

with open('./output_file/satd2.txt', 'w') as f:
    # ファイルにテキストを書き込む
    for i in lists:
        f.write(submit_satd_refund['satd'][i] + "\n")


with open('./output_file/refund2.txt', 'w') as f:
    # ファイルにテキストを書き込む
    for i in lists:
        f.write(submit_satd_refund['refund'][i] + "\n")
