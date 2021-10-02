from setuptools import setup


setup(
    packages=['vex'],
    py_modules=['drivetrain', 'motor_group', 'smartdrive', 'timer', 'vision',
                'vexcode', '__decor'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    namespace_packages=[]
)
