from setuptools import setup


setup(
    name='pi_babe',
    version='0.0.1',
    description='Pi-Babe package',
    packages=['pi_babe',
              'pi_babe.babe_cam',
              'pi_babe.babe_web',],
    install_requires=['flask>=0.10.0'])
