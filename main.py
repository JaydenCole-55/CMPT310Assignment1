import utils
from search import *
import random
import time
import math

# Keep everything consistent
random.seed(1)

# Define the numbers in the puzzle
puzzleNums = range(10)

def make_rand_StagePuzzle():
    """ 
    Will create a new solvable instance of a StagePuzzle
    Passed: None
    Returns: StagePuzzle
    """
    initPuzzleConfig = tuple(random.sample(puzzleNums, len(puzzleNums)))

    newStage = StagePuzzle(initPuzzleConfig)
    if (newStage.check_solvability):
        return newStage
    else:
        print("Not solvable")
        return None

def display(state):
    """ 
    Displays a StagePuzzle state and displays it nicely
    Passed: Tuple of len = 10
    Returns None
    """
    # Turn the tuple into a string, replacing "0" with "*""
    stateAsStr = ""

    for i in state:
        if i == 0:
            stateAsStr = stateAsStr + "*"
        else:
            stateAsStr = stateAsStr + str(i)

    # Format the printing of the string
    print()
    print(" " + stateAsStr[0] + stateAsStr[1])
    print(stateAsStr[2] + stateAsStr[3] + stateAsStr[4] + stateAsStr[5])
    print(stateAsStr[6] + stateAsStr[7] + stateAsStr[8] + stateAsStr[9])
    print()

def fnCompareSearchMethods():
    """ 
    This function will create 8 stagePuzzles and compare the computational and time 
    resources needed for different algorithms to complete
    Passed: None
    Returns: None
    """
    # 1. Make 8 initial puzzle boards
    puzzleLst = []
    numPuzzles = 8

    while numPuzzles > 0:
        puzzle = make_rand_StagePuzzle()
        if puzzle:
            puzzleLst = puzzleLst + [puzzle]
            numPuzzles = numPuzzles - 1

    # Copy list to use on the other methods
    puzzleLstCpy = puzzleLst

    # 2. Solve the boards one method at a time
    # Start with A* basic
    tic = time.time()
    i = 0

    while i < 8:
        #display( puzzleLstCpy[i].initial )
        tic2 = time.time()
        astar_search(puzzleLstCpy[i], None, True)
        toc2 = time.time()
        if math.ceil(toc2-tic2) == cutOff or math.floor(toc2-tic2) == cutOff:
            puzzleLstCpy[i] = make_rand_StagePuzzle()
            continue
        print("Solved number " + i + ".")
        print()
        i = i + 1

    toc = time.time()
    astarh1Time = toc - tic
    print(tastarh1Time)

def main():
    #********** PART A: **********
    # Create a new stage puzzle class and ensure it is solvable
    myNewPuzzle = make_rand_StagePuzzle()

    #********** PART B: **********
    # Display function for a StagePuzzle State
    exampleState = (5, 3, 8, 1, 4, 0, 9, 2, 7, 6)
    display( exampleState )

    #********** PART C: **********
    # Create 8 stagePuzzles and use different methods to solve them
    fnCompareSearchMethods()

    print("\nFinished Program")

""" Entry Point """
if(__name__ == "__main__"):
    main()