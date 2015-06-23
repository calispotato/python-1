'''hi meow.'''
import colors as c
def ask(question):
    print(question)
    answer = input(c.green + '> ')
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    name = ask('what is your name') 
