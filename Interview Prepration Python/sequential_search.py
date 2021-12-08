def sequential_list(nums,n):
    foud =False
    for  i in nums:
        if i == n:
            found =True
            break
    return found

def seq(list_,no):
    for i in list_:
        if i == no:
            return True
    return False
