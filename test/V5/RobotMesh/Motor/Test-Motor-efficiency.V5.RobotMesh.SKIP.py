"""robotmesh.com/studio/64a34cdcf47a886576b2fc1f."""


from vex import (
    Brain, Motor,
    Ports, PercentUnits,
    PERCENT, SECONDS,
    wait,
)


brain = Brain()

motor = Motor(Ports.PORT1)


motor_efficiency = motor.efficiency()

motor_efficiency_pct = motor.efficiency(PercentUnits.PCT)

motor_efficiency_percent = motor.efficiency(PERCENT)


brain.screen.print_line(1, motor_efficiency)
brain.screen.print_line(2, motor_efficiency_pct)
brain.screen.print_line(3, motor_efficiency_percent)


wait(3, SECONDS)
