#定義函式
def reverse(number):
    result=[]
    temp=0
    #迴圈,將number除以10,餘數存至esul中,商數繼續放入迴圈執行直至終止
    while number!=0:
        temp=number%10
        result+=[int(temp)]
        number=number//10
    for i in result:
        int(i)
        print(i,end="")
#使用者輸入
num=int(input("Enter an integer: "))
#執行函式
reverse(num)
