#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        integer_input = input('Please enter an integer: ')
        
        if int(integer_input) % 2 == 0: 
            print("even")
        else:
            print("odd")
    except: 
        return('Please give another try to type in an integer: ')


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    # why doesn't it work without the else " "
    for x in range(1, 101):
        print(x, end = "\n" if x % 10 == 0 else " ")

    


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    count = 0
    add_up = 0
    while True: 
        user_input = input("Please enter a number (or type done to start calculating average): ")
  
        if user_input == "done":
            if count > 0:
                average = add_up / count
                return average
            else:
                return

        else:
            try:
                input_number = float(user_input)
                add_up += input_number
                count += 1
                       
            except:
                print("Please type in another number:")
    

        
##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    # even_odd()
    ten_by_ten()
    # find_average()

if __name__ == '__main__':
    main()
