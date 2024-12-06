list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
#6th question a part
if len(list1)==len(list2):
    print("The lists have the same length ")
else:
    print("The list have different lengths")

#6th question b part
print(f"sum of list1:{sum(list1} & sum of list2:{sum(list2)}")
if sum(list1)==sum(list2):
    print("THe lists sum to the same value")
else:
    print("THe lists do not sum to the same value")


#6th question c part
common_values=set(list1) & set(list2)
if common_values:
    print(f"common values in both lists : {common_values}")
else:
    print("There are no common values in both lists")
