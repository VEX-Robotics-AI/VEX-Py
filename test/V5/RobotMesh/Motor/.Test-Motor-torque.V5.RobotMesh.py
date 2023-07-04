"""robotmesh.com/studio/64a36af1a3776a661acced96."""


from vex import (
    Brain, Motor,
    Ports, TorqueUnits,
    SECONDS,
    wait,
)


brain = Brain()

motor = Motor(Ports.PORT1)


motor_torque = motor.torque()

motor_torque_nm = motor.torque(TorqueUnits.NM)

motor_torque_in_lb = motor.torque(TorqueUnits.IN_LB)


brain.screen.print_line(1, motor_torque)
brain.screen.print_line(2, motor_torque_nm)
brain.screen.print_line(3, motor_torque_in_lb)


wait(3, SECONDS)
