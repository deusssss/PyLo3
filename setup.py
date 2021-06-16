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
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ["biopython", "philogenetic analysis", "web application", "python server", "university project", "bioinformatics"],   
  install_requires=[            # I get to this in a second
          'matplotlib',
          'biopython',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Students',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: cc0-1.0 License',   
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
  ],
)