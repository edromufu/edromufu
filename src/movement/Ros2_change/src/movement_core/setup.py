from setuptools import find_packages, setup

package_name = 'movement_core'

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
    description='TODO: Package description',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'core = movement_core.core:main',
        	'core_head = movement_core.core_head:main',
        ],
    },
)
