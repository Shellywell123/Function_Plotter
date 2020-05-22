# Function Plotter
Program for plotting 2D & 3D functions from direct input, written in Python3 for linux terminal
Uses matplotlib and numpy libraries.

## Instructions:

### How to setup:
In terminal/cmd prompt, clone the repository into you desired location:
```bash
git clone https://github.com/Shellywell123/Function_Plotter.git
```

### How to update:
Navigate to program directory:
```bash
cd Function_Plotter/
```
In terminal/cmd prompt, pull the latest version:
```bash
git pull
```

### How to run:
For 2D functions, in terminal/cmd prompt, execute 'run2d.py' with python 3:
```bash
python3 run2d.py
```
For 3D functions, in terminal/cmd prompt, execute 'run3d.py' with python 3:
```bash
python3 run3d.py
```

## Features
 - Supports 2D and 3D functions
 - Supports trigonometry functions
 - Supports multiple input forms:
    - y = f(x,z), y = f(x), y = f(z)
    - x = f(y,z), x = f(y), x = f(z)
    - z = f(x,y), z = f(x), z = f(y)
 - User inputted lims (2d only supported thus far)
 - batman function 
 ```bash
batman
```

## Fixes to be made
- Some features break after one false input

## Examples
In terminal/cmd prompt:
```bash
python3 run3d.py
```
```bash
z = x*sin(y)**2
```
output:

![screenshot](Images/screenshot.png)