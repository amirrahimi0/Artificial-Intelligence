import numpy as np
import random

def create_population(n,size):
    population=[[random.randint(0,n-1) for j in range(n)] for j in range(size)]
    return population

def fitness(person):
    colision=0
    n=len(person)
    max_score=(n*(n-1))//2
    for i in range(n):
            for j in range(i + 1, n):
                if (
                    person[i] == person[j]
                    or abs(person[i] - person[j]) == j - i
                ):
                    colision += 1
    return max_score-colision

def crossover(p1,p2):
    n=len(p1)
    split_point = random.randint(0, n-1)
    new_child=[None]*n
    new_child[:split_point] = p1[:split_point]
    new_child[split_point:] = p2[split_point:]
    return new_child

def choose_parents(population):
    while True:
        p1,p2=random.sample(population,k=2)
        if p1!=p2:
             return p1,p2
    
def mutate(person,probabilty):
     n=len(person)
     for i in range(n):
        if random.random()<probabilty/n:
            person[i]=random.randint(0,n-1)

def produce_childs(population,number_of_childs,probablity):
    p1,p2=choose_parents(population)
    childs=[]
    for i in range(number_of_childs):
        child=crossover(p1,p2)
        mutate(child,probablity)
        childs.append(child)
    return childs
          
def next_generation(population,number_of_childs,probablity):
    n=len(population[0])
    size=len(population)
    next_population=[]
    max_score=(n*(n-1))//2
    for i in range(size):
        next_population+=produce_childs(population,number_of_childs,probablity)
    population+=next_population
    population=sorted(population,key=fitness,reverse=True)[:size]
    return population



def get_best(population):
    best=population[0]
    for p in population:
        if fitness(p)>fitness(best):
            best=p
    return best

def run(n,size,probabilty,max_iteration):
    population=create_population(n,size)
    max_score=(n*(n-1))//2
    for i in range(max_iteration):
        best=get_best(population)
        if fitness(best)==max_score:
            print("Found the answer in iteration {iter}. the answer is:".format(iter=i))
            return best
        population=next_generation(population,3,probabilty)
    best=get_best(population)
    print("Could not find the answer in max iter. the closest answer with score {score} is:".format(score=fitness(best)))
    return best

def print_board(person):
    n=len(person)
    for i in range(n):
            for j in range(n):
                if person[j] == i:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        

         
solution=run(8,100,1/8,1000)
print_board(solution)
