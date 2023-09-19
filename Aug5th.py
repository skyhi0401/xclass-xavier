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


food1_input = app.createInput("Bạn có ăn thịt không?","text-area")
food2_input = app.createInput("Bạn có ăn rau không?","text-area")

food1_value = food1_input.value()
food2_value = food2_input.value()

output = app.createOutput("Kết quả") 

if food1_value == "Có" and food2_value == "Có":
    app.display(output, "Bạn là một người có thói quen ăn uống bình thường")
else:
    if food1_value == "Có" and food2_value == "Không":
        app.display(output, "Bạn là một người ngược đãi động vật")
    if food1_value == "Không" and food2_value == "Có":
        app.display(output, "Bạn là một cái máy nhai cỏ nhạt nhẽo")
    if food1_value == "Không" and food2_value == "Không":
        app.display(output, "Một người kén ăn như bạn không nên tồn tại")


app.build(__file__)