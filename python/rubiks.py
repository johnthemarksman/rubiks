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
steps = 0

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


def yc(cube):
    global steps
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
        print(steps,": yc")
        steps += 1

    return(cube)
def ycc(cube):
    global steps
    global showSteps
    showSteps = False
    cube = yc(cube)
    cube = yc(cube)
    cube = yc(cube)
    showSteps = True


    if(showSteps == True):
        print(steps,": ycc")
        steps += 1

    return(cube)
def wc(cube):
    global steps
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
        print(steps,": wc")
        steps += 1

    return(cube)
def wcc(cube):
    global steps
    global showSteps
    showSteps = False
    cube = wc(cube)
    cube = wc(cube)
    cube = wc(cube)
    showSteps = True

    if(showSteps == True):
        print(steps,": wcc")
        steps += 1

    return(cube)
def rc(cube):
    global steps
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
        print(steps,": rc")
        steps += 1

    return(cube)
def rcc(cube):
    global steps
    global showSteps
    showSteps = False
    cube = rc(cube)
    cube = rc(cube)
    cube = rc(cube)
    showSteps = True

    if(showSteps == True):
        print(steps,": rcc")
        steps += 1

    return(cube)
def oc(cube):
    global steps
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
        print(steps,": oc")
        steps += 1

    return(cube)
def occ(cube):
    global steps
    global showSteps
    showSteps = False
    cube = oc(cube)
    cube = oc(cube)
    cube = oc(cube)
    showSteps = True

    if(showSteps == True):
        print(steps,": occ")
        steps += 1

    return(cube)
    
def gc(cube):
    global steps
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
        print(steps,": gc")
        steps += 1

    return(cube)
def gcc(cube):
    global steps
    global showSteps
    showSteps = False
    cube = gc(cube)
    cube = gc(cube)
    cube = gc(cube)
    showSteps = True

    if(showSteps == True):
        print(steps,": gcc")
        steps += 1
    
    return(cube)
def bc(cube):
    global steps
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
        print(steps,": bc")
        steps += 1

    return(cube)
def bcc(cube):
    global steps
    global showSteps
    showSteps = False
    cube = bc(cube)
    cube = bc(cube)
    cube = bc(cube)
    showSteps = True

    if(showSteps == True):
        print(steps,": bcc")
        steps += 1

    return(cube)

