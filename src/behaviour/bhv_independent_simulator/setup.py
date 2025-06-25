from setuptools import setup
import os
from glob import glob

package_name = 'bhv_independent_simulator'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'bhv_sim = bhv_independent_simulator.bhv_sim:main',
        ],
    },
)