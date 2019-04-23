#include <iostream>
#tesitghgfhsdfasdffdshgsdfh
import random
import arcade
"""
string printCube(string cube)
string rightclock(string cube)
string leftclock(string cube)
string topclock(string cube)
string bottomclock(string cube)
/*string frontclock(string cube)
string awayclock(string cube)*/"""

showSteps = True

def printCube(cube):
    #int i,j
    #//red test

    for i in range(3):
        print( end ="      "),
        for j in range(3):
            print( cube[i*3+j], end =" "),
        print( end ="      \n"),

    #//white,green,yellow
    for i in range(3,6):
        for j in range(3):#(j=0j<3j++)
            print( cube[i*3+j], end =" "),
        for j in range(3):#(j=0j<3j++)
            print( cube[i*3+j+9], end =" "),
        for j in range(3):#(j=0j<3j++)
            print( cube[i*3+j+18], end =" "),
        print(end ="\n"),


    #//orange
    for i in range(12,15):#(i=12i<15i++)
        print(end = "      ")
        for j in range(3):#(j=0j<3j++)
            print( cube[i*3+j], end =" ")
        print(end = "      \n")
    #//blue
    for i in range(15,18):#(i=15i<18i++)
        print( end ="      ")
        for j in range(3):#(j=0j<3j++)
            print( cube[i*3+j], end =" ")
        print(end = "      \n")
    print(end ="\n")


def rc(cube):
    #//rotate right right side clockwise with green facing you and red on top
    tempCube = cube.copy()
    start = 27
    for i in range(3):# (i=0 i<3 i++)
        cube[i*3+2]=tempCube[i*3+18+2]
        cube[i*3+18+2]=tempCube[i*3+36+2]
        cube[i*3+36+2]=tempCube[i*3+45+2]
        cube[i*3+45+2]=tempCube[i*3+2]

        cube[i+start] = tempCube[start+6-i*3]
        cube[i+3+start] = tempCube[start+7-i*3]
        cube[i+6+start] = tempCube[start+8-i*3]

    if(showSteps == True):
        print("rc")

    return(cube)
def rcc(cube):
    cube = rc(cube)
    cube = rc(cube)
    cube = rc(cube)

    if(showSteps == True):
        print("rcc")

    return(cube)
def lc(cube):
    #//rotate right right side clockwise with green facing you and red on top
    tempCube = cube.copy()
    start = 9
    for i in range(3): #(i=0i<3i++)
        cube[i*3]=tempCube[i*3+45]
        cube[i*3+18]=tempCube[i*3]
        cube[i*3+36]=tempCube[i*3+18]
        cube[i*3+45]=tempCube[i*3+36]

        cube[i+start] = tempCube[start+6-i*3]
        cube[i+3+start] = tempCube[start+7-i*3]
        cube[i+6+start] = tempCube[start+8-i*3]

    if(showSteps == True):
        print("lc")

    return(cube)
def lcc(cube):
    cube = lc(cube)
    cube = lc(cube)
    cube = lc(cube)

    if(showSteps == True):
        print("lcc")

    return(cube)
def tc(cube):
    #//rotate right right side clockwise with green facing you and red on top
    tempCube = cube.copy()
    start = 0
    for i in range(3): #(i=0i<3i++)
        cube[i+9]=tempCube[i+18]
        cube[i+18]=tempCube[i+27]
        cube[i+27]=tempCube[53-i]
        cube[53-i]=tempCube[i+9]

        cube[i+start] = tempCube[start+6-i*3]
        cube[i+3+start] = tempCube[start+7-i*3]
        cube[i+6+start] = tempCube[start+8-i*3]
    
    if(showSteps == True):
        print("tc")

    return(cube)
def tcc(cube):
    cube = tc(cube)
    cube = tc(cube)
    cube = tc(cube)

    if(showSteps == True):
        print("tcc")

    return(cube)
def bc(cube):
    #rotate bottom side clockwise with green facing you and red on top
    tempCube = cube.copy()
    start = 36
    for i in range(3): #(i=0i<3i++)
        cube[i+9+6]=tempCube[47-i]
        cube[i+18+6]=tempCube[i+9+6]
        cube[i+27+6]=tempCube[i+18+6]
        cube[47-i]=tempCube[i+27+6]

        cube[i+start] = tempCube[start+6-i*3]
        cube[i+3+start] = tempCube[start+7-i*3]
        cube[i+6+start] = tempCube[start+8-i*3]
    
    if(showSteps == True):
        print("bc")

    return(cube)
