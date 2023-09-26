# with recursion
def search_with_recursion(item_arr,search_item,start,end):
    mid= (start+end)//2
    if search_item==item_arr[mid]:
        return mid
    elif search_item>item_arr[mid]:
        return search_with_recursion(item_arr,search_item,mid+1,end)
    elif search_item<item_arr[mid]:
       return search_with_recursion(item_arr,search_item,start,mid-1)
    else:
      return -1

    
def search(item_arr,search_item):
    strt,end=0,len(item_arr)
    while strt<=end:
        mid=(strt+end)//2
        if search_item==item_arr[mid]:
            return mid
        elif search_item>item_arr[mid]:
            strt=mid+1
        else:
            end=mid-1
    return -1




arr=[0,0,1,1,1,1,2,3,4,4,5,6,6,7,8,9,9]

# print(search(arr,2))
print(search_with_recursion(arr,2,0,len(arr)))




