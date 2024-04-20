import random
num_ships=9

def generate_unique_coordinates(locations):
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if (x, y) not in locations:  #unique ship
            return (x, y)

def init_population(numofships,population_size):
    geneset=[]
    
    def generate_gene(): #generating a single gene
        chromosome=[]
        for _ in range(numofships):
            location=generate_unique_coordinates(chromosome)
            chromosome.append(location)
        return chromosome
    
    for i in range(population_size): #generating the geneset
        geneset.append(generate_gene())
    return geneset

def get_fitness(target,hg):
    genesetWithFitness={}
    #making use of hashing to make the geneset with fitness and deal with it
    for key in hg.keys():
        fitness=0
        gene=hg[key]
        
        for location in gene:
            if location in target:
                fitness+=1 
        genesetWithFitness[key]=fitness

    return genesetWithFitness

def individual_fitness(target,individual):
    fitness=0
    individual=set(individual)#to avoid counting repeated locations
    for location in individual:
        if location in target:
            fitness+=1
    return fitness
        
#selection
def roulette_wheel_selection(geneset_fitness, num_selections):
    total_fitness = sum(geneset_fitness.values())
    selection_probs = {key: fitness / total_fitness for key, fitness in geneset_fitness.items()}#need to fix the issue with total fitness=0

    selected_indices = set()
    selected_genes = []

    while len(selected_indices) < num_selections:
        random_number = random.uniform(0, 1)
        cumulative_prob = 0

        for key, prob in selection_probs.items():
            cumulative_prob += prob
            if random_number <= cumulative_prob and key not in selected_indices:
                selected_indices.add(key)
                selected_genes.append(key)
                break

    return tuple(selected_genes)

def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def bit_flip_mutation(individual, mutation_rate):
    mutated_individual = []
    for allele in individual:
        mutated_allele = []
        for value in allele:
            # Convert the value to binary 
            binary_value = bin(value)[2:].zfill(3)  # 3 bit because our board max val is 7
            # Select a random bit index to flip
            bit_index = random.randint(0, 2)
            #flip using mutation rate
            mutated_bit = str(int(binary_value[bit_index]) ^ 1) if random.random() < mutation_rate else binary_value[bit_index]
            # replace bits
            mutated_value = binary_value[:bit_index] + mutated_bit + binary_value[bit_index+1:]
            # Convert the mutated binary value back to integer
            mutated_allele.append(int(mutated_value, 2))
        mutated_individual.append(tuple(mutated_allele))
    return mutated_individual


def weak_parent_replacement(geneset_with_fitness, new_individual, hashed_geneset, target):
    weakest_key = min(geneset_with_fitness, key=geneset_with_fitness.get)
    hashed_geneset[weakest_key] = new_individual
    geneset_with_fitness[weakest_key] = individual_fitness(target, new_individual)


#generate random ships
ships=[]
for _ in range(num_ships):
    new_ship = generate_unique_coordinates(ships)
    ships.append(new_ship)

def genetic_algorithm(target):
    iterations=0
    mRate=0.5
    hashed_geneset={}
    test=init_population(num_ships,8)
    for i in range(len(test)):
        hashed_geneset[i]=test[i]
    gensetWithFitness=get_fitness(target,hashed_geneset)
    while len(target)>max(gensetWithFitness.values()) and iterations<100000:
        iterations+=1
        index1,index2=roulette_wheel_selection(gensetWithFitness,2)
        #new offspring
        child1,child2=single_point_crossover(hashed_geneset[index1],hashed_geneset[index2])
        child1=bit_flip_mutation(child1,mRate)
        child2=bit_flip_mutation(child2,mRate)
        #replacement
        weak_parent_replacement(gensetWithFitness,child1,hashed_geneset,target)
        weak_parent_replacement(gensetWithFitness,child2,hashed_geneset,target)
 
    return gensetWithFitness,hashed_geneset

x,y=genetic_algorithm(ships)
print(y[max(x)], x[max(x)])
print(ships)