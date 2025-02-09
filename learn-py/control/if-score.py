while True:
    try:
        score = int(input("请输入学生成绩: "))
        if score < 0 or score > 100:
            print("输入的成绩无效，请输入0到100之间的数字.")
        else:
            break
    except ValueError:
        print("输入错误，请输入一个有效的整数.")

if score >= 90:
    print("评级为: A")
elif score >= 80:
    print("评级为: B")
elif score >= 60:
    print("评级为: C")
else:
    print("评级为: D")

