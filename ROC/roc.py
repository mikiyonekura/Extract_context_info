# GroundTruth.csvとPredicted.csvを読み込んでROC曲線を作成する

from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# GroundTruth.csvを読み込む
with open('/Users/yonekuramiki/Desktop/resarch/prepare_project/ROC/GroundTruth_pilot.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')  # カンマでデータを分割

    # 正解ラベルを格納するリスト
    label = []
    for row in reader:
        label.append(row[1])

# Predicted.csvを読み込む
with open('/Users/yonekuramiki/Desktop/resarch/prepare_project/ROC/Prediction_pilot.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')  # カンマでデータを分割

    # 予測ラベルを格納するリスト
    predicted = []
    for row in reader:
        predicted.append(row[1])

# 正解ラベルと予測ラベルをnumpy配列に変換
label = np.array(label)
predicted = np.array(predicted)

# 正解ラベルと予測ラベルをfloat型に変換
label = label.astype(np.float64)
predicted = predicted.astype(np.float64)

# ROC曲線を作成
fpr, tpr, thresholds = roc_curve(label, predicted)
roc_auc = auc(fpr, tpr)

# ROC曲線をプロット
plt.plot(fpr, tpr, label='ROC curve (area = %.2f)' % roc_auc)
plt.legend()
plt.title('ROC curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.grid(True)
# 画像として保存
# plt.savefig('pilot_roc.png')

# PR曲線を作成

precision, recall, thresholds = precision_recall_curve(label, predicted)
average_precision = average_precision_score(label, predicted)

plt.plot(recall, precision, label='PR curve (area = %.2f)' % average_precision)
plt.legend()
plt.title('PR curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.grid(True)
# 画像として保存
plt.savefig('/Users/yonekuramiki/Desktop/resarch/prepare_project/ROC/pilot_roc_pr.png')
