import string
dict={}
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[(i+5)%26]
print(dict)

f=input("The first line of the input contains a string indicating the plain text")
cyper_input=input("The second line of the input a string indicating a possible cipher text")
while True:
    c=f #read the file character by character
    if not c:           #check end of file
        print("End of File")
        break
    if c in dict:
        data=dict[c]
    else:
        data = c
    
    print(data)
        