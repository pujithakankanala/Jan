# 9. Remove duplicates form the list

list1= [12,24,35,24,88,120,155,88,120,155]
unique=[]
seen = set()

for i in list1:
    if i not in seen:
        unique.append(i)
        seen.add(i)
print("List after removing the duplicate elements", unique )

# 10. Removing 24 form the list

filtered=[i for i in list1 if i != 24]
        
        
print("List after removing 24", filtered )

# 11. Removing the 0th, 4th, 5th values form the list

filtered_list = [x for i, x in enumerate(list1) if i not in (0, 4, 5)]
print("list after removing the 0th, 4th and 5th values:", filtered_list) 

#12. remove the values which are divisible by 5 and 7

list2 =[12,24,35,70,88,120,155]
filter_list = [x for x in list2 if not (x % 5 == 0 and x % 7 == 0)]
print("List after removing the divisible by 5 and 7:", filter_list)