def find_next_empty(puzzle): 
	#finds the next row, col on the puzzle that's not filled in yet 
	#return row, col tuple (or {None, None} if there is none)


	#0-8 for indices 

	for r in range(9): 
		for c in range(9): 
			if puzzle[r][c] == -1:
				return r, c 

	return None, None    #if no spaces in puzzle are empty or everything is solved 


def is_valid(puzzle, guess, row, col): 
	#figures out whether the guess at the row/col of the puzzle is a valid guess 

	#return true if it works, return false if it does not work 

	row_vals = puzzle[row] 
	if guess in row_vals: 
		return False

	col_vals = []
	for i in range(9): 
		col_vals.append(puzzle[i][col]) 

	if guess in col_vals:
		return False

	#and then the the 3x3 square matrix  
	#this is tricky  
 	
	row_start = (row//3)*3 
	column_start = (col//3)*3 

	for r in range(row_start, row_start + 3):
 		for c in range(column_start, column_start + 3): 
				if (guess == puzzle[r][c]):
					return False 

	return True  

 	



def solve_sudoku_main(puzzle): 

	#solve sudoku using backtracking technique  

	#return wheter a solution exists  

	#step 1: choose  

	row, col = find_next_empty(puzzle) 

	if row is None: 			#if there are no spaces in puzzle empty (its solved)
		return True 

	#step 2: if there is a place to put a number, then make a guess between 1 and 9

	for guess in range(1, 10):  

		if is_valid(puzzle, guess, row, col): #if this is true then place the guess on the empty space of the puzzle   

			puzzle[row][col] = guess 

			if solve_sudoku_main(puzzle):
				return True  


	#if valid check is not valid OR if the sudoku is not solved with the guess 
	#backtrack and try a new number 

		puzzle[row][col] = -1  #reset the value at that empty location 

	#step 6: if none of the numbers work then the sudoku is unsolvable 

	return False 


if __name__== '__main__': 

	example_board = [

	[-1,-1,6,  1,-1,-1,  3,4,5],
	[8,-1,1,  -1,4,-1,   7,2,-1],
	[-1,-1,3,  6,-1,2,   8,9,1 ], 

	[5,6,-1,   -1,2,-1,   9,1,3], 
	[3,4,2,    -1,-1,9,   -1,8,7], 
	[-1,-1,7,  3,-1,-1,   -1,-1,-1], 

	[-1,8,-1,  -1,-1,1,   4,7,-1],
	[-1,1,-1,   4,6,7,    -1,-1,-1],
	[-1,-1,-1,  -1,-1,-1,  -1,-1,-1]
	]

	print(solve_sudoku_main(example_board))
	print(example_board)






			



