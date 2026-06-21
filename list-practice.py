#human = int(input("点数を入力する人数を入力してください："))

#scores = []

#for i in range(human):
    

#    scores.append(int(input(f"{i + 1}人目のスコアを入力してください：")))


#print(f"それぞれの点数:{scores}(点)")

text = input("点数を,で区切って入力してください：")

scores = text.split(",")
#print(scores)

total = 0

print(f"{len(scores)}人それぞれの点数を表示します")
for score in scores:
    print(f"{score}点")
    total = total + int(score)

print("=======================")
print()
print(f"合計：{total}点")

#ave = total / human
ave = total / len(scores)
print(f"平均：{ave}点")
