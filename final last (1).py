fname=("")
x=()
name = input('Enter your name :')
choice2=()
try:
    game=open(f'{name}.txt','r')
    game1=game.read()
    game.close()
except :
    game = open(f'{name}.txt','w')
    game.close()
    game = open(f'{name}.txt','r')
    game1 = game.read()
    game.close()

if name not in game1:
    print("The game is about to start!\n Let's play Hangman")
    print("1. Fruits")
    print("2. Vegetables")
    print("3. Countries")
    print("4. Deserts")
    print("5. random")
    try:
        choice2=float(input("Please select a category:"))
        if choice2==(-1):
            endgame()
        game = open(f'{name}.txt','a')
        game.write(name+'\n')
        game.close()
        fname=("")
        x=(" ")
    except (ValueError):
        choice2=float(input("Please select a category:"))
        
else:
    f=open(f'{name}_wwords.txt','r')
    ww=f.read()
    f.close()
    ff=open(f'{name}_lwords.txt','r')
    www=ff.read()
    ff.close()
    print(f'Words guessed right {ww}')
    print(f'Words guessed wrong {www}')
    print('Choice 1 or 2')
    print('1. Start new game')
    choice1=input('2. Load old game')
    if choice1==("-1"):
        endgame()
    if choice1 == ("1"):
        print("1. Fruits")
        print("2. Vegetables")
        print("3. Countries")
        print("4. Deserts")
        print("5. Random")
        choice2=float(input("Please select a category:"))    
    if choice1 == ("2"):
        r=open(f'{name}_cword.txt','r')
        x =r.read()
        r.close
        t=open(f'{name}_rletters.txt','r')
        y=t.read()
        t.close()
        i=open(f'{name}_wletters.txt','r')
        z=i.read()
        i.close()
        fname=(f'{x}')
        print(x)
        y=(input("enter a letter"))
        if y==(-1):
            endgame(x,wword,lword,c,z) 
        c=("")
        z=("")

        newword=set(x)
        count=0
        while count!=6:
            if (y in x.lower()) or (y in x.upper()):
                try:
                    y= y.lower()
                    newword.remove(y)
                    c += y
                    print (f'letters guessed right: {c}')
                    if (newword)==set():
                        print("winner")
                        worl=(f'word guessed right is {x}')
                        wword=x
                        lword=("")
                        print(worl)
                        endgame(x,wword,lword,c,z)
                        break
                    y=input(f"Good guess {y} is in the word")
                    if y==("-1"):
                        endgame(x,wword,lword,c,z)
                        break
                except (KeyError):
                    y=input("you already gussed that letter")
                    if y ==("-1"):
                        endgame(lword,wword,c,z,x,sore)
            if (y not in x.lower()) and (y not in x.upper()):
                if y==("-1"):
                    endgame()
                hangman_body(count)
                count+=1
                z+=y
                print(f'letters guessed wrong: {z}')
                y=input("wrong guess please enter another letter")
                if count==5:
                    hangman_body(count)
                    worl=("endgame you lost")
                    lword=(x)
                    print (lword)
                    print(worl)
                    endgame(x,wword,lword,c,z)
                    break
wword=()
lword=()
c=()
z=()
def playagain(x,wword,lword,c,z):
    choice22=float(input("choose a categorie"))
    fname=""
    x=()
    import random
    if fname!=x:
        if choice22==(1):
            fname=("fruits")
        if choice22==(2):
            fname=("vegs")
        if choice22==(3):
            fname=("countries")
        if choice22==(4):
            fname=("desert")
        if choice22==(5):
            fname=("words")
        with open(f'{fname}.txt', "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            x=(random.choice(words))
            newword= set(x.lower())
    else:
        pass
        
    print(x)
    y=(input("enter a letter"))
    if y==(-1):
        endgame(x,wword,lword,c,z) 
    c=("")
    z=("")


    count=0
    while count!=6:
        if (y in x.lower()) or (y in x.upper()):
            try:
                y= y.lower()
                newword.remove(y)
                c += y
                print (f'letters guessed right: {c}')
                if (newword)==set():
                    print("winner")
                    worl=(f'word guessed right is {x}')
                    wword=x
                    lword=("")
                    print(worl)
                    endgame(x,wword,lword,c,z)
                    break
                y=input(f"Good guess {y} is in the word")
                if y==("-1"):
                    endgame(x,wword,lword,c,z)
                    break
            except (KeyError):
                y=input("you already gussed that letter")
                if y ==("-1"):
                    endgame(lword,wword,c,z,x,sore)
        if (y not in x.lower()) and (y not in x.upper()):
            if y==("-1"):
                endgame()
            hangman_body(count)
            count+=1
            z+=y
            print(f'letters guessed wrong: {z}')
            y=input("wrong guess please enter another letter")
            if count==5:
                hangman_body(count)
                worl=("endgame you lost")
                lword=(x)
                print (lword)
                print(worl)
                endgame(x,wword,lword,c,z)
                break
    return(x,wword,lword,c,z)
      
def endgame(x,wword,lword,c,z):
    try:
        sore=(input("1.exit game without saving / 2.save game and exit / 3.start new game and save / 4.start new game"))
        if sore==("1"):
            exit
        elif sore==("2"):
            o=open(f'{name}_wwords.txt',"a")
            o.write(str(wword))
            o.close()
        
            q=open(f'{name}_lwords.txt',"a")
            q.write(str(lword))
            q.close()
        
            m=open(f'{name}_rletters.txt',"w")
            m.write(str(c))
            m.close()
    
            j=open(f'{name}_wletters.txt',"w")
            j.write(str(z))
            j.close()
        
            b=open(f'{name}_cword.txt',"w")
            b.write(str(x))
            b.close()
            exit
        elif sore==("3"):
            o=open(f'{name}_wwords.txt',"a")
            o.write(str(wword))
            o.close()
        
            q=open(f'{name}_lwords.txt',"a")
            q.write(str(lword))
            q.close()
        
            m=open(f'{name}_rletters.txt',"w")
            m.write(str(c))
            m.close()
       
        
            j=open(f'{name}_wletters.txt',"w")
            j.write(str(z))
            j.close()
        
            b=open(f'{name}_cword.txt',"w")
            b.write(str(x))
            b.close()
            choice1=1
            playagain(x,z,c,wword,lword)
            
        elif sore==("4"):
            playagain()
        else:
            sore=input("please entera valid number")
            

    except(ValueError):
        try:
            y=float(input("please enter a number"))
        except(ValueError):
            y=float(input("please enter a number"))
            exit


def hangman_body(count):
 
    if count > 0:
        print(' _')
    else:
        print()
        
    if count > 1:
        print(' |     |')
    else:
        print(' |')
        
    if count > 2:
        print(' |     O')
    else:
        print(' |')
        
    if count > 3:
        print(' |    /|\\')
    else:
        print(' |')
        
    if count > 4:
        print(' |    / \\')
    else:
        print(' |')
        
    if count > 0:
        print(' |')
    else:
        print()


import random
if fname!=x:
    if choice2==(1):
        fname=("fruits")
    if choice2==(2):
        fname=("vegs")
    if choice2==(3):
        fname=("countries")
    if choice2==(4):
        fname=("desert")
    if choice2==(5):
        fname=("words")
    with open(f'{fname}.txt', "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    x=(random.choice(words))
    newword= set(x.lower())
else:
    pass
        
playagain(x,wword,lword,c,z)