def blueFlower(cube):
    debug = True
    blues = 0
    print("entering blue cross phase")
    while(not(cube[46]=='g' and cube[50]=='g' and cube[52]=='g' and cube[48]=='g')):
        ### Green Side
        
        if(cube[19] == 'g'):
            if(debug == True):
                print("19")
            while(cube[52] == 'g'):
                cube = bc(cube)
            
            cube = rc(cube)
            cube = rc(cube)
        
        if(cube[23] == 'g'):
            if(debug == True):
                print("23")
            while(cube[50] == 'g'):
                cube = bc(cube)
            
            cube = yc(cube)
            cube = yc(cube)

        if(cube[21] == 'g'):
            if(debug == True):
                print("21")
            while(cube[48] == 'g'):
                cube = bc(cube)
            
            cube = wc(cube)
            cube = wc(cube)
            
        if(cube[25] == 'g'):
            if(debug == True):
                print("25")
            while(cube[46] == 'g'):
                cube = bc(cube)
            
            cube = oc(cube)
            cube = oc(cube)

        ### Yellow Side
        if(cube[30] == 'g'):
            
            if(debug == True):
                print("30")
            while(cube[52] == 'g'):
                cube = bc(cube)
            
            cube = yc(cube)
            cube = bc(cube)
            cube = rcc(cube)
        
        if(cube[28] == 'g'):
            
            if(debug == True):
                print("28")
            while(cube[52] == 'g'):
                cube = bc(cube)
            
            cube = rcc(cube)

        if(cube[32] == 'g'):
            if(debug == True):
                print("32")
            while(cube[48] == 'g'):
                cube = bc(cube)
            
            cube = ycc(cube)
            cube = bcc(cube)
            cube = rcc(cube)

        if(cube[34] == 'g'):
            
            if(debug == True):
                print("34")
            while(cube[46] == 'g'):
                cube = bc(cube)
            
            cube = oc(cube)

        ###  red side
        if(cube[1] == 'g'):
            if(debug == True):
                print("1")
            cube = rc(cube)
            cube = bcc(cube)
            cube = yc(cube)
        
        if(cube[3] == 'g'):
            
            if(debug == True):
                print("3")
            while(cube[48] == 'g'):
                cube = bc(cube)
            
            cube = wcc(cube)

        if(cube[5] == 'g'):
            if(debug == True):
                print("5")
            while(cube[50] == 'g'):
                cube = bc(cube)
            
            cube = yc(cube)

        if(cube[7] == 'g'):
            if(debug == True):
                print("7")
            while(cube[52] == 'g'):
                cube = bc(cube)
            
            cube = rc(cube)
            cube = oc(cube)
            cube = wcc(cube)

        ###  white side
        if(cube[10] == 'g'):
            
            if(debug == True):
                print("10")
            while(cube[52] == 'g'):
                cube = bc(cube)
            
            cube = rc(cube)
        
        if(cube[12] == 'g'):
            
            if(debug == True):
                print("12")
            while(cube[48] == 'g'):
                cube = bc(cube)
            
            cube = wcc(cube)
            cube = bcc(cube)
            cube = rc(cube)

        if(cube[14] == 'g'):
            
            if(debug == True):
                print("14")
            while(cube[48] == 'g'):
                cube = bc(cube)
            
            cube = wcc(cube)
            cube = bcc(cube)
            cube = rc(cube)

        if(cube[16] == 'g'):
            
            if(debug == True):
                print("16")
            while(cube[46] == 'g'):
                cube = bc(cube)
            
            cube = occ(cube)

        ###  orange side
        if(cube[37] == 'g'):
            
            if(debug == True):
                print("37")
            while(cube[46] == 'g'):
                cube = bc(cube)
            
            cube = oc(cube)
            cube = bc(cube)
            cube = ycc(cube)
        
        if(cube[39] == 'g'):
            if(debug == True):
                print("39")
            while(cube[48] == 'g'):
                cube = bc(cube)

            cube = wc(cube)

        if(cube[41] == 'g'):
            if(debug == True):
                print("41")
            while(cube[50] == 'g'):
                cube = bc(cube)
            
            cube = ycc(cube)

        if(cube[43] == 'g'):
            
            if(debug == True):
                print("43")
            while(cube[46] == 'g'):
                cube = bc(cube)
            
            cube = oc(cube)
            cube = bcc(cube)
            cube = wc(cube)

        print(blues)
        blues += 1
        # if blues == 100:
        #     break
        #if(cube)
    print("leaving blue cross phase")
    return cube

def greenCross(cube):
    while not(cube[19] == 'g' and cube[21] == 'g' and cube[23] == 'g' and cube[25] == 'g'):
        if((cube[43] == 'o' and cube[46] == 'g') or (cube[32] == 'y' and cube[50] == 'g') or (cube[1] == 'r' and cube[52] == 'g') or (cube[12] == 'w' and cube[48] == 'g')):
            if (cube[43] == 'o' and cube[46] == 'g') :
                cube = oc(cube)
                cube = oc(cube)

            if (cube[32] == 'y' and cube[50] == 'g'):
                cube = yc(cube)
                cube = yc(cube)

            if (cube[1] == 'r' and cube[52] == 'g'):
                cube = rc(cube)
                cube = rc(cube)

            if (cube[12] == 'w' and cube[48] == 'g'):
                cube = wc(cube)
                cube = wc(cube)
        else:
            cube = bc(cube)
    return cube

