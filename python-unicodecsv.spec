#
# Conditional build:
%bcond_with	tests	# do perform "make test" (broken, will download dependecies)

%define 	module	unicodecsv
Summary:	Replacement for csv module which supports unicode strings without a hassle
Name:		python-%{module}
Version:	0.14.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/u/unicodecsv/%{module}-%{version}.tar.gz
# Source0-md5:	ae2aaff1c2de7b15c741ac394f75a429
URL:		https://github.com/jdunck/python-unicodecsv
BuildRequires:	python-setuptools
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unicodecsv is a drop-in replacement for Python 2's csv module
which supports unicode strings without a hassle.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-*.egg-info
