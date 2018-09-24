from src.chesspiece import index_valid
from src.chesspiece import Color
import numpy as np
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


def genetic_algorithm(chessboard):
    """ Genetic Algorithm for solving N-ything problem
    
    :param chessboard : Initial state of the chessboard
    :param generation : Number of steps before the algorithm stops
    :param mutation_percentage : Percentage of gene mutation 

    # I.S. : Random chessboard
    # F.S. : Chessboard at global maximum/minimum
    """

    def create_population(population_size):
        """ Create random chromosome from the chessboard """

        # Initiate empty population 
        population = []

        for i in range (population_size) :
            chromosome = []

            for j in range(len(chessboard.list)):
                gene = (random.randint(0,7), random.randint(0,7))

                while gene in chromosome:
                    gene = (random.randint(0,7), random.randint(0,7))

                chromosome.append(gene)

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
        maximum_defense = (white_count * (white_count - 1)) + (black_count * (black_count - 1))

        for i in range (chestpiece_length):
            chessboard.list[i].x = chromosome[i][0]
            chessboard.list[i].y = chromosome[i][1]

        defense, attack = chessboard.cost()

        return (maximum_defense - defense + attack) ** 2

    def fitness_percentage(population):
        """
        Returns list of fitness percentage of chromosome
        """
        fitness_scores = []
        for chromosome in population:
            score = fitness(chromosome)
            fitness_scores.append(score)

        total_scores = sum(fitness_scores)

        percentages = []
        # get 3 largest element
        for score in fitness_scores:
            percentage = score / total_scores
            percentages.append(percentage)

        return percentages

    def select_chromosome(population_index, percentages):
        """
        Selecting chromosome for crossover
        """
        first_index = np.random.choice(population_index, p = percentages)
        second_index = np.random.choice(population_index, p = percentages)

        while second_index == first_index:
            second_index = np.random.choice(population_index, p = percentages)

        return (first_index, second_index)

    def crossbreed(chromosome_1, chromosome_2):
        """
        Crossbreed chromosome to create new chromosome
        """
        # choose pivot point (for this case the middle)
        pivot = random.randint(0, chestpiece_length - 1)

        # create breed from first largest and second largest
        sub_chromosome_1 = chromosome_1[0:pivot]
        sub_chromosome_2 = chromosome_2[pivot:chestpiece_length]

        new_chromosome = sub_chromosome_1[:]
        for gene in sub_chromosome_2:
            while gene in new_chromosome:
                gene = (random.randint(0,7), random.randint(0,7))
            new_chromosome.append(gene)

        return new_chromosome


    def mutation(chromosome, mutation_percentage):
        """
        Mutate some gen after crossbreed
        """
        # random mutation probability
        probability = random.randint(0,100)

        # probability fulfilled
        if probability < mutation_percentage:
            index = random.randint(0, len(chromosome) - 1)

            (x, y) = (random.randint(0,7), random.randint(0,7))
            while (x,y) in chromosome:
                (x, y) = (random.randint(0,7), random.randint(0,7))

            chromosome[index] = (x,y)

    def create_generation(population, population_index, population_size, mutation_percentage):
        """
        One iteration of population crossbreed
        """
        # get percentage of population
        percentages = fitness_percentage(population)

        new_population = []
        # crossbreed as many as population size
        for i in range(population_size):
            # select chromosome for crossbreed
            chromosome_index_1, chromosome_index_2 = select_chromosome(population_index, percentages)

            chromosome_1 = population[chromosome_index_1]
            chromosome_2 = population[chromosome_index_2]

            new_chromosome = crossbreed(chromosome_1, chromosome_2)
            new_population.append(new_chromosome)

        mutation_index = random.randint(0, population_size - 1)
        mutation(new_population[mutation_index], mutation_percentage)

        population = new_population

    def select_best_result(population):
        """
        Select best result from population
        """
        fitness_scores = []
        for chromosome in population:
            score = fitness(chromosome)
            fitness_scores.append(score)

        best_index = fitness_scores.index(max(fitness_scores))

        return population[best_index]


    # get population size
    population_size = int(input("Enter population size : "))
    generation = int(input("Enter number of generation : "))
    mutation_percentage = int(input("Enter probability of mutation (0-100) : "))

    # start program
    start_time = time.time()

    # index of population
    population_index = list(range(0, population_size))

    # save list length
    chestpiece_length = len(chessboard.list)

    # get white and black count
    white_count = 0
    for chesspice in chessboard.list:
        if chesspice.color == Color.WHITE: # color white
            white_count += 1

    black_count = chestpiece_length - white_count

    # create iniitial population population
    population = create_population(population_size)

    # iteration algorithm
    for i in range (generation) :
        print("iteration " + str(i))
        create_generation(population, population_index, population_size, mutation_percentage)

    # select best chromosome
    chromosome = select_best_result(population)

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



