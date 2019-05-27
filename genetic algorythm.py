import random
import itertools as it
import time
import json
import collections


class Being:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = fitness(genes)


class Population:
    def __init__(self, members):
        global current_pop
        self.size = 0
        self.members = members
        self.reproducing_mems = []
        self.iter_number = current_pop
        self.fitnessi = []
        self.best_member = None
        self.perfect_member = None
        current_pop += 1
        for member in self.members:
            if member.fitness == length:
                self.perfect_member = member
            self.fitnessi.append(member.fitness)
            self.size += 1
            for h in range(member.fitness):
                self.reproducing_mems.append(member)
            if self.best_member is None:
                self.best_member = member
            elif member.fitness > self.best_member.fitness:
                self.best_member = member
        self.avg_fit = float(sum(self.fitnessi) / len(self.members))


def mutate():
    if random.randint(0, 101) < mut_rate:
        return False
    else:
        return True


def reproduce(parent1, parent2):
    child_genes = []
    if length % 2 == 0:
        for d, y in zip(it.islice(parent1.genes, 0, None, 2), it.islice(parent2.genes, 1, None, 2)):
            if not mutate():
                child_genes.append(d)
            else:
                child_genes.append(random.choice(valid_chars))
            if not mutate():
                child_genes.append(y)
            else:
                child_genes.append(random.choice(valid_chars))
    else:
        for e, y in zip(it.islice(parent1.genes, 0, None, 2), it.islice(parent2.genes, 1, None, 2)):
            if not mutate():
                child_genes.append(e)
            else:
                child_genes.append(random.choice(valid_chars))
            if not mutate():
                child_genes.append(y)
            else:
                child_genes.append(random.choice(valid_chars))
        if not mutate():
            child_genes.append(parent1.genes[length - 1])
        else:
            child_genes.append(random.choice(valid_chars))
    return Being(child_genes)


def reproduce_pop(pop):
    new_pop = []
    while len(new_pop) < pop.size:
        new_pop.append(reproduce(pop.reproducing_mems[random.randint(0, len(pop.reproducing_mems) - 1)],
                                 pop.reproducing_mems[random.randint(0, len(pop.reproducing_mems) - 1)]))
    return Population(new_pop)


def rand_pop(size):
    pop = []
    for c in range(size):
        genes = []
        for z in range(length):
            genes.append(random.choice(valid_chars))
        pop.append(Being(genes))
    return Population(pop)


def fitness(genes):
    fitness_ = 0
    for y in range(length):
        if genes[y] == list_word[y]:
            fitness_ += 1
    return fitness_


def mother_function():
        global last_pop
        last_pop = rand_pop(pop_size)
        while True:
                if last_pop.best_member == last_pop.perfect_member:
                    return Result(a, j, i, last_pop.iter_number, str(time.time() - start_time)[:5])
                elif len(last_pop.reproducing_mems) == 0:
                    last_pop = rand_pop(pop_size)
                else:
                    last_pop = reproduce_pop(last_pop)


results = []
Result = collections.namedtuple('result', [
    'mut_rate',
    'pop_size',
    'word_length',
    'iterations',
    'time'
])

for a in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
    mut_rate = int(a)
    for j in [50, 100, 200, 250, 500, 1000]:
        pop_size = int(j)
        for i in range(1, 6):
            valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            word = []
            for x in range(i):
                word.append(random.choice(valid_chars))
            word = ''.join(word)
            list_word = [char for char in word]
            length = len(word)
            current_pop = 0
            start_time = time.time()
            results.append(mother_function())
        print("check lower %s" % j)
        with open("results.json", "w") as fp:
            json.dump(results, fp)
    print("check upper %s" % a)
with open("results.json", "w") as fp:
    json.dump(results, fp)
