from setuptools import find_packages, setup

package_name = 'object_finder'
__version__ = '0.0.1'

setup(
    name=package_name,
    version=__version__,
    
    packages=find_packages(exclude=['docs', 'tests*']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='Ball finder for EDROM',
    long_description='This program finds the ball, robots and other features in an image',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points={
        'console_scripts': [
            'vision = object_finder.connecting_and_showing:main',
        ],
    },
    author='EDROM',
)
