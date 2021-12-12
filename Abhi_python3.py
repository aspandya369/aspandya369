numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd_no=0
even_no=0
for i in numbers:
    if not i%2:
        even_no+=1
    else:
        odd_no+=1
print("odd no is :",odd_no)
print("even no is :",even_no)
