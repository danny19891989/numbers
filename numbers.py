import random
def cool(x,y):
    print("hey")
    question = x + y
    while True:
        questionPrint = f'{x} + {y} = ?'
        print(questionPrint)
        answer = input('/nAnswer: ')
        if int(answer) ==  x + y:
            print('Right')
            break
        else:
            print(f'Wrong...\n{questionPrint}')

def numberGenerator():
    numbers = []
    numbersList = list(range(10))
    a = random.choice(numbersList)
    b = random.choice(numbersList)
    numbers.append(a)
    numbers.append(b)
    return numbers

# print(cool(numberGenerator(0), numberGenerator(1)))
cool(1,2)

