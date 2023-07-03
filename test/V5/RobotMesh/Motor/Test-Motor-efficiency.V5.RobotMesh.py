"""robotmesh.com/studio/64a34cdcf47a886576b2fc1f."""


from vex import (
    Brain, Motor,
    Ports, PercentUnits,
    PERCENT, SECONDS,
    wait,
)


MOTOR_EFFICIENCY: float = 0.0
MOTOR_EFFICIENCY_PCT: float = 0.0
MOTOR_EFFICIENCY_PERCENT: float = 0.0


brain: Brain = Brain()

motor: Motor = Motor(Ports.PORT1)


motor.efficiency(set=MOTOR_EFFICIENCY)
motor_efficiency: float = motor.efficiency()
assert isinstance(motor_efficiency, float)
assert motor_efficiency == MOTOR_EFFICIENCY

motor.efficiency(PercentUnits.PCT, set=MOTOR_EFFICIENCY_PCT)
motor_efficiency_pct: float = motor.efficiency(PercentUnits.PCT)
assert isinstance(motor_efficiency_pct, float)
assert motor_efficiency_pct == MOTOR_EFFICIENCY_PCT

motor.efficiency(PERCENT, set=MOTOR_EFFICIENCY_PERCENT)
motor_efficiency_percent: float = motor.efficiency(PERCENT)
assert isinstance(motor_efficiency_percent, float)
assert motor_efficiency_percent == MOTOR_EFFICIENCY_PERCENT


brain.screen.print_line(1, motor_efficiency)
brain.screen.print_line(2, motor_efficiency_pct)
brain.screen.print_line(3, motor_efficiency_percent)


wait(3, SECONDS)
