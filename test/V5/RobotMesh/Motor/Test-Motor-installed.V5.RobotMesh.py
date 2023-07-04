"""robotmesh.com/studio/64a3343ef47a886576b2fc0d."""


from vex import (
    Brain, Motor,
    Ports,
    SECONDS,
    wait,
)


MOTOR_INSTALLED: bool = True


brain = Brain()

motor = Motor(Ports.PORT1)


motor.installed(set=MOTOR_INSTALLED)


motor_installed = motor.installed()
assert isinstance(motor_installed, bool)
assert motor_installed == MOTOR_INSTALLED


brain.screen.print_line(1, motor_installed)


wait(3, SECONDS)
