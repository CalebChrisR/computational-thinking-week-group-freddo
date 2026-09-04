from bonus_story import paragraph1 as par1, Paragraph2 as par2, Paragraph3 as par3, Paragraph4 as par4, Paragraph5 as par5, Paragraph6 as par6

text = "" 
t1 = par1.act1_par1()
t2 = par2.act1_par2()
t3= par3.act1_par3()
t4= par4.act1_par4()
t5 = par5.act1_par5()
t6 = par6.act1_par6()

t7= par1.act2_par1()
t8= par2.act2_par2()
t9= par3.act2_par3()
t10= par4.act2_par4()
t11= par5.act2_par5()
t12= par6.act2_par6()    

t13 = par1.act3_par1()
t14=par2.act3_par2()
t15=par3.act3_par3()
t16=par4.act3_par4()
t17=par5.act3_par5()
t18=par6.act3_par6()    

text = t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12+t13+t14+t15+t16+t17+t18

text = par1.replace_jesus(text)
text = par2.replace_holyspirit(text)
text = par3.replace_ladygaga(text)
text = par4.replace_mary(text)
text = par5.replace_judas(text)
text = par6.replace_steve(text)

print(text)


