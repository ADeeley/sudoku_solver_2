import numpy as np

# references for the buckets so a set of coordinates can be associated with 
# a single bucket
bucket_locations = np.array([["b1", "b1", "b1", "b2", "b2", "b2", "b3", "b3", "b3"], 
                                             ["b1", "b1", "b1", "b2", "b2", "b2", "b3", "b3", "b3"],
                                             ["b1", "b1", "b1", "b2", "b2", "b2", "b3", "b3", "b3"],
                                             ["b4", "b4", "b4", "b5", "b5", "b5", "b6", "b6", "b6"],
                                             ["b4", "b4", "b4", "b5", "b5", "b5", "b6", "b6", "b6"],
                                             ["b4", "b4", "b4", "b5", "b5", "b5", "b6", "b6", "b6"],
                                             ["b7", "b7", "b7", "b8", "b8", "b8", "b9", "b9", "b9"],
                                             ["b7", "b7", "b7", "b8", "b8", "b8", "b9", "b9", "b9"],
                                             ["b7", "b7", "b7", "b8", "b8", "b8", "b9", "b9", "b9"]])
    
# test array of a complete and correct puzzle
solvedPuzzle = np.array([[8,2,9,4,3,1,6,5,7], 
                                       [4,6,7,5,8,9,2,1,3],
                                       [3,5,1,2,6,7,9,8,4],
                                       [7,1,6,8,4,2,3,9,5],
                                       [5,3,2,1,9,6,4,7,8],
                                       [9,8,4,7,5,3,1,6,2],
                                       [1,4,3,6,7,5,8,2,9],
                                       [6,9,5,3,2,8,7,4,1],
                                       [2,7,8,9,1,4,5,3,6]])   
# solvedPuzzle with elements removed                                   
puzzle = np.array([[8,2,0,0,0,1,6,0,7], 
                             [0,6,7,5,0,9,2,0,0],
                             [3,0,0,0,6,0,9,0,0],
                             [0,1,0,0,0,0,3,9,5],
                             [0,0,2,0,0,0,4,0,0],
                             [9,8,4,0,0,0,0,6,0],
                             [0,0,3,0,7,0,0,0,9],
                             [0,0,5,3,0,8,7,4,0],
                             [2,0,8,9,0,0,0,3,6]])             

def gen_buckets(puzzle):
    ''' Generates a dictionary with bucket names as the keys.
        Each key has a list of the values present.
        Should be updated when adding values to the puzzle
    '''
    buckets = {}

    a = puzzle[0][0:3]
    b = puzzle[1][0:3]
    c = puzzle[2][0:3]
    bucket = np.concatenate([a,b,c])
    buckets["b1"] = bucket

    a = puzzle[0][3:6]
    b = puzzle[1][3:6]
    c = puzzle[2][3:6]
    bucket = np.concatenate([a,b,c])
    buckets["b2"] = bucket

    a = puzzle[0][6:9]
    b = puzzle[1][6:9]
    c = puzzle[2][6:9]
    bucket = np.concatenate([a,b,c])
    buckets["b3"] = bucket

    a = puzzle[3][0:3]
    b = puzzle[4][0:3]
    c = puzzle[5][0:3]
    bucket = np.concatenate([a,b,c])
    buckets["b4"] = bucket

    a = puzzle[3][3:6]
    b = puzzle[4][3:6]
    c = puzzle[5][3:6]
    bucket = np.concatenate([a,b,c])
    buckets["b5"] = bucket

    a = puzzle[3][6:9]
    b = puzzle[4][6:9]
    c = puzzle[5][6:9]
    bucket = np.concatenate([a,b,c])
    buckets["b6"] = bucket

    a = puzzle[6][0:3]
    b = puzzle[7][0:3]
    c = puzzle[8][0:3]
    bucket = np.concatenate([a,b,c])
    buckets["b7"] = bucket

    a = puzzle[6][3:6]
    b = puzzle[7][3:6]
    c = puzzle[8][3:6]
    bucket = np.concatenate([a,b,c])
    buckets["b8"] = bucket

    a = puzzle[6][6:9]
    b = puzzle[7][6:9]
    c = puzzle[8][6:9]
    bucket = np.concatenate([a,b,c])
    buckets["b9"] = bucket    
    
    return buckets
    
    # find a loop to generate this code...
    
def gen_possibilities():
    ''' Assigns a possibility matrix containing numbers 1-9 for each 
    x,y  coordinate.
    - returns a 3d numpy array   
    '''
    a = [1,2,3,4,5,6,7,8,9]
    poss =  np.array([[a for x in range(9)] for x in range(9)])
    
    return poss

def is_conflicting(val, x, y, buckets, puzzle):
    '''Checks any conflicts within the row n[0] and the columnn[1]
    - val is an int of which we are checking for instances of in the lists
    - n is a list of length 2
    returns True if the val conflicts in the lists, False otherwise
    '''
    bucket = bucket_locations[x][y]
    numberToCheck = puzzle[x][y]
    row = puzzle[x]
    col = puzzle[:, y]
    
    return val in row or val in col or val in buckets[bucket]

def trim_possibilities(x, y, poss, buckets, puzzle):
    '''Narrows down the possibility space for each coordinate.
      Calls is_conflicting for each possibility remaining in coordinate x,y.
      - returns nothing
    '''
    # if the number is already in the puzzle, set the possibilities to 0
    if puzzle[x][y] != 0 and len(set(poss[x][y])) not in [1,2]: 
        poss[x][y] = np.zeros(9, int)
        
    for n in range(9):
        # check if the number is an available slot in the puzzle or if the value has already been found
        if poss[x][y][n] == 0 or puzzle[x][y] != 0:
            continue
        # if there are no conflicts, continue to next iteration
        elif is_conflicting(poss[x][y][n], x, y, buckets, puzzle) == False:
            continue
        # otherwise, assign this value to 0 in order to ignore this possibility on the next pass
        else:
            poss[x][y][n] = 0
    
def add_to_puzzle(puzzle, poss):
    '''Adds possibilities where there is only one nonzero number remaining
    to the puzzle'''
    for x in range(9):        
        for y in range(9):
            if len(set(poss[x][y])) == 2:
                puzzle[x][y] = sum(poss[x][y])

    return puzzle
    
def trim_pass(puzzle, runs, poss, buckets):
    ''' Runs trim_possibilities runs amount of times '''
    
    runCount =  1
    for run in range(runs):
        print("Pass %d" %runCount)
        buckets = gen_buckets(puzzle)
        for x in range(9):        
            for y in range(9):
                trim_possibilities(x,y, poss, buckets, puzzle)
        puzzle = add_to_puzzle(puzzle, poss) 
        
        if 0 not in puzzle:
                return puzzle
        runCount += 1
    
    return puzzle
        
def print_possibilities(poss):
    for x in range(9):        
        for y in range(9):
            print("row ", x, "col ", y, " ", poss[x][y])

def run_solver(puzzle, solvedPuzzle):
    print("\nStarting puzzle state:\n", puzzle)
    puzzle = trim_pass(puzzle, 6, gen_possibilities(), gen_buckets(puzzle))
    print("\nFinished puzzle:", puzzle)            
    print("\nIs equal to solvedPuzzle:  \n", puzzle == solvedPuzzle)            