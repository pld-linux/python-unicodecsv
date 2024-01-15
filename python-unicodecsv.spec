#
# Conditional build:
%bcond_without	tests	# unit tests

%define 	module	unicodecsv
Summary:	Replacement for csv module which supports unicode strings without a hassle
Summary(pl.UTF-8):	Zamiennik modułu csv obsługujący łańcuchy unikodowe bez problemów
Name:		python-%{module}
Version:	0.14.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/u/unicodecsv/%{module}-%{version}.tar.gz
# Source0-md5:	c18ffe8ded29a4f429224877b2b34252
URL:		https://github.com/jdunck/python-unicodecsv
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-unittest2 >= 0.5.1
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unicodecsv is a drop-in replacement for Python 2's csv module
which supports unicode strings without a hassle.

%description -l pl.UTF-8
Moduł unicodecsv to zamiennik modułu csv z Pythona 2, obsługujący
łańcuchy unikodowe bez problemów.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
%{__python} -m unittest unicodecsv.test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

# not used with python 2.x
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/py3.*
# tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/test.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/unicodecsv
%{py_sitescriptdir}/unicodecsv-%{version}-py*.egg-info
