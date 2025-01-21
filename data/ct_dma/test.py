import pandas as pd

with open('./data/ct_dma/ct_dma_train.pkl', 'rb') as f:
    data = pd.read_pickle(f)

# # 读取 .pkl 文件
# data = pd.read_pickle('ct_dma_train.pkl')


df = pd.DataFrame(data)
# 将数据保存为 .csv 文件
df.to_csv('output_file.csv', index=False)