"""robotmesh.com/studio/64a348f6a3776a661acced72."""


from vex import (
    Brain, Motor,
    Ports, TemperatureUnits,
    SECONDS,
    wait,
)


brain = Brain()

motor = Motor(Ports.PORT1)


motor_temperature = motor.temperature()

motor_temperature_c = motor.temperature(TemperatureUnits.CELSIUS)

motor_temperature_f = motor.temperature(TemperatureUnits.FAHRENHEIT)

motor_temperature_pct = motor.temperature(TemperatureUnits.PCT)


brain.screen.print_line(1, motor_temperature)
brain.screen.print_line(2, motor_temperature_c)
brain.screen.print_line(3, motor_temperature_f)
brain.screen.print_line(4, motor_temperature_pct)


wait(3, SECONDS)
