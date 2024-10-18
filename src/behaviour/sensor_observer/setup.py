from setuptools import find_packages, setup

package_name = 'sensor_observer'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kirlin',
    maintainer_email='kirlin@todo.todo',
    description='The sensor_observer package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
     'console_scripts': [
             'ball_interpreter = sensor_observer.ball_interpreter:main',
             'fall_interpreter = sensor_observer.fall_interpreter:main',
             'neck_interpreter = sensor_observer.neck_interpreter:main',
             'ros_packer = sensor_observer.ros_packer:main'
     ],
    },
)
