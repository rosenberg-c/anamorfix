from setuptools import setup

setup(name='anamorfix',
      version='0.1.0',
      description='desqueeze anamorphic images',
      url='none',
      author='Romain Dura',
      author_email='',
      license='MIT License',
      packages=['anamorfix'],
      install_requires=[
          'Pillow',
      ],
      include_package_data=True,
      zip_safe=False)
