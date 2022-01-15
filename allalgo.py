#bubble sort
def କ୍ରମ(list): 

# Swap the elements to arrange in order
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
   return list
#bubble sort


#merge sort
def ଭାଗମିଶାଅକ୍ରମ(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
# Find the middle point and devide it
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = ଭାଗମିଶାଅକ୍ରମ(left_list)
   right_list = ଭାଗମିଶାଅକ୍ରମ(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res

#merge sort
#insertion sort
def ବଡକ୍ରମ(InputList):
   for i in range(1, len(InputList)):
      j = i-1
      nxt_element = InputList[i]
# Compare the current element with next one
   while (InputList[j] > nxt_element) and (j >= 0):
      InputList[j+1] = InputList[j]
      j=j-1
   InputList[j+1] = nxt_element
   return InputList
#insertion_sort

#selection sort
def ଚୟନକ୍ରମ(inp):
   for idx in range(len(inp)):
      min_idx = idx
      for j in range( idx +1, len(inp)):
         if inp[min_idx] > inp[j]:
            min_idx = j
# Swap the minimum value with the compared value
   inp[idx], inp[min_idx] = inp[min_idx], inp[idx]
   return inp
#selection  sort

