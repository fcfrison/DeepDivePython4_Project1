import datetime
import sys

# TODO: find a way to specify the module that have defined the error. 

def record_error(err: Exception) -> None:
    """
    Description
    ----------
    The record_error function generates a text file and record it on the 
    hard drive. 
    Função que gera um arquivo de texto descrevendo o erro ocorrido e o salva
    em disco.

    Parameters
    ----------
        err: Exception
        Exception class object.

    Return
    ----------
        None
    """

    # Save a reference to the original standard output
    original_stdout = sys.stdout
    with open(
        f'./logs/ERRO_{datetime.datetime.now().strftime("%d-%m-%Y_%H_%M_%S")}.txt', "w"
    ) as f:
        # Change the standard output to the file we created.
        sys.stdout = f
        print(
            f'ERRO:\t{err}\nDATA:\t{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}'
        )
        sys.stdout = original_stdout
        print(err)
