import pandas as pd 
from data_schedule import data


# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data["data"])

# Chuyển đổi cột "thoi_gian" thành nhiều cột riêng biệt
df = pd.concat([df.drop(['thoi_gian'], axis=1), df['thoi_gian'].apply(pd.Series)], axis=1)

# Lưu DataFrame vào file CSV
df.to_csv('csv_folder/data.csv', index=False)