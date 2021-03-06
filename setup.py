import os
from setuptools import setup, find_packages

version = '0.5.0'

setup(name='xmldirector.bookalope',
      version=version,
      description="Plone/XML-Director integration with bookalope.net",
      long_description=open(os.path.join("docs", "source", "README.rst")).read() + "\n" +
      open(os.path.join("docs", "source", "HISTORY.rst")).read(),
      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: 5.0",
          "Framework :: Zope2",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='xml-director bookalope XML Plone Python ebooks ',
      author='Andreas Jung',
      author_email='info@zopyx.com',
      url='http://pypi.python.org/pypi/xmldirector.bookalope',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['xmldirector'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'babel',
      ],
      tests_require=['zope.testing'],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
