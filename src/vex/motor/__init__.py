"""Motor."""


from collections.abc import Sequence
from typing import Any, Literal, LiteralString, Optional, Self, overload

from abm.decor import act, sense

from .._device import Device
from .._device.v5 import V5DeviceType
from ..brain.port import Ports
from ..time import TimeUnits, SECONDS
from .._common_enums.percent import PercentUnits, PERCENT
from .._common_enums.rotation import RotationUnits, DEGREES
from .._common_enums.temperature import TemperatureUnits
from .._common_enums.velocity import VelocityUnits

from .brake import BrakeType, COAST, BRAKE, HOLD
from .current import CurrentUnits
from .direction import DirectionType, FORWARD, REVERSE
from .gear import GearSetting
from .torque import TorqueUnits
from .turn import TurnType, LEFT, RIGHT
from .voltage import VoltageUnits

from .._util.doc import robotmesh_doc, vexcode_doc
from .._util.type import Num


__all__: Sequence[LiteralString] = ('Motor',
                                    'BrakeType', 'COAST', 'BRAKE', 'HOLD',
                                    'CurrentUnits',
                                    'DirectionType', 'FORWARD', 'REVERSE',
                                    'GearSetting',
                                    'TorqueUnits',
                                    'TurnType', 'LEFT', 'RIGHT',
                                    'VoltageUnits')


