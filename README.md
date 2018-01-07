Game of life
============
 
 ## Description ##
Just another Conway's Game of Life with glider spaceship example, entirely written in Python 3 

## How to run ##
```
$ git clone https://github.com/pysimone/game_of_life.git
```

```
$ cd game_of_life
```

```
$ python3 gameoflife.py
```

## Rules ##
At each generation:

A living cell with two or three live neighbours lives on to the next generation.

A dead cell with three living neighbours becomes a live cell.

## Output ##
As output you obtain the matrices containing the glider and its evolution in four generations. The glider is made of "1" and the empty part of the matrix is made of "0".
After the execution of the script, you should see at video something like this:

```
Glider
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 

Generation 1
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 1 0 1 0 0 0 0 0 0 
0 0 1 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 

Generation 2
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 0 
0 1 0 1 0 0 0 0 0 0 
0 0 1 1 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 

Generation 3
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 0 
0 0 0 1 1 0 0 0 0 0 
0 0 1 1 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 

Generation 4
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 0 0 
0 0 1 1 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
```

The glider travels at c/4 !
