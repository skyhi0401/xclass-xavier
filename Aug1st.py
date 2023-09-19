from xclass_sdk.general_app import GeneralApp
# Create an instance of General App
app = GeneralApp("890174f7f3")

app.name = 'Gordon Roast Generator'
app.description = 'Chef Ramsay is here and he is going to shout at you like a pig!'
app.author='SkyHi'
app.appLogo='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2018%2F09%2Fgordon-ramsay-hells-kitchen-02-2000.jpg&q=60'


app.okButton['text'] = 'Cook It'
app.okButton['color'] = 'white'
app.okButton['background'] = '#44c7d9'


app.resetButton['text'] = 'Trash It'
app.resetButton['color'] = 'white'
app.resetButton['background'] = 'red'

NameInput = app.createInput("name","text-area")
FoodInput = app.createInput("food","text-area")

Name = NameInput.value()
Food = FoodInput.value()
 

order = "You can take that " + str(Food) + " and shove it up your arse, " + str(Name) +"!"

output = app.createOutput('insult')

app.display(output,str(order))


app.build(__file__)