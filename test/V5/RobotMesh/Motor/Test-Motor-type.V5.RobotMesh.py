"""robotmesh.com/studio/64a33791a3776a661acced69."""


from vex import (
    Brain, Motor,
    V5DeviceType, Ports,
    SECONDS,
    wait,
)


brain: Brain = Brain()

motor: Motor = Motor(Ports.PORT1)


motor_type: V5DeviceType = motor.type()
assert isinstance(motor_type, V5DeviceType)
assert motor_type == V5DeviceType.MOTOR


brain.screen.print_line(1, motor_type)


wait(3, SECONDS)
