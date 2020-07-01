import random
import numpy as np

def random_chromosome(queen_size): 
    return [ random.randint(1, queen_size) for i in range(queen_size) ]

def fitness(chromosome):
    horizontal_hit = sum([chromosome.count(queen)-1 for queen in chromosome])/2
    
    len_chrom = len(chromosome)
    left_diagonal = [0] * 2 * len_chrom
    right_diagonal = [0] * 2 * len_chrom
    for i in range(len_chrom):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len_chrom - i + chromosome[i] - 2] += 1

    diagonal_hit = 0
    for i in range(2 * len_chrom -1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_hit += counter / (len_chrom - abs(i - len_chrom + 1))
    
    return int(maxFitness - (horizontal_hit + diagonal_hit)) 

def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Max Reached"
        
def reproduce(x, y): #doing cross_over between two chromosomes
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutate(x):  #randomly changing the value of a random index of a chromosome
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def genetic_queen(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities) 
        y = random_pick(population, probabilities) 
        child = reproduce(x, y) 
        if random.random() < mutation_probability:
            child = mutate(child)
        print (child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
    return new_population

if __name__ == "__main__":
    nq = 8 #no. of queens
    maxFitness = (nq*(nq-1))/2  # 8*7/2 = 28
    population = [random_chromosome(nq) for _ in range(100)]
    
    generation = 1

    while not maxFitness in [fitness(chrom) for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, fitness)
        print("")
        print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1
    chrom_out = []
    print("Solved in Generation {}!".format(generation-1))
    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("");
            chrom_out = chrom
            print ([queen - 1 for queen in chrom])
            print (chrom_out)