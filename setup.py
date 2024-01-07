from setuptools import setup

setup(
    name='paperplots',
    version='0.1.0',    
    description='Camera ready machine learning plots with a Tensorboard-like API',
    url='https://github.com/anishhdiwan/paperplots',
    author='Anish Abhijit Diwan',
    author_email='A.A.Diwan@student.tudelft.nl',
    license='MIT',
    packages=['paperplots'],
    install_requires=['matplotlib',
                      'numpy', 
                      'csv',
                      'pickle',
                      'os',
                      'datetime',                    
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)