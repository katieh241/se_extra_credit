def array_sum(array, target_sum):
    array.sort()
    x = 0
    y = len(array)-1
    B=[]
     
    while x<y:
        if (array[x] + array[y] == target_sum):
            B.append(array[x])
            B.append(array[y])
            return B
        elif (array[x] + array[y] < target_sum):
            x += 1
        else:
            y -= 1
    return 0