def bcc(cube):
    cube = bc(cube)
    cube = bc(cube)
    cube = bc(cube)

    if(showSteps == True):
        print("bcc")

    return(cube)
    
def fc(cube):
    tempCube = cube.copy()
    start = 18
    for i in range(3): #(i=0i<3i++)
        cube[i+6]=tempCube[6+3*(3-i)+2]
        cube[6+3*(3-i)+2]=tempCube[38-i]
        cube[36+i]=tempCube[33-(i*3)]
        cube[27+(i*3)]=tempCube[i+6]

        cube[i+start] = tempCube[start+6-i*3]
        cube[i+3+start] = tempCube[start+7-i*3]
        cube[i+6+start] = tempCube[start+8-i*3]

    if(showSteps == True):
        print("fc")

    return(cube)
def fcc(cube):
    cube = fc(cube)
    cube = fc(cube)
    cube = fc(cube)

    if(showSteps == True):
        print("fcc")
    
    return(cube)
def ac(cube):
    #//rotate right right side clockwise with green facing you and red on top
    tempCube = cube.copy()
    start = 53
    for i in range(3):# (i=0 i<3 i++)
        
        cube[i]=tempCube[29+i*3]
        cube[29+i*3]=tempCube[44-i]
        cube[44-i]=tempCube[15-i*3]
        cube[9+i*3]=tempCube[2-i]
        

        cube[start-i] = tempCube[start-6+i*3] #good
        cube[start-i-3] = tempCube[start-7+i*3] 
        cube[start-i-6] = tempCube[start-8+i*3]

    if(showSteps == True):
        print("ac")

    return(cube)
def acc(cube):
    cube = ac(cube)
    cube = ac(cube)
    cube = ac(cube)

    if(showSteps == True):
        print("acc")

    return(cube)

def blueCross(cube):
    debug = True
    blues = 0
    print("entering blue cross phase")
    while(not(cube[46]=='g' and cube[50]=='g' and cube[52]=='g' and cube[48]=='g')):
        ### Green Side
        
        if(cube[19] == 'g'):
            if(debug == True):
                print("19")
            while(cube[52] == 'g'):
                cube = ac(cube)
            
            cube = tc(cube)
            cube = tc(cube)
        
        if(cube[23] == 'g'):
            if(debug == True):
                print("23")
            while(cube[50] == 'g'):
                cube = ac(cube)
            
            cube = rc(cube)
            cube = rc(cube)

        if(cube[21] == 'g'):
            if(debug == True):
                print("21")
            while(cube[48] == 'g'):
                cube = ac(cube)
            
            cube = lc(cube)
            cube = lc(cube)
            
        if(cube[25] == 'g'):
            if(debug == True):
                print("25")
            while(cube[46] == 'g'):
                cube = ac(cube)
            
            cube = bc(cube)
            cube = bc(cube)

        ### Yellow Side
        if(cube[30] == 'g'):
            
            if(debug == True):
                print("30")
            while(cube[52] == 'g'):
                cube = ac(cube)
            
            cube = rc(cube)
            cube = ac(cube)
            cube = tcc(cube)
        
        if(cube[28] == 'g'):
            
            if(debug == True):
                print("28")
            while(cube[52] == 'g'):
                cube = ac(cube)
            
            cube = tcc(cube)

        if(cube[32] == 'g'):
            if(debug == True):
                print("32")
            while(cube[48] == 'g'):
                cube = ac(cube)
            
            cube = rcc(cube)
            cube = acc(cube)
            cube = tcc(cube)

        if(cube[34] == 'g'):
            
            if(debug == True):
                print("34")
            while(cube[46] == 'g'):
                cube = ac(cube)
            
            cube = bc(cube)

        ###  red side
        if(cube[1] == 'g'):
            if(debug == True):
                print("1")
            cube = tc(cube)
            cube = acc(cube)
            cube = rc(cube)
        
        if(cube[3] == 'g'):
            
            if(debug == True):
                print("3")
            while(cube[48] == 'g'):
                cube = ac(cube)
            
            cube = lcc(cube)

        if(cube[5] == 'g'):
            if(debug == True):
                print("5")
            while(cube[50] == 'g'):
                cube = ac(cube)
            
            cube = rc(cube)

        if(cube[7] == 'g'):
            if(debug == True):
                print("7")
            while(cube[52] == 'g'):
                cube = ac(cube)
            
            cube = tc(cube)
            cube = bc(cube)
            cube = lcc(cube)

        ###  white side
        if(cube[10] == 'g'):
            
            if(debug == True):
                print("10")
            while(cube[52] == 'g'):
                cube = ac(cube)
            
            cube = tc(cube)
        
        if(cube[12] == 'g'):
            
            if(debug == True):
                print("12")
            while(cube[48] == 'g'):
                cube = ac(cube)
            
            cube = lcc(cube)
            cube = acc(cube)
            cube = tc(cube)

        if(cube[14] == 'g'):
            
            if(debug == True):
                print("14")
            while(cube[48] == 'g'):
                cube = ac(cube)
            
            cube = lcc(cube)
            cube = acc(cube)
            cube = tc(cube)

        if(cube[16] == 'g'):
            
            if(debug == True):
                print("16")
            while(cube[46] == 'g'):
                cube = ac(cube)
            
            cube = bcc(cube)

        ###  orange side
        if(cube[37] == 'g'):
            
            if(debug == True):
                print("37")
            while(cube[46] == 'g'):
                cube = ac(cube)
            
            cube = bc(cube)
            cube = ac(cube)
            cube = rcc(cube)
        
        if(cube[39] == 'g'):
            if(debug == True):
                print("39")
            while(cube[48] == 'g'):
                cube = ac(cube)

            cube = lc(cube)

        if(cube[41] == 'g'):
            if(debug == True):
                print("41")
            while(cube[50] == 'g'):
                cube = ac(cube)
            
            cube = rcc(cube)

        if(cube[43] == 'g'):
            
            if(debug == True):
                print("43")
            while(cube[46] == 'g'):
                cube = ac(cube)
            
            cube = bc(cube)
            cube = acc(cube)
            cube = lc(cube)

        print(blues)
        blues += 1
        # if blues == 100:
        #     break
        #if(cube)
    print("leaving blue cross phase")
    return cube
