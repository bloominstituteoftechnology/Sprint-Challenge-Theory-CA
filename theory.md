### 1. Regular Expressions
Find regexes that match the following. (e.g. find a single regex that matches
both `antelope` and `antelopes`.)

a. Single regex that matches either of these:

    antelope rocks out
    
    antelopes rock out

b. Regex that matches either of:

    goat
    
    moat

  but not:

    boat

c. Regex that matches dates in YYYY-MM-DD format. (Year can be 1-4 digits, and
  month and day can each be 1-2 digits). This does not need to verify the date
  is correct (e.g 3333-33-33 can match).

    2000-10-12
  
    1999-1-20
  
    1999-01-20
  
    812-2-10

### 2. State Machines

> A useful tool for drawing state machines is [Evan's FSM
> Designer](http://madebyevan.com/fsm/). Add image files 
> showing your state diagrams to this repo to submit.

a. Draw a state machine that corresponds to the following regex:

      ab*c+d?[ef]

  Remember the ε transition can be used to move between states without
  consuming input. 

b. Draw a state machine diagram for the lion and label the transition events that
  cause state transitions.
  
    A lion can be sleeping, eating, hunting, or preening. 


You are expected to be able to answer all these questions. Your responses contribute to your Sprint Challenge grade. [Skipping this section *will* prevent you from passing this challenge.]
