letter = input("アルファベット1文字を入力してください：")

number = ord(letter)
print(number)

if number >=97:
    number_boder = 123
else:
    number_boder = 91
number = number + 3
print(number)

if number >= number_boder:
    number = number -26
print(number)

print(chr(number))

