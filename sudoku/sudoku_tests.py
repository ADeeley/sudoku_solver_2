from sudoku import *

# ---------------------- test 1 -----------------------

solution = np.array([[9,8,3,4,5,7,6,2,1], 
                              [1,6,7,2,8,9,3,5,4],
                              [2,5,4,3,6,1,8,9,7],
                              [8,1,5,7,9,4,2,3,6],
                              [4,7,6,5,3,2,1,8,9],
                              [3,2,9,6,1,8,4,7,5],
                              [5,9,8,1,4,3,7,6,2],
                              [6,4,2,8,7,5,9,1,3],
                              [7,3,1,9,2,6,5,4,8]])
              
unsolved = np.array([[0,0,0,4,5,7,0,2,1], 
                               [1,6,0,0,0,0,0,5,4],
                               [0,5,0,0,6,1,0,0,7],
                               [0,0,5,7,9,4,0,3,6],
                               [4,7,6,0,0,0,1,8,0],
                               [0,2,0,6,1,0,4,7,5],
                               [5,0,0,0,4,0,0,6,2],
                               [6,0,2,0,0,5,0,0,3],
                               [7,3,0,0,0,0,5,4,0]])   

poss = gen_possibilities()
buckets = gen_buckets(unsolved)
trim_pass(unsolved,3, poss, buckets)
#print_possibilities()
print(solution, "\n\n", unsolved)            
print("Is equal to control:  \n", unsolved == solution)      
print_possibilities(poss)

     
# ---------------------- test 2 -----------------------
def test_2():
    solution = np.array([[8,2,9,4,3,1,6,5,7], 
                                   [4,6,7,5,8,9,2,1,3],
                                   [3,5,1,2,6,7,9,8,4],
                                   [7,1,6,8,4,2,3,9,5],
                                   [5,3,2,1,9,6,4,7,8],
                                   [9,8,4,7,5,3,1,6,2],
                                   [1,4,3,6,7,5,8,2,9],
                                   [6,9,5,3,2,8,7,4,1],
                                   [2,7,8,9,1,4,5,3,6]])   
                                   
    unsolved = np.array([[8,2,0,0,0,1,6,0,7], 
                                    [0,6,7,5,0,9,2,0,0],
                                    [3,0,0,0,6,0,9,0,0],
                                    [0,1,0,0,0,0,3,9,5],
                                    [0,0,2,0,0,0,4,0,0],
                                    [9,8,4,0,0,0,0,6,0],
                                    [0,0,3,0,7,0,0,0,9],
                                    [0,0,5,3,0,8,7,4,0],
                                    [2,0,8,9,0,0,0,3,6]])
          
    poss = gen_possibilities()
    buckets = gen_buckets(unsolved)
    trim_pass(30, poss, buckets)
    #print_possibilities()
    print(unsolved)            
    print("Is equal to control:  \n", unsolved == solution)      
    print_possibilities(poss)
    