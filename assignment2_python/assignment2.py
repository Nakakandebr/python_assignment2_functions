
def concatenate_args(*args):
    answer = ""
    for arg in args:
        answer += arg
    return answer
    

    #A function named concatenate_kwargs that takes any number of string arguments in 
    #keyword arguments  format and concatenates them into a single string

def concatenate_kwargs(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += value
    return result
