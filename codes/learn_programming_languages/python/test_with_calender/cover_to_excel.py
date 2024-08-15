import pandas as pd


def convert_csv_to_excel(csv_file, excel_file):
    # Đọc dữ liệu từ tệp CSV bằng pandas
    df = pd.read_csv(csv_file)

    # Ghi dữ liệu vào tệp Excel
    df.to_excel(excel_file, index=False)


convert_csv_to_excel(
    # csv_file="csv_folder/test2.csv", excel_file="excel_folder/test2.xlsx"
    csv_file="csv_folder/test3_sorted_updated.csv",
    excel_file="excel_folder/test3_sorted_updated.xlsx",
)
