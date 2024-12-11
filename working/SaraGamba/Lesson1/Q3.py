"""
Q3: Books
author: Sara Gamba
"""
import argparse

titles = ["don quixote", 
          "in search of lost time", 
          "ulysses", 
          "the odyssey", 
          "war and peace", 
          "moby dick", 
          "the divine comedy", 
          "hamlet", 
          "the adventures of huckleberry finn", 
          "the great gatsby"]

def UpperCaseFunction(list_of_titles):
    """
    UpperCaseFunction
    param: list of titles
    return: capitalize each word in each title
    """
    list_of_titles = [title.title() for title in list_of_titles]
    return list_of_titles

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Upper Case Program')
    parser.add_argument('--UpperCaseFunction', type=str, help='Convert in upper case[y/n]')
    parser.add_argument('--PrintList', type=str, help='Print List [y/n]')

    args = parser.parse_args()
   
    if(args.UpperCaseFunction is None or args.PrintList is None):
        print('Cannot start the program: missing the arguments!')
    elif(args.UpperCaseFunction == "n"):
        if(args.PrintList=="y"):
            print(titles)
    elif(args.UpperCaseFunction == "y"):
        titles=UpperCaseFunction(titles)
        if(args.PrintList=="y"):
            print(titles)



    