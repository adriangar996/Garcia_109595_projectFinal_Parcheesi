import random

from graphics import*

 

win= GraphWin("Parcheesi", 500, 500)

 

rect1= Rectangle(Point(15,15), Point(485,485))

rect1.setFill(color_rgb(30,50,30))

rect1.setWidth(3)

rect1.draw(win)

 

#BLUE RECTANGLES

Brect1= Rectangle(Point(300,200), Point(475,25)) #Blue Rectangle

Brect1.setFill('blue')

Brect1.draw(win)

 

Brect2= Rectangle(Point(200,25), Point(300,200)) #Blue Rectangle

Brect2.setWidth(1)

Brect2.draw(win)

 

Brect3= Rectangle(Point(200,25), Point(230,200)) #Blue Rectangle

Brect3.setWidth(1)

Brect3.draw(win)

 

Brect4= Rectangle(Point(230,25), Point(270,200)) #Blue Rectangle

Brect4.setFill('blue')

Brect4.setWidth(1)

Brect4.draw(win)

 

Brect5= Rectangle(Point(200,171), Point(300,200)) #Blue Rectangle

Brect5.setWidth(1)

Brect5.draw(win)

 

Brect6= Rectangle(Point(200,142), Point(300,171)) #Blue Rectangle

Brect6.setWidth(1)

Brect6.draw(win)

 

Brect7= Rectangle(Point(200,113), Point(300,142)) #Blue Rectangle

Brect7.setWidth(1)

Brect7.draw(win)

 

Brect8= Rectangle(Point(200,84), Point(300,113)) #Blue Rectangle

#Brect8.setFill('blue')

Brect8.setWidth(1)

Brect8.draw(win)

 

Brect9= Rectangle(Point(300,55), Point(300,84)) #Blue Rectangle

Brect9.setFill('blue')

Brect9.setWidth(1)

Brect9.draw(win)

 

Brect10= Rectangle(Point(200,25), Point(300,55)) #Blue Rectangle

#Brect10.setFill('blue')

Brect10.setWidth(1)

Brect10.draw(win)

 

Brect11= Rectangle(Point(270,55), Point(300,84)) #Blue Rectangle

Brect11.setFill('blue')

#Brect11.setWidth(1)

Brect11.draw(win)

 

Brect12= Rectangle(Point(230,25), Point(270,55)) #Blue Rectangle

Brect12.setFill(color_rgb(30,50,30))

#Brect12.setWidth(1)

Brect12.draw(win)

 

Brect14= Rectangle(Point(325,175),Point(450,50))

#Brect14.setFill(color_rgb(115,125,255))
Brect14.setFill('white')
Brect14.setWidth(1)

Brect14.draw(win)

 

#Red rectangle

Rrect1= Rectangle(Point(25,475), Point(200,300)) # Red Rectangle

Rrect1.setFill('red')

Rrect1.setWidth(1)

Rrect1.draw(win)

 

Rrect2= Rectangle(Point(200,300), Point(300,475)) # Red Rectangle

Rrect2.setWidth(1)

Rrect2.draw(win)

 

Rrect3= Rectangle(Point(200,300), Point(230,475)) # Red Rectangle

Rrect3.setWidth(1)

Rrect3.draw(win)

 

Rrect4= Rectangle(Point(230,300), Point(270,475)) # Red Rectangle

Rrect4.setFill('red')

Rrect4.setWidth(1)

Rrect4.draw(win)

 

Rrect5= Rectangle(Point(200,446), Point(300,475)) # Red Rectangle

#Rrect5.setFill('red')

Rrect5.setWidth(1)

Rrect5.draw(win)

 

Rrect6= Rectangle(Point(200,417), Point(300,446)) # Red Rectangle

#Rrect6.setFill('red')

Rrect6.setWidth(1)

Rrect6.draw(win)

 

Rrect7= Rectangle(Point(200,388), Point(300,417)) # Red Rectangle

#Rrect7.setFill('red')

Rrect7.setWidth(1)

Rrect7.draw(win)

 

Rrect8= Rectangle(Point(200,359), Point(300,388)) # Red Rectangle

#Rrect8.setFill('red')

Rrect8.setWidth(1)

Rrect8.draw(win)

 

Rrect9= Rectangle(Point(200,330), Point(300,359)) # Red Rectangle

