# deb_pkg_utils

It is a set of python utilities to handle debian package etc. 

Debian uses *.deb packages to deploy and upgrade software. The packages
are stored in repositories and each repository contains the so called "Contents
index". The format of that file is well described here
https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices

## Features

* package_statistics - A python command line tool that:
    
    * **Input**: takes the architecture (amd64, arm64, mips etc.) and 
a debian mirror (default at http://ftp.uk.debian.org/debian/dists/stable/main/) as arguments and 
    * **output**: the top 10 packages that have the most files associated with the architecture. 

An example output could be:

```
./package_statistics.py amd64

1. <package name 1>         <number of files>
2. <package name 2>         <number of files>
......
10. <package name 10>         <number of files>
```

* to follow as much python's best practices as possible.
    * especially, linting
