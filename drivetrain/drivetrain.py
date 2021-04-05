"""
VexIQ Python API B for Robot Mesh.
"""


from __future__ import annotations
from vex import Motor
from vex import (DirectionType, DistanceUnits, RotationUnits, TimeUnits, VelocityUnits)


# CLASSES
# =======

class Drivetrain:
    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_travel: int = 200, track_width: int = 176, distanceUnits: DistanceUnits = DistanceUnits.MM, gear_ratio: double = 1.0):
        pass

    def drive(self, directionType: DirectionType, velocity: int =None, velocityUnits=VelocityUnits.PCT):
        """
        Turns the motors on and drives in the specified direction.
        """

    def drive_for(self, directionType: DirectionType, distance, distanceUnits: DistanceUnits = DistanceUnits.MM, velocity: int =None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        """
        Drives for a specified distance.
        """

    def start_drive_for(self, directionType: DirectionType, distance, distanceUnits: DistanceUnits = DistanceUnits.MM, velocity: int =None, velocityUnits=VelocityUnits.PCT):
        """
        Start driving for a specified distance.
        """

    def turn(self, turnType, velocity: int =None, velocityUnits=VelocityUnits.PCT):
        """
        Turn the drivetrain left or right.
        """

    def turn_for(self, turnType, angle, rotationUnits=RotationUnits.DEG, velocity: int =None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        """
        Turn the drivetrain left or right until the specified angle is reached.
        """

    def start_turn_for(self, turnType, angle, angleUnits=RotationUnits.DEG, velocity: int =None, velocityUnits=VelocityUnits.PCT):
        """
        Start turning the drivetrain left or right unitl the specified angle is reached.
        """

    def arcade(self, drivePower: int, turnPower: int):
        """
        Drive in arcade mode, normally corresponding to two controller joystick axis values.
        """

    def stop(self, brakeType=None):
        """
        Stops the drive using a specified brake mode.
        """

    def set_gear_ratio(self, gear_ratio):
        """
        Sets the external gear ratio of the drivetrain.
        """

    def set_drive_velocity(self, velocity, velocityUnits=VelocityUnits.PCT):
        """
        Sets the velocity of the drive.
        """

    def set_turn_velocity(self, velocity, velocityUnits=VelocityUnits.PCT):
        """
        Sets the velocity of the turn.
        """

    def set_timeout(self, time, timeUnits=TimeUnits.SEC):
        """
        Sets the timeout for the drivetrain.
        """

    def timeout(self, timeUnits=TimeUnits.SEC):
        """
        Returns a timeout in given time units.
        """

    def did_timeout(self):
        """
        True if the last drivetrain operation timed out, False otherwise.
        """

    def is_done(self):
        """
        True if drivetrain is done driving/turning to a specified target, False otherwise.
        """

    def set_stopping(self, brakeType):
        """
        Sets the stopping mode of the motor group by passing a brake mode as a parameter.
        """

    def velocity(self, velocityUnits=VelocityUnits.PCT):
        """
        Gets the average current velocity of all motors.
        """

    def current(self):
        """
        Gets the electrical current of all motors.
        """
