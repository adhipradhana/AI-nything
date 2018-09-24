import ChessBoard
from chesspiece import index_valid
from math import exp


def hill_climbing(chessboard):
    """ Stochastic Hill Climbing algorithm function for N-ything problem
    
    :param chessboard: initial state of the chessboard

    # I.S : random chessboard
    # F.S : chessboard at global/local maximum
    """
    best_result = {}

    def find_neighbour(chessboard, selected_piece):
        """ function to find valid adjacent move

        :param chessboard: current state of the chessboard
        :param selected_piece: randomly selected piece
        :return: list of valid adjacent move
        """
        valid_neighbour = []
        movement = [ [0,1] , [1,1] , [1,0] , [1,-1] , [0,-1] , [-1,-1] , [-1,0] , [-1,1] ]
        for inc_x, inc_y in movement:
            new_x = selected_piece.x + inc_x
            new_y = selected_piece.y + inc_y
            if index_valid(new_x,new_y):
                if chessboard.grid[new_x][new_y] is None::
                    valid_neighbour.append([new_x,new_y])
        return valid_neighbour


    def solve_hill_climbing(chessboard, limit):
        """ function to solve a simulated algorithm once, step limited

        :param chessboard: initial chessboard state
        :param limit: step limit
        :return: solution chessboard, best cost, final cost, time elapsed, how many step, and how many improvement from initial state
        """
        best_cost = [99999,-1]
        current_cost = chessboard.cost()
        step = 0
        improve = 0
        start_time = time.time()

        while step < limit && best_cost[0] > 0 :
            step += 1
            current_cost = chessboard.cost()
            selected_piece = chessboard.list[random.randint(0, len(chessboard.list) - 1)]
            neighbour = find_neighbour(selected_piece)
            while len(neighbour) > 0:
                selected_move = neighbour[random.randint(0, len(neighbour) - 1)]
                neighbour.remove(selected_move)

                next_cost = chessboard.seek_cost(selected_piece,*selected_move)
                
                if next_cost[0] < best_cost[0] && next_cost[1] > best_cost[1]:
                    best_cost = next_cost

                if next_cost[0] < current_cost[0] && next_cost[1] > current_cost[1]:
                    chessboard = chessboard.move(selected_piece,*selected_move)
                    current_cost = next_cost
                    improve += 1
                    break

        time_elapsed = time.time() - start_time
        result = {
            "best_cost": best_cost,
            "final_cost": current_cost,
            "time_elapsed": time_elapsed,
            "improve": improve,
            "step": step,
            "chessboard": chessboard
        }
        return result

    def update_best_result(new_result):
        """ update the value of best result

        :param new_result: a new result
        :return: the best result 
        """
        if len(best_result) == 0:
            return new_result
        elif best_result['best_cost'] > new_result['best_cost']:
            return new_result
        return best_result

    # main
    trial = input('input trial amount: ')
    limit = int(input('input step limit: '))
    success = 0
    for i in range(int(trial)):
        chessboard.randomize()
        current_result = solve_hill_climbing(chessboard, limit)
        if current_result['best_cost'] == 0:
            success += 1
        best_result = update_best_result(current_result)
        print(str(round((current_result['time_elapsed'] * 1000), 4)) + ' ms' + ', cost: ' + str(current_result['best_cost']))
    success_rate = round((success / int(trial)), 4)

    # print result
    print('\n')
    best_result['chessboard'].print()
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n------------------- STOCHASTIC HILL CLIMBING ALGORITHM -------------------\n')
    print('Total trial(s):   {}'.format(trial))
    print('Solution found:   {} times'.format(success))
    print('Success rate:     {} %'.format(success_rate * 100))
    print('\nBest result:')
    print('  * best cost:    {}'.format(best_result['best_cost']))
    print('  * final cost:   {}'.format(best_result['final_cost']))
    print('  * total step:   {}'.format(best_result['step']))
    print('  * improvement:  {}'.format(best_result['improve']))
    print('  * elapsed time: {} ms'.format(best_result['time_elapsed'] * 1000))
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')




def simulated_annealing(chessboard):
	""" Simulated Annealing algorithm for solving N-ything problem

	note: using linear decrease for temperature with gradient user-specified per 100 steps.

	params:	chessboard: chessboard 	-> initial state of chessboard

	I.S. 	: random chessboard, init_temp specified
	F.S.	: chessboard at/near global maximum

	"""

	init_temp = input("Input initial temperature: ")
    temp_dec_gradient = input("Input temperature decrease gradient: ")
	best_cost = [999999, -1]
	curr_temp = init_temp

	def find_neighbour(chessboard, selected_piece):
        """ Find valid adjacent move

        params:	chessboard: chessboard 		-> current state of the chessboard
        		selected_piece: chesspiece 	-> randomly selected piece

        return: list of valid adjacent move

        """
        valid_neighbour = []
        movement = [ [0,1] , [1,1] , [1,0] , [1,-1] , [0,-1] , [-1,-1] , [-1,0] , [-1,1] ]
        for inc_x, inc_y in movement:
            new_x = selected_piece.x + inc_x
            new_y = selected_piece.y + inc_y
            if index_valid(new_x,new_y):
                if chessboard.grid[new_x][new_y] is None::
                    valid_neighbour.append([new_x,new_y])
        return valid_neighbour

    def select_random_neighbour(neighbour_list):
    	""" Select a random neighbour from neighbours list

    	params:	neightbour_list: list of neighbour

    	raturn: selected_neighbour: neighbour

    	"""
    	return neighbour_list[random.randint(0, len(neighbour_list) - 1)]

    def choose_current_path(move_cost, best_cost, temperature):
    	""" Selecting current move as best move with probability calculated using Boltzman Distribution

    	params: move_cost: int 		-> to-be-selected current move cost
    			best_cost: int 		-> current best move cost
    			temperature: int	-> current temperature

    	return: choose current move? boolean

    	"""
    	if (best_cost == None) || ((move_cost[0] <= best_cost[0]) && (move_cost[1] >= best_cost[1])) :
    		return True
    	else:
    		probability_0 = min(exp((best_cost[0] - move_cost[0]) / temperature), 1)
    		probability_1 = min(exp((move_cost[1] - best_cost[1]) / temperature), 1)
    		avg_probability = (probability_0 + probability_1) / 2
    		return random.choices([True, False], cum_weights = [avg_probability, 1-avg_probability], k = 1)[0]

    #Main
    start_time = time.time()
    j = 0
    iteration = 0
    while (curr_temp > 0):
    	j += 1
    	for i in range(100):
    		iteration += 1
    		print("Iteration ", iteration)
    		selected_piece = chessboard.list[random.randint(0, len(chessboard.list) - 1)]
    		neighbours_list = find_neighbour(selected_piece)
    		selected_neighbour = select_random_neighbour(neighbours_list)
    		selected_cost = chessboard.seek_cost(selected_piece, *selected_neighbour)
    		if (choose_current_path(selected_cost, best_cost, curr_temp)):
    			chessboard = chessboard.move(selected_piece, *selected_neighbour)
    	curr_temp = init_temp - j*temp_dec_gradient
    end_time = time.time()

 	# print result
    print('\n')
    chessboard.print()
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n------------------- SIMULATED ANNEALING ALGORITHM -------------------\n')
    print('Total trial(s):   {}'.format(iteration))
    print('\nBest result:')
    print('  * best cost:    {}'.format(best_cost))
    print('  * final cost:   {}'.format(final_cost))
    print('  * elapsed time: {} ms'.format((end_time - start_time) * 1000))
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')



