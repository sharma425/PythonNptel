inp="PYTHON"
out="TDMSUY"
x=""
for i in list(inp):
    x=x+chr((ord(i)-65+5)%26+65)
    print(x)
if(sorted(x)==sorted(out)):
    print("Yes",end='')
else:
    print("No",end='')