#Rrect9.setFill('red')

Rrect9.setWidth(1)

Rrect9.draw(win)

 

Rrect10= Rectangle(Point(200,300), Point(300,330)) # Red Rectangle

#Rrect10.setFill('red')

Rrect10.setWidth(1)

Rrect10.draw(win)

 

Rrect11= Rectangle(Point(200,417), Point(230,446)) # Red Rectangle

Rrect11.setFill('red')

Rrect11.setWidth(1)

Rrect11.draw(win)

 

Rrect12= Rectangle(Point(230,446), Point(270,475)) # Red Rectangle

Rrect12.setFill(color_rgb(30,50,30))

#Rrect12.setWidth(1)

Rrect12.draw(win)

 

Rrect14= Rectangle(Point(50,450),Point(175,325))

Rrect14.setFill('white')

Rrect14.setWidth(1)

Rrect14.draw(win)

 

#GREEN RECTANGLES

Grect1= Rectangle(Point(25,25), Point(200,200)) #Green Rectangle

Grect1.setFill('green')

Grect1.draw(win)

 

Grect2= Rectangle(Point(25,25), Point(200,200)) #Green Rectangle

Grect2.setWidth(1)

Grect2.draw(win)

 

Grect3= Rectangle(Point(200,200), Point(25,230)) #Green Rectangle

Grect3.setWidth(1)

Grect3.draw(win)

 

Grect4= Rectangle(Point(200,230), Point(25,270)) #Green Rectangle

Grect4.setFill('green')

Grect4.setWidth(1)

Grect4.draw(win)

 

Grect5= Rectangle(Point(25,200), Point(54,300)) #Green Rectangle

Grect5.setWidth(1)

Grect5.draw(win)

 

Grect6= Rectangle(Point(54,200), Point(83,300)) #Green Rectangle

Grect6.setWidth(1)

Grect6.draw(win)

 

Grect7= Rectangle(Point(83,200), Point(112,300)) #Green Rectangle

Grect7.setWidth(1)

Grect7.draw(win)

 

Grect8= Rectangle(Point(112,200), Point(141,300)) #Green Rectangle

Grect8.setWidth(1)

Grect8.draw(win)

 

Grect9= Rectangle(Point(141,200), Point(170,300)) #Green Rectangle

Grect9.setWidth(1)

Grect9.draw(win)

 

Grect10= Rectangle(Point(170,200), Point(200,300)) #Green Rectangle

Grect10.setWidth(1)

Grect10.draw(win)

 

Grect11= Rectangle(Point(54,200), Point(83,230)) #Green Rectangle

Grect11.setFill('green')

Grect11.draw(win)

 

Grect12= Rectangle(Point(25,230), Point(54,270)) #Green Rectangle

Grect12.setFill(color_rgb(30,50,30))

Grect12.draw(win)

 

Grect14= Rectangle(Point(50,175),Point(175,50))

#Grect14.setFill(color_rgb(45,255,15))

Grect14.setFill('white')

Grect14.setWidth(1)

Grect14.draw(win)

 

#YELLOW RECTANGLES

Yrect1= Rectangle(Point(300,300), Point(475,475)) #Yellow Rectangle

Yrect1.setFill('yellow')

Yrect1.draw(win)

 

Yrect2= Rectangle(Point(200,200), Point(475,475)) #Yellow Rectangle

Yrect2.setWidth(1)

Yrect2.draw(win)

 

 

Yrect3= Rectangle(Point(300,200), Point(475,230)) #Yellow Rectangle

#Yrect3.setFill('white')

Yrect3.setWidth(1)

Yrect3.draw(win)

 

Yrect4= Rectangle(Point(300,230), Point(475,270)) #Yellow Rectangle

Yrect4.setFill('yellow')

Yrect4.setWidth(1)

Yrect4.draw(win)

 

Yrect5= Rectangle(Point(300,200), Point(329,300)) #Yellow Rectangle

Yrect5.setWidth(1)

Yrect5.draw(win)

 

Yrect6= Rectangle(Point(329,200), Point(358,300)) #Yellow Rectangle

Yrect6.setWidth(1)

Yrect6.draw(win)

 

Yrect7= Rectangle(Point(358,200), Point(387,300)) #Yellow Rectangle

Yrect7.setWidth(1)

Yrect7.draw(win)

 

