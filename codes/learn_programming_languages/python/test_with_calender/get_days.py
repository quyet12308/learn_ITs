from datetime import timedelta, date, datetime

def get_dates(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y").date()
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y").date()
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    return dates

def get_dates2(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y").date()
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y").date()
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime("%d-%m-%Y"))
        current_date += timedelta(days=1)
    return dates

def get_dates3(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime("%d/%m/%Y"))
        current_date += timedelta(days=1)
    return dates

# a = get_dates2(end_date_str="10-1-2024",start_date_str="1-12-2023")
# print(a)