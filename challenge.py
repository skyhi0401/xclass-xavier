# pip install xclass-sdk==1.6.1

# to make things easier, let's create a new file, copy this code into that file and modify accordingly
from xclass_sdk.general_app import GeneralApp
# Create an instance of General App
app = GeneralApp("890174f7f3") # insert your API key given by X-Class here

# customize the app, like title, description, author, logo and button color.
# Some example can refer to https://app.xclass.edu.vn/general-app/xclass
app.name = 'Test app'
app.description = 'Test description'
app.author='SkyHi'
app.appLogo='https://uploads-ssl.webflow.com/64b02318b9d14ab16e20227a/64b3fda42fdf5ab7222c5a80_logo-xclass.png'


app.okButton['text'] = 'Generate'
app.okButton['color'] = '#ea850c'
app.okButton['background'] = '#EFEFEF'


app.resetButton['text'] = 'Cancel'
app.resetButton['color'] = 'red'
app.resetButton['background'] = 'blue'

# we only create the input box here.
# U can customize the label/prompt of the input box
input1 = app.createInput("Nhập ngày sinh","text-area")

from datetime import date
import calendar

date_components = input('Enter a date formatted as DD-MM-YYYY: ').split('-')

day, month, year= [int(item) for item in date_components]

d = date(year, month, day)

intDay = d.date(year, month, day).weekday()
days = ["Monday", "Tuesday", "Wednesday","Thu"]

dotw = days[intDay]

print()

# to actually get the value, we can do: 
input1_value = str(input1.value()) # str(...): convert the value to a string
input2_value = str(input2.value())

# usually input1_value is a string, so u can convert it to an int, float,...
input1_value_int = int(input1_value)
input2_value_int = int(input2_value)

# You can do some operations with those variables
sum = input1_value_int + input2_value_int
sum_str = input1_value + input2_value
# but not this, as input1 and input2 are 2 variables pointing to 2 input boxes, not the actual value
# sum = input1 + input2


# create the output box (with a prompt)
# u can create many outputs
output1 = app.createOutput('Output 1')
output2 = app.createOutput('Output 2')

# to display to particular output, use this function
# app.display(<output variable>, message)
app.display(output1, f'Value input1: {input1.value()}. Value input2: {input2.value()}')
app.display(output2, "Sum is {0}".format(sum))

# never forget to add this command. This is crucial so that X-Class SDK can build your app with beautiful UI
app.build(__file__)