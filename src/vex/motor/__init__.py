"""Motor."""


from collections.abc import Sequence
from typing import Optional, Tuple
from typing_extensions import Self

from abm.decor import act, sense

from .._abstract_device import Device
from ..brain.port import Ports
from ..time import TimeUnits
from ..units_common import RotationUnits
from ..util.doc import robotmesh_doc, vexcode_doc
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

        self.selected_velocity_unit: VelocityUnits = None
        self.velocities: dict[VelocityUnits, float] = dict[VelocityUnits, float]()  # noqa: E501
        self.stopping: Optional[BrakeType] = None
        self.rotations: dict[RotationUnits, float] = dict[RotationUnits, float]()  # noqa: E501
        self.timeouts: dict[TimeUnits, float] = dict[TimeUnits, float]()

        self.max_torque: dict[TorqueUnits, float] = dict[TorqueUnits, float]()

    def __eq__(self, other: Self) -> bool:
        """Check equality."""
        return (isinstance(other, type(self)) and
                (other.port == self.port) and
                (other.reverse == self.reverse))

    def __hash__(self) -> int:
        """Return integer hash."""
        return hash((self.port, self.reverse))

    def __repr__(self) -> str:
        """Return String Representation."""
        return f'{type(self).__name__}({self.port.name}' + (', reverse)'
                                                            if self.reverse
                                                            else ')')

    def _get_selected_velocity_and_unit(
            self,
            velocity: Optional[float],
            velocityUnits: VelocityUnits) -> Tuple[float, VelocityUnits]:
        if (velocity is None) or (type(velocity) not in (float, int)):
            # VEX Py API v2
            if (self.selected_velocity_unit is None) or (
                    self.selected_velocity_unit not in self.velocities):
                raise ValueError("You have not selected any velocity. "
                                 "Please call "
                                 "set_velocity(velocity, velocityUnits) first.")  # noqa: E501

            velocity = self.velocities[self.selected_velocity_unit]
            velocityUnits = self.selected_velocity_unit  # noqa: N806

        return (velocity, velocityUnits)

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
        """Set Reversed Mode."""
        self.reverse: bool = is_reversed

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
    def set_velocity(self, velocity: float,
                     velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Set Velocity."""
        self.velocities[velocityUnits] = velocity
        self.selected_velocity_unit = velocityUnits
        return self._set_velocity(velocity, velocityUnits)

    @act
    def _set_velocity(self, velocity: float,
                      velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Set Velocity."""

    @robotmesh_doc("""
        Set stopping mode of the motor by passing a brake mode as a parameter.

        (note this will stop the motor if it's spinning)

        Parameters:
        - brakeType: The stopping mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
    """)
    @act
    def set_stopping(self, brakeType: BrakeType, /):
        """Set Stopping Mode."""
        self.stopping: BrakeType = brakeType

    @robotmesh_doc("""
        Reset the motor's encoder to the value of zero.
    """)
    @act
    def reset_rotation(self):
        """Reset Motor Rotation Value to 0."""
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
        """Set Motor Rotation Value to specific value."""
        self.rotations[rotationUnits] = value

    @robotmesh_doc("""
        Set the timeout for the motor.

        If the motor does not reach its commanded position prior
        to the completion of the timeout, the motor will stop.

        Parameters:
        - time: Sets the amount of time.
        - timeUnits: The measurement unit for the time, a TimeUnits enum value.
    """)
    @act
    def set_timeout(self, time: float, timeUnits: TimeUnits = TimeUnits.SEC, /):   # noqa: E501
        """Set Motor Timeout Threshold."""
        self.timeouts[timeUnits] = time

    @robotmesh_doc("""
        Return a timeout in given time units.
    """)
    @sense
    def timeout(self, timeUnits: TimeUnits = TimeUnits.SEC, /) -> float:
        """Return Motor Timeout."""
        return self.timeouts[timeUnits]

    @robotmesh_doc("""
        Return True if the last motor operation timed out.
    """)
    @sense
    def did_timeout(self) -> bool:
        """Return whether Motor timed out."""

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
        Turn on the motor and spins it.

        (in a specified direction and a specified velocity)

        Must call set_velocity(velocity, velocityUnits)
        before calling this method.

        Parameters:
        - dir: The direction to spin the motor, DirectionType enum value.
        - velocity: Sets the amount of velocity.
        - velocityUnits: The measurement unit for the velocity,
                         a VelocityUnits enum value.
    """)
    def spin(self, dir: DirectionType,  # pylint: disable=redefined-builtin
             velocity: Optional[float] = None,
             velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """Spin Motor."""
        velocity, velocityUnits = self._get_selected_velocity_and_unit(  # noqa: E501,N806
            velocity, velocityUnits)

        return self._spin(dir, velocity, velocityUnits)

    @act
    def _spin(self, dir: DirectionType,  # pylint: disable=redefined-builtin
              velocity: Optional[float] = None,
              velocityUnits: VelocityUnits = VelocityUnits.PCT):
        """Spin Motor."""

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
    def spin_to(  # pylint: disable=too-many-arguments
            self,
            rotation: float,
            rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Spin Motor to target Rotation Angle Value."""

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
        Turn on the motor and spins it.

        Must call set_velocity(velocity, velocityUnits)
        before calling this method.

        Parameters:
        - dir: The direction to spin the motor, DirectionType enum value.
        - rotation: Sets the amount of rotation.
        - rotationUnits: The measurement unit for the rotation value.
        - waitForCompletion: (Optional) If True, your program will wait
                             until the motor reaches the target rotational
                             value. If false, the program will continue after
                             calling this function.
                             By default, this parameter is true.

        Returns:
        Returns a Boolean that signifies when the motor
        has reached the target rotation value.
    """)
    def spin_for(  # pylint: disable=too-many-arguments
            self,
            dir: DirectionType,  # pylint: disable=redefined-builtin
            rotation: float,
            rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Spin Motor for a certain Rotation Angle Value."""
        velocity, velocityUnits = self._get_selected_velocity_and_unit(  # noqa: E501,N806
            velocity, velocityUnits)

        return self._spin_for(dir,
                              rotation, rotationUnits,
                              velocity, velocityUnits,
                              waitForCompletion)

    @act
    def _spin_for(  # pylint: disable=too-many-arguments
            self,
            dir: DirectionType,  # pylint: disable=redefined-builtin
            rotation: float,
            rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT,
            waitForCompletion: bool = True, /) -> bool:
        """Spin Motor for a certain Rotation Angle Value."""

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
    def spin_for_time(  # pylint: disable=too-many-arguments
            self,
            dir: DirectionType,  # pylint: disable=redefined-builtin
            time: str,
            timeUnits: TimeUnits = TimeUnits.SEC,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Spin Motor for a certain Time Duration."""

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
        """Start spinning Motor to a certain Target Rotation Angle Value."""

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
    def start_spin_for(  # pylint: disable=too-many-arguments
            self,
            dir: DirectionType,  # pylint: disable=redefined-builtin
            rotation: float,
            rotationUnits: RotationUnits = RotationUnits.DEG,
            velocity: Optional[float] = None,
            velocityUnits: VelocityUnits = VelocityUnits.PCT, /):
        """Start spinning motor for a certain Rotation Angle Value."""

    @robotmesh_doc("""
        Determine if a spin_for/spin_to command is in progress.

        Returns:
        True if the motor is on and is rotating to a target,
        False if the motor is done rotating to a target.
    """)
    @sense
    def is_spinning(self) -> bool:
        """Check if Motor is spinning."""

    @robotmesh_doc("""
        Determine if spin_for/spin_to command has reached its target position.

        Returns:
        False if the motor is on and is rotating
        to a target, True if the motor is done rotating to a target.
    """)
    @sense
    def is_done(self) -> bool:
        """Check if Motor has finished spinning."""

    @robotmesh_doc("""
        Stop the motor using the default brake mode.

        Parameters:
        - brakeType: The brake mode can be set to
                     BrakeType.COAST, BRAKE, or HOLD.
    """)
    @act
    def stop(self, brakeType: Optional[BrakeType] = None, /):
        """Stop Motor."""

    @robotmesh_doc("""
        Set the max torque of the motor as a percentage.

        Parameters:
        - value: Sets the amount of torque (0 to 100%)
    """)
    @act
    def set_max_torque_percent(self, value: float, /):
        """Set Max Torque Percent."""
        self.max_torque[TorqueUnits.PCT] = value

    @robotmesh_doc("""
        Set the max torque of the motor.

        Parameters:
        - value: Sets the amount of torque (max 0.414 Nm)
        - torqueUnits: The measurement unit for the torque value.
    """)
    @act
    def set_max_torque(self, value: float,
                       torqueUnits: TorqueUnits = TorqueUnits.NM, /):
        """Set Max Torque."""
        self.max_torque[torqueUnits] = value

    @robotmesh_doc("""
        Set the max torque of the motor.

        Parameters:
        - value: Sets the amount of torque in Amps (max 1.2A)
    """)
    @act
    def set_max_torque_current(self, value: float, /):
        """Set Max Torque Current."""
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
        """Return Motor's cumulative Rotation Angle Value."""

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
        """Return Motor's Velocity."""

    @robotmesh_doc("""
        Get the electrical current of the motor.

        Returns:
        a float that represents the electrical current of the motor in Amps.
    """)
    @sense
    def current(self) -> float:
        """Return Motor's Electrical Current."""
