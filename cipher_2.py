text = input("文字列を入力してください：")
amount = int(input("ずらす文字数を入力してください(0~25)："))

result = ""

for letter in text:

    number = ord(letter)
    range_size  = 26
    
    if 123 >= number >= 97:
        base = 97
    elif 91 >= number >=65:
        base = 65
    else:
        base = 0
        amount = 0
        range_size = number + 1

    number = number - base
    number = (number + amount) % range_size
    number = number + base

    
    result = result + chr(number)

print(result)
