# Paragraph 1's for each act, 
# Character 1 became ch1

def act1_par1():
    text = "ch1 is born in the manger. His mother, ch4, just knows that the ch2 is with him." \
        "ch3 is dancing to a song which calls on ch5. ch6 is vibing in the corner, doing an interpretive dance. It seems wicked..."
    return text
def act2_par1():
    text ="Time has passed. ch1 is hosting supper. ch5, however, knows it's the last supper for them all. " \
        "The ch2 allows water to turn to wine, and they are all fed. " \
        "ch4 and ch3 sit in the corner sipping on some spirit (not holy), " \
        "ch4 adds tomato juice to hers. 'This is kind of good,'ch3 remarks after trying it." \
        "'It's bloody good even!' says ch6 as he bursts into existence, 'can I join this last supper?"

    return text

def act3_par1():
    text = "ch6 appears with a burst of light. His witch hat looks a little sad, he can't travel through time anymore :(." \
        "ch4, ch5, and the ch2 wait outside ch1' resting place." \
        "ch3, for once, is not singing, understanding the serious situation."
    return text

def replace_jesus(text: str):
    return str(text).replace("ch1", "Jesus")


def main():
    act1_par1()
    act2_par1()
    act3_par1()
    
if __name__ == "__main__":
    main()