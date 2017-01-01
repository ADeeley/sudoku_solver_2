from sudoku import *
import unittest
import numpy as np



class TestUnits(unittest.TestCase):
    unsolved = np.array([[9,0,0,3,7,0,0,1,0],
                        [6,2,0,0,9,0,0,0,0],
                        [0,0,1,0,0,0,4,0,8],
                        [0,0,0,5,3,0,0,0,0],
                        [3,9,0,6,0,7,0,4,5],
                        [0,0,0,0,1,4,0,0,0],
                        [5,0,3,0,0,0,8,0,0],
                        [0,0,0,0,4,0,0,5,3],
                        [0,6,0,0,5,3,0,0,4]])   
                
    solution = np.array([[9,5,4,3,7,8,6,1,2],
                    [6,2,8,4,9,1,5,3,7],
                    [7,3,1,2,6,5,4,9,8],
                    [4,1,6,5,3,2,7,8,9],
                    [3,9,2,6,8,7,1,4,5],
                    [8,7,5,9,1,4,3,2,6],
                    [5,4,3,7,2,9,8,6,1],
                    [2,8,7,1,4,6,9,5,3],
                    [1,6,9,8,5,3,2,7,4]]) 
    buckets = gen_buckets(unsolved)
    
    def test_gen_buckets(self):
        
        self.assertEqual(sum(self.buckets["b1"]), 18)
        self.assertEqual(sum(self.buckets["b3"]), 13)
        self.assertEqual(sum(self.buckets["b7"]), 14)
        self.assertEqual(sum(self.buckets["b9"]), 20)

    
    def test_gen_possibilities(self):
        a = [1,2,3,4,5,6,7,8,9]
        poss =  np.array([[a for x in range(9)] for x in range(9)])
        self.assertEqual(sum(poss[0][0]), sum(gen_possibilities()[0][0]))
        self.assertEqual(sum(poss[8][8]), sum(gen_possibilities()[8][8]))
        self.assertEqual(sum(poss[0][8]), sum(gen_possibilities()[0][8]))
        self.assertEqual(sum(poss[8][0]), sum(gen_possibilities()[8][0]))
     
    def test_is_conflicting(self):
        self.assertTrue(is_conflicting(3, 0,0 , self.buckets, self.unsolved))
        self.assertFalse(is_conflicting(2, 0,8 , self.buckets, self.unsolved))
        self.assertFalse(is_conflicting(2, 8,0 , self.buckets, self.unsolved))
        self.assertFalse(is_conflicting(9, 8,8 , self.buckets, self.unsolved))

    def test_trim_possibilities(self):
        a = [1,2,3,4,5,6,7,8,9]

        poss =  np.array([[a for x in range(9)] for x in range(9)])
        x = trim_possibilities(0, 0, poss, gen_buckets(s), self.unsolved)
        self.assertEqual(np.count_nonzero(poss[0][0]), 0)
        
        poss =  np.array([[a for x in range(9)] for x in range(9)])
        x = trim_possibilities(1, 3, poss, gen_buckets(s), self.unsolved)
        self.assertTrue(len(set(np.array(poss[1][3]))) == 2)

    def test_add_to_puzzle(self):
        poss = self.solution
        add_to_puzzle(self.unsolved, poss)
        
        
class general_tests():       
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
    
    def test_1(self, unsolved):
  

        poss = gen_possibilities()
        buckets = gen_buckets(self.unsolved)
        solved = trim_pass(self.unsolved, 10, poss, buckets)
        #print_possibilities()
        # print("Test 1\n", unsolved, "\n\n", solved)            
        # print("Is equal to control:  \n", unsolved == solved)      


         
    def test_2(self):              
        poss = gen_possibilities()
        buckets = gen_buckets(self.unsolved)
        solved = trim_pass(self.unsolved, 10, poss, buckets)
        #print_possibilities()
        # print("Test 2\n", unsolved, "\n\n", solved)            
        # print("Is equal to control:  \n", unsolved == solved)      

  
if __name__ == '__main__':
    unittest.main()