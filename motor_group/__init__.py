from vex import Motor


class MotorGroup:
    def __init__(self, motors: list[Motor]):
        """
        Creates a new motor group with specified motors

        param:
        motors: a list or tuple of motors in the group
        """
