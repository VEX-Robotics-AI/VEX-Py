"""Motor."""


from collections.abc import Sequence
from typing import Literal, Optional, overload
from typing_extensions import Self

from abm.decor import act, sense

from .._abstract_device import Device
from ..brain.port import Ports
from ..time import TimeUnits, SECONDS
from .._common_enums.numeric import NumType, PERCENT
from .._common_enums.rotation import RotationUnits, DEGREES

from .._util.doc import robotmesh_doc, vexcode_doc

from .brake_type import BrakeType, COAST, BRAKE, HOLD
from .current_units import CurrentUnits
from .direction_type import DirectionType, FORWARD, REVERSE
from .torque_units import TorqueUnits
from .turn_type import TurnType, LEFT, RIGHT
from .velocity_units import VelocityUnits, RPM, DPS


__all__: Sequence[str] = ('Motor',
                          'BrakeType', 'COAST', 'BRAKE', 'HOLD',
                          'CurrentUnits',
                          'DirectionType', 'FORWARD', 'REVERSE',
                          'TorqueUnits',
                          'TurnType', 'LEFT', 'RIGHT',
                          'VelocityUnits', 'RPM', 'DPS')


@robotmesh_doc("""
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_motor.html
""")
class Motor(Device):
    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    """Motor."""

    @robotmesh_doc("""
        Create new motor object on specified port and set reversed flag.

        Parameters:
        - index: The port index for this motor. The index is zero-based.
        - reverse: Sets the reverse flag for the new motor object.
    """)
    def __init__(self, index: Ports, reverse: bool = False, /):
        """Initialize Motor."""
        self.port: Ports = index
        self.reverse: bool = reverse

        self.rotations: dict[RotationUnits, float] = dict[RotationUnits, float]()  # noqa: E501
        self.stopping_mode: Optional[BrakeType] = None
        self.timeouts: dict[TimeUnits, NumType] = dict[TimeUnits, NumType]()
        self.max_torque: dict[TorqueUnits, NumType] = dict[TorqueUnits, NumType]()  # noqa: E501
        self.velocities: dict[VelocityUnits, NumType] = {PERCENT: 50}
        self.selected_velocity_unit: VelocityUnits = PERCENT

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, type(self)) and
                (other.port == self.port) and
                (other.reverse == self.reverse))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.port, self.reverse))

    def __repr__(self) -> str:
        """Return string representation."""
        return f'{type(self).__name__}({self.port.name}' + (', reverse)'
                                                            if self.reverse
                                                            else ')')

    def _get_selected_velocity_and_unit(
            self,
            velocity: Optional[float],
            unit: VelocityUnits) -> tuple[float, VelocityUnits]:
        if (velocity is None) or (not isinstance(velocity, float | int)):
            if self.selected_velocity_unit not in self.velocities:
                raise ValueError('You have not selected any velocity; '
                                 'please call '
                                 'set_velocity(velocity, velocityUnits) first')

            velocity = self.velocities[self.selected_velocity_unit]
            unit = self.selected_velocity_unit

        return (velocity, unit)

    @overload
    def spin(self, direction: DirectionType = FORWARD):
        ...

    @overload
    def spin(self,
             dir: DirectionType,  # pylint: disable=redefined-builtin
             velocity: Optional[float] = None,
             velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        ...

    @robotmesh_doc("""
        Turn on the motor and spins it.

        (in a specified direction and a specified velocity)

        Parameters:
        - dir: The direction to spin the motor, DirectionType enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
    """)
    @vexcode_doc("""
        Spin

        Spins an IQ Motor or Motor Group indefinitely.

        Choose which DIRECTION the Motor or Motor Group will spin to with
        either FORWARD or REVERSE as the parameter.
    """)
    def spin(self, direction: DirectionType = FORWARD,
             velocity: Optional[float] = None,
             velocity_unit: VelocityUnits = PERCENT):
        # pylint: disable=unused-argument
        """Spin in specified direction (at specified velocity)."""
        velocity, velocity_unit = self._get_selected_velocity_and_unit(
            velocity, velocity_unit)

        return self._spin(direction=direction,
                          velocity=velocity, velocity_unit=velocity_unit)

    @act
    def _spin(self, direction: DirectionType = FORWARD,
              velocity: float = 50, velocity_unit: VelocityUnits = PERCENT):
        """Spin in specified direction (at specified velocity)."""

    @overload
    def spin_for(self, direction: DirectionType = FORWARD,
                 angle: NumType = 90, /, units: RotationUnits = DEGREES,
                 wait: bool = True):
        ...

    @overload
    def spin_for(self, dir: DirectionType,  # pylint: disable=redefined-builtin
                 rotation: NumType,
                 rotationUnits: RotationUnits = RotationUnits.DEG,
                 velocity: Optional[float] = None,
                 velocityUnits: VelocityUnits = VelocityUnits.PCT,
                 waitForCompletion: bool = True, /) -> bool:
        ...

    @robotmesh_doc("""
        Turn on the motor and spins it.

        (to a relative target rotation value at a specified velocity)

        Parameters:
        - dir: The direction to spin the motor, DirectionType enum value.
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        - waitForCompletion: (Optional) If True, your program will wait
                             until the motor reaches the target rotational
                             value. If false, the program will continue after
                             calling this function.
                             By default, this parameter is true.

        Returns:
        Returns a Boolean that signifies when the motor
        has reached the target rotation value.
    """)
    @vexcode_doc("""
        Spin For

        This command spins an IQ Motor or Motor Group
        for a given amount of degrees or turns.

        Choose which DIRECTION the Motor or Motor Group will spin to:
        FORWARD or REVERSE.

        Choose the UNIT of measurement to be either DEGREES or TURNS.

        Choose whether or not this command should be waited on
        by proceeding commands by setting an optional fourth parameter
        to either wait=True or wait=False.

        By default, this command is a blocking command
        unless wait=False is passed as the fourth parameter.
    """)
    def spin_for(self, *args):
        """Spin for specified rotational angle."""
        if (n_args := len(args)) == 0:
            direction: DirectionType = FORWARD
            rotation: float = 90
            rotation_unit: RotationUnits = DEGREES
            velocity, velocity_unit = self._get_selected_velocity_and_unit(
                None, self.selected_velocity_unit)
            wait: bool = True

        elif n_args == 1:
            direction = args[0]
            rotation: float = 90
            rotation_unit: RotationUnits = DEGREES
            velocity, velocity_unit = self._get_selected_velocity_and_unit(
                None, self.selected_velocity_unit)
            wait: bool = True

        elif n_args == 2:
            direction, rotation = args
            rotation_unit: RotationUnits = DEGREES
            velocity, velocity_unit = self._get_selected_velocity_and_unit(
                None, self.selected_velocity_unit)
            wait: bool = True

        elif n_args == 3:
            direction, rotation, rotation_unit = args
            velocity, velocity_unit = self._get_selected_velocity_and_unit(
                None, self.selected_velocity_unit)
            wait: bool = True

        elif n_args == 4:
            # pylint: disable=unbalanced-tuple-unpacking
            direction, rotation, rotation_unit = args[:3]

            if isinstance(arg3 := args[3], bool):
                velocity, velocity_unit = self._get_selected_velocity_and_unit(
                    None, self.selected_velocity_unit)
                wait: bool = arg3

            else:
                assert isinstance(arg3, float | int)
                velocity: float = arg3
                velocity_unit: VelocityUnits = self.selected_velocity_unit
                wait: bool = True

        elif n_args == 5:
            direction, rotation, rotation_unit, velocity, velocity_unit = args
            wait: bool = True

        else:
            assert n_args == 6
            direction, rotation, rotation_unit, velocity, velocity_unit, wait = args  # noqa: E501

        if velocity is None:
            velocity, velocity_unit = self._get_selected_velocity_and_unit(
                None, self.selected_velocity_unit)

        return self._spin_for(direction=direction,
                              rotation=rotation, rotation_unit=rotation_unit,
                              velocity=velocity, velocity_unit=velocity_unit,
                              wait=wait)

    @act
    def _spin_for(
            self, direction: DirectionType = FORWARD,
            rotation: NumType = 90, rotation_unit: RotationUnits = DEGREES,
            velocity: Optional[float] = None, velocity_unit: VelocityUnits = PERCENT,  # noqa: E501
            wait: bool = True):
        # pylint: disable=too-many-arguments
        """Spin for specified rotational angle."""

    @vexcode_doc("""
        Spin To Position

        Spins an IQ Motor or Motor Group to a given position.

        This command will tell a Motor or Motor Group to travel to a specific
        position. Based on the current position of the Motor or Motor Group,
        Spin To Position will determine the direction to rotate the Motor or
        Motor Group.

        Choose the unit of measurement to be either DEGREES or TURNS.

        Choose whether or not this command should be waited on by other
        commands by changing the optional third parameter to either
        wait=True or wait=False.

        Setting wait=True means that proceeding commands will not execute until
        the motor spin is completed.
        Conversely, wait=False will not wait for it to be completed.

        By default, this command will have the wait to be set to True.
    """)
    @act
    def spin_to_position(self,
                         angle: NumType = 90, /, units: RotationUnits = DEGREES,  # noqa: E501
                         wait: bool = True):
        """Spin motor to specified rotational angle."""

    @robotmesh_doc("""
        Stop the motor using the default brake mode.

        Parameters:
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
    """)
    @vexcode_doc("""
        Stop Motor

        Stops an IQ Motor or Motor Group.
    """)
    @act
    def stop(self, brakeType: Optional[BrakeType] = None, /):
        """Stop."""

    @vexcode_doc("""
        Set Motor Position

        Sets an IQ Motor's or Motor Group's encoder(s) position
        to the given position value.

        This command can be used to set a Motor or Motor Group's position
        to a given positional value.

        Usually, the Set Motor Position command is used to set the position to
        0 to reset a Motor or Motor Group's encoder position(s).

        The Set Motor Position command accepts DEGREES or TURNS as valid UNITS.
    """)
    @act
    def set_position(self, value: float = 0, unit: RotationUnits = DEGREES, /):  # noqa: E501
        """Set rotation position to specified value."""

    @robotmesh_doc("""
        Set velocity of the motor based on the parameters set in the command.

        This command will not run the motor.
        Any subsequent call that does not contain
        a specified motor velocity will use this value.

        Parameters:
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
    """)
    @vexcode_doc("""
        Set Motor Velocity

        Sets the speed of an IQ Motor or Motor Group.

        This command accepts a range
        from -100 to 100 when used with the PERCENT parameter
        or -127 to 127 when used with RPM.

        Setting an IQ Motor or Motor Group's velocity to a negative value
        will cause the Motor/Motor Group to spin in reverse.

        Setting velocity to 0 will prevent the Motor/Motor Group from spinning.
    """)
    def set_velocity(self, velocity: float = 50, unit: VelocityUnits = PERCENT, /):  # noqa: E501
        """Set velocity."""
        self.velocities[unit] = velocity
        self.selected_velocity_unit = unit
        return self._set_velocity(velocity, unit)

    @act
    def _set_velocity(self, velocity: float = 50, unit: VelocityUnits = PERCENT, /):  # noqa: E501
        """Set velocity."""

    @overload
    def set_stopping(self, value: BrakeType, /):
        ...

    @overload
    def set_stopping(self, brakeType: BrakeType, /):
        ...

    @robotmesh_doc("""
        Set stopping mode of the motor by passing a brake mode as a parameter.

        (note this will stop the motor if it's spinning)

        Parameters:
        - brakeType: The stopping mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
    """)
    @vexcode_doc("""
        Set Motor Stopping

        Sets the behavior of an IQ Motor or Motor Group once it stops moving.

        The MODE parameter can be replaced with any of the following options:
        - BRAKE: will cause the Motor/Motor Group to come to an immediate stop.
        - COAST: lets the Motor/Motor Group spin gradually to a stop.
        - HOLD: will cause the Motor/Motor Group to come to an immediate stop,
                and returns it to its stopped position if moved.

        The stopping behavior set by this command will apply to subsequent
        Motor/Motor Group Stop commands for the entirety of the project,
        unless otherwise changed.
    """)
    @act
    def set_stopping(self, mode: BrakeType, /):
        """Set stopping mode."""
        self.stopping_mode: BrakeType = mode

    @robotmesh_doc("""
        Set the max torque of the motor.

        Parameters:
        - value: Sets the amount of torque (max 0.414 Nm)
        - torqueUnits: The measurement unit for the torque value.
    """)
    @vexcode_doc("""
        Set Motor Torque

        Sets the strength of an IQ Motor or Motor Group.

        This command accepts a range of 0 to 100 for the AMOUNT parameter.

        The Set Max Torque command accepts decimals, integers or numerics.
    """)
    @act
    def set_max_torque(self, amount_value: float = 50,
                       unit: TorqueUnits = PERCENT, /):  # noqa: E501
        """Set max torque."""
        self.max_torque[unit] = amount_value

    @robotmesh_doc("""
        Set the timeout for the motor.

        If the motor does not reach its commanded position prior
        to the completion of the timeout, the motor will stop.

        Parameters:
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time, a TimeUnits enum value.
    """)
    @vexcode_doc("""
        Set Motor Timeout

        Sets a time limit for an IQ Motor or Motor Group movement commands.

        A Motor or Motor Group's Set Motor Timeout command is used to prevent
        motion commands that do not reach their intended position from
        preventing subsequent commands from running.

        An example of a Motor not reaching its position is an Arm or Claw that
        reaches its mechanical limit and cannot complete its movement.
    """)
    @act
    def set_timeout(self, time: float, unit: Literal[SECONDS] = SECONDS, /):
        """Set Motor Timeout Threshold."""
        self.timeouts[unit] = time

    @robotmesh_doc("""
        Set the motor mode to "reverse".

        (which will make motor commands
        spin the motor in the opposite direction)

        Parameters:
        - is_reversed: If set to True, motor commands
                       spin the motor in the opposite direction.
    """)
    @act
    def set_reversed(self, is_reversed: bool, /):
        """Set reversed mode."""
        self.reverse: bool = is_reversed

    @robotmesh_doc("""
        Reset the motor's encoder to the value of zero.
    """)
    @act
    def reset_rotation(self):
        """Reset motor rotation value to 0."""
        for rotation_unit in self.rotations:
            self.rotations[rotation_unit] = 0

    @robotmesh_doc("""
        Set value of motor's encoder to value specified in parameter.

        Parameters:
        - value: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation,
                         a RotationUnits enum value.
    """)
    @act
    def set_rotation(self, value: float,
                     rotationUnits: RotationUnits = RotationUnits.DEG, /):
        """Set motor rotation value to specific value."""
        self.rotations[rotationUnits] = value

    @robotmesh_doc("""
        Return a timeout in given time units.
    """)
    @sense
    def timeout(self, timeUnits: TimeUnits = TimeUnits.SEC, /) -> float:
        """Return motor timeout."""
        return self.timeouts[timeUnits]

    @robotmesh_doc("""
        Return True if the last motor operation timed out.
    """)
    @sense
    def did_timeout(self) -> bool:
        """Return whether motor timed out."""

    @robotmesh_doc("""
        Turn on the motor and spins it.

        (to an absolute target rotation value at a specified velocity)

        Parameters:
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
        - waitForCompletion: (Optional) If True, your program will wait
                             until the motor reaches the target rotational
                             value. If false, the program will continue after
                             calling this function.
                             By default, this parameter is true.
    """)
    @act
    def spin_to(self,
                rotation: float,
                rotationUnits: RotationUnits = RotationUnits.DEG,
                velocity: Optional[float] = None,
                velocityUnits: VelocityUnits = VelocityUnits.PCT,
                waitForCompletion: bool = True, /) -> bool:
        """Spin motor to target rotation angle value."""

    @robotmesh_doc("""
        Turn on the motor and spins it.

        (to a relative target time value at a specified velocity)

        Parameters:
        - dir: direction to spin in, a DirectionType enum value or None.
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
    """)
    @act
    def spin_for_time(self,
                      dir: DirectionType,  # pylint: disable=redefined-builtin
                      time: str,
                      timeUnits: TimeUnits = TimeUnits.SEC,
                      velocity: Optional[float] = None,
                      velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Spin motor for a certain time duration."""

    @robotmesh_doc("""
        Start spinning a motor.

        (to an absolute target rotation
        but does not wait for the motor to reach that target)

        Params:
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
    """)
    @act
    def start_spin_to(self,
                      rotation: float,
                      rotationUnits: RotationUnits = RotationUnits.DEG,
                      velocity: Optional[float] = None,
                      velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning motor to a certain target rotation angle value."""

    @robotmesh_doc("""
        Start spinning a motor.

        (to a relative target rotation
        but does not wait for the motor to reach that target)

        Parameters:
        - dir: direction to spin in, a DirectionType enum value or None.
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity value.
    """)
    @act
    def start_spin_for(self,
                       dir: DirectionType,  # pylint: disable=redefined-builtin
                       rotation: float,
                       rotationUnits: RotationUnits = RotationUnits.DEG,
                       velocity: Optional[float] = None,
                       velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning motor for a certain rotation angle value."""

    @robotmesh_doc("""
        Determine if a spin_for/spin_to command is in progress.

        Returns:
        True if the motor is on and is rotating to a target,
        False if the motor is done rotating to a target.
    """)
    @sense
    def is_spinning(self) -> bool:
        """Check if motor is still spinning."""

    @robotmesh_doc("""
        Determine if spin_for/spin_to command has reached its target position.

        Returns:
        False if the motor is on and is rotating
        to a target, True if the motor is done rotating to a target.
    """)
    @sense
    def is_done(self) -> bool:
        """Check if motor has finished spinning."""

    @robotmesh_doc("""
        Set the max torque of the motor as a percentage.

        Parameters:
        - value: Sets the amount of torque (0 to 100%)
    """)
    @act
    def set_max_torque_percent(self, value: float, /):
        """Set max torque percent."""
        self.max_torque[TorqueUnits.PCT] = value

    @robotmesh_doc("""
        Set the max torque of the motor.

        Parameters:
        - value: Sets the amount of torque in Amps (max 1.2A)
    """)
    @act
    def set_max_torque_current(self, value: float, /):
        """Set max torque current."""
        # pylint: disable=attribute-defined-outside-init
        self.max_torque_current: float = value

    @robotmesh_doc("""
        Get the current rotation of the motor's encoder.

        Parameters:
        rotationUnits: The measurement unit for the rotation.

        Returns:
        a float that represents the current rotation of
        the motor in the units defined in the parameter.
    """)
    @sense
    def rotation(self, rotationUnits: RotationUnits = RotationUnits.DEG, /) -> float:  # noqa: E501
        """Return motor's cumulative rotation angle value."""

    @robotmesh_doc("""
        Get the current velocity of the motor.

        Parameters:
        - velocityUnits: The measurement unit for the velocity.

        Returns:
        a float that represents the current velocity
        of the motor in the units defined in the parameter.
    """)
    @sense
    def velocity(self, velocityUnits: VelocityUnits = VelocityUnits.PCT, /) -> float:  # noqa: E501
        """Return motor's velocity."""

    @robotmesh_doc("""
        Get the electrical current of the motor.

        Returns:
        a float that represents the electrical current of the motor in Amps.
    """)
    @sense
    def current(self) -> float:
        """Return motor's electrical current."""
