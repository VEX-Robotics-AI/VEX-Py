"""robotmesh.com/studio/638a82b20e64b96eee8ea87a."""


from vex import (
    Brain, Motor,
    Ports,
    SECONDS,
    wait,
)


MOTOR_VALUE: int = 0


brain: Brain = Brain()

motor: Motor = Motor(Ports.PORT1)


motor.value(set=MOTOR_VALUE)
motor_value: int = motor.value()
assert isinstance(motor_value, int)
assert motor_value == MOTOR_VALUE


brain.screen.print_line(1, motor_value)


wait(3, SECONDS)
