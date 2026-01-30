name = input("请输入您的名字:")
money = 5000000
def menu():
    print("-------------主菜单-------------")
    print(f"{name},您好,欢迎来到黑马银行ATM。请选择操作:")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    input_num = input("请输入您的选择:")
    return input_num
def query(title):
    if title:
        print("------------查询余额------------")
    print(f"{name}您好,您的余额剩余:{money}元")
def deposit():
    global money
    amount = int(input("请输入存款金额:"))
    money += amount
    print(f"{name}您好,您存款{amount}元成功")
    query(False)
def withdraw():
    global money
    amount = int(input("请输入取款金额:"))
    if amount > money:
        print("余额不足,取款失败")
        return
    money -= amount
    print(f"{name}您好,您取款{amount}元成功")
    query(False)
while True:
    input_num = menu()
    if input_num == "1":
        query(True)
    elif input_num == "2":
        deposit()
    elif input_num == "3":
        withdraw()
    elif input_num == "4":
        print("感谢使用,再见!")
        break
    else:
        print("输入错误,请重新选择！")
