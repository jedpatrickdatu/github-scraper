import setuptools

setuptools.setup(name='scraper',
      version='0.1',
      description='Scraper of data from public GitHub repositories',
      url='https://github.com/jedpatrickdatu/github-scraper',
      author='Jed Patrick Datu',
      author_email='jedpatrickdatu@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          'requests',
          'requests_mock'
      ],
      zip_safe=False)