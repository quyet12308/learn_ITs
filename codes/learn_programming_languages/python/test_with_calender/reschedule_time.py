import pandas as pd


def sort_csv_by_date_time(csv_file):
    # Đọc dữ liệu từ tệp CSV bằng pandas
    df = pd.read_csv(csv_file)

    # Chuyển đổi cột "date" sang định dạng ngày-tháng-năm
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")

    # Sắp xếp DataFrame theo cột "date" và "time_of_lesson"
    df = df.sort_values(by=["date", "time_of_lesson"])

    # Ghi lại tệp CSV đã sắp xếp
    sorted_csv_file = csv_file.split(".")[0] + "_sorted.csv"
    df.to_csv(sorted_csv_file, index=False)

    return sorted_csv_file


def sort_csv_by_date_time2(csv_file):
    # Đọc dữ liệu từ tệp CSV bằng pandas
    df = pd.read_csv(csv_file)

    # Chuyển đổi cột "date" sang định dạng ngày-tháng-năm
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")

    # Sắp xếp DataFrame theo cột "date" và "time_of_lesson"
    df = df.sort_values(by=["date", "time_of_lesson"])

    # Ghi lại tệp CSV đã sắp xếp với định dạng ngày-tháng-năm "dd/mm/yyyy"
    sorted_csv_file = csv_file.split(".")[0] + "_sorted.csv"
    df.to_csv(sorted_csv_file, index=False, date_format="%d/%m/%Y")

    return sorted_csv_file


sort_csv_by_date_time2(csv_file="csv_folder/test3.csv")
