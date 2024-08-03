from datetime import datetime, timedelta
from data_schedule import data
from write_csv_file import *


def get_specific_days(start_date_str, end_date_str, day_of_week):
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y").date()
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y").date()
    days = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.strftime("%A") == day_of_week:
            days.append(current_date.strftime("%d-%m-%Y"))
        current_date += timedelta(days=1)
    return days


def get_specific_days2(start_date_str, end_date_str, day_of_week):
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y").date()
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y").date()

    # Ánh xạ số với tên thứ
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    # Kiểm tra xem số có hợp lệ hay không
    if day_of_week not in days_of_week:
        raise ValueError("Invalid day of week. Please provide a number from 1 to 7.")

    specific_day = days_of_week[day_of_week]
    days = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.strftime("%A") == specific_day:
            days.append(current_date.strftime("%d-%m-%Y"))
        current_date += timedelta(days=1)
    return days


def get_specific_days3(start_date_str, end_date_str, day_of_week):
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()

    # Ánh xạ số với tên thứ
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    # Kiểm tra xem số có hợp lệ hay không
    if day_of_week not in days_of_week:
        raise ValueError("Invalid day of week. Please provide a number from 1 to 7.")

    specific_day = days_of_week[day_of_week]
    days = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.strftime("%A") == specific_day:
            days.append(current_date.strftime("%d/%m/%Y"))
        current_date += timedelta(days=1)
    return days


# a = get_specific_days2(
#     day_of_week=3, start_date_str="31-12-2023", end_date_str="10-2-2024"
# )
# print(a)


for j in range(len(data["data"])):
    # print(data["data"][i]["thoi_gian"])
    data_obj = data["data"][j]
    data_obj_thoi_gian = data_obj["thoi_gian"]

    for i in range(len(data_obj_thoi_gian)):
        date_str = f"{data_obj_thoi_gian[i]['thoi_gian']}".split("-")
        start_date_str = date_str[0]
        end_date_str = date_str[1]
        data_obj_num_days = get_specific_days3(
            day_of_week=int(data_obj_thoi_gian[i]["thu"][-1]) - 1,
            end_date_str=end_date_str,
            start_date_str=start_date_str,
        )
        # print("====================")
        print(
            f"{data_obj['ten_hoc_phan']} , {data_obj_thoi_gian[i]['thu']} học các ngày: {data_obj_num_days} tiết {data_obj_thoi_gian[i]['tiet']} lop {data_obj_thoi_gian[i]['phong_hoc']} giáo viên {data_obj['giao_vien']}"
        )
        print("====================")
        write_dates_to_csv3(
            date_of_week=[
                data_obj_thoi_gian[i]["thu"] for k in range(len(data_obj_num_days))
            ],
            dates=data_obj_num_days,
            filename="csv_folder/test3.csv",
            phong_hoc=[
                data_obj_thoi_gian[i]["phong_hoc"]
                for k in range(len(data_obj_num_days))
            ],
            subject_title=[
                data_obj["ten_hoc_phan"] for k in range(len(data_obj_num_days))
            ],
            time_of_lesson=[
                data_obj_thoi_gian[i]["tiet"] for k in range(len(data_obj_num_days))
            ],
            name_of_teacher=[
                data_obj["giao_vien"] for k in range(len(data_obj_num_days))
            ],
        )
    print("-------------------")
