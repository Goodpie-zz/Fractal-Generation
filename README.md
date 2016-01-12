# Fractal-Generation
Collection of fractal generation algorithms mainly based off of http://www.gameprogrammer.com/fractal.html. Programming done in Python 2.7.5 using the PyGame Library.

## Midpoint Displacement

Creates a line and iterates over it x times translating the y position by a semi-random amount

![Midline displacement example 1](http://i.imgur.com/PCgRKdw.png)
![Midline displacement example 2](http://i.imgur.com/AJa36Br.png)

## Diamond Square

Creates a grid that is (2 ^ x) in size (height and width) and iterates over that grid using the diamond square algorithm which populates the grid with clamped values between 0 and 1. Each grid point has a random amount of roughness generated to it to prevent distinct patterns from appearing. As of now, the roughness only looks nice on very low levels (0.01 - 0.3) and the program generally does not run on iterations above 10.

![Diamond Square example 1](http://i.imgur.com/K1BHBCw.png "Roughness of 0.01")
![Diamond Square example 2](http://i.imgur.com/NZAop1W.png "Roughness of 0.1")
![Diamond Square example 3](http://i.imgur.com/gbX4gXS.png "Roughness of 0.03")
