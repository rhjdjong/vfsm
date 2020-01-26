from setuptools import find_packages, setup

setup(
    name='vfsm',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/rhjdjong/vfsm',
    license='MIT',
    author='Ruud de Jong',
    author_email='ruud.de.jong@xs4all.nl',
    description='Python framework for virtual finite state machine implementations',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
