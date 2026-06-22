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

tools = {
    "合計": calc_total,
    "平均": calc_average,
    "最大値": calc_highest,
    "最小値": calc_lowest
    }

text = input("数字を”,”で区切って入力してください：")
scores = text.split(",")


tool_input = input("合計/平均/最大値/最小値の中から欲しい値を入力してください：")

while tool_input != "":
     
  tool = tools[tool_input]
  result = tool(scores)
  input("Enterで結果を表示します")
  print("=============================")
  print(tool_input)
  print(result)
  print("=============================")
  print()
  print("終了する場合はそのままEnterを押してください")
  tool_input = input("続ける場合はもう一度 合計/平均/最大値/最小値の中から欲しい値を入力してください：")

print("プログラムを終了します")
print(tools.keys())
print(tools.values())




