from setuptools import setup


setup(
    name='RobotMesh-VEXIQ-PyB-API-Stubs',
    version='1.0.4',
    description='Robot Mesh VEX IQ Python B API Stubs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='STEAM for Vietnam Foundation',
    author_email='Edu.Robotics@STEAMforVietnam.org',
    url='https://GitHub.com/STEAMforVietnam/RobotMesh-VEXIQ-PyB-API-Stubs',
    download_url='https://GitHub.com/STEAMforVietnam/'
                 'RobotMesh-VEXIQ-PyB-API-Stubs/archive/main.zip',
    packages=['vex'],
    py_modules=['drivetrain', 'motor_group', 'smartdrive', 'timer', 'vision',
                'vexcode', '__decor'],
    scripts=[],
    classifiers=[],
    license='MIT',
    keywords=[],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=open('requirements.txt').readlines(),
    entry_points={},
    extras_require={'devtest': open('requirements-devtest.txt').readlines()},
    python_requires='>= 3.9',
    setup_requires=[],
    namespace_packages=[]
)