def greenCorners(cube):
    ### green red white corner
    print("green red white corner")
    grw = ('g', 'r', 'w')
    correct = (18,6,11)
    belowCorrect = (0,9,51)

    if(cube[20] in grw and cube[27] in grw and cube[8] in grw):
        cube = rcc(cube)
        cube = bcc(cube)
        cube = rc(cube)
        cube = bc(cube)
    elif(cube[24] in grw and cube[17] in grw and cube[36] in grw):
        cube = occ(cube)
        cube = bcc(cube)
        cube = oc(cube)
        cube = bc(cube)
    elif(cube[26] in grw and cube[38] in grw and cube[33] in grw):
        cube = ycc(cube)
        cube = bcc(cube)
        cube = yc(cube)
        cube = bc(cube)
    
    while(not((cube[belowCorrect[0]] in grw) and (cube[belowCorrect[1]] in grw) and (cube[belowCorrect[2]] in grw)) and not(cube[correct[0]] in grw and cube[correct[1]] in grw and cube[correct[2]] in grw)):
        cube = bc(cube)

    if(cube[correct[0]] in grw and cube[correct[1]] in grw and cube[correct[2]] in grw) or (cube[0] in grw) and (cube[9] in grw) and (cube[51] in grw) and not(cube[correct[0]] == 'g' and cube[correct[1]] == 'r' and cube[correct[2]] == 'w'):
        while(not(cube[correct[0]] == 'g' and cube[correct[1]] == 'r' and cube[correct[2]] == 'w')):
            cube = wcc(cube)
            cube = bcc(cube)
            cube = wc(cube)
            cube = bc(cube)






    ### green yellow red corner
    print("green yellow red corner")
    grw = ('g', 'y', 'r')
    correct = (20,27,8)
    belowCorrect = (29,2,53)


    if(cube[18] in grw and cube[6] in grw and cube[11] in grw):
        cube = wcc(cube)
        cube = bcc(cube)
        cube = wc(cube)
        cube = wc(cube)

    # elif(cube[20] in grw and cube[27] in grw and cube[8] in grw):
    #     cube = rcc(cube)
    #     cube = bcc(cube)
    #     cube = rc(cube)
    #     cube = bc(cube)
    elif(cube[24] in grw and cube[17] in grw and cube[36] in grw):
        cube = occ(cube)
        cube = bcc(cube)
        cube = oc(cube)
        cube = bc(cube)
    elif(cube[26] in grw and cube[38] in grw and cube[33] in grw):
        cube = ycc(cube)
        cube = bcc(cube)
        cube = yc(cube)
        cube = bc(cube)
    
    while(not((cube[belowCorrect[0]] in grw) and (cube[belowCorrect[1]] in grw) and (cube[belowCorrect[2]] in grw)) and not(cube[correct[0]] in grw and cube[correct[1]] in grw and cube[correct[2]] in grw)):
        cube = bc(cube)

    if(cube[correct[0]] in grw and cube[correct[1]] in grw and cube[correct[2]] in grw) or (cube[belowCorrect[0]] in grw) and (cube[belowCorrect[1]] in grw) and (cube[belowCorrect[2]] in grw) and not(cube[correct[0]] == grw[0] and cube[correct[1]] == grw[1] and cube[correct[2]] == grw[2]):
        while(not(cube[correct[0]] == grw[0] and cube[correct[1]] == grw[1] and cube[correct[2]] == grw[2])):
            cube = rcc(cube)
            cube = bcc(cube)
            cube = rc(cube)
            cube = bc(cube)

    ### green white orange corner
    print("green white orange corner")
    grw = ('g', 'w', 'o')
    correct = (24,17,36)
    belowCorrect = (15,42,45)


    if(cube[18] in grw and cube[6] in grw and cube[11] in grw):
        cube = wcc(cube)
        cube = bcc(cube)
        cube = wc(cube)
        cube = wc(cube)

    elif(cube[20] in grw and cube[27] in grw and cube[8] in grw):
        cube = rcc(cube)
        cube = bcc(cube)
        cube = rc(cube)
        cube = bc(cube)
    # elif(cube[24] in grw and cube[17] in grw and cube[36] in grw):
    #     cube = occ(cube)
    #     cube = bcc(cube)
    #     cube = oc(cube)
    #     cube = bc(cube)
    elif(cube[26] in grw and cube[38] in grw and cube[33] in grw):
        cube = ycc(cube)
        cube = bcc(cube)
        cube = yc(cube)
        cube = bc(cube)
    
    while(not((cube[belowCorrect[0]] in grw) and (cube[belowCorrect[1]] in grw) and (cube[belowCorrect[2]] in grw)) and not(cube[correct[0]] in grw and cube[correct[1]] in grw and cube[correct[2]] in grw)):
        cube = bc(cube)

    if(cube[correct[0]] in grw and cube[correct[1]] in grw and cube[correct[2]] in grw) or (cube[belowCorrect[0]] in grw) and (cube[belowCorrect[1]] in grw) and (cube[belowCorrect[2]] in grw) and not(cube[correct[0]] == grw[0] and cube[correct[1]] == grw[1] and cube[correct[2]] == grw[2]):
        while(not(cube[correct[0]] == grw[0] and cube[correct[1]] == grw[1] and cube[correct[2]] == grw[2])):
            cube = occ(cube)
            cube = bcc(cube)
            cube = oc(cube)
            cube = bc(cube)


    ### green orange yellow corner
    print("green orange yellow corner")
    grw = ('g', 'o', 'y')
    correct = (26,38,33)
    belowCorrect = (44,35,47)


    if(cube[18] in grw and cube[6] in grw and cube[11] in grw):
        cube = wcc(cube)
        cube = bcc(cube)
        cube = wc(cube)
        cube = wc(cube)

    elif(cube[20] in grw and cube[27] in grw and cube[8] in grw):
        cube = rcc(cube)
        cube = bcc(cube)
        cube = rc(cube)
        cube = bc(cube)
    elif(cube[24] in grw and cube[17] in grw and cube[36] in grw):
        cube = occ(cube)
        cube = bcc(cube)
        cube = oc(cube)
        cube = bc(cube)
    # elif(cube[26] in grw and cube[38] in grw and cube[33] in grw):
    #     cube = ycc(cube)
    #     cube = bcc(cube)
    #     cube = yc(cube)
    #     cube = bc(cube)
    
    while(not((cube[belowCorrect[0]] in grw) and (cube[belowCorrect[1]] in grw) and (cube[belowCorrect[2]] in grw)) and not(cube[correct[0]] in grw and cube[correct[1]] in grw and cube[correct[2]] in grw)):
        cube = bc(cube)

    if(cube[correct[0]] in grw and cube[correct[1]] in grw and cube[correct[2]] in grw) or (cube[belowCorrect[0]] in grw) and (cube[belowCorrect[1]] in grw) and (cube[belowCorrect[2]] in grw) and not(cube[correct[0]] == grw[0] and cube[correct[1]] == grw[1] and cube[correct[2]] == grw[2]):
        while(not(cube[correct[0]] == grw[0] and cube[correct[1]] == grw[1] and cube[correct[2]] == grw[2])):
            cube = ycc(cube)
            cube = bcc(cube)
            cube = yc(cube)
            cube = bc(cube)








    return(cube)


