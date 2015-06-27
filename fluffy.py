"""This is a comment"""

import colors as c
import random
from utils import ask 

intro = c.magenta + '''
Welcome to the Pink Fluffy Unicorns quiz.
Lets test your knowledge...
''' + c.reset

def q1():
    answer = ask('what color are the unicorns')
    if answer == 'pink':
        print('and what a lovely color it is')
        return True
    print ('that is incorrect')
    return False

def q2():
    answer = ask('where are the dancing')
    if answer == 'rainbows':
        print('meow')
        return True
    print('nope')
    return False

def q3():
    answer = ask('use one word to describe their magical fur')
    if answer == 'smiles':
        print('XD')
        return True
    print('smile more')
    return False

questions = [q1,q2,q3]
