msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

x = ""
oper = ""
y = ""
result = 0.0
number = False
operand = False
zero = False
repeat = True
operators = "+, -, *, /"
memory = 0.0


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v == round(v):
        output = True
    else:
        output = False
    return output


while repeat:
    number = False
    while number is False or operand is False or zero is False:
        number = False
        operand = False
        zero = False
        val = input(msg_0)
        val = val.split(" ")
        oper = val[1]
        answer = ""

        try:
            if val[0] == "M":
                x = memory
            else:
                x = float(val[0])
            if val[2] == "M":
                y = memory
            else:
                y = float(val[2])
        except ValueError:
            print(msg_1)
        else:
            number = True

        if oper in operators:
            operand = True
        else:
            print(msg_2)

        check(x, y, oper)

        if oper == "/" and y == 0.0:
            print(msg_3)
            zero = False
        else:
            zero = True

    if oper == "+":
        result = x + y
        print(result)
    if oper == "-":
        result = x - y
        print(result)
    if oper == "*":
        result = x * y
        print(result)
    if oper == "/":
        result = x / y
        print(result)

    while answer not in ["y", "n"]:
        answer = input(msg_4)
        if answer == "y" and is_one_digit(result) is False:
            memory = result
        elif answer == "y":
            msg_index = 10
            answer = ""
            while answer not in ["y", "n"] or msg_index < 13:
                answer = input(msg_[msg_index])
                if answer == "n":
                    msg_index = 15
                elif answer == "y":
                    msg_index += 1
            if answer == "y":
                memory = result

    answer = ""
    while answer not in ["y", "n"]:
        answer = input(msg_5)
        if answer == "y":
            repeat = True
        else:
            repeat = False
