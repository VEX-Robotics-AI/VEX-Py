"""Setup script."""


from setuptools import setup


setup(name='RobotMesh-VEX-PyB-API-Stubs',
      version='1.0.8',
      packages=['vex'],
      py_modules=['drivetrain', 'motor_group', 'smartdrive', 'timer', 'vision',
                  'vexcode', '__vex_decor'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      namespace_packages=[],
      entry_points=dict(
          console_scripts=[
              'robotmesh-vex=vex._cli:robotmesh_vex_cli'
          ]
      ))
