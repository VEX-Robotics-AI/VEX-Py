"""robotmesh.com/studio/64a36af1a3776a661acced96."""


from vex import (
    Brain, Motor,
    Ports, TorqueUnits,
    SECONDS,
    wait,
)


MOTOR_TORQUE: float = 0.0
MOTOR_TORQUE_NM: float = 0.0
MOTOR_TORQUE_IN_LB: float = 0.0


brain: Brain = Brain()

motor: Motor = Motor(Ports.PORT1)


motor.torque(set=MOTOR_TORQUE)
motor_torque: float = motor.torque()
assert isinstance(motor_torque, float)
assert motor_torque == MOTOR_TORQUE

motor.torque(TorqueUnits.NM, set=MOTOR_TORQUE_NM)
motor_torque_nm: float = motor.torque(TorqueUnits.NM)
assert isinstance(motor_torque_nm, float)
assert motor_torque_nm == MOTOR_TORQUE_NM

motor.torque(TorqueUnits.IN_LB, set=MOTOR_TORQUE_IN_LB)
motor_torque_in_lb: float = motor.torque(TorqueUnits.IN_LB)
assert isinstance(motor_torque_in_lb, float)
assert motor_torque_in_lb == MOTOR_TORQUE_IN_LB


brain.screen.print_line(1, motor_torque)
brain.screen.print_line(2, motor_torque_nm)
brain.screen.print_line(3, motor_torque_in_lb)


wait(3, SECONDS)
