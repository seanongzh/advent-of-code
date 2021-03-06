# Advent of Code
The Advent of Code is an advent calendar of coding challenges, published every December. Visit the [AOC website](https://adventofcode.com/) for the full archive of coding challenges. I discovered this too late (after Christmas), but I'm attempting the 2019 challenges anyway as a side project.

My solutions to AOC 2019 are written mostly in Python. Documentation might be sparse. All input files can be found on the [website](https://adventofcode.com/). Below is a log of how I have done, with synopses of my code.

## Day 1
Started and finished on December 28. Created a fuel calculator based on a spaceship's weight, which also accounted for the fuel needed to transport the fuel.

## Day 2
Started and finished on December 29. Created a basic integer instruction [interpreter](https://en.wikipedia.org/wiki/Bytecode).

## Day 3
Started on January 1 and finished on January 2. Simple code for [taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry) (Manhattan distance) problems.

## Day 4
Started and finished on January 2. Created a number checker based on certain rules about its digits (repeating, increasing, etc.)

## Day 5
Started and finished on January 4. Extended Day 2's Intcode interpreter with [instructions](https://en.wikipedia.org/wiki/Opcode) for I/O, [conditional jumps](https://en.wikipedia.org/wiki/Indirect_branch), and comparisons. Also added support for variable/literal parameter modes.

## Day 6
Started on January 5 and finished on January 6. Created simple graphs representing an orbital map to find the number of reachable vertices for every vertex and the shortest path between two vertices (implemented using BFS).