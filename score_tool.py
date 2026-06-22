def calc_total(scores):
    total = 0
    for score in scores:
         total = total + int(score) 
    return total

def calc_highest(scores):
     highest = 0
     for score in scores:
           if int(score) >= highest:
               highest = int(score)
     return highest

def calc_lowest(scores):
     lowest = int(scores[0])
     for score in scores:
          if int(score) <= lowest:
               lowest = int(score)
     return lowest

def calc_average(scores):
     average = calc_total(scores) / len(scores)
     return average

text = input("数字を”,”で区切って入力してください：")
scores = text.split(",")

tool_input = input("合計/平均/最大値/最小値の中から欲しい値を入力してください：")
if tool_input == "合計":
     result = calc_total(scores)
elif tool_input == "平均":
     result = calc_average(scores)
elif tool_input == "最大値":
     result = calc_highest(scores)
elif tool_input == "最小値":
     result = calc_lowest(scores)
else:
     result = "error-入力値を確認してください-"

input("Enterで結果を表示します")
print("==============================")
print(tool_input)
print(result)
print("==============================")


again = "はい"
while again == "はい":

 number = input("数字を入力してください：")
 print(f"入力された数字は{number}です")

 again = input("続けますか？(はい/いいえ)：")


print("プログラム終了")