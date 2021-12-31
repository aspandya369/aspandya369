def rev_str(name):#define function
    for ch in range(len(name)-1,-1,-1):#loop for reverce
        print(name[ch],end="")
    print("\n")
rev_str("1234abcd")#recall/Use function
