# bubble 

def sort(arr_to_sort):
    for i in range(0,len(arr_to_sort)):
        for j in range(0,len(arr_to_sort)-i-1):
            if arr_to_sort[j]>arr_to_sort[j+1]:
                arr_to_sort[j],arr_to_sort[j+1]=arr_to_sort[j+1],arr_to_sort[j]
    return arr_to_sort

arr=[2,4,8,2,5,9,8,4,2,7,9,3,8,3,7,0,7,6,4,6,8,1,3,8,5,4,4,6,7,9,8]
print(sort(arr))

