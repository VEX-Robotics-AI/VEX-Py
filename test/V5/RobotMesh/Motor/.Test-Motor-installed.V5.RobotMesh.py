"""robotmesh.com/studio/64a3343ef47a886576b2fc0d."""


from vex import (
    Brain, Motor,
    Ports,
    SECONDS,
    wait,
)


brain = Brain()

motor = Motor(Ports.PORT1)


motor_installed = motor.installed()


brain.screen.print_line(1, motor_installed)


wait(3, SECONDS)
