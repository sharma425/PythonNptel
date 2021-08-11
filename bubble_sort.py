
def sort(list):
    
    for i in list:
        print(i,end="")
        for i in range (len(list)-1):
            print(i)
            if(list[i]>list[i+1]):
               list[i],list[i+1] =list[i+1], list[i]
    return list


def sort1(list):
    for i in range(len(list)):
        print(i,end="")
        for j in range (len(list)-1-i): 
            print(j)
            if(list[j]>list[j+1]):
               list[j],list[j+1] =list[j+1], list[j]
    return list
    
list = [7,1,5,9,6,2,4,3,8]
sorted_list =sort(list)
print(sorted_list)
sorted_list1 =sort1(list)
print(sorted_list1)
