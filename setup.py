from setuptools import setup


setup(name='reflect',
      version='1.0',
      description='WIP NLP RT NLP analytics',
      author='Patrick Long',
      author_email='patrick.long@gmail.com',
      #py_modules=['runner'],
      packages=
      ['reflect',],
      package_dir = {'': 'src'},
      #scripts=['src/reflect/.py'],
      include_package_data=True,
      entry_points = {
       'console_scripts': ['reflect=app/streamlit_app.py']
        },
      install_requires=[
          'pandas'
      ],
        )
