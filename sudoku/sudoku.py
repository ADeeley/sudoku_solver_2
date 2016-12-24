import numpy as np

# ----- Unique test values ----------
# s = np.arange(81) # arrange has US spelling...
# s = s.reshape(9,9)

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
s = np.array([[9,8,3,4,5,7,6,2,1], 
              [1,6,7,2,8,9,3,5,4],
              [2,5,4,3,6,1,8,9,7],
              [8,1,5,7,9,4,2,3,6],
              [4,7,6,5,3,2,1,8,9],
              [3,2,9,6,1,8,4,7,5],
              [5,9,8,1,4,3,7,6,2],
              [6,4,2,8,7,5,9,1,3],
              [7,3,1,9,2,6,5,4,8]])
print(s)        


# ---- Uncomment this to run ----------
# s = np.zeros(81)
# s = s.reshape(9,9)

def gen_buckets(s):
    ''' Generates 9*(3*3) buckets to check values '''
    buckets = {}

    a = s[0][0:3]
    b = s[1][0:3]
    c = s[2][0:3]
    bucket = np.concatenate([a,b,c])
    buckets["b1"] = bucket

    a = s[0][3:6]
    b = s[1][3:6]
    c = s[2][3:6]
    bucket = np.concatenate([a,b,c])
    buckets["b2"] = bucket

    a = s[0][6:9]
    b = s[1][6:9]
    c = s[2][6:9]
    bucket = np.concatenate([a,b,c])
    buckets["b3"] = bucket

    a = s[3][0:3]
    b = s[4][0:3]
    c = s[5][0:3]
    bucket = np.concatenate([a,b,c])
    buckets["b4"] = bucket

    a = s[3][3:6]
    b = s[4][3:6]
    c = s[5][3:6]
    bucket = np.concatenate([a,b,c])
    buckets["b5"] = bucket

    a = s[3][6:9]
    b = s[4][6:9]
    c = s[5][6:9]
    bucket = np.concatenate([a,b,c])
    buckets["b6"] = bucket

    a = s[6][0:3]
    b = s[7][0:3]
    c = s[8][0:3]
    bucket = np.concatenate([a,b,c])
    buckets["b7"] = bucket

    a = s[6][3:6]
    b = s[7][3:6]
    c = s[8][3:6]
    bucket = np.concatenate([a,b,c])
    buckets["b8"] = bucket

    a = s[6][6:9]
    b = s[7][6:9]
    c = s[8][6:9]
    bucket = np.concatenate([a,b,c])
    buckets["b9"] = bucket    
    
    return buckets
    
    # find a loop to generate this code...
    
def gen_possibilities():
    ''' Assigns a list from 1-9 for each coordinate '''
    a = [1,2,3,4,5,6,7,8,9]
    return [[a for x in range(9)] for x in range(9)]


def check_conflicts(val, n):
    '''Checks any conflicts within the row n[0] and the columnn[1]
    - val is an int of which we are checking for instances in the lists
    - n is a list of length 2
    returns True if the val is in the lists, False otherwise
    
    '''
    assert type(n) == list, "n not list. n provided is of type %s" % type(n)
    assert len(n) == 2, "n must be of length 2. n provided is of length %d" % len(n)
    
    bucket = bucket_locations[n[0]][n[1]]
    numberToCheck = s[n[0]][n[1]]
    row = s[n[0]]
    col = s[:, n[1]]
    print(bucket)
    return val in row or val in col or val in buckets[bucket]
    # add check bucket conflicts separately
    # convert n to two ints, c and r
    
    
# ------------------------check_conflicts tests ----------------------
poss = gen_possibilities()
print(poss[0][0][0] == 1)
print(poss[8][8][8] == 9)
print(poss[3][7][5] == 6)
print(poss[0][8][4] == 5)
print(poss[8][0][8] == 9)


buckets = gen_buckets(s)
# for x in range(1,10):
    # print(check_conflicts(x, [1,2]))
# print(check_conflicts(2, [1,1]))
# print(check_conflicts(2, [0,0]))
# print(check_conflicts(5, [8,8]))
# print(check_conflicts(2, [1,8]))
# print(check_conflicts(2, [8,1]))
# print(check_conflicts(2, [8,2]))


def trim_possibilities(n):
    '''Works in a similar way to check_conflicts, but narrows down the possibility
        space for each coordinate.
        Calls check_conflicts for each possibility remaining in coordinate n.
    - n is a list of length 2
    
    '''
    pass