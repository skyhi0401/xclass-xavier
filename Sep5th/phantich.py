
# 
import pandas as pd
# doc file
df = pd.read_csv("2021.csv")
# in 5 dòng đầu
print(df.head())
# in tất cả feature (in tất cả các cột đang có)
print("Cac cot trong du lieu")
print(df.columns)

print("Du lieu diem Toan, Ly, Hoa")
df = df["mathematics_score"]

# Xoa cac dong du lieu bi thieu
df.dropna(inplace=True)
print(df.head())

# import cac thu vien bieu dien du lieu
import matplotlib.pyplot as plt
import seaborn as sns

# ve heatmap de nhin thay tuong quan cua cac cot du lieu voi nhau
#numeric_df = df.select
#plt.figure(figsize=(10,10))
#sns.heatmap(numeric_df.corr)
#plt.show()

#Thu vien dung Machine learning AI scikitlearn
# cai thu vien bang lenh
# pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# tao feature va target
# feature
x = df[["mathematics_score"]]
# target
y = df["physics_score"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

model = LinearRegression()

print("Dang train AI...")
print("sdasdas")