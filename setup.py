from setuptools import setup

setup(name='dev_aberto_felipebpl',
      version='0.1',
      packages=['pacote_exemplo'],
      install_requires=[
        'setuptools',
        'requests'
      ],
      scripts=['scripts/hello.py']

      )

