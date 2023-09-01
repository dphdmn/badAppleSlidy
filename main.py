
import cv2
import numpy as np
import sys

def convertRgbToWeight(rgbArray):
    arrayWithPixelWeight = []
    for i in range(int(rgbArray.size / rgbArray[0].size)):
        for j in range(int(rgbArray[0].size / 3)):
            lum = 255 - (int(rgbArray[i][j][0]) + int(rgbArray[i][j][1]) + int(
                rgbArray[i][j][2]) / 3)  # Reversed luminosity
            arrayWithPixelWeight.append(lum / 255)  # Map values from range 0-255 to 0-1
    return arrayWithPixelWeight

w = 24
h = 18
puzzleSize = 48
img_amount = 6572

np.set_printoptions(threshold=sys.maxsize)
f = open("scrambles.txt","w+")
for num in range(img_amount):
    name="small_frames/"+str(num+1)+".jpg"
    my_img = cv2.imread(name)
    print(name)
    convertedList = convertRgbToWeight(my_img)
    c = 0
    curline = 0
    curid = 0

    colors = np.zeros((h, w), dtype=int)
    for i in range(w*h):
        if convertedList[i] > 0.7:
            colors[curline, curid] = 1
        curid = curid+1
        if curid == w:
            curid=0
            curline = curline+1
    #print(colors)

    puzzle = np.zeros((puzzleSize, puzzleSize), dtype=int)
    c = 1
    for j in range(puzzleSize):
        for i in range(puzzleSize):
            puzzle[j,i]=c
            c = c+1
    puzzle[puzzleSize-1, puzzleSize-1]=0

    #print(puzzle)
    swaps=0
    for i in range(h):
        for j in range(w):
            if colors[i, j] == 1:
                a, b = puzzle[i][j], puzzle[i+w][j]
                puzzle[i][j], puzzle[i+w][j] = puzzle[i+w][j], puzzle[i][j]
                if a != 0 and b != 0:
                    swaps = swaps + 1
                a, b = puzzle[i][j + w], puzzle[i+w][j+w]
                puzzle[i][j + w], puzzle[i+w][j+w] = puzzle[i+w][j+w], puzzle[i][j + w]
                if a != 0 and b != 0:
                    swaps = swaps + 1
    print(swaps)
    if (swaps % 2) != 0:
        a, b = puzzle[puzzleSize-1][puzzleSize-3], puzzle[puzzleSize-1][puzzleSize-2]
        puzzle[puzzleSize-1][puzzleSize-3], puzzle[puzzleSize-1][puzzleSize-2] = puzzle[puzzleSize-1][puzzleSize-2], puzzle[puzzleSize-1][puzzleSize-3]
    #print(puzzle)
    #mystr=str(num) + ": "
    mystr=""
    for x in puzzle:
        for y in x:
            mystr = mystr + str(y) + " "
        mystr = mystr[:-1]
        mystr = mystr + "/"
    mystr = mystr[:-1]
    #print(mystr)
    f.write(mystr+"\n")
f.close()
