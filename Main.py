'''
Created on Nov 9, 2014
@author: c

Use this class for testing out the Turing Machines. A sample TM is shown below.
'''
from TMHelper import TMHelper


def main():    
    # Specify the start and accept states:
    startState = 'A'
    acceptState = 'E'
    
    
    # Define each transition as a string, like this:
    #         t = 'stateA -> stateB X,Y,Z'
    # where stateA and stateB are states of the TM;
    # X is the symbol to be read and Y is the symbol to be written;
    # Z is either L, R or S, indicating left, right or stay.
    # See the docs from the class TMHelper for details.
    
    # Example: These are the transitions of a TM that recognizes palindromes of
    # even length:
    t1 = 'A -> B0 0,_,R'
    t2 = 'B0 -> B0 0,0,R'
    t3 = 'B0 -> B0 1,1,R'
    t4 = 'B0 -> C0 _,_,L'
    t5 = 'C0 -> D 0,_,L'
    t6 = 'D -> D 0,0,L'
    t7 = 'D -> D 1,1,L'
    t8 = 'D -> A _,_,R'
    t9 = 'A -> E _,_,S'
    t10 = 'A -> B1 1,_,R'
    t11 = 'B1 -> B1 0,0,R'
    t12 = 'B1 -> B1 1,1,R'
    t13 = 'B1 -> C1 _,_,L'
    t14 = 'C1 -> D 1,_,L'
    
    # Create a list out of these transitions:
    transitions = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14]
    
    #Use the TMHelper to construct a TM object:
    tm = TMHelper(transitions, startState, acceptState).getTM()
    
    # An input string is needed to run this TM:
    inputString = '110011'
    # To test multiple strings, create a list of strings and use a loop to run
    # the TM on all those strings.
    
    
    # Run the TM with the input string; the return value is a list of tuples
    runSequence = tm.run(inputString)
    
    # Use the function 'printSequence' from TMHelper to print the output:
    TMHelper.printSequence(runSequence)
    
main()

