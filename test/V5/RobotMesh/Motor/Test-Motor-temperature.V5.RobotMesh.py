"""robotmesh.com/studio/64a348f6a3776a661acced72."""


from vex import (
    Brain, Motor,
    Ports, TemperatureUnits,
    SECONDS,
    wait,
)


MOTOR_TEMPERATURE: float = 40.0
MOTOR_TEMPERATURE_C: float = 40.0
MOTOR_TEMPERATURE_F: float = 104.0
MOTOR_TEMPERATURE_PCT: float = 24.0


brain: Brain = Brain()

motor: Motor = Motor(Ports.PORT1)


motor.temperature(set=MOTOR_TEMPERATURE)
motor_temperature: float = motor.temperature()
assert isinstance(motor_temperature, float)
assert MOTOR_TEMPERATURE == MOTOR_TEMPERATURE

motor.temperature(TemperatureUnits.CELSIUS, set=MOTOR_TEMPERATURE_C)
motor_temperature_c: float = motor.temperature(TemperatureUnits.CELSIUS)
assert isinstance(motor_temperature_c, float)
assert motor_temperature_c == MOTOR_TEMPERATURE_C

motor.temperature(TemperatureUnits.FAHRENHEIT, set=MOTOR_TEMPERATURE_F)
motor_temperature_f: float = motor.temperature(TemperatureUnits.FAHRENHEIT)
assert isinstance(motor_temperature_f, float)
assert motor_temperature_f == MOTOR_TEMPERATURE_F

motor.temperature(TemperatureUnits.PCT, set=MOTOR_TEMPERATURE_PCT)
motor_temperature_pct: float = motor.temperature(TemperatureUnits.PCT)
assert isinstance(motor_temperature_pct, float)
assert motor_temperature_pct == MOTOR_TEMPERATURE_PCT


brain.screen.print_line(1, motor_temperature)
brain.screen.print_line(2, motor_temperature_c)
brain.screen.print_line(3, motor_temperature_f)
brain.screen.print_line(4, motor_temperature_pct)


wait(3, SECONDS)
