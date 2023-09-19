def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_anchor_day(year):
    anchor_day = 2  # 1800 is an anchor year with anchor day as Tuesday
    year_difference = year - 1800
    anchor_day = (anchor_day + year_difference) % 7
    return anchor_day

def get_doomsday(month, year):
    anchor_day = get_anchor_day(year)
    if is_leap_year(year):
        doomsday_offset = [3, 7, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]  # For leap years
    else:
        doomsday_offset = [3, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]  # For non-leap years
    return (doomsday_offset[month - 1] + anchor_day) % 7

def main():
    date_input = input("Enter a date in dd/mm/yyyy format: ")
    day, month, year = map(int, date_input.split('/'))
    
    if month < 1 or month > 12 or day < 1 or day > 31:
        print("Invalid date.")
        return
    
    if month == 2:
        if is_leap_year(year):
            if day > 29:
                print("Invalid date.")
                return
        elif day > 28:
            print("Invalid date.")
            return
    elif month in [4, 6, 9, 11] and day > 30:
        print("Invalid date.")
        return
    elif day > 31:
        print("Invalid date.")
        return
    
    day_of_weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    doomsday = get_doomsday(month, year)
    day_of_week = (doomsday + day - 1) % 7
    
    print(f"The day of the week for {day}/{month}/{year} is {day_of_weeks[day_of_week]}.")

if __name__ == "__main__":
    main()