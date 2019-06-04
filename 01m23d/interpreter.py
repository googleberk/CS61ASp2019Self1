# I am trying to build an interpreter that can interpret string literals
# with basic [operator(operand, operand)] inside of it.
# for example: my program should output 7 when the string is "add(3,4)"
# currently, I only support add and mul

# s is the string to be interpreted
def eval(s):
    i = 0

    if s[i] == 'a' and s[i + 1] == 'd' and s[i + 2] == 'd':
        operator = "add"
    elif s[i] == 'm' and s[i + 1] == 'u' and s[i + 2] == 'l':
        operator = "mul"

    firstOperand = s[4]
    secondOperand = s[7]

    if operator == "add":
        return int(firstOperand) + int(secondOperand)
    elif operator == "mul":
        return int(firstOperand) * int(secondOperand)

# Main Function
if __name__ == '__main__':
    string = "add(3, 4)"
    print(eval(string))
    string = "mul(3, 4)"
    print(eval(string))
    string = "add(add(1, 2), 4)"
    print(eval(string))
