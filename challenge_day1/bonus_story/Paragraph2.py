# Act 1
def act1_par2 ():
    return("ch1 takes a breath. The Holy Spirit flows within ch1, and also ch4. " \
"ch4 is kind of relieved to be done with the birth. ch5 can predict the baby " \
"screams. ch3 knows she's gonna have to sing louder once ch1 starts crying. " \
"ch6 stops dancing to get the witch hat on.")

# Act 2
def act2_par2 ():
    return(" 'What?' Asks ch1, confused why ch6 would call it a last supper. " \
" 'This is just normal supper.' ch5, feeling that his secret is up, buries his face " \
" in the wine, determined not to think about it. ch4 and ch3 are a little too in " \
" their cups, and gossip about who is gonna win the local dog race. The Holy Spirit" \
" turns the wine back into water, because they are sober.")

# Act 3
def act3_par2 ():
    return("The Holy Spirit realises that they have the power to change this." \
" “I can fix your hat,” they tell ch6. ch6 hands over the Witch's hat, drawing the" \
" attention of ch4, ch5, and ch3. This is the first time in a week that their" \
" attention is broken from ch1' resting place.")

if __name__ == "__main__":
    act1_par2()
    act2_par2()
    act3_par2()


def replace_holyspirit(chnum, text):
    return(text.replace(chnum, "Holy Spirit"))
    
