# noqa: D104


from vex import (
    Motor,
    Ports, GearSetting,
)


motor = Motor(Ports.PORT1)

motor = Motor(Ports.PORT1, GearSetting.RATIO18_1)

motor = Motor(Ports.PORT1, True)
