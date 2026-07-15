height = float(input("身長(cm)："))
weight = float(input("体重(kg)："))
height_m = height/100
bmi = weight/(height_m**2)

print("=========================")
print("BMI計算機")
print("=========================")
print(f"身長：{height}cm")
print(f"体重：{weight}kg")
print("-------------------------")
print()
print("結果")
print (f"BMI：{bmi:.2f}")
if bmi >= 25:
    print("判定：肥満")
elif bmi >=18.5:
    print("判定：標準")
else:
    print("判定：低体重")
print()
print("=========================")