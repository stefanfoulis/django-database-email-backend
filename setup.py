from setuptools import setup, find_packages
import os

version = __import__('database_email_backend').__version__

install_requires = [
]

setup(
    name = "django-database-email-backend",
    version = version,
    url = 'http://github.com/stefanfoulis/django-database-email-backend',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "A django EmailBackend for debugging that saves Emails in the database instead of delivering them.",
    long_description = open('README.rst').read(),
    author = 'Stefan Foulis',
    author_email = 'stefan.foulis@gmail.com',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
