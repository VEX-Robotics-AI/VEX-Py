"""robotmesh.com/studio/64a32968f47a886576b2fc04."""


from vex import (
    Motor,
    Ports, GearSetting,
)


motor: Motor = Motor(Ports.PORT1)

motor: Motor = Motor(Ports.PORT1, GearSetting.RATIO18_1, False)

motor: Motor = Motor(Ports.PORT1, GearSetting.RATIO18_1, True)