@robotmesh_doc("""
    Robot Mesh VEX IQ Python B:
    robotmesh.com/studio/content/docs/vexiq-python_b/html/classvex_1_1_motor.html

    Robot Mesh VEX V5 Python:
    robotmesh.com/studio/content/docs/vexv5-python/html/classvex_1_1_motor.html
""")
class Motor(Device):
    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    """Motor."""

    @overload
    def __init__(self: Self, index: Ports, reverse: bool = False, /) -> None:
        """Initialize Motor."""

    @overload
    def __init__(self: Self,
                 index: Ports,
                 gearSetting: GearSetting = GearSetting.RATIO18_1,
                 reverse: bool = False, /) -> None:
        """Initialize Motor with Gear Setting."""

    @robotmesh_doc("""
        Creates new motor object on specified port.

        Parameters
        - index: Port index for this motor. The index is zero-based.
        - gearSetting (if specified): Sets gear setting.
        - reverse: Sets reverse flag.
    """)
    def __init__(self: Self, index: Ports, /, *args: GearSetting | bool) -> None:  # noqa: E501
        """Initialize Motor."""
        self.port: Ports = index

        if (n_args := len(args)) == 0:
            self.gear_setting: Optional[GearSetting] = None

            self.reverse: bool = False

        elif n_args == 1:
            self.gear_setting: Optional[GearSetting] = None

            self.reverse: bool = args[0]

            assert isinstance(self.reverse, bool), \
                TypeError(f'*** 2ND ARG {self.reverse} NOT BOOLEAN ***')

        else:
            assert n_args == 2

            self.gear_setting, self.reverse = args

            assert isinstance(self.gear_setting, GearSetting), \
                TypeError(f'*** 2ND ARG {self.gear_setting} NOT GearSetting ***')  # noqa: E501

            assert isinstance(self.reverse, bool), \
                TypeError(f'*** 3ND ARG {self.reverse} NOT BOOLEAN ***')

        self._rotation: dict[RotationUnits, float] = dict[RotationUnits, float]()  # noqa: E501

        self.selected_velocity_unit: VelocityUnits = PERCENT
        self._velocity: dict[VelocityUnits, Num] = {PERCENT: 50}

        self.stopping_mode: Optional[BrakeType] = None

        self._timeout: dict[TimeUnits, Num] = dict[TimeUnits, Num]()

        self.max_torque: dict[TorqueUnits, Num] = dict[TorqueUnits, Num]()  # noqa: E501
        self.max_torque_current: Optional[float] = None

    def __eq__(self: Self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, type(self)) and
                (other.port == self.port) and
                (other.gear_setting == self.gear_setting) and
                (other.reverse == self.reverse))

    def __hash__(self: Self) -> int:
        """Return integer hash."""
        return hash((self.port, self.gear_setting, self.reverse))

    def __repr__(self: Self) -> str:
        """Return string representation."""
        return f'{type(self).__name__}({self.port.name}' + (', reverse)'
                                                            if self.reverse
                                                            else ')')

    @robotmesh_doc("""
        Use this function to reverse setting for the motor.

        Sets the motor mode to "reverse",
        which will make motor commands spin the motor in the opposite direction

        Parameters
        - is_reversed / isReversed: If set to True, motor commands
                                    spin the motor in the opposite direction
    """)
    @act
    def set_reversed(self: Self, is_reversed: bool, /):
        """Set reversed mode."""
        assert isinstance(is_reversed, bool), \
            TypeError('*** is_reversed={is_reversed} NOT A BOOL ***')

        self.reverse: bool = is_reversed

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
    def set_position(self: Self, position: Num, unit: RotationUnits, /):
        """Set rotational angle to specified position."""
        assert isinstance(position, Num), \
            TypeError(f'*** position {position} NEITHER A FLOAT NOR AN INT ***')  # noqa: E501

        assert isinstance(unit, RotationUnits), \
            TypeError(f'*** unit {unit} NOT ONE OF RotationUnits ***')

    @robotmesh_doc("""
        Sets value of motor's encoder to value specified in parameter.

        Parameters
        - value: amount of rotation
        - rotationUnits: measurement unit for the rotation,
                         a RotationUnits enum value.
    """)
    @act
    def set_rotation(self: Self, value: Num,
                     rotationUnits: RotationUnits = RotationUnits.DEG, /):
        """Set rotational angle to specified value."""
        assert isinstance(value, Num), \
            TypeError(f'*** value {value} NEITHER A FLOAT NOR AN INT ***')

        assert isinstance(rotationUnits, RotationUnits), \
            TypeError(f'*** rotationUnits {rotationUnits} '
                      'NOT ONE OF RotationUnits ***')

        self._rotation[rotationUnits] = value

    @robotmesh_doc("""
        Resets the motor's encoder to the value of zero.
    """)
    @act
    def reset_rotation(self: Self):
        """Reset rotational angle to 0."""
        for rotation_unit in self._rotation:
            self._rotation[rotation_unit] = 0

    @overload
    def set_velocity(self: Self, value: Num, unit: VelocityUnits = PERCENT, /):  # noqa: E501
        ...

    @overload
    def set_velocity(self: Self, velocity: Num,
                     velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        ...

    @robotmesh_doc("""
        Sets the velocity of the motor
        based on the parameters set in the command.

        This command will not run the motor.
        Any subsequent call that does not contain a specified motor velocity
        will use this value.

        Parameters
        - velocity: amount of velocity
        - velocityUnits: measurement unit for velocity,
                         a VelocityUnits enum value
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
    @act
    def set_velocity(self: Self,
                     value: Num, unit: VelocityUnits = PERCENT, /):
        """Set velocity."""
        assert isinstance(value, Num), \
            TypeError(f'*** value {value} NEITHER A FLOAT NOR AN INT ***')

        assert (unit is PERCENT) or isinstance(unit, VelocityUnits), \
            TypeError(f'*** unit {unit} NOT ONE OF VelocityUnits ***')

        self.selected_velocity_unit: VelocityUnits = unit
        self._velocity[unit]: Num = value

    @overload
    def set_stopping(self: Self, value: BrakeType, /):
        ...

    @overload
    def set_stopping(self: Self, brakeType: BrakeType, /):
        ...

    @robotmesh_doc("""
        Sets stopping mode of the motor by passing a brake mode as a parameter.

        (note this will stop the motor if it's spinning)

        Parameters
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
    def set_stopping(self: Self, mode: BrakeType, /):
        """Set stopping mode."""
        assert isinstance(mode, BrakeType), \
            TypeError('*** mode MUST BE A BrakeType ***')

        self.stopping_mode: BrakeType = mode

    @overload
    def set_timeout(self: Self, value: Num, /, units: Literal[SECONDS]):
        ...

    @overload
    def set_timeout(self: Self,
                    time: Num, timeUnits: TimeUnits = TimeUnits.SEC, /):
        ...

    @robotmesh_doc("""
        Sets the timeout for the motor.

        If the motor does not reach its commanded position
        prior to the completion of the timeout, the motor will stop.

        Parameters
        - time: amount of time
        - timeUnits: measurement unit for the time, a TimeUnits enum value
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
    def set_timeout(self: Self, value: Num, unit: Literal[SECONDS], /):
        """Set timeout."""
        assert isinstance(value, Num), \
            TypeError(f'*** value {value} NEITHER A FLOAT NOR AN INT ***')
        assert value > 0, ValueError('*** value MUST BE POSITIVE ***')

        assert unit is SECONDS, ValueError('*** unit MUST BE SECONDS ***')

        self._timeout[unit] = value

    @robotmesh_doc("""
        Returns a timeout in given time unit.
    """)
    def timeout(self: Self, timeUnits: TimeUnits = TimeUnits.SEC, /) -> Num:  # noqa: E501
        """Return timeout."""
        assert isinstance(timeUnits, TimeUnits), \
            TypeError('*** timeUnits MUST BE ONE OF TimeUnits ***')

        return self._timeout[timeUnits]

    @overload
    def set_max_torque(self: Self, value: Num, unit: Literal[PERCENT], /):
        ...

    @overload
    def set_max_torque(self: Self, value: Num,
                       torqueUnits: TorqueUnits = TorqueUnits.NM, /):
        ...

    @robotmesh_doc("""
        Sets the max torque of the motor.

        Parameters
        - value: amount of torque (max 0.414 Nm)
        - torqueUnits: measurement unit for torque
    """)
    @vexcode_doc("""
        Set Motor Torque

        Sets the strength of an IQ Motor or Motor Group.

        This command accepts a range of 0 to 100 for the AMOUNT parameter.

        The Set Max Torque command accepts decimals, integers or numerics.
    """)
    @act
    def set_max_torque(self: Self,
                       value: Num, unit: Literal[PERCENT] | TorqueUnits, /):  # noqa: E501
        """Set max torque."""
        assert isinstance(value, Num), \
            TypeError(f'*** value {value} NEITHER A FLOAT NOR AN INT ***')
        assert value > 0, ValueError('*** value MUST BE POSITIVE ***')

        assert (unit is PERCENT) or isinstance(unit, TorqueUnits), \
            TypeError('*** unit MUST BE ONE OF TorqueUnits ***')

        self.max_torque[unit] = value

    @robotmesh_doc("""
        Sets the max torque of the motor as a percentage.

        Parameters
        - value: amount of torque (0 to 100%)
    """)
    @act
    def set_max_torque_percent(self: Self, value: int, /):
        """Set max torque percent."""
        assert isinstance(value, int), TypeError('*** value MUST BE int ***')
        assert 1 <= value <= 100, ValueError('*** value MUST BE 1-100 ***')

        self.max_torque[PERCENT] = value

    @robotmesh_doc("""
        Sets the max torque of the motor.

        Parameters
        - value: amount of torque in Amps (max 1.2A)
    """)
    @act
    def set_max_torque_current(self: Self, value: float, /):
        """Set max torque current."""
        assert isinstance(value, Num), \
            TypeError(f'*** value {value} NEITHER A FLOAT NOR AN INT ***')
        assert value <= 1.2, ValueError(f'*** value {value} NOT 1.2 OR LESS ***')  # noqa: E501

        self.max_torque_current: float = value

    def _resolve_velocity_and_unit(self: Self,
                                   velocity: Optional[Num],
                                   velocity_unit: Optional[VelocityUnits], /) \
            -> tuple[Num, VelocityUnits]:
        if velocity is None:
            if velocity_unit is None:
                assert self.selected_velocity_unit in self._velocity, \
                    ValueError('*** NO VELOCITY SET YET; '
                               'PLEASE CALL set_velocity(...) FIRST ***')

                return (self._velocity[self.selected_velocity_unit],
                        self.selected_velocity_unit)

            assert ((velocity_unit is PERCENT) or
                    isinstance(velocity_unit, VelocityUnits)), \
                TypeError(f'*** velocity_unit {velocity_unit} '
                          'NOT ONE OF VelocityUnits ***')

            assert velocity_unit in self._velocity, \
                ValueError(f'*** NO VELOCITY SET FOR UNIT {velocity_unit} YET;'
                           ' PLEASE CALL set_velocity(...) FIRST ***')

            return self._velocity[velocity_unit], velocity_unit

        assert isinstance(velocity, Num), \
            TypeError('*** velocity {velocity} NEITHER None, A FLOAT NOR AN INT ***')  # noqa: E501

        return velocity, velocity_unit

    @overload
    def spin(self: Self, direction: DirectionType):
        ...

    @overload
    def spin(self: Self,
             dir: DirectionType,  # pylint: disable=redefined-builtin
             velocity: Optional[Num] = None,
             velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        ...

    @robotmesh_doc("""
        Turns on the motor and spins it in a specified direction
        and a specified velocity.

        Parameters
        - dir: direction to spin the motor, DirectionType enum
        - velocity: amount of velocity
        - velocityUnits: measurement unit for velocity, VelocityUnits enum
    """)
    @vexcode_doc("""
        Spin

        Spins an IQ Motor or Motor Group indefinitely.

        Choose which DIRECTION the Motor or Motor Group will spin to with
        either FORWARD or REVERSE as the parameter.
    """)
    def spin(self: Self, direction: DirectionType,
             velocity: Optional[Num] = None,
             velocity_unit: VelocityUnits = PERCENT):
        """Spin in specified direction (at specified velocity)."""
        assert isinstance(direction, DirectionType), \
            TypeError('*** direction {direction} NOT A DirectionType ***')

        assert (velocity is None) or isinstance(velocity, Num), \
            TypeError('*** velocity {velocity} NEITHER None, A FLOAT NOR AN INT ***')  # noqa: E501

        assert ((velocity_unit is PERCENT) or
                isinstance(velocity_unit, VelocityUnits)), \
            TypeError(f'*** velocity_unit {velocity_unit} '
                      'NOT ONE OF VelocityUnits ***')

        velocity, velocity_unit = self._resolve_velocity_and_unit(
            velocity, velocity_unit)

        return self._spin(direction=direction,
                          velocity=velocity, velocity_unit=velocity_unit)

    @act
    def _spin(self: Self, direction: DirectionType,
              velocity: Num, velocity_unit: VelocityUnits):
        """Spin in specified direction (at specified velocity)."""

    @overload
    def spin_for(self: Self, direction: DirectionType,
                 angle: Num, /, units: RotationUnits = DEGREES,
                 wait: bool = True):
        ...

    @overload
    def spin_for(
            self,
            dir: Optional[DirectionType],  # pylint: disable=redefined-builtin
            rotation: Num,
            rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[Num] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        ...

    @robotmesh_doc("""
        Turns on the motor and spins it to a relative target rotation value
        at a specified velocity.

        Returns
        True if motor has reached the target rotation value, False otherwise

        Parameters
        - dir: direction to spin in, DirectionType enum value or None
        - rotation: amount of rotation
        - rotationUnits: measurement unit for rotation
        - velocity: amount of velocity
        - velocityUnits: measurement unit for velocity
        - waitForCompletion: (Optional) If True, your program will wait
                             until the motor reaches the target rotational
                             value. If false, the program will continue after
                             calling this function.
                             By default, this parameter is true.
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
    def spin_for(self: Self, direction: DirectionType,
                 rotation: Num, rotation_unit: RotationUnits = DEGREES, /,
                 velocity: Optional[Num] = None,
                 velocity_unit: Optional[VelocityUnits] = None,
                 wait: bool = True):
        # pylint: disable=too-many-arguments
        """Spin for specified rotational angle."""
        assert isinstance(direction, DirectionType), \
            TypeError('*** direction {direction} NOT A DirectionType ***')

        assert isinstance(rotation, Num), \
            TypeError('*** rotation {rotation} NEITHER A FLOAT NOR AN INT ***')

        assert isinstance(rotation_unit, RotationUnits), \
            TypeError(f'*** rotation_unit {rotation_unit} '
                      'NOT ONE OF RotationUnits ***')

        if isinstance(velocity, bool):
            wait: bool = velocity
            velocity: Optional[Num] = None
            velocity_unit: Optional[VelocityUnits] = None

        assert (velocity is None) or isinstance(velocity, Num), \
            TypeError('*** velocity {velocity} NEITHER None, A FLOAT NOR AN INT ***')  # noqa: E501

        assert ((velocity_unit in (None, PERCENT)) or
                isinstance(velocity_unit, VelocityUnits)), \
            TypeError(f'*** velocity_unit {velocity_unit} '
                      'NOT ONE OF VelocityUnits ***')

        assert isinstance(wait, bool), TypeError(f'*** wait {wait} NOT A BOOL ***')  # noqa: E501

        velocity, velocity_unit = self._resolve_velocity_and_unit(
            velocity, self.selected_velocity_unit)

        return self._spin_for(direction=direction,
                              rotation=rotation, rotation_unit=rotation_unit,
                              velocity=velocity, velocity_unit=velocity_unit,
                              wait=wait)

    @act
    def _spin_for(self: Self, direction: DirectionType,
                  rotation: Num, rotation_unit: RotationUnits,
                  velocity: Num, velocity_unit: VelocityUnits, wait: bool):
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
    def spin_to_position(self: Self,
                         angle: Num, /, units: RotationUnits = DEGREES,
                         wait: bool = True):
        """Spin to specified rotational angle."""
        assert isinstance(angle, Num), \
            TypeError(f'*** angle {angle} NEITHER A FLOAT NOR AN INT ***')

        assert isinstance(units, RotationUnits), \
            TypeError(f'*** units {units} NOT ONE OF RotationUnits ***')

        assert isinstance(wait, bool), TypeError(f'*** wait {wait} NOT A BOOL ***')  # noqa: E501

    @robotmesh_doc("""
        Turns on the motor and spins it to an absolute target rotation value
        at a specified velocity.

        Returns
        a Boolean signifying when motor has reached target rotation value.

        Parameters
        - rotation: amount of rotation
        - rotationUnits: measurement unit for rotation
        - velocity: amount of velocity
        - velocityUnits: measurement unit for velocity
        - waitForCompletion: (Optional) If True, your program will wait
                             until the motor reaches the target rotational
                             value. If false, the program will continue after
                             calling this function.
                             By default, this parameter is true.
    """)
    @act
    def spin_to(self: Self,
                rotation: Num,
                rotationUnits: RotationUnits = RotationUnits.DEG,
                velocity: Optional[Num] = None,
                velocityUnits: VelocityUnits = VelocityUnits.PCT,
                waitForCompletion: bool = True, /) -> bool:
        """Spin motor to target rotation angle value."""
        assert isinstance(rotation, Num), \
            TypeError(f'*** rotation {rotation} NEITHER A FLOAT NOR AN INT ***')  # noqa: E501

        assert isinstance(rotationUnits, RotationUnits), \
            TypeError(f'*** rotationUnits {rotationUnits} '
                      'NOT ONE OF RotationUnits ***')

        assert (velocity is None) or isinstance(velocity, Num), \
            TypeError('*** velocity {velocity} NEITHER None, A FLOAT NOR AN INT ***')  # noqa: E501

        assert isinstance(velocityUnits, VelocityUnits), \
            TypeError(f'*** velocityUnits {velocityUnits} '
                      'NOT ONE OF VelocityUnits ***')

        assert isinstance(waitForCompletion, bool), \
            TypeError(f'*** waitForCompletion {waitForCompletion} NOT A BOOL ***')  # noqa: E501

    @robotmesh_doc("""
        Turns on the motor and spins it
        to a relative target time value at a specified velocity.

        Parameters
        - dir: direction to spin in, a DirectionType enum value or None
        - time: amount of time.
        - timeUnits: measurement unit for time
        - velocity: amount of velocity
        - velocityUnits: measurement unit for velocity
    """)
    @act
    def spin_for_time(
            self,
            dir: Optional[DirectionType],  # pylint: disable=redefined-builtin
            time: Num,
            timeUnits: TimeUnits = TimeUnits.SEC,
            velocity: Optional[Num] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Spin for specified duration."""
        assert (dir is None) or isinstance(dir, DirectionType), \
            TypeError('*** dir MUST BE None OR A DirectionType ***')

        assert isinstance(time, Num), \
            TypeError('*** time MUST BE A float OR AN int ***')

        assert isinstance(timeUnits, TimeUnits), \
            TypeError('*** timeUnits MUST BE ONE OF TimeUnits ***')

        assert (velocity is None) or isinstance(velocity, Num), \
            TypeError('*** velocity MUST BE None, A float OR AN int ***')

        assert ((velocityUnits is PERCENT) or
                isinstance(velocityUnits, VelocityUnits)), \
            TypeError('**** velocityUnits MUST BE ONE OF VelocityUnits ***')

    @robotmesh_doc("""
        Starts spinning a motor to a relative target rotation
        but does not wait for the motor to reach that target.

        Parameters
        - dir: direction to spin in, a DirectionType enum value or None
        - rotation: amount of rotation
        - rotationUnits: measurement unit for rotation
        - velocity: amount of velocity
        - velocityUnits: measurement unit for velocity
    """)
    @act
    def start_spin_for(
            self,
            dir: Optional[DirectionType],  # pylint: disable=redefined-builtin
            rotation: Num,
            rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[Num] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning for specified rotational angle."""
        assert (dir is None) or isinstance(dir, DirectionType), \
            TypeError(f'*** dir {dir} NEITHER None NOR A DirectionType ***')

        assert isinstance(rotation, Num), \
            TypeError(f'*** rotation {rotation} NEITHER A FLOAT NOR AN INT ***')  # noqa: E501

        assert isinstance(rotationUnits, RotationUnits), \
            TypeError(f'*** rotationUnits {rotationUnits} '
                      'NOT ONE OF RotationUnits ***')

        assert (velocity is None) or isinstance(velocity, Num), \
            TypeError(f'*** velocity {velocity} NEITHER None, A FLOAT OR AN INT ***')  # noqa: E501

        assert ((velocityUnits is PERCENT) or
                isinstance(velocityUnits, VelocityUnits)), \
            TypeError(f'**** velocityUnits {velocityUnits} '
                      'NOT ONE OF VelocityUnits ***')

    @robotmesh_doc("""
        Starts spinning a motor to an absolute target rotation
        but does not wait for the motor to reach that target.

        Parameters
        - rotation: amount of rotation
        - rotationUnits: measurement unit for rotation
        - velocity: amount of velocity
        - velocityUnits: measurement unit for velocity
    """)
    @act
    def start_spin_to(self: Self,
                      rotation: Num,
                      rotationUnits: RotationUnits = RotationUnits.DEG,
                      velocity: Optional[Num] = None,
                      velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning to specified target rotational angle."""
        assert isinstance(rotation, Num), \
            TypeError(f'*** rotation {rotation} NEITHER A FLOAT OR AN INT ***')

        assert isinstance(rotationUnits, RotationUnits), \
            TypeError(f'*** rotationUnits {rotationUnits} '
                      'NOT ONE OF RotationUnits ***')

        assert (velocity is None) or isinstance(velocity, Num), \
            TypeError(f'*** velocity {velocity} NEITHER None, A FLOAT NOR AN INT ***')  # noqa: E501

        assert ((velocityUnits is PERCENT) or
                isinstance(velocityUnits, VelocityUnits)), \
            TypeError(f'**** velocityUnits {velocityUnits} '
                      'NOT ONE OF VelocityUnits ***')

    @overload
    def stop(self: Self):
        ...

    @overload
    def stop(self: Self, brakeType: Optional[BrakeType] = None, /):
        ...

    @robotmesh_doc("""
        Stops the motor using the default brake mode.

        Parameters
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
    """)
    @vexcode_doc("""
        Stop Motor

        Stops an IQ Motor or Motor Group.
    """)
    def stop(self: Self, mode: Optional[BrakeType] = None, /):
        """Stop."""
        assert (mode is None) or isinstance(mode, BrakeType), \
            TypeError(f'*** mode {mode} NEITHER None NOR A BrakeType ***')

        self._stop(self.stopping_mode
                   if (mode is None) and (self.stopping_mode is not None)
                   else mode)

    @act
    def _stop(self: Self, mode: Optional[BrakeType] = None, /):
        """Stop."""
        assert (mode is None) or isinstance(mode, BrakeType), \
            TypeError(f'*** mode {mode} NEITHER None NOR A BrakeType ***')

    @robotmesh_doc("""
        Determines if spin_for/spin_to command has reached its target position.

        Returns:
        False if the motor is on and is rotating to a target,
        True if the motor is done rotating to a target.
    """)
    @vexcode_doc("""
        Motor Is Done

        Reports if an IQ Motor or Motor Group has completed its movement.

        Motor Is Done reports True when the selected Motor or Motor Group
        has completed its movement.

        Motor Is Done reports False when the selected Motor or Motor Group
        is still moving.
    """)
    @sense
    def is_done(self: Self) -> bool:
        """Check whether motor has finished spinning."""

    @robotmesh_doc("""
        Determines if a spin_for/spin_to command is in progress.

        Returns:
        True if the motor is on and is rotating to a target,
        False if the motor is done rotating to a target.
    """)
    @vexcode_doc("""
        Motor Is Spinning

        Reports if an IQ Motor or Motor Group is currently spinning.

        Motor Is Spinning reports True when the selected Motor or Motor Group
        is still moving.

        Motor Is Spinning reports False when the selected Motor or Motor Group
        is stopped.

        Note: This command will always return false if the Motor/Motor Group
        is spinning as a result of a previous motor.spin command
        (which does not specify a set distance to spin).
    """)
    @sense
    def is_spinning(self: Self) -> bool:
        """Check whether motor is still spinning."""

    @robotmesh_doc("""
        Returns True if the last motor operation timed out.
    """)
    @sense
    def did_timeout(self: Self) -> bool:
        """Return whether motor timed out."""

    @vexcode_doc("""
        Motor Position

        Reports the current rotational position of the selected IQ Motor
        or the first motor of the selected Motor Group.

        Motor Position reports the position of an IQ Motor
        or the first motor in a Motor Group.

        Acceptable values for UNITS are: DEGREES or TURNS.
    """)
    @sense
    def position(self: Self, unit: RotationUnits = DEGREES, /) -> Num:
        """Return rotational angle."""

    @robotmesh_doc("""
        Gets the current rotation of the motor's encoder.

        Parameters
        - rotationUnits: measurement unit for rotation.

        Returns: a float that represents the current rotation of
                 the motor in the units defined in the parameter.
    """)
    @sense
    def rotation(self: Self,
                 rotationUnits: RotationUnits = RotationUnits.DEG, /) -> float:
        """Return rotational angle."""

    @overload
    def velocity(self: Self, unit: VelocityUnits = PERCENT, /) -> Num:
        ...

    @overload
    def velocity(self: Self,
                 velocityUnits: VelocityUnits = VelocityUnits.PCT, /) -> float:
        ...

    @robotmesh_doc("""
        Gets the current velocity of the motor.

        Parameters
        - velocityUnits: measurement unit for velocity.

        Returns: a float that represents the current velocity
                 of the motor in the units defined in the parameter.
    """)
    @vexcode_doc("""
        Motor Velocity

        Reports the current velocity of an IQ Motor
        or the first motor of a Motor Group.

        Motor velocity reports a range from -100 to 100 when PERCENT is passed
        as the UNITS parameter, or -127 to 127 if RPM is passed.
    """)
    @sense
    def velocity(self: Self, unit: VelocityUnits = PERCENT, /) -> Num:
        """Return velocity."""

    @overload
    def current(self: Self,
                unit: Literal[CurrentUnits.AMP] = CurrentUnits.AMP, /) -> float:  # noqa: E501
        ...

    @overload
    def current(self: Self) -> float:
        ...

    @robotmesh_doc("""
        Gets the electrical current of the motor.

        Returns:
        a float that represents the electrical current of the motor in Amps.
    """)
    @vexcode_doc("""
        Motor Current

        Reports the amount of current an IQ Motor or Motor Group is using.

        Motor Current reports a range from 0.0 to 2.5
        when CurrentUnits.AMP is passed as the UNITS parameter.
    """)
    @sense
    def current(self: Self,
                unit: Literal[CurrentUnits.AMP] = CurrentUnits.AMP, /) -> float:  # noqa: E501
        """Return electrical current."""

    @robotmesh_doc("""
        Gets torque of motor

        Parameters:
        - torqueUnits: Defines unit type of torque

        Returns: double that represents torque of motor in unit defined
    """)
    @sense
    def torque(self: Self, torqueUnits: TorqueUnits = TorqueUnits.NM) -> float:
        """Return torque."""

    @robotmesh_doc("""
        Gets efficiency of motor

        Parameters
        - percentUnits: unit type of efficiency value

        Returns: efficiency of motor in unit defined
    """)
    @sense
    def efficiency(self: Self,
                   percentUnits: PercentUnits = PercentUnits.PCT, /) -> Num:
        """Return efficiency."""

    @robotmesh_doc("""
        Gets temperature of motor

        Parameters
        - temperatureUnits: unit type of temperature value, default Celsius

        Returns: temperature of motor in unit defined
    """)
    @sense
    def temperature(
            self: Self,
            temperatureUnits: TemperatureUnits = TemperatureUnits.CELSIUS, /) -> Num:  # noqa: E501
        """Return temperature."""

    @robotmesh_doc("""
        Get device type
    """)
    def type(self: Self, /) -> Literal[V5DeviceType.MOTOR]:
        """Return device type, in the case of V5 only."""
        return V5DeviceType.MOTOR

    @robotmesh_doc("""
        Gets status of what is installed

        Returns: True if triport is installed, False if not
    """)
    @sense
    def installed(self: Self, /) -> bool:
        """Check if triport is installed."""

    @sense
    def value(self: Self, /) -> Any:
        """Return (some kind of?) value."""
