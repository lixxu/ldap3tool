"""
ldaptool
--------------
Simple wrapper for ldap3, used in Nypro & Jabil Shanghai internal
"""
from setuptools import setup

setup(
    name='ldaptool',
    version='0.2.0',
    url='http://10.116.168.15:81/lix/ldaptool',
    license='BSD',
    author='Lix Xu',
    author_email='lix_xu@jabil.com',
    description='Simple wrapper for ldap3',
    long_description=__doc__,
    packages=['ldaptool'],
    zip_safe=False,
    platforms='any',
    install_requires=['ldap3'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
