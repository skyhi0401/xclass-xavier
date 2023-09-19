# pip install xclass-sdk==1.7.4

from xclass_sdk.chat_bot_app import ChatBotApp

app = ChatBotApp("890174f7f3")
app.name = "Chat Bot App"
app.author = "X-Class"
app.slug = "welcome-bot" # app will be hosted in `https://app.xclass.edu.vn/<username>/welcome-bot`
app.description = "This is my chat bot app"
app.greetingMessage = "Hello, welcome to my chat bot app"
app.appLogo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEBx9Wr0-Vrvo7-X_EwAXnCxBrBODj3sjPLE_6DZPA&s"
# pass the name of logic file (in the same folder with build.py file)
app.build("logic.py")

# python build.