'''
Created on Nov 10, 2014
@author: c

This is a helper class that makes it easier to run a TM. Instead of having to
construct State and Rule objects manually and then creating a TM object, the 
user can create an instance of this class by specifying the TM's transitions 
as simple strings. The TMHelper object will then parse the input, perform the 
necessary actions to create the actual TM object, and then return it.
'''
from State import State
from Rule import Rule
from TM import TM
import sys

class TMHelper:
    
    '''
    Transitions: a list of strings that specify how the TM should work.
    Each transition should be a string of the following format:
        t = 'stateA -> stateB X,Y,Z'
    where stateA and stateB are the names of any two states of the TM;
    X is the symbol to be read and Y is the symbol to be written;
    Z must be one of 'L', 'R' or 'S', indicating left, right or stay.
    
    Note: if X or Y is not a single char, the behavior of this TM is undefined.
    
    startState is the name of any one of the states mentioned in the list of transitions.
    acceptState is the name of any one of the states mentioned in the list of transitions.
    '''
    def __init__(self, transitions, startState, acceptState):
        self.transitions = transitions
        self.startState = startState
        self.acceptState = acceptState
    
        
    ''' 
    This function iterates thru the given list of states and returns the state with
    the given name. If not found, returns None.
    '''
    def findState(self, listOfStates, stateName):
        for state in listOfStates:
            if state.getName() == stateName:
                return state
        return None
        
    '''
    This function creates the actual TM object by parsing the user input and 
    creating the appropriate rules, states, etc.
    '''
    def getTM(self):
        # Go thru the list of transitions and create a list of states, rules and 
        # tape alphabet symbols:
        states = []
        tapeAlphabet = []
        rules = []
        
        for t in self.transitions:
            # The next several lines are for parsing the user input and splitting the string into parts:
            stateOne, separator, rightSide = t.partition(' -> ')
            stateTwo, separator, rightSide = rightSide.partition(' ')
            stateOne = stateOne.strip()
            stateTwo = stateTwo.strip()
            rightSide = rightSide.strip()
                        
            
            # Process the first state that is mentioned in this transition string:
            stateA = self.findState(states, stateOne)
            if not stateA:
                # A State with this name has not been constructed yet, so do it now:
                stateA = State(stateOne)
                states.append(stateA)
            # Check if this state is either the accept/start state:
            if stateOne is self.acceptState:
                stateA.setAcceptState(True)
            if stateOne is self.startState:
                stateA.setStartState(True)
                
                
            # Process the second state that is in mentioned in this string:
            stateB = self.findState(states, stateTwo)
            if not stateB:
                # A State with this name has not been constructed yet, so do it now:
                stateB = State(stateTwo)
                states.append(stateB)
            # Check if this state is either the accept/start state:
            if stateTwo is self.acceptState:
                stateB.setAcceptState(True)
            if stateTwo is self.startState:
                stateB.setStartState(True)
            
            
            # Now examine the transition string in order to construct the Rule objects:
            char1, separator, rightSide = rightSide.partition(',')
            char2, separator, char3 = rightSide.partition(',')
            char1 = char1.strip()
            char2 = char2.strip()
            char3 = char3.strip()
            
            if char1 not in tapeAlphabet:
                tapeAlphabet.append(char1)
            if char2 not in tapeAlphabet:
                tapeAlphabet.append(char2)
            # Check whether the move direction is left, right or stay:
            moveDirection = None
            if char3 == 'L':
                moveDirection = -1
            if char3 == 'R':
                moveDirection = 1
            if char3 == 'S':
                moveDirection = 0
            # Construct the Rule object:
            rule = Rule(stateA, stateB, char1, char2, moveDirection)
            rules.append(rule)
            
            
            # Some printout for debugging:
#             if stateOne is self.acceptState:
#                 print(stateOne + " is the accept state")
#             if stateTwo is self.acceptState:
#                 print(stateTwo + " is the accept state")
#             if stateOne is self.startState:
#                 print(stateOne + " is the start state")
#             if stateTwo is self.startState:
#                 print(stateTwo + " is the start state")
#             print("Rule is from " + stateA.getName() + " to " + stateB.getName() + " as follows: " + char1 + ", " + char2 + ", " + char3)
            
            
            
        # All transitions have been processed, with the list of states and rules 
        # created. Now the TM is ready to be constructed:
        tm = TM(states, rules, self.startState, self.acceptState)
        return tm

#------------------------- STATIC FUNCTIONS ---------------------------------
    
    
    '''
    Behaves exactly like the C library function printf.
    '''
    @staticmethod
    def printf(format, *args):
        sys.stdout.write(format % args)
    
    
    '''
    This function prints the sequence of steps that the TM performs in a neat,
    tabular format. The input parameter must be the return value of the TM.run function.
    '''
    @staticmethod
    def printSequence(listOfTuples):
        if not listOfTuples:
            print("EMPTY SEQUENCE")
            return
        
        
        status = None
        for oneTuple in listOfTuples:
            state = oneTuple[0]
            tape = oneTuple[1]
            position = oneTuple[2]
            
            if oneTuple[3] is -1:
                status = 'Rejected'
            elif oneTuple[3] is 0:
                status = 'Still Running'
            elif oneTuple[3] is 1:
                status = 'Accepted'

            
            TMHelper.printf("State: %s\tTape: ", state)
            # Use a loop to print the tape, as the current symbol needs to be "wrapped"
            # in some symbol (like quotes) for easy identification:
            for i in range(len(tape)):
                if i is position:
                    TMHelper.printf("\'%c\'", tape[i])
                else:
                    TMHelper.printf("%c", tape[i])
            
            print("\tTape position: " + str(position) + "\tStatus: " + status)
            
        
    '''
    This is identical to the printSequence function, but prints the result to
    a file instead.
    '''
    @staticmethod
    def printSequenceToFile(listOfTuples, filename):
            f = open(filename, 'w')
            
            
            if not listOfTuples:
                f.write("EMPTY SEQUENCE\n")
                f.close()
                return
            
                
            status = None
            for oneTuple in listOfTuples:
                state = oneTuple[0]
                tape = oneTuple[1]
                position = oneTuple[2]
                
                if oneTuple[3] is -1:
                    status = 'Rejected'
                elif oneTuple[3] is 0:
                    status = 'Still Running'
                elif oneTuple[3] is 1:
                    status = 'Accepted'
    
                f.write("State: " + state + "\tTape:")
                # Use a loop to print the tape, as the current symbol needs to be "wrapped"
                # in some symbol (like quotes) for easy identification:
                for i in range(len(tape)):
                    if i is position:
                        f.write("\'" + tape[i] + "\'")
                    else:
                        f.write(tape[i])
                f.write("\tTape position: " + str(position) + '\tStatus: ' + status + "\n")
            f.close()
    
