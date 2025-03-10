#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	whoosh
Summary:	Fast, pure-Python full text indexing, search, and spell checking library
Summary(pl.UTF-8):	Szybka, czysto pythonowa biblioteka do pełnotekstowego indeksowania, wyszukiwania i sprawdzania pisowni
Name:		python-%{module}
Version:	2.7.4
Release:	8
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/Whoosh/
Source0:	https://files.pythonhosted.org/packages/source/W/Whoosh/Whoosh-%{version}.tar.gz
# Source0-md5:	c2710105f20b3e29936bd2357383c325
Patch0:		%{name}-tests.patch
URL:		https://pypi.org/project/Whoosh/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.0.0
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add
search functionality to their applications and websites. Every part of
how Whoosh works can be extended or replaced to meet your needs
exactly.

%description -l pl.UTF-8
Whoosh to szybka biblioteka pełnotekstowego indeksowania i
wyszukiwania, zaimplementowana w czystym Pythonie. Programiści mogą
łatwo używać jej do rozszerzania funkcjonalności w swoich aplikacjach
i serwisach. Każda część funkcjonalności Whoosha może być rozszerzona
lub podmieniona w celu dostosowania do własnych potrzeb.

%package -n python3-%{module}
Summary:	Fast, Python3 full text indexing, search, and spell checking library
Summary(pl.UTF-8):	Szybka, czysto pythonowa biblioteka do pełnotekstowego indeksowania, wyszukiwania i sprawdzania pisowni
Group:		Libraries/Python

%description -n python3-%{module}
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add
search functionality to their applications and websites. Every part of
how Whoosh works can be extended or replaced to meet your needs
exactly.

%description -n python3-%{module} -l pl.UTF-8
Whoosh to szybka biblioteka pełnotekstowego indeksowania i
wyszukiwania, zaimplementowana w czystym Pythonie. Programiści mogą
łatwo używać jej do rozszerzania funkcjonalności w swoich aplikacjach
i serwisach. Każda część funkcjonalności Whoosha może być rozszerzona
lub podmieniona w celu dostosowania do własnych potrzeb.

%package apidocs
Summary:	API documentation for Whoosh module
Summary(pl.UTF-8):	Dokumentacja API modułu Whoosh
Group:		Documentation

%description apidocs
API documentation for Whoosh module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Whoosh.

%prep
%setup -q -n Whoosh-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-2 docs/source docs/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%files
%defattr(644,root,root,755)
%doc README.txt LICENSE.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/Whoosh-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.txt LICENSE.txt
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/Whoosh-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/html/{_static,api,releases,tech,*.html,*.js}
%endif
