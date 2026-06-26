def calc_total(scores):
    total = 0
    for score in scores:
         total = total + int(score) 
    return total

def calc_highest(scores):
     highest = int(scores[0])
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

def calc_count(scores):
    return len(scores)

def calc_80over(scores):
    over80 = 0
    for score in scores:
        if int(score) >= 80:
            over80 = over80 + 1
    return over80

def calc_countscore(scores):
    count = 0
    border = int(input("何点以上の人数を数えますか？"))
    for score in scores:
        if int(score) >= border:
            count = count + 1
    return border , count

tools = {
    "合計": (calc_total,"点"),
    "平均": (calc_average,"点"),
    "最大値": (calc_highest,"点"),
    "最小値": (calc_lowest,"点"),
    "人数": (calc_count,"人"),
    "80点以上の人数": (calc_80over,"人"),
    "任意の点以上の人数": (calc_countscore,"人")
    }

text = input("数字を”,”で区切って入力してください：")
scores = text.split(",")


tool_input = input("合計/平均/最大値/最小値/人数の中から欲しい値を入力してください：")

while tool_input != "":
         
  if tool_input in tools:
          
     tool,unit = tools[tool_input]
     result = tool(scores)
     label = tool_input
     if tool_input == "任意の点以上の人数":
           border,count = result
           label = (f"{border}点以上の人数")
           result = count

     input("Enterで結果を表示します")
     print("=============================")
     print(label)
     print(f"{result}{unit}")
     print("=============================")
     print()
     print("終了する場合はそのままEnterを押してください")
     
  else:
      print("入力値を確認してください")
 
  tool_input = input("続ける場合はもう一度 合計/平均/最大値/最小値/人数の中から欲しい値を入力してください：")

print("プログラムを終了します")



