from setuptools import find_packages, setup

package_name = 'states_routine'

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
    description='The states_routine package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'getting_up_routine = states_routine.getting_up_routine:main',
            'kick_routine = states_routine.kick_routine:main',
            'stand_still_routine = states_routine.stand_still_routine:main',
            'walking_routine = states_routine.walking_routine:main',
            
            
        ],
    },
)
