expression = input('Nhập biểu thức: ')

expr_length = len(expression)
current_value = 0

for i in range (0,expr_length):
    current_char = expression[i]
    if current_char.isdigit() and (i==0) or not expression[i-1].isdigit():
        final_pos = i
        while(final_pos < expr_length and expression[final_pos].isdigit()):
            final_pos += 1
        #final_pos will be the position of the first non-digit character after i
        toan_hang = int(expression[i:final_pos])
        # xac dinh toan tu
        toan_tu = '+'
        if i > 0:
            toan_tu = expression[i-1]
        # tinh toan vao current_value
        if toan_tu == '+':
            current_value += toan_hang
        else:
            current_value -= toan_hang
print(current_value)