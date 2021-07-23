#定義函式,參數維一個lis與要刪除的數量n
def remove_outliers(a_list,n):
    b_list=[]
    #將要刪除的值存入另一個lis並刪除原本lis中的值
    for i in range (0,n):
        b_list+=[int(max(a_list))]
        b_list+=[int(min(a_list))]
        a_list.remove(max(a_list))
        a_list.remove(min(a_list))
    #返還被刪除的值所組成的陣列
    return b_list
a_list=[]
#使用者輸入,至輸入q或Q時停止
n=int(input('Enter the number of smallest and largest values to remove: '))
s=input('Enter a value (q or Q to quit): ')
while (s!='Q' and s!='q'):
    a_list+=[int(s)]
    s = input('Enter a value (q or Q to quit): ')
#列印原始lis
print('The original data: ',a_list)
#防呆
length=len(a_list)-1
if length<2*n:
    print('error')
#執行函數並列印
else:
    b_list=remove_outliers(a_list,n)
    print('The data with the outliers removed: ',a_list)
    print('The outliers: ', b_list)
