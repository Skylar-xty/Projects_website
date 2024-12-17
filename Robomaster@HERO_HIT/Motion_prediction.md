# Target Tracking and Aiming System in Complex Motion Environment
I was an algorithm designer and tester in my university's robotics team, participating in Robomaster University Championships Competition (organized by Dajiang Innovation), progressing from provincial and regional competitions to the national finals.

## Videos

Here are some videos during testing and real performance.

The Figure shows the UI of our robots when the target mobile armor was moving in both X, Y directions with different moving speeds.
Green notation meanings:

1. tracking: Now, the robot is tracking the same enemy robot.

2. target_X, target_Y, target_Z: THe world coordinate after conversion of the enemy armor center.

3. final_yaw, final_pitch: 

4. Armor_Type: 0 represents small size of armor, 1 represents big size of armor.

5. no gyro!: The target armor's motion is not in the "gyro" mode(which means doing self-rotation).

6. dir: right represents the target is moving right in the UI.

7. bullet_speed: the set bullet speed of our robot.

<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./test.mp4" type="video/mp4">
  Fig1: Mobile Armor Plate Recognition, Coordinate Computation, and Tracking UI Interface
</video>

This Figure shows the performance of our robot shooting the outpost (one kind of devices in the competition). The successful rate is 100%.
<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./demo1-1.mp4" type="video/mp4">
  The performance of the shooting algorithms.
</video>


<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./demo2-1.mp4" type="video/mp4">
</video>

This is part of the live streaming of one game in the National Robomaster Finals. And our team is the red side, you can focus on two number-five robots having one-to-one shooting.
<video width="640" height="360" controls style="display: block; margin: 20px auto;">
  <source src="./real.mp4" type="video/mp4">
</video>