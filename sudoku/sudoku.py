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