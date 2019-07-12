# Sprint Challenge: Theory-Cellular Automata

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint explored Theory of Computation and applications of Cellular Automata. During this Sprint, you studied state machine diagrams, regular expressions, logic & truth tables, and Conway's Game of Life. In your challenge this week, you will demonstrate proficiency by completing tasks related to these concepts.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your command of the concepts related to Theory of Computation and Cellular Automata.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

[Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.]

## Description

In this challenge, you will...
1. Write 3 regular expressions for specific tasks 
2. Design 2 state machine diagrams
3. Create a variant of Conway's Game of Life

## Self-Study/Essay Questions

Demonstrate your understanding of this week's concepts by answering the free-form questions in [theory.md](). Edit this document to include your answers after each question. Make sure to leave a blank line above and below your answer so it is clear and easy to read by your project manager.

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


## Project Set Up - 1D Life

> This is an implementation of Wolfram's [Rule 126](http://mathworld.wolfram.com/Rule126.html).

Follow these steps to set up your project:

* You'll need to complete the `getNewVal()` function in `1d-life.js`.
  * This is a standalone, vanilla (non-React) web page. You should be able to open the `index.html` file in your browser and see the result. (Before you complete your implementation, the image should show as all black).

* If there are issues opening the `index.html` file directly, you can also run a Python web browser on port 8000 from the command line:

```
cd 1d-life/src
python -m SimpleHTTPServer
```

* Then navigate to `http://localhost:8000` to see the app.

## Minimum Viable Product

### What is 1D Life?

In the Game of Life, we used a 2D grid to store the cellular automaton.
In 1D life, it's a simple 1D array.

Each "generation", the array is examined and new values for each cell
are computed based on the values of that cell and its surrounding
cells.

Usually the subsequent generations are displayed on the next row of a
bitmap. Generation 0 is shown on row 0, generation 1 on row 1, and so
on.


### Algorithm

Everything is written for you except the code in `getNewVal()`. This
function accepts a 1D array of the current life status, and an `x`
coordinate into that array.

It should return `0` if the cell at that `x` should become dead, and
should return `1` if it should be alive next generation.

Whether or not the cell should remain alive or die depends on the
results of the calculation of [Rule 126](#rule-126), that you will
implement, below.

The remaining, existing code sets up a canvas, loops through the
generations, manages the double-buffered life status, etc.

## Rule 126

This rule describes how cells live and die based on their own values,
and that of their immediate neighbors.

For example, if a cell is dead, and its immediate neighbors are alive,
that pattern of 3 cells is:

```
#.#
```

For any of 8 possible combinations of 3 cells surrounding and
including a cell at an _x_ coordinate, we produce a new single cell
at that _x_ coordinate as given by the following table (`.` is 0, `x`
is 1):

```
...  ..#  .#.  .##  #..  #.#  ##.  ###     <- this pattern
 .    #    #    #    #    #    #    .      <- produces this result
```

The final output should look like this:

![Rule 126](https://tk-assets.lambdaschool.com/bcccf169-3288-490a-b7e3-dd955e010256_rule126.png)

This result is a [Sierpinski
Triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle), a
[fractal](https://en.wikipedia.org/wiki/Fractal) that has a habit of
turning up in surprising places.

In your solution, it is essential that you follow best practices and produce clean and professional results. Schedule time to review, refine, and assess your work and perform basic professional polishing including spell-checking and grammar-checking on your work. It is better to submit a challenge that meets MVP than one that attempts to much and does not.

[Validate your work through testing and ensure that your code operates as designed.]

## Stretch Problems

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module but they build on the material you just studied. Time allowing, stretch your limits and see if you can deliver on the following optional goals:

* The VT-100 terminal (console) outputs text to the screen as it
  receives it over the wire. One exception is that when it receives an
  ESC character (ASCII 27), it goes into a special mode where it looks
  for commands to change its behavior. For example:

      ESC[12;45f

  moves the cursor to line 12, column 45.

      ESC[1m

  changes the font to bold.

  * Come up with regexes for the two above sequences. The one to set the
    cursor position should accept any digits for the row and column. The
    bold sequence need only accept `1` (and is a trivial regex). (ESC is
    a single character which can be represented with `\e` in the regex.)

  * Draw a state machine diagram for a VT-100 that can consume regular
    character sequences as well as the two above ESC sequences.

> If you're curious, [here are all the VT-100 escape
> sequences](http://ascii-table.com/ansi-escape-sequences-vt-100.php).
> More common these days is a superset of VT-100 called [ANSI escape
> sequences](http://ascii-table.com/ansi-escape-sequences.php). If
> you've ever put colors and stuff in your Bash prompt, this is what you
> used to do it.
>
> One of your instructors was once hired to implement VT-100 emulation
> in an app, and they used a state machine to do it.