'''
string awayclock(string cube)*/'''

def populateCube():
    gSide = "ggggggggg"
    ySide = "yyyyyyyyy"
    bSide = "bbbbbbbbb"
    wSide = "wwwwwwwww"
    rSide = "rrrrrrrrr"
    oSide = "ooooooooo"
    cube = str(rSide+wSide+gSide+ySide+oSide+bSide)
    return cube

def main():
    """
    #int i,j
    print("This program is going to solve a rubik's cube")
    /*print( "Enter the colors of the side with \na green center piece:\n"
    string gSide
    cin >> gSide
    print(gSide,endl
    print( "\nEnter the colors of the side with \na yellow center piece:\n"
    string ySide
    cin >> ySide
    print(ySide,endl
    print( "\nEnter the colors of the side with \na blue center piece:\n"
    string bSide
    cin >> bSide
    print(bSide,endl
    print( "\nEnter the colors of the side with \na white center piece:\n"
    string wSide
    cin >> wSide
    print(wSide,endl
    print( "\nEnter the colors of the side with \na red center piece:\n"
    string rSide
    cin >> rSide
    print(rSide,endl
    print( "\nEnter the colors of the side with \na orange center piece:\n"
    string oSide
    cin >> oSide
    print(oSide,endl

    string cube = rSide+wSide+gSide+ySide+oSide+bSide
    print( cube,endl*/

    string gSide = "ggggggggg"
    string ySide = "yyyyyyyyy"
    string bSide = "bbbbbbbbb"
    string wSide = "wwwwwwwww"
    string rSide = "rrrrrrrrr"
    string oSide = "ooooooooo"
    string cube = rSide+wSide+gSide+ySide+oSide+bSide
    print( cube,endl
    printCube(cube)
    cube = leftclock(cube)
    printCube(cube)
    cube = topclock(cube)
    printCube(cube)
    cube = leftclock(cube)
    print( "test"
    printCube(cube)
    cube = bottomclock(cube)
    """
    
    cube = populateCube()
    cube = list(cube)
    
    #for i in range(54):
    #    cube[i] = i
    solution = cube.copy()
    printCube(cube)
    for i in range(10):
        
        x = random.randint(1,6)
        if(x==0):
            continue
        if(x==1):
            #print(x)
            cube = rc(cube)

        if(x==2):
            cube = ac(cube)

        if(x==3):
            cube = lc(cube)
        
        if(x==4):
            cube = fc(cube)
        
        if(x==5):
            cube = bc(cube)

        if(x==6):
            cube = tc(cube)
        if(i%100000 == 0):
            print(i)
        if (cube == solution):
            print(i)
            break
        

    printCube(cube)
    cube = blueCross(cube)
    printCube(cube)
    print (cube)
   



    return 0


main()