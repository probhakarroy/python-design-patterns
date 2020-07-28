def count_to(count):
    """Our iterator implementation"""

    # list
    numbers_in_german = ['eins', 'zwei', 'drei', 'vier', 'funf']

    # Our built-in iterator 
    # creates a tuple such as (1, 'eins')
    iterator = zip(range(count), numbers_in_german)

    #Iterate through our iterable list

    #Extract the german numbers
    #Put them in a generator called number

    for _, number in iterator:

        #Returns a 'generator' containing numbers in german
        yield number


if __name__ == "__main__":
    
    #Let's test the gerator returned by the iterator
    for num in count_to(3):
        print(f'{num}')

