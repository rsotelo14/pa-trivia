#Load csv
import csv
from functools import partial, reduce
import random
import os

def check_file_exists(func):
    '''
    Decorator to check if the file exists
    '''

    def wrapper(*args, **kwargs):
        try:
            if os.path.exists(args[0]):
                return func(*args, **kwargs)
        except FileNotFoundError:
            print("El archivo no existe")
            return None
    return wrapper



@check_file_exists
def load_data(file_path):
    '''
    Load the data from the csv file
    '''
    with open('trivia_questions.csv') as file:
        #Read the file
        reader = csv.reader(file)
        
        q_and_as = [q for q in reader] # List comprehension
        q_and_as.pop(0) # Remove the header
        # Shuffle the questions
        random.shuffle(q_and_as)
        return q_and_as

def process_questions(q_and_as, amount=5):
    '''
    Process the questions and return a generator
    '''
    for q_and_a in q_and_as[:amount]:
        question, a1, a2, a3, correct_answer = q_and_a[0], q_and_a[1], q_and_a[2], q_and_a[3], q_and_a[4]
        # Check to which answer the correct answer corresponds
        for i, a in enumerate([a1, a2, a3]):
            if a == correct_answer:
                correct_index = i + 1
                break

        yield {
            "question": question,
            "answers": [a1, a2, a3],
            "correct_answer": correct_answer,
            "correct_index": correct_index
        }
def show_question(q_and_a):
    '''
    Show the question and the answers
    '''
    print(q_and_a["question"])
    for i, answer in enumerate(q_and_a["answers"]):
        print(f"{i + 1}. {answer}")

def get_user_answer():
    '''
    Get the user answer. Use recursion to keep asking until the user enters a valid answer
    '''
    try:
        i = int(input("Ingrese su respuesta: "))
        if i not in [1, 2, 3]:
            raise ValueError
        return i
    except ValueError:
        print("Por favor ingrese un número válido")
        return get_user_answer()

def show_result_message(is_correct, correct_answer=None):
    '''
    Show the result message
    '''
    if is_correct:
        print("Correcto!")
    else:
        print(f"Incorrecto! La respuesta correcta es: {correct_answer}")

# Partial functions
show_correct_message = partial(show_result_message, True)
show_incorrect_message = partial(show_result_message, False)

# Monad for the score yes sir 
class ScoreMonad:
    def __init__(self, score):
        self.score = score

    def bind(self, func):
        return func(self.score)

    def __str__(self):
        return f"Puntaje: {self.score}"

    def __add__(self, other):
        if isinstance(other, ScoreMonad):
            return ScoreMonad(self.score + other.score)
        else:
            return ScoreMonad(self.score + other)

    @staticmethod
    def unit(score):
        return ScoreMonad(score)

def process_results(results):
    '''
    Process the results and return the score
    '''
    true_count = filter(lambda x: x, results)
    score = map(lambda x: ScoreMonad.unit(10), true_count)
    return reduce(lambda x, y: x + y, score)



if __name__ == '__main__':
    #Load the data
    q_and_as = load_data('trivia_questions.csv')

    #Initialize the score
    results = []
    for q_and_a in process_questions(q_and_as):
        show_question(q_and_a)
        user_answer = get_user_answer()
        is_correct = user_answer == q_and_a["correct_index"]
        if is_correct:
            show_correct_message()
        else:
            show_incorrect_message(q_and_a["correct_answer"])
        results.append(is_correct)
    
        score = process_results(results)
    print(score)
        

'''
1. recursión, check
2. generadores, check
3. listas por comprensión, check
4. decoradores, check
5. itertools.chain,
6. mónadas, check
7. funciones lambda check
8. funciones map, filter, reduce check
'''