def prepEdge(cube, location):
    if(location == 0):
        cube = bc(cube)
        cube = rc(cube)
        cube = bcc(cube)
        cube = rcc(cube)
        cube = bcc(cube)
        cube = wcc(cube)
        cube = bc(cube)
        cube = wc(cube)
    elif(location == 1):
        cube = bc(cube)
        cube = yc(cube)
        cube = bcc(cube)
        cube = ycc(cube)
        cube = bcc(cube)
        cube = rcc(cube)
        cube = bc(cube)
        cube = rc(cube)
    elif(location == 2):
        cube = bc(cube)
        cube = oc(cube)
        cube = bcc(cube)
        cube = occ(cube)
        cube = bcc(cube)
        cube = ycc(cube)
        cube = bc(cube)
        cube = yc(cube)
    elif(location == 3):
        cube = bc(cube)
        cube = wc(cube)
        cube = bcc(cube)
        cube = wcc(cube)
        cube = bcc(cube)
        cube = occ(cube)
        cube = bc(cube)
        cube = oc(cube)
    return cube

def edges(cube):
    allEdges = ( (10, 3) , (5, 28) , (34, 41) , (16, 39) , (1, 52) , (32, 50) , (43, 46) , (12, 48) )
    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
    sideEdges = ( (10, 3) , (5, 28) , (34, 41) , (16, 39) )
    topEdges = ( (1, 52) , (32, 50) , (43, 46) , (12, 48) )
    
    #white red edge
    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
    print("white red edge")
    printCube(cube)
    correct = allEdges[0]
    colors = ('r', 'w')
    location = -1
    for i in range(8):
        if(colors[0] in allColors[i] and colors[1] in allColors[i]):
            location = i
            break

    cube = prepEdge(cube, location)

    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
   
    for i in range(8):
        if(colors[0] in allColors[i] and colors[1] in allColors[i]):
            location = i
            break

    if colors[0] == allColors[location][0]:
        while not(cube[52] in colors and cube[1] in colors):
            cube = bc(cube)
        cube = bcc(cube)
        cube = wcc(cube)
        cube = bc(cube)
        cube = wc(cube)
        cube = bc(cube)
        cube = rc(cube)
        cube = bcc(cube)
        cube = rcc(cube)
    else:
        while not(cube[48] in colors and cube[12] in colors):
            cube = bc(cube)
        cube = bc(cube)
        cube = rc(cube)
        cube = bcc(cube)
        cube = rcc(cube)
        cube = bcc(cube)
        cube = wcc(cube)
        cube = bc(cube)
        cube = wc(cube)

    #red yellow edge
    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
    print("red yellow edge")
    printCube(cube)
    e = 1
    correct = allEdges[e]
    colors = ('y', 'r')
    location = -1
    for i in range(8):
        if(colors[0] in allColors[i] and colors[1] in allColors[i]):
            location = i
            break

    cube = prepEdge(cube, location)

    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
   
    for i in range(8):
        if(colors[0] in allColors[i] and colors[1] in allColors[i]):
            location = i
            break

    if colors[0] == allColors[location][0]:
        while not(cube[50] in colors and cube[32] in colors):
            cube = bc(cube)
        cube = bcc(cube)
        cube = rcc(cube)
        cube = bc(cube)
        cube = rc(cube)
        cube = bc(cube)
        cube = yc(cube)
        cube = bcc(cube)
        cube = ycc(cube)
    else:
        while not(cube[52] in colors and cube[1] in colors):
            cube = bc(cube)
        cube = bc(cube)
        cube = yc(cube)
        cube = bcc(cube)
        cube = ycc(cube)
        cube = bcc(cube)
        cube = rcc(cube)
        cube = bc(cube)
        cube = rc(cube)
    
    #yellow orange edge
    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
    print("yellow orange edge")
    printCube(cube)
    e = 2
    correct = allEdges[e]
    colors = ('o', 'y')
    location = -1
    for i in range(8):
        if(colors[0] in allColors[i] and colors[1] in allColors[i]):
            location = i
            break
    
    cube = prepEdge(cube, location)

    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
   
    for i in range(8):
        if(colors[0] in allColors[i] and colors[1] in allColors[i]):
            location = i
            break

    if colors[0] == allColors[location][0]:
        while not(cube[46] in colors and cube[43] in colors):
            cube = bc(cube)
        cube = bcc(cube)
        cube = ycc(cube)
        cube = bc(cube)
        cube = yc(cube)
        cube = bc(cube)
        cube = oc(cube)
        cube = bcc(cube)
        cube = occ(cube)
    else:
        while not(cube[50] in colors and cube[32] in colors):
            cube = bc(cube)
        cube = bc(cube)
        cube = oc(cube)
        cube = bcc(cube)
        cube = occ(cube)
        cube = bcc(cube)
        cube = ycc(cube)
        cube = bc(cube)
        cube = yc(cube)

    #orange white edge
    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
    print("orange white edge")
    printCube(cube)
    e = 3
    correct = allEdges[e]
    colors = ('w', 'o')
    location = -1
    for i in range(8):
        if(colors[0] in allColors[i] and colors[1] in allColors[i]):
            location = i
            break

    cube = prepEdge(cube, location)

    allColors = ( (cube[10], cube[3]) , (cube[5], cube[28]) , (cube[34], cube[41]) , (cube[16], cube[39]) , (cube[1], cube[52]) , (cube[32], cube[50]) , (cube[43], cube[46]) , (cube[12], cube[48]) )
   
    for i in range(8):
        if(colors[0] in allColors[i] and colors[1] in allColors[i]):
            location = i
            break

    if colors[0] == allColors[location][0]:
        while not(cube[48] in colors and cube[12] in colors):
            cube = bc(cube)
        cube = bcc(cube)
        cube = occ(cube)
        cube = bc(cube)
        cube = oc(cube)
        cube = bc(cube)
        cube = wc(cube)
        cube = bcc(cube)
        cube = wcc(cube)
    else:
        while not(cube[46] in colors and cube[43] in colors):
            cube = bc(cube)
        cube = bc(cube)
        cube = wc(cube)
        cube = bcc(cube)
        cube = wcc(cube)
        cube = bcc(cube)
        cube = occ(cube)
        cube = bc(cube)
        cube = oc(cube)

    
        
    return cube
    
