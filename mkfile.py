import os

def save_to_java_files(txt_file_name,type):
    # 入力ファイルを開く
    with open(txt_file_name, 'r') as txt_file:
        lines = txt_file.readlines()

    # 各行を新しいJavaファイルに書き込む
    # a = len(lines) #本当はこれ
    a = 100
    for i in range(a):
        java_file_name = f"{type}_output{i+1}.java" # Javaファイルの名前を作成
        with open(f"./{type}_split_file/"+java_file_name, 'w') as java_file:
            java_file.write(lines[i]) # ファイルに行を書き込む

    print(f"{a} Java files have been successfully created.")

# 例えば、'submit.txt'というテキストファイルからJavaファイルを作りたい場合
save_to_java_files('./output_file/submit.txt',type="submit")
save_to_java_files('./output_file/refund.txt',type="refund")
