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

## How to use

Building from source:

```
(venv) D:\projects\deb_pkg_utils>python setup.py sdist
WARNING: '' not a valid package name; please use only .-separated package names in setup.py
D:\projects\deb_pkg_utils\venv\lib\site-packages\setuptools-39.1.0-py3.5.egg\setuptools\dist.py:388: UserWarning: Normalizing '0.1.004' to '0.1.4'
running sdist
running egg_info
writing requirements to deb_pkg_utils.egg-info\requires.txt
writing top-level names to deb_pkg_utils.egg-info\top_level.txt
writing dependency_links to deb_pkg_utils.egg-info\dependency_links.txt
writing deb_pkg_utils.egg-info\PKG-INFO
reading manifest file 'deb_pkg_utils.egg-info\SOURCES.txt'
writing manifest file 'deb_pkg_utils.egg-info\SOURCES.txt'
running check
warning: check: missing required meta-data: url

warning: check: missing meta-data: if 'author' supplied, 'author_email' must be supplied too

creating deb_pkg_utils-0.1.4
creating deb_pkg_utils-0.1.4\deb_pkg_utils.egg-info
copying files to deb_pkg_utils-0.1.4...
copying README.md -> deb_pkg_utils-0.1.4
copying package_statistics.py -> deb_pkg_utils-0.1.4
copying requirements.txt -> deb_pkg_utils-0.1.4
copying setup.py -> deb_pkg_utils-0.1.4
copying deb_pkg_utils.egg-info\PKG-INFO -> deb_pkg_utils-0.1.4\deb_pkg_utils.egg-info
copying deb_pkg_utils.egg-info\SOURCES.txt -> deb_pkg_utils-0.1.4\deb_pkg_utils.egg-info
copying deb_pkg_utils.egg-info\dependency_links.txt -> deb_pkg_utils-0.1.4\deb_pkg_utils.egg-info
copying deb_pkg_utils.egg-info\requires.txt -> deb_pkg_utils-0.1.4\deb_pkg_utils.egg-info
copying deb_pkg_utils.egg-info\top_level.txt -> deb_pkg_utils-0.1.4\deb_pkg_utils.egg-info
Writing deb_pkg_utils-0.1.4\setup.cfg
creating dist
Creating tar archive
removing 'deb_pkg_utils-0.1.4' (and everything under it)

```

Installing from the distributed tar file (check in dist directory):

```
(base) D:\projects>pip install deb_pkg_utils-0.1.4.tar.gz
Processing d:\projects\deb_pkg_utils-0.1.4.tar.gz
Collecting plac (from deb-pkg-utils==0.1.4)
  Using cached https://files.pythonhosted.org/packages/6f/53/b4d63dd6f1bf876d8c658cea5d9c926e85fb9f4d9ece53415bbe67f49987/plac-1.0.0-py2.py3-none-any.whl
Building wheels for collected packages: deb-pkg-utils
  Running setup.py bdist_wheel for deb-pkg-utils ... done
  Stored in directory: C:\Users\Edward Law\AppData\Local\pip\Cache\wheels\69\60\49\56ff16fb9186b6cf0b775fd348c75f4a783e52ab97d709a97e
Successfully built deb-pkg-utils
Installing collected packages: plac, deb-pkg-utils
Successfully installed deb-pkg-utils-0.1.4 plac-1.0.0

```

Using it after installing:

```

(base) D:\projects>python -m package_statistics 'amd64'
usage: package_statistics.py [-h]
                             [-u http://ftp.uk.debian.org/debian/dists/stable/main/]
                             [-k 10]
                             [{arm64,amd64,armel,armhf,i386,mips,mips64el,mipsel,ppc64el,s390x,udeb-arm64,udeb-amd64,udeb-armel,udeb-armhf,udeb-i386,udeb-mips,udeb-mips64el,udeb-mipsel,udeb-ppc64el,udeb-s390x}]
package_statistics.py: error: argument architecture: invalid choice: "'amd64'" (choose from 'arm64', 'amd64', 'armel', 'armhf', 'i386', 'mips', 'mips64el', 'mipsel', 'ppc64el', 's390x', 'udeb-arm64', 'udeb-amd64', 'udeb-armel', 'udeb-armhf', 'udeb-i386', 'udeb-mips', 'udeb-mips64el', 'udeb-mipsel', 'udeb-ppc64el', 'udeb-s390x')

(base) D:\projects>python -m package_statistics amd64
INFO:package_statistics.py:package_statistics.py starts with architecture: amd64 and mirror: http://ftp.uk.debian.org/debian/dists/stable/main/
INFO:package_statistics.py:processed ... 0 lines in input.
INFO:package_statistics.py:processed ... 1000 lines in input.
INFO:package_statistics.py:processed ... 10000 lines in input.
INFO:package_statistics.py:processed ... 100000 lines in input.
INFO:package_statistics.py:processed ... 1000000 lines in input.
1. x11/numix-icon-theme 68920
2. games/flightgear-data-base 64704
3. fonts/texlive-fonts-extra 45910
4. rust/rust-doc 45641
5. doc/trilinos-doc 45567
6. games/widelands-data 34985
7. misc/moka-icon-theme 32533
8. doc/vtk6-doc 29464
9. gnome/faenza-icon-theme 29400
10. fonts/fonts-mathjax-extras 29035
```