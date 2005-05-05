%include	/usr/lib/rpm/macros.php
%define		_snap		dev1

Summary:	PHPTAL is an implementation of Zope Page Templates (ZPT) for PHP
Summary(pl):	PHPTAL jest implementacj± Zope Page Templates (ZPT) w PHP
Name:		PHPTAL
Version:	1.0.0
Release:	0.%{_snap}.4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/phptal/%{name}-%{version}%{_snap}.tar.gz
# Source0-md5:	151f4bb4799d8c8fe6646a25f6069897
URL:		http://phptal.sourceforge.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-GetText
Requires:	php-Types
Requires:	php-Algo_map
Requires:	php >= 5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHPTAL is an implementation of Zope Page Templates (ZPT) for PHP.

%description -l pl
PHPTAL jest implementacj± Zope Page Templates (ZPT) w PHP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}

cp -rf %{name}-%{version}%{_snap}/* $RPM_BUILD_ROOT%{php_pear_dir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{name}
