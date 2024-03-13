import numpy as np
import random


class ParetoFront:
    def __init__(self,pop_size) -> None:
        self.best_pop = np.zeros((pop_size,1))
        self.best_fit = np.zeros((pop_size,1))


    def update(self,P,P_fitness):

        
        for individual, fitness in zip(P,P_fitness):


            i = np.argmin(self.best_fit)
            if fitness > self.best_fit[i]:
                self.best_fit[i] = fitness
                self.best_pop[i] = individual


            

    


def genetic_algorith(pop_size,gmax,p,q):

    PF = None
    P = initialise_population(pop_size)
    P_fitness = fitness(P)
    PF.update(P, P_fitness)


    for gen in range(gmax):
        
        Q = []
        n = len(P)
        for _ in range(n):
            r = random.random()

            if r < p:
                s1,s2 = np.random.choice(P,2,replace = False)
                sprime = crossover(s1,s2)
            elif r < q+p:
                s = np.random.choice(P,1)
                sprime = mutation(s,q)
            else:
                sprime = np.random.choice(P,1)
            Q.append(sprime)
        Q_fitness = fitness(Q)
        Pprime = P+Q
        sorted(P+Q, key =lambda x : rank(x))
        P = Pprime[0:n]
                

def crossover(s1,s2):


    return s1

def mutation(s,q):

    return s





def initialise_population(pop_size):
    
    pop = np.zeros((pop_size,1))
    
    return pop

def fitness(pop):


    return  0

