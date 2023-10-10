

# linear search
def search(item_arr,search_item):
  for i in range(0,len(item_arr)):
    if item_arr[i]==search_item:
      return i
  return -1


print(search([3,5,2,7,9,5,5,3,8,1,8,4,3,7,9,2],1))
