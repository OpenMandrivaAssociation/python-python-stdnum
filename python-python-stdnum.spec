Name:		python-python-stdnum
Version:	2.2
Release:	2
Summary:	Python module to handle standardized numbers and codes
License:	LGPL-2.1-or-later
Group:		Development/Python
URL:		https://pypi.org/project/python-stdnum/
Source0:	python_stdnum-2.2.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Python module to handle standardized numbers and codes.

%files
%{py_sitedir}/*
