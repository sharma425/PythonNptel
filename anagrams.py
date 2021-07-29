#x={'q':4,'w':3,'e':1,'t':2}
#print(sorted(x))
#l=["ccccc","bb","a","ddd"]
#print(sorted(l))

str1 = input("enter the first string : ")
str2 = input("enter the second string : ")  
if sorted(str1)==sorted(str2):
    print("These are anagrams ")
else:
    print("these are not anagrams")
    
print(sorted(str1))
print(sorted(str2))

