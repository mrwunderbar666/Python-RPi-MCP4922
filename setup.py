from setuptools import setup, find_packages

classifiers = ['Development Status :: 3 - Alpha'
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'Python_RPi_MCP4922',
      version           = '0.3',
      author            = 'Paul Balluff',
      author_email      = 'paul.balluff@gmail.com',
      description       = 'Python code to use the MCP4922 digital to analog converter with a Raspberry Pi.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/mrwunderbar666/Python-RPi-MCP4922/',
      install_requires  = ['spidev>=3.2','RPi.GPIO>=0.6.3'],
      packages          = find_packages()
      )
