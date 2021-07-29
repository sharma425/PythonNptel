import random
def movie_name():
    movie_list=['TERENAM','KABHIKHUSIKABHIGAM','TITANIC','MATRIX','HARRYPOTTER','SPYDERMAN','IRONMAN',
                'AVENGERS','MONEYHEIST','THEHUNGERGAMES','TRANSFORMERS','TWILIGHT','UNDERWORLD','MASK']
    movie_name = random.choice(movie_list)
    return movie_name

def print_guess(guess_movie):
    for i in range (len(guess_movie)):
        print(guess_movie[i],end=" ")
    
    
def play_game(movie):
    guess_movie=[]
    known_index=0
    for i in range(len(movie)):                     #for appending _ in place of alphabet
        guess_movie.append("_")
    print_guess(guess_movie)
    score = 10
    while (known_index != (len(movie))):            
        ch = input("Guess the aplhabet in movie : ")
        ch=ch.upper()                               # case insensitive
        if (ch in movie and ch not in guess_movie):     # prevent repeat of favorable alphabet 
            for i in range(len(movie)):                 #checking all index
                if (ch == movie[i]):                    
                    guess_movie[i]=ch
                    known_index +=1
        else:
            print("Try Again")
            score-=1
        print_guess(guess_movie)
    return score
        
    
    
    
movie_name = movie_name()
movie= list(movie_name)
print(movie)
score = play_game(movie)
print("\nYour Score is :",score)