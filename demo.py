operators = []
    values = []
    i = 0
    
    while i < len(expression):
        if expression[i] == '+':
            operators.append(expression[i])
            i += 1
        elif expression[i] == '-':
            operators.append(expression[i])
            i += 1
        else:
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
    
    result = values[0]
    for j in range(1, len(values)):
        if operators[j-1] == '+':
            result += values[j]
        elif operators[j-1] == '-':
            result -= values[j]