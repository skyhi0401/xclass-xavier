# pip install xclass-sdk==1.6.1

# to make things easier, let's create a new file, copy this code into that file and modify accordingly
from xclass_sdk.general_app import GeneralApp
# Create an instance of General App
app = GeneralApp("890174f7f3") # insert your API key given by X-Class here

# customize the app, like title, description, author, logo and button color.
# Some example can refer to https://app.xclass.edu.vn/general-app/xclass
app.name = 'Điền dãy số lẻ'
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
number = app.createInput("Nhập số","text-area")

# to actually get the value, we can do: 

# usually input1_value is a string, so u can convert it to an int, float,...
n = int(number.value())

output1 = app.createOutput('Tạo ra dãy số')
dayso = ""

# You can do some operations with those variables
for i in range(1, n+1):
    if i % 2 == 1:
        if i == 1:
            dayso = dayso + str(i)
        else:
            dayso = dayso + ", " + str(i)


# but not this, as input1 and input2 are 2 variables pointing to 2 input boxes, not the actual value
# sum = input1 + input2


# create the output box (with a prompt)
# u can create many outputs

# to display to particular output, use this function
# app.display(<output variable>, message)
app.display(output1, dayso)

# never forget to add this command. This is crucial so that X-Class SDK can build your app with beautiful UI
app.build(__file__)