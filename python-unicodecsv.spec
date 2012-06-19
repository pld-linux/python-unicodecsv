#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	unicodecsv
Summary:	Replacement for csv module which supports unicode strings without a hassle
Name:		python-%{module}
Version:	0.9.0
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/u/unicodecsv/%{module}-%{version}.tar.gz
# Source0-md5:	83044c801fc761ccd5722bb63b5ed952
URL:		-
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:		python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unicodecsv is a drop-in replacement for Python 2's csv module
which supports unicode strings without a hassle.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
