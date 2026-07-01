def calc_total(scores):
    total = 0
    for score in scores:
         total = total + (score) 
    return total

def calc_highest(scores):
     highest = scores[0]
     for score in scores:
           if score >= highest:
               highest = score
     return highest

def calc_lowest(scores):
     lowest = (scores[0])
     for score in scores:
          if (score) <= lowest:
               lowest = (score)
     return lowest

def calc_average(scores):
     average = calc_total(scores) / len(scores)
     return average

def calc_count(scores):
    return len(scores)

def calc_80over(scores):
    over80 = 0
    for score in scores:
        if (score) >= 80:
            over80 = over80 + 1
    return over80

def calc_countscore(scores):
    count = 0
    border = int(input("何点以上の人数を数えますか？"))
    for score in scores:
        if (score) >= border:
            count = count + 1
    return border , count

def calc_middle(scores):
    scores_sorted = sorted(scores)
    middle_index = len(scores)//2
    middle = scores_sorted[middle_index]
    if len(scores) % 2 == 0 :
        middle = ((scores_sorted[middle_index]) + (scores_sorted[middle_index - 1])) / 2
    return middle

def calc_sort_ascending(scores):
    scores_sorted = sorted(scores)

    scores_text = []
    for score in scores_sorted:
        scores_text.append(str(score))

    return ",".join(scores_text)

def calc_sort_descending(scores):
    scores_sorted = sorted(scores,reverse=True)

    scores_text = []
    for score in scores_sorted:
        scores_text.append(str(score))

    return ",".join(scores_text)

def calc_sort(scores):
    order_name = ""
    while order_name == "":
        sort_input = input("昇順なら1を、降順なら2を入力してください")
        if sort_input == "1":
           reverse = False
           order_name = "昇順"
        elif sort_input == "2":
           reverse = True
           order_name = "降順"
        else:
            print("入力値を確認してください")
    scores_sorted = sorted(scores,reverse = reverse)

    scores_text = []
    for score in scores_sorted:
        scores_text.append(str(score))

    return ",".join(scores_text) , order_name


def menu():
    number = 0
    print("============================")
    print("使えるツール一覧")

    for name in tools:
         number = number + 1
         print(f"{number} . {name}")

    print("============================")


tools = {
    "合計": (calc_total,"点"),
    "平均": (calc_average,"点"),
    "最大値": (calc_highest,"点"),
    "最小値": (calc_lowest,"点"),
    "人数": (calc_count,"人"),
    "80点以上の人数": (calc_80over,"人"),
    "任意の点以上の人数": (calc_countscore,"人"),
    "中央値": (calc_middle,"点"),
    "並び替え(昇順)":(calc_sort_ascending,""),
    "並び替え(降順)":(calc_sort_descending,""),
    "並び替え":(calc_sort,"")
    }
names = list(tools)

text = input("数字を”,”で区切って入力してください：")
scores_text = text.split(",")

scores = []
for score in scores_text:
    scores.append(int(score))

menu()

tool_input = input("使いたいツールの名前か番号を入力してください：")

while tool_input != "":
  if tool_input.isdigit():
      menu_number = int(tool_input)
      if 1 <= menu_number <= len(tools):
         tool_input = names[menu_number - 1]
      else:
          tool_input = "error"

  if tool_input in tools:
          
     tool,unit = tools[tool_input]
     result = tool(scores)
     label = tool_input
     if tool_input == "任意の点以上の人数":
           border,count = result
           label = (f"{border}点以上の人数")
           result = count
     elif tool_input == "並び替え":
           sorted_text, order_name = result
           label = (f"並び替え({order_name})")
           result = sorted_text

     input("Enterで結果を表示します")
     print("=============================")
     print(label)
     print(f"{result}{unit}")
     print("=============================")

  else:
      print("入力値を確認してください")

  again = input("計算を続けますか？はい/いいえ：")
  if again == "はい" :
     menu() 
     tool_input = input("もう一度ツール名か番号を入力してください：")
  else:
     tool_input = ""

print("プログラムを終了します")


