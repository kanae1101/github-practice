text = input("文字列を入力してください：")
amount = int(input("ずらす文字数を入力してください："))

result = ""

for letter in text:

    number = ord(letter)
    range_size  = 26
    
    if 122 >= number >= 97:
        base = 97
    elif 90 >= number >=65:
        base = 65
    else:
        result = result + letter
        continue

    number = number - base
    number = (number + amount) % range_size
    number = number + base

    
    result = result + chr(number)

print(result)