def blueCross(cube):
    crossColors = (cube[46],cube[48],cube[50],cube[52])
    if not(cube[46] == 'b' and cube[48] == 'b' and cube[50] == 'b' and cube[52] == 'b'):
        if not(cube[46] == 'b' or cube[48] == 'b' or cube[50] == 'b' or cube[52] == 'b'):
            print(1)
            cube = oc(cube)
            cube = wc(cube)
            cube = bc(cube)
            cube = wcc(cube)
            cube = bcc(cube)
            cube = occ(cube)
        printCube(cube)

        while(1):
            cube = bc(cube)
            if(cube[50] == 'b' and cube[52] == 'b'):
                break
            elif(cube[50] == 'b' and cube[48] == 'b'):
                break
        printCube(cube)
        if(cube[50] == 'b'  and cube[52] == 'b'):
            print(2)
            cube = oc(cube)
            cube = wc(cube)
            cube = bc(cube)
            cube = wcc(cube)
            cube = bcc(cube)
            cube = occ(cube)
            cube = oc(cube)
            cube = wc(cube)
            cube = bc(cube)
            cube = wcc(cube)
            cube = bcc(cube)
            cube = occ(cube)
        elif( cube[50] == 'b'  and cube[48] == 'b'  ):
            print(3)
            cube = oc(cube)
            cube = wc(cube)
            cube = bc(cube)
            cube = wcc(cube)
            cube = bcc(cube)
            cube = occ(cube)



    return cube


