def calculate_bmi(weight_kg, height_m):
    """
    BMIを計算する関数
    :param weight_kg: 体重（キログラム）
    :param height_m: 身長（メートル）
    :return: 計算されたBMI値
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

print('世界保健機関(WHO)の判定基準')
print('BMI: 16未満...痩せすぎ 16.00〜16.99以下...痩せ 17.00〜18.49以下...痩せぎみ 18.50〜24.99以下...普通体重 25.00〜29.99以下...前肥満 30.00〜34.99以下...肥満(1度) 35.00〜39.99以下...肥満(2度) 40.00以上...肥満(3度)')

# ユーザーからの入力を受け取る
weight = float(input("体重（kg）を入力してください: "))
height = float(input("身長（m）を入力してください: "))

# BMIを計算
bmi_result = calculate_bmi(weight, height)

# BMIを表示
print(f"計算されたBMIは {bmi_result:.2f} です。")

# BMIに基づいたメッセージを表示
if bmi_result < 18.50:
    print("たくさん食べて運動しよう！")
elif 25.00 <= bmi_result:
    print("酸素運動を計画的にしよう！")
else:
    print("いいよ！その調子で頑張れ！")