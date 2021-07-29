import random
import string
def card1():
    symbols=[]
    symbols=list(string.ascii_uppercase)
    card = []
    for i in range(6):
        alpha = random.choice(symbols)
        card.append(alpha)
        symbols.remove(alpha)                   #deleting alphabet from symbols to avoid repetation
    return card

def card2(card1):
    card1_symbol = random.choice(card1)         #choosing random alphabet from list1
    card1_symbol_index = random.randint(1,6)    #choosing random index for common alphabet
    symbols=[]
    symbols=list(string.ascii_uppercase)
    for i in range(6):  
        symbols.remove(card1[i])                #deleting common alphabet from symbols
    card = []
    for i in range(5):
        alpha = random.choice(symbols)
        card.append(alpha)
        symbols.remove(alpha)                   #deleting alphabet from symbols to avoid repetation
    card.insert(card1_symbol_index,card1_symbol)
    return card1_symbol, card

        
card1 = card1()
common_symbol, card2 = card2(card1)
print(card1)
print(card2)
ch = input("spot the similar symbol")
if(ch == common_symbol):
    print("Great success")
else:
    print("try again")