def blueCrossSides(cube):
    if not(cube[1]== 'r' and cube[12] == 'w' and cube[43] == 'o' and cube[32] == 'y'):
        print('test1')
        while(not(cube[1]== 'r' and cube[12] == 'w' and cube[43] == 'o' and cube[32] == 'y')):
            if cube[1] == 'r' and cube[12] == 'w':
                cube = wc(cube)
                cube = bc(cube)
                cube = wcc(cube)
                cube = bc(cube)
                cube = wc(cube)
                cube = bc(cube)
                cube = bc(cube)
                cube = wcc(cube)
                cube = bc(cube)
            elif cube[12] == 'w' and cube[43] == 'o':
                cube = oc(cube)
                cube = bc(cube)
                cube = occ(cube)
                cube = bc(cube)
                cube = oc(cube)
                cube = bc(cube)
                cube = bc(cube)
                cube = occ(cube)
                cube = bc(cube)
            elif cube[43] == 'o' and cube[32] == 'y':
                cube = yc(cube)
                cube = bc(cube)
                cube = ycc(cube)
                cube = bc(cube)
                cube = yc(cube)
                cube = bc(cube)
                cube = bc(cube)
                cube = ycc(cube)
                cube = bc(cube)
            elif cube[32] == 'y' and cube[1] == 'r':
                cube = rc(cube)
                cube = bc(cube)
                cube = rcc(cube)
                cube = bc(cube)
                cube = rc(cube)
                cube = bc(cube)
                cube = bc(cube)
                cube = rcc(cube)
                cube = bc(cube)
            elif cube[1] == 'r' and cube[43] == 'o':
                cube = oc(cube)
                cube = bc(cube)
                cube = occ(cube)
                cube = bc(cube)
                cube = oc(cube)
                cube = bc(cube)
                cube = bc(cube)
                cube = occ(cube)
                cube = bc(cube)
            elif cube[12] == 'w' and cube[32] == 'y':
                cube = yc(cube)
                cube = bc(cube)
                cube = ycc(cube)
                cube = bc(cube)
                cube = yc(cube)
                cube = bc(cube)
                cube = bc(cube)
                cube = ycc(cube)
                cube = bc(cube)
            else:
                cube = bc(cube)





    return cube

