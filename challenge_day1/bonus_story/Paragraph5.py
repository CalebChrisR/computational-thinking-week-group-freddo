#ACT 1
def act1_par5():
    return ("'I can’t help it ch4, I was born this way,' ch1 responds and continues crying. " \
    "ch3 gives a proud look, while ch6, ch5, and the ch2 start clapping.")


#ACT 2
def act2_par5():
    return ("ch1 and ch5 can still faintly hear ch3’s song of ch5, but they try to ignore her. " \
    "ch4 and the ch2 watch and ch5 kisses ch1’ cheek and murmurs something, " \
    "but are then horrified when ch1 is arrested. ch6 perks up at the commotion and stops eating.")


#ACT 3
def act3_par5(): 
    return ("There’s a happy shout as ch4 and ch5 give ch1 a hug. " \
    "ch3 bursts into song, accompanying ch6's guitar. " \
    "'I can’t remember, but it’s alright a-alright. Just Dance!' " \
    "The ch2 summons a dance floor and lights.")


def replace_judas(text: str):
    return str(text).replace("ch5", "Judas")


if __name__ == "__main__":
    act1_par5()
    act2_par5()
    act3_par5()
    pass

