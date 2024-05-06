#Create a Python program which can find prime numbers between a given range 
from colorama import Fore 
import time 
import sys 
import logging 
def log_prime_number():
    #Creating a logger object 
    prime_number_logger=logging.getLogger('prime_number_logger')
    prime_number_logger.setLevel(logging.INFO)
    file_handler=logging.FileHandler('primenumbers.log',mode='a')
    logging_format=logging.Formatter('%(name)s-%(message)s')
    file_handler.setFormatter(logging_format)
    file_handler.setLevel(logging.INFO)
    prime_number_logger.addHandler(file_handler)
    prime_number_logger.info(f'Prime numbers between {start} and {stop}:\n')
    for prime_number in prime_numbers:
        prime_number_logger.info(f'{prime_number}')
    else:
        pass
def error_msg(error_message):
    for n in error_message:
        sys.stderr.flush()
        time.sleep(0.1)
        sys.stderr.write(f'{Fore.RED}{n}')
    else:
        print(f'{Fore.RESET}') 
        
try:
    start=int(input('start:'))
    time.sleep(1)
    stop=int(input('stop:'))
    if start>stop:
        error_msg(error_message='Error,the stop value cannot be smaller than the start value')
    else:
     time.sleep(1)
     print(f'\tPrime numbers between the given ranges of {start}  and {stop}:')
     time.sleep(1)
     prime_numbers=[]
     for prime_number in range(start,stop,1):
        if prime_number%2!=0 and prime_number%3!=0 and prime_number%5!=0 and prime_number%7!=0 and prime_number!=1 or prime_number==2 or prime_number==3 or prime_number==5 or prime_number==7:
            print(f'{prime_number}')
            prime_numbers.append(prime_number)
        else:
            continue 
     else:
        log_prime_number()
        sys.exit('')
except ValueError:
    error_msg(error_message=f'ValueError, non-numerical value was entered')
