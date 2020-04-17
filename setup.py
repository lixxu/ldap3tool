"""
ldap3tool
--------------
Simple wrapper for ldap3
"""
import io
import os.path
from setuptools import setup

work_dir = os.path.dirname(os.path.abspath(__file__))
fp = os.path.join(work_dir, "ldap3tool/__init__.py")

with io.open(fp, encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__ = "):
            version = line.split("=")[-1].strip().replace("'", "")
            break

setup(
    name="ldap3tool",
    version=version.replace('"', ""),
    url="https://github.com/lixxu/ldap3tool",
    license="BSD",
    author="Lix Xu",
    author_email="xuzenglin@gmail.com",
    description="Simple wrapper for ldap3",
    long_description=__doc__,
    packages=["ldap3tool"],
    zip_safe=False,
    platforms="any",
    install_requires=["ldap3"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)
