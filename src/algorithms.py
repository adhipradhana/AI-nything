from src.chesspiece import index_valid
from math import exp
import src.chessboard
import src.chesspiece
import time
import random
import copy

def hill_climbing(chessboard):
    """ Random-restart Stochastic Hill Climbing algorithm function for N-ything problem

    :param chessboard: initial state of the chessboard

    # I.S : random chessboard
    # F.S : chessboard at global/local maximum
    """
    best_result = {}

    def find_neighbour(chessboard):
        """ function to find valid adjacent move

        :param chessboard: current state of the chessboard
        :param selected_piece: randomly selected piece
        :return: list of valid adjacent move
        """
        valid_neighbour = []
        for x in range(0,8):
            for y in range(0,8):
                if chessboard.grid[x][y] is None:
                    valid_neighbour.append([x,y])
        return valid_neighbour


    def solve_hill_climbing(chessboard):
        """ function to solve a chessboard

        :param chessboard: initial chessboard state
        :return: solution chessboard, best cost, time elapsed, and how many step
        """
        best_cost = [99999,-1]
        current_cost = chessboard.cost()
        step = 0
        start_time = time.time()
        no_better_moves = False

        # run until no better moves
        while not no_better_moves:
            better_moves_found = False
            step += 1
            list_piece = list(range(0,len(chessboard.list)))
            while len(list_piece) > 0 and not better_moves_found:

                random_number = random.randint(0, len(chessboard.list) - 1)
                while(random_number not in list_piece):
                    random_number = random.randint(0, len(chessboard.list) - 1)

                selected_piece = chessboard.list[random_number]
                list_piece.remove(random_number)

                neighbour = find_neighbour(chessboard)
                while len(neighbour) > 0 and not better_moves_found:
                    selected_move = neighbour[random.randint(0, len(neighbour) - 1)]
                    neighbour.remove(selected_move)

                    init_x = selected_piece.x
                    init_y = selected_piece.y
                    # print("{} {} init".format(selected_piece.x,selected_piece.y))
                    chessboard.move(selected_piece, *selected_move)
                    # print("{} {} moved".format(selected_piece.x,selected_piece.y))
                    next_cost = chessboard.cost()

                    if (next_cost[0] < best_cost[0] and next_cost[1] >= best_cost[1]) or (next_cost[0] <= best_cost[0] and next_cost[1] > best_cost[1]):
                        best_cost = next_cost

                    if (next_cost[0] < current_cost[0] and next_cost[1] >= current_cost[1]) or (next_cost[0] <= current_cost[0] and next_cost[1] > current_cost[1]):
                        current_cost = next_cost
                        better_moves_found = True
                    else:
                        chessboard.move(selected_piece, init_x, init_y)

            if not better_moves_found:
                no_better_moves = True

        time_elapsed = time.time() - start_time
        result = {
            "best_cost": best_cost,
            "time_elapsed": time_elapsed,
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
            return copy.deepcopy(new_result)

        elif (best_result['best_cost'][0] > new_result['best_cost'][0] and best_result['best_cost'][1] <= new_result['best_cost'][1]) or (best_result['best_cost'][0] >= new_result['best_cost'][0] and best_result['best_cost'][1] < new_result['best_cost'][1]):
            return copy.deepcopy(new_result)
        else:
            return best_result

    # main
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n------------------- RANDOM-RESTART STOCHASTIC HILL CLIMBING ALGORITHM -------------------\n')
    restart = input('input total restart(s): ')
    success = 0
    for i in range(int(restart)):
        chessboard.randomize()
        current_result = solve_hill_climbing(chessboard)
        if current_result['best_cost'][0] == 0:
            success += 1
        best_result = update_best_result(current_result)
        print(str(round((current_result['time_elapsed'] * 1000), 4)) + ' ms' + ', cost: ' + str(current_result['best_cost']))
    success_rate = round((success / int(restart)), 4)

    # print result
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Total restart(s):   {}'.format(restart))
    # print('Solution found:   {} times'.format(success))
    # print('Success rate:     {} %'.format(success_rate * 100))
    print('\nBest result:')
    best_result['chessboard'].print()
    print('{} {}'.format(best_result['best_cost'][0],best_result['best_cost'][1]))
    print('  * best cost:    {}'.format(best_result['best_cost']))
    print('  * total step:   {}'.format(best_result['step']))
    print('  * elapsed time: {} ms'.format(best_result['time_elapsed'] * 1000))
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def simulated_annealing(chessboard):
	"""
	Simulated Annealing algorithm for solving N-ything problem

	note: using linear decrease for temperature with gradient user-specified per 100 steps.

	params:	chessboard: chessboard 	-> initial state of chessboard

	I.S. 	: random chessboard, init_temp specified
	F.S.	: chessboard at/near global maximum

	"""

	def find_neighbour(chessboard, selected_piece):
		"""
		Find valid adjacent move

		params:	chessboard: chessboard 		-> current state of the chessboard
				selected_piece: chesspiece 	-> randomly selected piece

		return: list of valid adjacent move

		"""
		valid_neighbour = []
		for x in range(0,8):
			for y in range(0,8):
				if chessboard.grid[x][y] is None:
					valid_neighbour.append([x,y])
		return valid_neighbour

	def select_random_neighbour(neighbour_list):
		"""
		Select a random neighbour from neighbours list

		params:	neightbour_list: list of neighbour

		raturn: selected_neighbour: neighbour

		"""
		return neighbour_list[random.randint(0, len(neighbour_list) - 1)]

	def choose_current_path(move_cost, best_cost, temperature):
		"""
		Selecting current move as best move with probability calculated using Boltzman Distribution

		params: move_cost: int,int		-> to-be-selected current move cost
				best_cost: int,int 		-> current best move cost
				temperature: int		-> current temperature

		return: choose current move? boolean

		"""
		if (best_cost == None) or ((move_cost[0] <= best_cost[0]) and (move_cost[1] >= best_cost[1])):
			return True
		else:
			probability_0 = min(exp((best_cost[0] - move_cost[0]) / temperature), 1)
			probability_1 = min(exp((move_cost[1] - best_cost[1]) / temperature), 1)
			avg_probability = (probability_0 + probability_1) / 2 if (probability_1 != 0) else probability_0
			return True if (avg_probability > 0.7) else False

	def execute_iteration(chessboard, best_cost, temperature):
		"""
		Do an iteration of the program using simulated annealing

		params: chessboard: chessboard
				best_cost: int, int 	-> current best move cost
				temperature: int 		-> current temperature
		"""
		start_time = time.time()
		for i in range(100):

			selected_piece = chessboard.list[random.randint(0, len(chessboard.list) - 1)]
			init_x = selected_piece.x
			init_y = selected_piece.y

			neighbours_list = find_neighbour(chessboard, selected_piece)
			selected_neighbour = select_random_neighbour(neighbours_list)
			chessboard.move(selected_piece, *selected_neighbour)

			selected_cost = chessboard.cost()
			if (choose_current_path(selected_cost, best_cost, temperature)):
				best_cost = selected_cost
			else:
				chessboard.move(selected_piece, init_x, init_y)
		end_time = time.time()

		print(chr(27) + "[2J")
		chessboard.print()
		print(str(round(((end_time - start_time) * 1000), 4)) + ' ms' + ', Cost: ' + str(best_cost) + ', Temperature: ' + str(temperature))

		return copy.deepcopy(best_cost)


	#Main
	print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('\n------------------- SIMULATED ANNEALING ALGORITHM -------------------\n')
	chessboard.print()
	print("Initial cost: {}".format(chessboard.cost()))
	init_temp = float(input("Input initial temperature: "))
	temp_dec_gradient = float(input("Input temperature decrease gradient: "))
	best_cost = [999999, 0]
	curr_temp = init_temp

	start_time = time.time()

	iteration = 0
	while (curr_temp > 0.001):
		iteration += 1
		best_cost = execute_iteration(chessboard, best_cost, curr_temp)
		curr_temp = init_temp - (iteration*temp_dec_gradient)

	end_time = time.time()

	# print result

	print('\n')
	print(chr(27) + "[2J")
	chessboard.print()
	print('Total trial(s):   {}'.format(iteration * 100))
	print('\nBest result:')
	print('  * best cost:    {}'.format(best_cost))
	print('  * elapsed time: {} ms'.format((end_time - start_time) * 1000))
	print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
