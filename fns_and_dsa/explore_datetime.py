from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print(f"current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

    number_of_days = int(input("Enter a number of days: "))
    def calculate_future_date():
        future_date = current_date + timedelta(days = number_of_days)
        print(f"Future Date: {future_date.strftime("%Y-%m-%d")}")
    calculate_future_date()


display_current_datetime()