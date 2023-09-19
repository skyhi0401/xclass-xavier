ten=""
dang_hoi_ten=False

def output(message):
  global ten, dang_hoi_ten, is_sot
  if ten == "" and dang_hoi_ten == False:
    dang_hoi_ten = True
    return "Tên của bạn là gì?" # return a string to send a single message
  else:
    ten = message
    return [
      "Hello, tên của bạn là \n" + ten + ".",
      "Chào mừng đến với X-Class"
    ] # return a list of string to send multiple messages