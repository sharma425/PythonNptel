def swap(num1,num2):
    return num2,num1
def sort(list):
    
    for i in list:
        for i in range (len(list)-1):
            if(list[i]>list[i+1]):
               list[i],list[i+1] =swap(list[i], list[i+1])
    return list

list = [7,1,5,9,6,2,4,3,8]
sorted_list =sort(list)
print(sorted_list)