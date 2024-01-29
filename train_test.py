import pandas as pd
from sklearn.model_selection import train_test_split

# ファイルを読み込む関数


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


# コメントデータと追加のファイルを読み込み
comments = load_file('./output_file/satd_comment_line.txt')
labels = load_file('./output_file/label.txt')
one_under_block = load_file('./output_file/one_under_block.txt')
two_under_block = load_file('./output_file/two_under_block.txt')
three_under_block = load_file('./output_file/three_under_block.txt')
all_under_block = load_file('./output_file/all_under_block.txt')

# ラベルを整数に変換
labels = [int(label) for label in labels]

# データフレームに変換
df = pd.DataFrame({
    'comment': comments,
    'label': labels,
    'one_under_block': one_under_block,
    'two_under_block': two_under_block,
    'three_under_block': three_under_block,
    'all_under_block': all_under_block
})

# データをシャッフル
df = df.sample(frac=1).reset_index(drop=True)

# データを分割
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# ファイルに保存する関数


def save_to_file(dataframe, name, columns, folder='./output_file/train_test/'):
    for column in columns:
        file_path = f'{folder}{name}_{column}.txt'
        dataframe[column].to_csv(file_path, index=False, header=False)


# 分割したデータセットを保存
columns = ['comment', 'label', 'one_under_block', 'two_under_block', 'three_under_block', 'all_under_block']
for dataset, name in [(train_df, 'train'), (test_df, 'test')]:
    save_to_file(dataset, name, columns)
