Short summary of the important functions, if you want a more indepth explanation, you can probably ask Gemini or Copilot using the small code segment

If a function in the code is not here, it is either a function that serves very little purpose and is straightforward or a function for automating repetitive movements (Example being the inandout function)

2. `linefollowBlack`: Adjusts the robot's wheel speeds to follow a black line based on the position calculated by `getPosBlack`.
4. `linefollowWhite`: Adjusts the robot's wheel speeds to follow a white line based on the position calculated by `getPosWhite`.
5. `stop`: Stops the robot by setting both wheel speeds to zero.
6. `moveForward`: Moves the robot forward by setting both wheel speeds to a high value.
7. `turnRight`: Turns the robot right by setting the left wheel speed higher than the right wheel speed.
8. `turnLeft`: Turns the robot left by setting the right wheel speed higher than the left wheel speed.
9. `U_turn`: Makes the robot perform a U-turn by setting the wheels to rotate in opposite directions.
10. `isColor`: Checks if the current color detected by the color sensors matches the specified RGB values.
11. `is_orange`, `is_lightblue`, `is_blue`, `is_magenta`, `is_darkorange`, `is_darkgreen`, `is_purple`, `is_green`, `is_lightred`, `is_pink`, `is_brown`: Functions to check for specific colors using `isColor`.
12. `is_south`, `is_west`, `is_east`, `is_north`: Checks if the robot is facing a specific cardinal direction based on the `RotationZ` value.
13. `nextState`: Increments the `gameState` and resets the `stateTime`.
14. `is_duration`: Checks if the specified duration has passed based on the `stateTime`.
15. `gyro_follow`: Adjusts the robot's steering to follow a specified angle using the gyroscope.
16. `move_steering`: Adjusts the robot's wheel speeds based on the specified speed and steering values.
17. `checkpoint`: Stops the robot and turns on the LED to indicate a checkpoint.
18. `zRange`: Checks if the `RotationZ` value is within a specified range.
19. `invertzRange`: Placeholder function for inverting the `RotationZ` range.

Made changes.