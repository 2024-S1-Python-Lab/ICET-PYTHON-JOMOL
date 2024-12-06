List1=[]
n=int(input("enter number of elements in first list"))
for i in range(0,n):
      ele=int(input())
      List1.append(ele)

#2nd question a part
#List1=[2,4,-6,-8,9,7]
List2=[i for i in List1 if (i>0)];
print(f"Positive List={List2}")

#2nd question b part
list1=[1,2,3,4,5,6]
list2=[i**2 for i in list1]
print(list2)

#2nd question c part
word=input("Enter a word : ")
listVowel=[i for i in word if i in 'aeiouAEIOU']
print(f"Vowels are {listVowel}")


#2nd question d part
w=input("Enter any character :")
ordinalval=[ord(i) for i in w]
print(ordinalval)
