human = int(input("点数を入力する人数を入力してください："))

scores = []

for i in range(human):
    

    scores.append(int(input(f"{i + 1}人目のスコアを入力してください：")))


print(f"それぞれの点数:{scores}(点)")

total = 0

for score in scores:
    print(f"{score}点")
    total = total + score

print(f"合計：{total}点")

ave = total / human
print(f"平均：{ave}点")
