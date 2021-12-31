def case_cal(a):#Define Function
    j=0#define veriable
    k=0#define veriable
    o=0#define veriable
    for i in range(0,len(a)): #loop for check ch. for upper and lower
        if a[i].isupper(): #con_1 : check for upper
            j=j+1
        elif a[i].islower():#con_2 : check for lower
            k=k+1
        elif a[i] != " " :#con_3 : check for special ch
            o=o+1        
    print("No of upper-",j)# print result
    print("No of lowwer-",k)# print result
    print("Nither upper nor lower(special ch)-",o)# print result
case_cal("The quick Brow Fox")#Use/recall that function
