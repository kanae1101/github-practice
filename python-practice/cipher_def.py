text = input("文字列を入力してください：")
amount = int(input("ずらす文字数を入力してください："))

def convert_letter(letter, amount):


     number = ord(letter)
   
     if 122 >= number >= 97:
           base = 97
     elif 90 >= number >=65:
           base = 65
     else:
           return chr(number)
         
     number = number - base
     number = (number + amount) % 26
     number = number + base
     
     return chr(number)

result = ""
for letter in text:
    
    result = result + convert_letter(letter,amount)

print(result)
