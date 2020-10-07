import utils
from search import *
import random
import time
import math

# Keep everything consistent
random.seed(1)

# Define the numbers in the puzzle
puzzleNums = range(10)

# Define in seconds the time limit for the first algorithm to find a solution
timeLimit = 120
noTimeLimit = sys.maxsize

# Verbose output
verbose = True

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
            numPuzzles -= 1
      
    # 2. Solve the puzzle with A* basic
    print("Now using incorrectly placed tiles heuristic")
    astarTime = 0
    astarFrontierNodesRemoved = 0
    astarSolnPathLength = 0

    i = 0
    while i < 8:
        tic = time.time()
        result = astar_search(puzzleLst[i], None, verbose, timeLimit) 
        toc = time.time()
        
        # Make a new puzzle if no result was found
        if result is not None:
            print("Solved number " + str(i) + ".")
            print("Goal node found at depth: " + str(result.depth) + " after " + str(result.frontierNodesRemoved) + " frontier nodes were removed.")
            print("It took " + str(toc-tic) + "s to find the goal node ")
            display( puzzleLst[i].initial )
            astarTime += (toc - tic)
            astarFrontierNodesRemoved += result.frontierNodesRemoved
            astarSolnPathLength += result.depth
            i += 1
        else:
            puzzleLst[i] = make_rand_StagePuzzle()
    
    # 3. Use Manhatten heuristic to find 8 (quick) solutions
    print("Now using manhatten distance heuristic")
    i = 0
    manhattenTime = 0
    manhattenFrontierNodesRemoved = 0
    manhattenSolnPathLength = 0
    while i < 8:
        tic = time.time()
        result = astar_search(puzzleLst[i], puzzleLst[i].fnMyManhattenHeuristic, verbose, noTimeLimit)
        toc = time.time()

        print("Solved number " + str(i) + ".")
        print("Goal node found at depth: " + str(result.depth) + " after " + str(result.frontierNodesRemoved) + " frontier nodes were removed.")
        print("It took " + str(toc-tic) + "s to find the goal node ")
        display( puzzleLst[i].initial )
        manhattenTime += (toc - tic)
        manhattenFrontierNodesRemoved += result.frontierNodesRemoved
        manhattenSolnPathLength += result.depth
        i += 1
    
    # 4. Solve the puzzle with A* with maximum heuristic from the previous two
    print("Now using maximum value of the two heuristics")
    astarMaxTime = 0
    astarMaxFrontierNodesRemoved = 0
    astarMaxSolnPathLength = 0

    i = 0
    while i < 8:
        tic = time.time()
        result = astar_search(puzzleLst[i], puzzleLst[i].fnGetMaxHeuristic, verbose, noTimeLimit) 
        toc = time.time()
        
        print("Solved number " + str(i) + ".")
        print("Goal node found at depth: " + str(result.depth) + " after " + str(result.frontierNodesRemoved) + " frontier nodes were removed.")
        print("It took " + str(toc-tic) + "s to find the goal node ")
        display( puzzleLst[i].initial )
        astarMaxTime += (toc - tic)
        astarMaxFrontierNodesRemoved += result.frontierNodesRemoved
        astarMaxSolnPathLength += result.depth
        i += 1

    # Now we have the results for 8 solutions using all three methods.
    # Display the results
    print()
    print("Collecting results complete, displaying for combined total of all 8 results")
    print("Solution method    " + " "*10 + "Total Running time" + " "*10 + "Total Solution Length"      + " "*10 + "Total Removed Frontier Nodes")
    print("Manhatten Heuristic" + " "*10 + str(manhattenTime)   + " "*10 + str(manhattenSolnPathLength) + " "*10 + str(manhattenFrontierNodesRemoved))
    print("Misplaced Tiles    " + " "*10 + str(astarTime)       + " "*10 + str(astarSolnPathLength)     + " "*10 + str(astarFrontierNodesRemoved))    
    print("Maximum Heuristic  " + " "*10 + str(astarMaxTime)    + " "*10 + str(astarMaxSolnPathLength)  + " "*10 + str(astarMaxFrontierNodesRemoved))


def main():
    #********** PART A: **********
    # Create a new stage puzzle class and ensure it is solvable
    myNewPuzzle = make_rand_StagePuzzle()

    #********** PART B: **********
    # Display function for a StagePuzzle State
    display( myNewPuzzle.initial )

    #********** PART C: **********
    # Create 8 stagePuzzles and use different methods to solve them
    fnCompareSearchMethods()

    print("\nFinished Program")

""" Entry Point """
if(__name__ == "__main__"):
    main()