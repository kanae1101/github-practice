age = int(input("年齢を入力してください："))
if age >= 20:
    print("成人ですね")
    print("選挙に行けます")
    print("お酒も飲めます")
elif age >= 18:
    print("成人ですね")
    print("選挙には行けます")
    print("お酒はまだ飲めません")
else:
    print("未成年ですね")
print("プログラム終了")