import csv
from get_days import *
from data_schedule import data
import os

dates = get_dates3(start_date_str="29/01/2024", end_date_str="16/06/2024")


def write_dates_to_csv(dates, filename):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for date in dates:
            writer.writerow({"date": date})


def write_dates_to_csv2(
    dates,
    date_of_week,
    subject_title,
    time_of_lesson,
    phong_hoc,
    filename,
):
    with open(filename, "a", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "date",
            "date_of_week",
            "subject_title",
            "time_of_lesson",
            "phong_hoc",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if os.path.exists(filename):
            pass
        else:
            writer.writeheader()
        for i in range(len(dates)):
            writer.writerow(
                {
                    "date": dates[i],
                    "date_of_week": date_of_week[i],
                    "subject_title": subject_title[i],
                    "time_of_lesson": time_of_lesson[i],
                    "phong_hoc": phong_hoc[i],
                }
            )


def write_dates_to_csv3(
    dates,
    date_of_week,
    subject_title,
    time_of_lesson,
    phong_hoc,
    name_of_teacher,
    filename,
):
    if os.path.exists(filename):
        with open(filename, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for i in range(len(dates)):
                writer.writerow(
                    [
                        dates[i],
                        date_of_week[i],
                        subject_title[i],
                        time_of_lesson[i],
                        phong_hoc[i],
                        name_of_teacher[i],
                    ]
                )
    else:
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [
                    "date",
                    "date_of_week",
                    "subject_title",
                    "time_of_lesson",
                    "phong_hoc",
                    "name_of_teacher",
                ]
            )
            for i in range(len(dates)):
                writer.writerow(
                    [
                        dates[i],
                        date_of_week[i],
                        subject_title[i],
                        time_of_lesson[i],
                        phong_hoc[i],
                        name_of_teacher[i],
                    ]
                )


# write_dates_to_csv(dates=dates,filename="csv_folder/date_test.csv")

# write_dates_to_csv3(
#     date_of_week=["1", "2", "3", "4"],
#     dates=["26/1/2024", "25/1/2024", "24/1/2024", "23/1/2024"],
#     filename="csv_folder/test.csv",
#     subject_title=["mon1", "mon2", "mon3", "mon4"],
#     time_of_lesson=["time1", "time2", "time3", "time4"],
#     phong_hoc=["phong1", "phong2", "phong3", "phong4"],
# )
