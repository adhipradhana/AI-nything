from src.chesspiece import index_valid
from src.chesspiece import Color
import src.chessboard
import src.chesspiece
import heapq
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

    def find_neighbour(chessboard, selected_piece):
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

        while step < limit and best_cost[0] > 0 :
            step += 1
            selected_piece = chessboard.list[random.randint(0, len(chessboard.list) - 1)]
            neighbour = find_neighbour(chessboard, selected_piece)
            while len(neighbour) > 0:
                selected_move = neighbour[random.randint(0, len(neighbour) - 1)]
                neighbour.remove(selected_move)
                
                init_x = selected_piece.x
                init_y = selected_piece.y
                chessboard.move(selected_piece, *selected_move)
                next_cost = chessboard.cost()

                if next_cost[0] < best_cost[0] and next_cost[1] >= best_cost[1]:
                    best_cost = next_cost

                if next_cost[0] < current_cost[0] and next_cost[1] >= current_cost[1]:
                    current_cost = next_cost
                    improve += 1
                    break
                else:
                    chessboard.move(selected_piece, init_x, init_y)

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
            return copy.deepcopy(new_result)
        elif best_result['best_cost'][0] >= new_result['best_cost'][0] and best_result['best_cost'][1] <= new_result['best_cost'][1]:
            return copy.deepcopy(new_result)
        else:
            return copy.deepcopy(best_result)

    # main
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n------------------- RANDOM-RESTART STOCHASTIC HILL CLIMBING ALGORITHM -------------------\n')
    trial = input('input trial amount: ')
    limit = int(input('input step limit: '))
    print('\n')
    success = 0
    for i in range(int(trial)):
        chessboard.randomize()
        current_result = solve_hill_climbing(chessboard, limit)
        if current_result['best_cost'][0] == 0:
            success += 1
        best_result = update_best_result(current_result)
        print(str(round((current_result['time_elapsed'] * 1000), 4)) + ' ms' + ', cost: ' + str(current_result['best_cost']))
    success_rate = round((success / int(trial)), 4)

    # print result
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Total trial(s):   {}'.format(trial))
    print('Solution found:   {} times'.format(success))
    print('Success rate:     {} %'.format(success_rate * 100))
    print('\nBest result:')
    best_result['chessboard'].print()
    print('  * best cost:    {}'.format(best_result['best_cost']))
    print('  * final cost:   {}'.format(best_result['final_cost']))
    print('  * total step:   {}'.format(best_result['step']))
    print('  * improvement:  {}'.format(best_result['improve']))
    print('  * elapsed time: {} ms'.format(best_result['time_elapsed'] * 1000))
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def genetic_algorithm(chessboard, generation, mutation_percentage):
    """ Genetic Algorithm for solving N-ything problem
    
    :param chessboard : Initial state of the chessboard
    :param generation : Number of steps before the algorithm stops
    :param mutation_percentage : Percentage of gene mutation 

    # I.S. : Random chessboard
    # F.S. : Chessboard at global maximum/minimum
    """
    start_time = time.time()

    ### GLOBAL VARIABLE FOR THIS FUNCTION ###
    # dynamic programming approach for fitness scores
    fitness_scores = []

    # save list length
    chestpiece_length = len(chessboard.list)

    # get white and black count
    white_count = 0
    for chesspice in chessboard.list:
        if chesspice.color == Color.WHITE: # color white
            white_count += 1

    black_count = chestpiece_length - white_count

    def create_population():
        """ Create a 4 random chromosome from the chessboard """

        # Initiate empty population 
        population = []

        for i in range (4) :
            chromosome = []

            for j in range(len(chessboard.list)):
                position = (random.randint(0,7), random.randint(0,7))

                while position in chromosome:
                    position = (random.randint(0,7), random.randint(0,7))

                chromosome.append(position)

            population.append(chromosome)

        return population

    def fitness(chromosome):
        """ 
        Fitness function is for selecting chromosome to generate new chromosome
        maximum_defense = Sum of Combination(number of chestpiece, 2) by color
        defense = number of non attacking chestpiece with same color
        attack = number of attackung chestpiece with same color

        Returns fitness function
        """
        maximum_defense = (white_count * (white_count - 1) / 2) + (black_count * (black_count - 1) / 2)

        for i in range (chestpiece_length):
            chessboard.list[i].x = chromosome[i][0]
            chessboard.list[i].y = chromosome[i][1]

        defense, attack = chessboard.cost()

        return (maximum_defense - defense + attack) ** 2

    def fitness_percentage(population):
        """
        Returns list of fitness percentage of chromosome
        """
        for i in range(len(fitness_scores), len(population)):
            score = fitness(population[i])
            fitness_scores.append(score)

        total_scores = sum(fitness_scores)

        # for initiating map
        first_percentage = score / total_scores

        # initiate this with first element 
        largest_percentages = [
            (first_percentage, 0), (first_percentage, 0), (first_percentage, 0)
        ]

        # get 3 largest element
        for i in range(1, len(fitness_scores)):
            percentage = fitness_scores[i] / total_scores
            if percentage > largest_percentages[0][0]:
                largest_percentages[0] = (percentage, i)
            elif percentage > largest_percentages[1][0]:
                largest_percentages[1] = (percentage, i)
            elif percentage > largest_percentages[2][0]:
                largest_percentages[2] = (percentage, i)

        return largest_percentages

    def select_chromosome(population):
        """
        Selecting chromosome for crossover
        """
        # get 3 largest fitness score from population
        largest_percentages = fitness_percentage(population)

        # get 3 largest index
        largest_index = [largest_percentages[0][1], largest_percentages[1][1], largest_percentages[2][1]]

        return largest_index

    def crossbreed(population):
        """
        Crossbreed chromosome to create new chromosome
        """
        # select largest chromosome
        largest_index = select_chromosome(population)

        # choose pivot point (for this case the middle)
        pivot = chestpiece_length // 2

        # create breed from first largest and second largest
        sub_chromosome_1 = population[largest_index[0]][0:pivot]
        sub_chromosome_2 = population[largest_index[1]][pivot:chestpiece_length]

        new_chromosome_1 = sub_chromosome_1 + sub_chromosome_2
        mutation(new_chromosome_1, mutation_percentage)

        population.append(new_chromosome_1)

        # create bree from first largest and third largest
        sub_chromosome_1 = population[largest_index[2]][0:pivot]
        sub_chromosome_2 = population[largest_index[0]][pivot:len(chessboard.list)]

        new_chromosome_2 = sub_chromosome_1 + sub_chromosome_2
        mutation(new_chromosome_2, mutation_percentage)

        population.append(new_chromosome_2)


    def mutation(chromosome, mutation_percentage):
        """
        Mutate some gen after crossbreed
        """
        # random mutation probability
        probability = random.randint(0,100)

        # probability fulfilled
        if probability < mutation_percentage:
            index = random.randint(0, len(chromosome) - 1)
            x = random.randint(0,7)
            y = random.randint(0,7)

            chromosome[index] = (x,y)


    # create iniitial population population
    population = create_population()

    # iteration algorithm
    for i in range (generation) :
        print("iteration " + str(i))
        crossbreed(population)

    # select largest chromosome
    largest_index = select_chromosome(population)
    chromosome = population[largest_index[0]]

    # assign to chessboard
    for i in range (chestpiece_length):
        chessboard.list[i].x = chromosome[i][0]
        chessboard.list[i].y = chromosome[i][1]

    # print chessboard
    chessboard.print()
    defense, attack = chessboard.cost()

    print("Number of attack : " + str(attack))
    print("Number of defense : " + str(defense))
    
    end_time = time.time() - start_time
    print("elapsed time : " + str(end_time))



