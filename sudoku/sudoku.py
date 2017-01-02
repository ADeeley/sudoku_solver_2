import numpy as np

# references for the buckets so a set of coordinates can be associated with 
# a single bucket

# generate the unique square IDs


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
   

























   
solvedPuzzle = "829431657467589213351267984716842395532196478984753162143675829695328741278914536"                                     
puzzle = "820001607067509200300060900010000395002000400984000060003070009005308740208900036"
puzzleList = [n for n in puzzle]
solvedPuzzleList = [n for n in solvedPuzzle]
"""
820001607
067509200
300060900
010000395
002000400
984000060
003070009
005308740
208900036
"""

    
digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
[cross(r, cols) for r in rows] +
[cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)
poss = dict((a, {str(x) for x in range(1,10)}) for a in squares)
references = assign_refs_to_squares(puzzleList, squares)
peerValues = assign_peers_to_values(references, peers, squares)

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

def assign_refs_to_squares(puzzleList, squares):
    "Returns a dictionary of squares to values. Should be updated every run."
    return dict((s, puzzleList[squares.index(s)])for s in squares)
    
def assign_peers_to_values(references, peers, squares):
    """Returns a dictionary of peers, with each key a square and each value
    a set of the unique peer values."""
    peerValues = {}
    #print("\n\nReferences: ", references, "\n\nPeers: ", peers, "\n\nSquares :", squares)
    for p in squares: # gets the reference
        vals = set({})
        for s in peers[p]:
            vals.add(references[s])
        peerValues[p] = (vals)
    
    assert len(peerValues) == 81, "List must be of len 81"
    assert type(peerValues["A1"]) == set, "List element 0 not of type set"
    assert type(peerValues["I9"]) == set, "List element 80 not of type set"
    
    return peerValues


#iterate over the possibilites and remove any that conflict
def update_possibilities(squares, peerValues, poss):
    "Updates the possibility sets for each square."
    for square in squares:
        poss[square].difference_update(peerValues[square])
        assert len(poss) == 81
    
    return poss

def add_to_puzzle(squares, puzzleList):
    for square in squares:
        if len(poss[square]) == 1:
            puzzleList[squares.index(square)] = "".join(poss[square])
            poss[square].clear()

def run_solver(runs, peerValues, poss, references):            
    for run in range(runs):
        poss = update_possibilities(squares, peerValues, poss)
        add_to_puzzle(squares, puzzleList)  
        references = assign_refs_to_squares(puzzleList, squares)
        peerValues = assign_peers_to_values(references, peers, squares)
        
    assert solvedPuzzleList == puzzleList
    print(puzzleList)
    
run_solver(5, peerValues, poss, references)