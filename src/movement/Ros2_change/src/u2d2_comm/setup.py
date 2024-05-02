from setuptools import find_packages, setup

package_name = 'u2d2_comm'

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
    maintainer='matheus',
    maintainer_email='matheusbenigno090@gmail.com',
    description='The u2d2_comm package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
