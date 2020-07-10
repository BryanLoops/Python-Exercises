from turtle import *
import random as rnd

shape('turtle')

move = 1

def gen_rand():
    var_one = 1
    var_two = 1

    while move > 0:
        forward(var_one)
        right(var_two)

        var_one += 0.1
        var_two += 0.1

gen_rand()