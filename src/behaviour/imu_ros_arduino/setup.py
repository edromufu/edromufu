from setuptools import find_packages, setup

package_name = 'imu_ros_arduino'

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
    maintainer='edrom',
    maintainer_email='edrom@todo.todo',
    description='The imu_ros_arduino package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
     'console_scripts': [
             'IMU_node = imu_ros_arduino.IMU_node:main'
     ],
    },
)
