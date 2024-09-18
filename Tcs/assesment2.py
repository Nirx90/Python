def get_max_points():
    arr = [1,2,3,50,8,12]

    el = []
    for i in range(len(arr)):
        sam = 0
        for j in range(i,len(arr),2):
            sam += arr[j]
        el.append(sam)

    return max(el)

print(get_max_points())