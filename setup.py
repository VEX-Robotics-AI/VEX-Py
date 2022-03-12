from setuptools import setup


setup(name='RobotMesh-VEXIQ-PyB-API-Stubs',
      version='1.0.10',
      packages=['vex'],
      py_modules=['drivetrain', 'motor_group', 'smartdrive', 'timer', 'vision',
                  'vexcode', '__decor'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      namespace_packages=[])
