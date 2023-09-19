# pip install xclass-sdk==1.6.1

# to make things easier, let's create a new file, copy this code into that file and modify accordingly
from xclass_sdk.general_app import GeneralApp
# Create an instance of General App
app = GeneralApp("890174f7f3") # insert your API key given by X-Class here

# customize the app, like title, description, author, logo and button color.
# Some example can refer to https://app.xclass.edu.vn/general-app/xclass
app.name = 'Date calculator'
app.description = 'Give me a random date and I will show you the day of the week'
app.author='SkyHi'
app.appLogo='https://uploads-ssl.webflow.com/64b02318b9d14ab16e20227a/64b3fda42fdf5ab7222c5a80_logo-xclass.png'


app.okButton['text'] = 'Generate'
app.okButton['color'] = '#ea850c'
app.okButton['background'] = '#EFEFEF'


app.resetButton['text'] = 'Cancel'
app.resetButton['color'] = 'red'
app.resetButton['background'] = 'blue'

# we only create the input box here.
output = app.createOutput('Result')
# U can customize the label/prompt of the input box

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_anchor_day(year):
    anchor_days = [2, 0, 5, 3]  # Anchor days for the 4 centuries (1700, 1800, 1900, 2000)
    century = year // 100
    return (anchor_days[century % 4] + (year % 100) + ((year % 100) // 4)) % 7

def get_doomsday(month, year):
    doomsday_offset = [3, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    return (doomsday_offset[month - 1] + get_anchor_day(year)) % 7

date_input = app.createInput("Enter a date in dd/mm/yyyy format: ", "text-area")
date_string = date_input.value()
day, month, year = map(int, date_string.split('/'))
    
if month < 1 or month > 12 or day < 1 or day > 31 or day > 30 and month in [4, 6, 9, 11]:
     app.display(output,"Invalid date.")
    
if month == 2:
    if is_leap_year(year) and day > 29 or day > 28:
        app.display(output,"Invalid date.")
    
day_of_weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
doomsday = get_doomsday(month, year)
day_of_week = (doomsday + day - 1) % 7
    
app.display(output, f"The day of the week for {day}/{month}/{year} is {day_of_weeks[day_of_week]}.")


# create the output box (with a prompt)
# u can create many outputs


# to display to particular output, use this function
# app.display(<output variable>, message)

# never forget to add this command. This is crucial so that X-Class SDK can build your app with beautiful UI
app.build(__file__)

