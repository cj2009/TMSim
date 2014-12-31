'''
Created on Nov 9, 2014
@author: c

This class represents a complete Turing machine. It has a list of states,
rules (transitions), a unique accept state and a unique reject state.
'''
from Cell import Cell


class TM:
    # Some static variables to represent the current status of the TM:
    REJECTED = -1
    STILL_RUNNING = 0
    ACCEPTED = 1
    
    def __init__(self, states, rules, startState, acceptState):
        self.states = states
        self.rules = rules
        self.acceptState = acceptState
        self.startState = startState


    '''
    Returns true if list A is a subset of B - i.e., each element in A must be
    an element of B.
    '''
    def isSubsetOf(self, A, B):
        for x in A:
            if x not in B:
                return False
        return True
        
    '''
    Checks if this TM is valid, based on the specified string that is being fed
    into this machine. The rules must be valid, the string must be composed of
    the tape alphabet characters only, etc.
    '''
    def validate(self, string):
        # First, check that the list of states and rules is non-empty:
        if not self.states:
            raise Exception("List of states must be non-empty!")
        if not self.rules:
            raise Exception("List of rules must be non-empty!")
        
        
        # Find the unique start state:
        numStartStates = 0
        for state in self.states:
            if state.isStartState():
                self.startState = state
                numStartStates += 1
        if numStartStates is not 1:
            raise Exception("There must be a unique start state!")
        
        # Find the unique accept state:
        numAcceptStates = 0
        for state in self.states:
            if state.isAcceptState():
                self.acceptState = state
                numAcceptStates += 1
        if numAcceptStates is not 1:
            raise Exception("There must be a unique accept state")
        
        
        # Finally, go thru each char in the string and make sure they are
        # found in the rules. Otherwise it means that there are extraneous
        # characters in the string that this TM can't handle
        
        # The first loop is to gather all the chars from the rules into a single list:
        charsFromRules = []
        for rule in self.rules:
            char1 = rule.getReadSymbol()
            char2 = rule.getWriteSymbol()
            if char1 not in charsFromRules:
                charsFromRules.append(char1)
            if char2 not in charsFromRules:
                charsFromRules.append(char2)
                
        # Now make sure that 'string' is a subset of 'charsFromRules':
        if not self.isSubsetOf(string, charsFromRules):
            raise Exception("Input alphabet is not a subset of the tape alphabet!")


    '''
    Creates a linked list of Cell objects from the specified string.
    @param string: The input string for the TM. If the string is empty, an empty
            Cell object is constructed and returned.
    @return: Reference to the head and tail of the linked list. Note: head and
            tail may be the same object.
    '''
    def createLinkedListFromString(self, string):
        if not string or string == '':
            c = Cell()
            return c, c
        
        head = Cell(string[0])
        lastCreatedCell = head
        
        for i in range(1, len(string)):
            newCell = Cell(string[i])
            
            lastCreatedCell.next = newCell
            newCell.prev = lastCreatedCell
            lastCreatedCell = newCell
    
        return head, lastCreatedCell
    
    
    '''
    Creates a string from the given linked list of Cell objects. Basically, this
    function does the reverse of 'createLinkedListFromString'
    
    @param head: Reference to the head of the linked list of Cell objects
    '''
    def createStringFromLinkedList(self, head):
        charList = []
        cell = head
        
        while cell:
            charList.append(cell.symbol)
            cell = cell.next
        
        return "".join(charList)
    
        
    '''
    Runs a string through this TM and returns a list of tuples that indicate 
    what the TM is doing at each step. Each elements of the returned list will 
    be a tuple of the following format:
    
        (currentState, tape, tapePosition, currentStatus)
        
    where:
        'currentState' is the current state that the TM is in;
        'tape' is a reference to the head of the linked list;
        'tapePosition' is the index of the tape cell that the TM is currently at;
        'currentState' is REJECTED, STILL_RUNNING or ACCEPTED.
    
    @param string: A string of characters that represents the input portion of the tape.
    @param runLimit: maximum number of steps to simulate before the TM stops.
    '''
    def run(self, string, runLimit = 500):
        
        # First, validate the TM to make sure it is free of errors:
        self.validate(string)
        
        history = [] # This is the list that will be returned
        
        # Create a linked list to represent the input string on the tape:
        head, tail = self.createLinkedListFromString(string)
        currentState = self.startState
        currentCell = head

        cycles = 0                          # how many times the loop has run
        tapePosition = 0                    # index of the current cell
        
        # The history list will always have one entry
        newTuple = (str(currentState.getName()), 
                    self.createStringFromLinkedList(head), tapePosition, 
                    TM.STILL_RUNNING)
        history.append(newTuple)
        
        
        while True:
            if cycles is runLimit:
                return history
            
            c = currentCell.symbol
            
            # Find the rule that has 'currentState' as its first state and c as 
            # its readSymbol:
            neededRule = None
            for rule in self.rules:
                if rule.getState1() is currentState and rule.getReadSymbol() is c:
                    neededRule = rule
                    break
            if not neededRule:
                # No rule was found that matches the current input, so the TM rejects:
                newTuple = (str(currentState.getName()), 
                            self.createStringFromLinkedList(head), tapePosition,
                             TM.REJECTED)
                history.append(newTuple)
                return history
            
            
            # A rule was found, so update the tape and the states:
            currentCell.symbol = neededRule.getWriteSymbol()
            
            # In some cases, the linked list may need to be expanded by adding
            # an extra cell before the head or after the tail:
            if currentCell is head and rule.getMoveDirection() is -1:
                newCell = Cell()
                newCell.next = head
                head.prev = newCell
                tapePosition = 0
                head = newCell
            elif currentCell is tail and rule.getMoveDirection() is 1:
                newCell = Cell()
                newCell.prev = tail
                tail.next = newCell
                tapePosition += 1
                tail = newCell
            else:
                tapePosition += rule.getMoveDirection()
                
            # Update the 'currentCell' variable, depending on which direction
            # the TM is supposed to move to:
            if rule.getMoveDirection() is -1:
                currentCell = currentCell.prev
            elif rule.getMoveDirection() is 1:
                currentCell = currentCell.next
                
            
            currentState = rule.getState2()
            cycles += 1
            
            # Add this to the history list depending on what the current state is:
            if currentState.isAcceptState():
                newTuple = (str(currentState.getName()), 
                            self.createStringFromLinkedList(head), 
                            tapePosition, 1)
                history.append(newTuple)
                return history
            else:
                newTuple = (str(currentState.getName()), 
                            self.createStringFromLinkedList(head), 
                            tapePosition, 0)
                history.append(newTuple)
        
        
        

    

    
