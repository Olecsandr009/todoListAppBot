import datetime
import time

global current_date

named_tuple = time.localtime()
date_data = time.strftime("%Y-%m-%d %H-%M-%S", named_tuple)

current_date = str(date_data).split(" ")[0]
current_time = str(date_data).split(" ")[1]

current_hour = int(str(current_time).split("-")[0])
current_min = int(str(current_time).split("-")[1])
current_sec = int(str(current_time).split("-")[2])

deadline_date = current_date


# Get deadline function
def deadline(days):
    global deadline_date

    current_year = str(current_date).split("-")[0]
    current_month = str(current_date).split("-")[1]
    current_day = str(current_date).split("-")[2]

    try:
        d = datetime.date(2024, 2, int(current_day) + days)
        deadline_date = f"{current_year}-{current_month}-{int(current_day) + days}"

    except ValueError as error:
        deadline_date = get_new_date(current_year, current_month, int(current_day) + days)
        print(deadline_date, "function")

    return f"{deadline_date}"


# get month end function
def get_month_end(year, month):
    month_end = datetime.date(int(year), int(month) + 1, 1) - datetime.timedelta(days=1)
    return int(str(month_end).split("-")[2])


# get new date function
def get_new_date(year, month, day):
    month_end = get_month_end(year, month)

    current_year = int(year)
    current_month = int(month)
    current_day = int(day)

    while(True):
        current_day = int(current_day) - month_end
        current_month = current_month + 1

        if current_month > 12:
            current_year = current_year + 1
            current_month = 1

        if(current_day < month_end): break


    # return f"{current_year}-{current_month}-{current_day}"
    return datetime.datetime(current_year, current_month, current_day, current_hour, current_min, current_sec)



