def act1_par6():
    return('Steve cannot stand the screaming, “I am out of here,” so he twists '
    'the witch hat, and disappears. ch1 is so startled that he stops screaming. '
    'ch4 gets a little scared, and cradles ch1 closer. ch3, inspired by ch1, starts '
    'singing “born this way.” The ch2 is not confused, and just chills. ch5 is a bit ' 
    'upset they are no longer singing ch5.')

def act2_par6():
    return('Once Steve has finished, he joins ch4 and the ch2 at the window, watching '
    'as ch1 is pulled away to die. ch5 looks a little pained, but not that repentant. '  
    'They ask Steve, “how did you know?” ch3 listens in. Steve mumbles, “what a wicked ' 
    'problem,” and twists the hat to disappear.')

def act3_par6():
    return('Steve, upon seeing that they are all happy, pops his guitar away and bows. '
    '“I will see you next time.” With a twist of his hat, he disappears once more, '
    'travelling through time again. The ch2 and ch3 continue their concert. ch4, ch5, '
    'and ch1 remain together, happy that they are together again.')
    
if __name__ == "__main__":
    act1_par6()
    act2_par6() 
    act3_par6()


def replace_steve(chnum, text):
    print(text.replace(chnum, "Steve"))


