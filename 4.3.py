def translate(binary):
    Binary_number = []
    if binary != 0:
        while abs(binary)>1:
            if binary%2 == 0:
                Binary_number.append("0")
                binary = binary/2
            else:
                Binary_number.append("1")
                binary-=1
                binary = binary /2
        Binary_number.append("1")
    if binary < 0:
        Binary_number.append("-")
    Binary_number.reverse()
    if binary == 0:
        Binary_number.append("0")
    binary_print = ''.join(Binary_number)
    return binary_print

while 1:
    print("Send me a DECIMAL binary for translate it on binary binary")
    decimal = int(input())
    print("Binary code is " + translate(decimal))
    if translate(decimal) == "0":
        print("End")
        break
