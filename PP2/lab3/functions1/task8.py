def spy_game(nums):
    result = []
    for i in nums:
        if i==0 or i==7:
            result.append(i)
    
    flag =  False
    for i in range(len(result)-2):
        if result[i]==result[i+1] and result[i]==0 and result[i+2]==7:
            flag = True
        
    if flag:
        print("True")
    else:
        print("False")

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])