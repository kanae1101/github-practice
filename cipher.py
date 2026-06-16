text = input("文字列を入力してください：")
amount = int(input("ずらす文字数を入力してください(0~25)："))

result = ""

for letter in text:
    
    number = ord(letter)
    
    if number >=97:
        number_border = 123
    else:
        number_border = 91
    number = number + amount
    

    if number >= number_border:
        number = number -26
    
    result = result + chr(number)

print(result)



