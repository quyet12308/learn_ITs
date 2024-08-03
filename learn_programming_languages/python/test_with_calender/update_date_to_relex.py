import pandas as pd


def insert_missing_dates(csv_file):
    # Đọc dữ liệu từ tệp CSV bằng pandas
    df = pd.read_csv(csv_file)

    # Chuyển đổi cột "date" sang định dạng ngày-tháng-năm
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")

    # Tạo một DataFrame mới chứa tất cả các ngày trong khoảng từ ngày nhỏ nhất đến ngày lớn nhất
    min_date = df["date"].min()
    max_date = df["date"].max()
    date_range = pd.date_range(start=min_date, end=max_date, freq="D")
    all_dates_df = pd.DataFrame({"date": date_range})

    # Loại bỏ các ngày đã tồn tại trong DataFrame ban đầu
    all_dates_df = all_dates_df[~all_dates_df["date"].isin(df["date"])]

    # Thêm các hàng bị thiếu vào DataFrame ban đầu với giá trị "thu2" đến "chu_nhat" cho cột "date_of_week"
    missing_dates_df = pd.DataFrame(
        {
            "date": all_dates_df["date"],
            "date_of_week": all_dates_df["date"]
            .dt.day_name()
            .str.lower()
            .replace("monday", "thu2")
            .replace("tuesday", "thu3")
            .replace("wednesday", "thu4")
            .replace("thursday", "thu5")
            .replace("friday", "thu6")
            .replace("saturday", "thu7")
            .replace("sunday", "chu_nhat"),
            "subject_title": "Nghỉ",
            "time_of_lesson": "Nghỉ",
            "phong_hoc": "Nghỉ",
            "name_of_teacher": "Nghỉ",
        }
    )
    df = pd.concat([df, missing_dates_df]).sort_values("date").reset_index(drop=True)

    # Ghi lại tệp CSV đã cập nhật
    updated_csv_file = csv_file.split(".")[0] + "_updated.csv"
    df.to_csv(updated_csv_file, index=False)

    return updated_csv_file


insert_missing_dates(csv_file="csv_folder/test3_sorted.csv")