Yrect8= Rectangle(Point(387,200), Point(416,300)) #Yellow Rectangle

Yrect8.setWidth(1)

Yrect8.draw(win)

 

Yrect9= Rectangle(Point(416,200), Point(445,300)) #Yellow Rectangle

Yrect9.setWidth(1)

Yrect9.draw(win)

 

Yrect10= Rectangle(Point(445,200), Point(475,300)) #Yellow Rectangle

#Yrect10.setFill('white')

Yrect10.setWidth(1)

Yrect10.draw(win)

 

Yrect11= Rectangle(Point(416,270), Point(445,300)) #Yellow Rectangle

Yrect11.setFill('yellow')

Yrect11.setWidth(1)

Yrect11.draw(win)

 

Yrect12= Rectangle(Point(445,230), Point(475,270)) #Yellow Rectangle

Yrect12.setFill(color_rgb(30,50,30))

Yrect12.setWidth(1)

Yrect12.draw(win)

 

Yrect14 = Rectangle(Point(325,450),Point(450,325))

#Yrect14.setFill(color_rgb(255,255,120))
Yrect14.setFill('white')

Yrect14.setWidth(1)

Yrect14.draw(win)

 

 

rectA=Rectangle(Point(235,235), Point(265,265))

rectA.setFill('pink')

rectA.draw(win)

 

lineR2 = Rectangle(Point(200,200),Point(300,300))

lineR2.setFill('red')

lineR2.draw(win)

 

lineR1=Polygon(Point(235,265),Point(200,300),Point(200,200),Point(240,210))

lineR1.setWidth(1)

lineR1.setFill('green')

lineR1.draw(win)

 

PolyR2=Polygon(Point(235,235),Point(200,200),Point(300,200),Point(300,250))

PolyR2.setWidth(1)

PolyR2.setFill('blue')

PolyR2.draw(win)

 

PolyR3=Polygon(Point(300,300),Point(265,265),Point(265,235),Point(300,200))

PolyR3.setWidth(1)

PolyR3.setFill('yellow')

PolyR3.draw(win)

 

rectB=Rectangle(Point(235,235),Point(265,265))

rectB.setFill('white')

rectB.draw(win)

 

#Creating the players

#Red players
p_red1=Circle(Point(147,420),10)

p_red1.setFill('pink')

p_red1.draw(win)


p_red2=Circle(Point(84,420),10)

p_red2.setFill('pink')

p_red2.draw(win)


p_red3=Circle(Point(147,339),10)

p_red3.setFill('pink')

p_red3.draw(win)


p_red4=Circle(Point(84,339),10)

p_red4.setFill('pink')

p_red4.draw(win)

#Yellow players
p_yellow1=Circle(Point(420,420),10)

p_yellow1.setFill(color_rgb(255,255,120))

#_yellow1.setOutline('yellow')

p_yellow1.draw(win)


p_yellow2=Circle(Point(350,420),10)

p_yellow2.setFill(color_rgb(255,255,120))

p_yellow2.draw(win)


p_yellow3=Circle(Point(420,339),10)

p_yellow3.setFill(color_rgb(255,255,120))

p_yellow3.draw(win)


p_yellow4=Circle(Point(350,339),10)

p_yellow4.setFill(color_rgb(255,255,120))

p_yellow4.draw(win)

#Blue players
p_blue1=Circle(Point(420,76),10)

p_blue1.setFill(color_rgb(115,125,255))

p_blue1.draw(win)


p_blue2=Circle(Point(420,140),10)

p_blue2.setFill(color_rgb(115,125,255))

p_blue2.draw(win)


p_blue3=Circle(Point(350,76),10)

p_blue3.setFill(color_rgb(115,125,255))

p_blue3.draw(win)


p_blue4=Circle(Point(350,140),10)

p_blue4.setFill(color_rgb(115,125,255))

p_blue4.draw(win)

#Green players
p_green1=Circle(Point(147,76),10)

p_green1.setFill(color_rgb(45,255,15))

p_green1.draw(win)


p_green2=Circle(Point(84,140),10)

p_green2.setFill(color_rgb(45,255,15))

p_green2.draw(win)


p_green3=Circle(Point(147,140),10)

p_green3.setFill(color_rgb(45,255,15))

p_green3.draw(win)


p_green4=Circle(Point(84,76),10)