def blueCornersPrep(cube):
    count = 0
    while(count != 4):
        corners = ((cube[0],cube[9],cube[51]) , (cube[29],cube[2],cube[53]) , (cube[44], cube[35], cube[47]) , (cube[15], cube[42], cube[45]))
        correctCorners = (('r','w','b') , ('y', 'r' , 'b') , ('o', 'y', 'b') , ('w', 'o', 'b'))
    
        count = 0
        for i in range(4):
            if(corners[i][0] in correctCorners[i] and corners[i][1] in correctCorners[i] and corners[i][2] in correctCorners[i]):
                print(corners[i])
                c = i
                count += 1

        if count == 0:
            cube = bc(cube)
            cube = rc(cube)
            cube = bcc(cube)
            cube = occ(cube)
            cube = bc(cube) 
            cube = rcc(cube)
            cube = bcc(cube)
            cube = oc(cube)
        if count == 1:
            if c == 0:
                cube = bc(cube)
                cube = rc(cube)
                cube = bcc(cube)
                cube = occ(cube)
                cube = bc(cube) 
                cube = rcc(cube)
                cube = bcc(cube)
                cube = oc(cube)
            if c == 1:
                cube = bc(cube)
                cube = yc(cube)
                cube = bcc(cube)
                cube = wcc(cube)
                cube = bc(cube) 
                cube = ycc(cube)
                cube = bcc(cube)
                cube = wc(cube)
            if c == 2:
                cube = bc(cube)
                cube = oc(cube)
                cube = bcc(cube)
                cube = rcc(cube)
                cube = bc(cube) 
                cube = occ(cube)
                cube = bcc(cube)
                cube = rc(cube)
            if c == 3:
                cube = bc(cube)
                cube = wc(cube)
                cube = bcc(cube)
                cube = ycc(cube)
                cube = bc(cube) 
                cube = wcc(cube)
                cube = bcc(cube)
                cube = yc(cube)

            


    return cube

def blueCorners(cube):
    corners = ((cube[0],cube[9],cube[51]) , (cube[29],cube[2],cube[53]) , (cube[44], cube[35], cube[47]) , (cube[15], cube[42], cube[45]))

    for i in range(4):
        while corners[0][2] != 'b':
            cube = rcc(cube)
            cube = gcc(cube)
            cube = rc(cube)
            cube = gc(cube)

            corners = ((cube[0],cube[9],cube[51]) , (cube[29],cube[2],cube[53]) , (cube[44], cube[35], cube[47]) , (cube[15], cube[42], cube[45]))
        cube = bc(cube)
        corners = ((cube[0],cube[9],cube[51]) , (cube[29],cube[2],cube[53]) , (cube[44], cube[35], cube[47]) , (cube[15], cube[42], cube[45]))







    return cube
'''
string awayclock(string cube)*/'''

def populateCube():
    rSide = "rrrrrrrrr"
    wSide = "wwwwwwwww"
    gSide = "ggggggggg"
    ySide = "yyyyyyyyy"
    oSide = "ooooooooo"
    bSide = "bbbbbbbbb"

    rSide = input("Enter the red side with the blue side on top:")
    wSide = input("Enter the white side with the red side on top:")
    gSide = input("Enter the green side with the red side on top:")
    ySide = input("Enter the yellow side with the red side on top:")
    oSide = input("Enter the orange side with the green side on top:")
    bSide = input("Enter the blue side with the orange side on top:")

    
    cube = str(rSide+wSide+gSide+ySide+oSide+bSide)
    return cube

def main():
    global steps
    steps = 0
    
    cube = populateCube()
    cube = list(cube)
    
    # for i in range(54):
    #     cube[i] = i
    solution = cube.copy()
    printCube(cube)
    # for i in range(100):
        
    #     x = random.randint(1,6)
    #     if(x==0):
    #         continue
    #     if(x==1):
    #         #print(x)
    #         cube = yc(cube)

    #     if(x==2):
    #         cube = bc(cube)

    #     if(x==3):
    #         cube = wc(cube)
        
    #     if(x==4):
    #         cube = gc(cube)
        
    #     if(x==5):
    #         cube = oc(cube)

    #     if(x==6):
    #         cube = rc(cube)
    #     if(i%100000 == 0):
    #         print(i)
    #     if (cube == solution):
    #         print(i)
    #         break
    steps = 0

    printCube(cube)
    cube = blueFlower(cube)
    printCube(cube)
    cube = greenCross(cube)
    printCube(cube)
    cube = greenCorners(cube)
    printCube(cube)
    cube = edges(cube)
    printCube(cube)
    cube = blueCross(cube)
    printCube(cube)
    cube = blueCrossSides(cube)
    printCube(cube)
    cube = blueCornersPrep(cube)
    printCube(cube)
    cube = blueCorners(cube)
    printCube(cube)

    return 0

for i in range(1):
    main()