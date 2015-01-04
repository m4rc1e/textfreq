from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='textfreq',
      version='0.001',
      description='Count letters, letter pairs and words in text files.',
      long_description=readme(),
      keywords='Letters, Letter Pairs, Non-Latin, non Latin, count',
      url='http://github.com/m4rc1e/textfreq',
      author='Marc Foley',
      author_email='m.foley.88@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      include_package_data=True,
      zip_safe=False,
      entry_points={'console_scripts': ['textfreq = textfreq:main']})
