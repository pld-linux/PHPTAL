%include	/usr/lib/rpm/macros.php
%define		_class		PHPTAL
%define		_status		beta
%define		_pearname	%{_class}

Summary:	PHPTAL is an implementation of Zope Page Templates (ZPT) for PHP
Summary(pl.UTF-8):	PHPTAL jest implementacją Zope Page Templates (ZPT) w PHP
Name:		PHPTAL
Version:	1.1.11
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://phptal.motion-twin.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	56c1741a172bc098ab47097be8743fda
URL:		http://phptal.motion-twin.com/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
Obsoletes:	php-Algo_map
Obsoletes:	php-GetText
Obsoletes:	php-Types
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHPTAL is an implementation of Zope Page Templates (ZPT) for PHP.

%description -l pl.UTF-8
PHPTAL jest implementacją Zope Page Templates (ZPT) w PHP.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/README
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}.php
