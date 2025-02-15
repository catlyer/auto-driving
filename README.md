Inside each folder you can find the respective python files for each map as well as a planned route for them


Short summary of the important functions, if you want a more indepth explanation, you can probably ask Gemini or Copilot.


If a function in the code is not here, it is either a function that serves very little purpose and is straightforward or a function for automating repetitive movements (Example being the inandout function in the template)



1. `linefollowBlack`: Self explanatory, uses the `getPosBlack` function to get the inputs from the sensors and calculates where the line is located to then control the turning of the robot.
2. `linefollowWhite`: See `linefollowBlack`, fundementally similar but the sensors are tracking the opposite colour
3. `stop`, `moveForward`, `turnRight`, `turnLeft` and `U_turn` : Also self explanatory, manually sets the wheel values to provide said movement, however it is much preferred to use `gyro_follow` for turning to reduce the potential for timing errors
4. `isColor`: Uses the color sensors to output the RGB values of the floor below it
5. `is_orange`, `is_lightblue`, `is_blue` and such: Functions to check for specific colors through their RGB values using `isColor`.
6. `is_south`, `is_west`, `is_east`, `is_north`: Checks if the robot is facing a specific cardinal direction based on the `RotationZ` value.
7. `nextState`: Increments the `gameState` (Used to control the order of stuff running) and resets the `stateTime` (Used to measure `is_duration`)
8. `is_duration`: Checks if the specified duration has passed based on the `stateTime`. In simpler terms, think of the "tickrate" system in minecraft, this practically does the same thing.
9. `gyro_follow`: Adjusts the robot's steering to follow a specified angle using the gyroscope. (Reccommeded to use alongside `zRange`)
10. `move_steering`: Manual control over both wheels, not reccommended to use unless you are pulling a complex manuver with the robot.
11. `checkpoint`: Stops the robot and turns on the LED to activate the checkpoints. Requires the LED to be turned off after. (TODO: Make the light turning off independent)
12. `zRange`: Checks if the `RotationZ` value is within a specified range. Currently returns `True` if the angle is within +-10 degrees.
13. `invertzRange`: Same as `zRange` but inverse.


FAQ:
Q: How do I edit the values?
A: There are clearly labelled comments in the code where you can find the values to be modified

Q: How can I download the template code?
A: If you have git, run `git clone https://github.com/catlyer/auto-driving.git`
   If not, simply click the file you want to download and look for the download button at the top right


Made by every senior before me
