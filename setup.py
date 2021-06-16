from distutils.core import setup
setup(
  name = 'PyLo3',
  packages = ['PyLo3'],
  version = '1.0',
  license='cc0-1.0',
  description = 'creatore di alberi filogenetici',
  author = "Lorenzo D'Eusebio",
  author_email = 'deusebiolorenzo@gmail.com',
  url = 'https://github.com/deusssss/PyLo3',
  download_url = 'https://github.com/deusssss/PyLo3/archive/refs/tags/1.0.tar.gz',
  keywords = ["biopython", "philogenetic analysis", "web application", "python server", "university project", "bioinformatics"],
  install_requires=[
          'matplotlib',
          'biopython',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Programming Language :: Python'
  ],
)
