from distutils.core import setup

setup(
  name = 'appwrite',
  packages = ['appwrite', 'appwrite/services'],
  version = '0.0.1',
  license='BSD-3-Clause',
  description = 'Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)',
  author = 'Appwrite Team',
  author_email = 'team@appwrite.io',
  maintainer = 'Appwrite Team',
  maintainer_email = 'team@appwrite.io',
  url = 'https://appwrite.io/support',
  download_url='https://github.com/repoowner/reponame/archive/0.0.1.tar.gz',
  # keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 5 - PRODUCTION/STABLE',
    'Intended Audience :: Developers',
    'Environment :: Web Environment',
    'Topic :: Software Development',
    'License :: OSI Approved :: BSD-3-Clause',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)