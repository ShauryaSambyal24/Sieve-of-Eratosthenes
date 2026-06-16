# Sieve-of-Eratosthenes
A Python implementation of the Sieve of Eratosthenes with a terminal-based visualization that progressively removes composite numbers from a square grid.


# Pygame Sieve Visualizer

A simple Python + Pygame visualization of the Sieve of Eratosthenes algorithm.  
It displays numbers in a grid and visually eliminates non-prime numbers step by step.

---

## Features
- Grid-based number visualization
- Real-time elimination of non-prime numbers
- Console + Pygame dual display
- Adjustable grid size based on input
- Simple keyboard input system

---

## How it works
1. User inputs a number `N`
2. Array is filled from `1` to `N`
3. Sieve algorithm runs:
   - Keeps track of primes
   - Removes non-prime numbers
4. Grid updates in Pygame after each elimination

---

## Controls
- Type number → set size of sieve
- ENTER → confirm input
- BACKSPACE → delete input
- CLOSE WINDOW → exit program

---

## Requirements
- Python 3.x
- pygame


python your_file.py
Install pygame:
```bash
pip install pygame