p_green4.setFill(color_rgb(45,255,15))

p_green4.draw(win)


dice=[1,2,3,4,5,6]

Dice= random.choice(dice)

class shuffle():

  

    def get1():

        circ1=Circle(Point(250,250),3)

        circ1.setFill('black')

        circ1.draw(win)

        text=Text(Point(250,40),'1')

        text.setSize(28)

        text.setFill('red')

        text.draw(win)

 

    def get2():

      

        circ1=Circle(Point(242,250),3)

        circ1.setFill('black')

        circ2=Circle(Point(258,250),3)

        circ2.setFill('black')

        circ1.draw(win)

        circ2.draw(win)

        text=Text(Point(250,40),'2')

        text.setSize(28)

        text.setFill('red')

        text.draw(win)

 

 

    def get3():

        circ1=Circle(Point(240,240),2.5)

        circ1.setFill('black')

        circ2=Circle(Point(250,250),2.5)

        circ2.setFill('black')

        circ3=Circle(Point(260,260),2.5)

        circ3.setFill('black')

        circ1.draw(win)

        circ2.draw(win)

        circ3.draw(win)

        text=Text(Point(250,40),'3')

        text.setSize(28)

        text.setFill('red')

        text.draw(win)

 

    def get4():

        circ1=Circle(Point(242,242),2.5)

        circ1.setFill('black')

        circ2=Circle(Point(258,242),2.5)

        circ2.setFill('black')

        circ3=Circle(Point(242,258),2.5)

        circ3.setFill('black')

        circ4=Circle(Point(258,258),2.5)

        circ4.setFill('black')

        circ1.draw(win)

        circ2.draw(win)

        circ3.draw(win)

        circ4.draw(win)

        text=Text(Point(250,40),'4')

        text.setSize(28)

        text.setFill('red')

        text.draw(win)

 

      

    def get5():

        circ1=Circle(Point(241,241),2.5)

        circ1.setFill('black')

        circ2=Circle(Point(259,241),2.5)

        circ2.setFill('black')

        circ3=Circle(Point(241,259),2.5)

        circ3.setFill('black')

        circ4=Circle(Point(259,259),2.5)

        circ4.setFill('black')

        circ5=Circle(Point(250,250),2.5)

        circ5.setFill('black')

        circ2.draw(win)

        circ3.draw(win)

        circ4.draw(win)

        circ5.draw(win)

        circ1.draw(win)

        text=Text(Point(250,40),'5')

        text.setSize(28)

        text.setFill('red')

        text.draw(win)

 

    def get6():

        circ1=Circle(Point(240,242),2.5)

        circ1.setFill('black')

        circ2=Circle(Point(250,242),2.5)

        circ2.setFill('black')

        circ3=Circle(Point(260,242),2.5)

        circ3.setFill('black')

        circ4=Circle(Point(240,257),2.5)

        circ4.setFill('black')

        circ5=Circle(Point(250,257),2.5)

        circ5.setFill('black')

        circ6=Circle(Point(260,257),2.5)

        circ6.setFill('black')

        circ1.draw(win)

        circ2.draw(win)

        circ3.draw(win)

        circ4.draw(win)

        circ5.draw(win)

        circ6.draw(win)

        text=Text(Point(250,40),'6')

        text.setSize(28)

        text.setFill('red')

        text.draw(win)

 

 

    def reset():

 

        rectB=Rectangle(Point(235,235),Point(265,265))

        rectB.setFill('white')

        rectB.draw(win)

 

        rect=Rectangle(Point(230,25),Point(270,55))

        rect.setFill(color_rgb(30,50,30))

        rect.draw(win)

      

def main():

    Dice=random.choice(dice)

    if dice==6:
        
        p_red1.undraw()
            
        p_red=Circle(Point(213,432),10)

        p_red.setFill('pink')

        p_red.draw(win)

    
 

    while True:

        win.getMouse()

        Dice=random.choice(dice)

        if Dice==1:

            shuffle.get1()

        if Dice==2:

            shuffle.get2()

        if Dice==3:

            shuffle.get3()

        if Dice==4:

            shuffle.get4()

        if Dice==5:

            shuffle.get5()

        if Dice==6:

            shuffle.get6()

 

        win.getMouse()

        shuffle.reset()

        Dice=random.choice(dice)

if __name__=='__main__':

    main()
