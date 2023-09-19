from xclass_sdk.general_app import GeneralApp
# Create an instance of General App
app = GeneralApp("890174f7f3")

app.name = 'Kiểm Tra Ăn Uống'
app.description = 'Chú Roger ở đây để kiểm tra xem bạn có thói quen ăn uống như thế nào!'
app.author='SkyHi'
app.appLogo='https://s.keepmeme.com/files/en_posts/20200919/uncle-roger-haiyaaa-rice-meme-433d6de8d2c1d49a90ef1d92188007de.jpg'

app.okButton['text'] = 'Kiểm thôi'
app.okButton['color'] = 'white'
app.okButton['background'] = '#b3351c'

app.resetButton['text'] = 'Trả dép đi về'
app.resetButton['color'] = 'white'
app.resetButton['background'] = '#b79491'

sum = 0

word_input = app.createInput("Input words or phrases:","text-area")

output = app.createOutput("Total") 

length = len(str(word_input.value()))

for character in str(word_input.value()):
    if character in ("u", "e", "o", "a", "i"):
        sum += 1

app.display(output, sum)

app.build(__file__)