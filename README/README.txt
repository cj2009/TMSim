This is small Python project I made while taking a Theory of Computation class. 
When first learning how to build Turing Machines, students always have an 
element of doubt about the correctness of their TMs, especially for TMs that 
recognize complicated languages. I created this project in order to be able to 
quickly simulate hundreds or even thousands of strings on a TM.

The purpose of this project is to simulate a given string on a TM and output
the status of the TM in each step (e.g. the current state, what the tape 
currently looks like, etc.). Since there is a possibility that a TM will loop
forever on a given string, there is a parameter that limits how many steps the
TM will run for.

The convention used for drawing TMs is from the textbook "Introducing the 
Theory of Computation" by Goddard. A sample TM that recognizes strings that are
palindromes of even length is included for reference (see the included 
image). Note that there are no reject states, because any unlabeled transitions
are assumed to go to a reject state, and therefore the TM will "die" if no
suitable transition is found at a certain state.
