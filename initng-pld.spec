Summary:	initng initscripts for PLD
Name:		initng-pld
Version:	0.0.1
%define		_snap 20050730
Release:	0.%{_snap}.1
License:	GPL
Group:		Base
Source0:	http://glen.alkohol.ee/pld/initng/initscripts/initng-initscripts-%{_snap}.tar.bz2
# Source0-md5:	fd94362d83494fa6ea41a1cc83a3db33
Requires:	initng
Requires:	mount
Requires:	util-linux
Requires:	net-tools
Requires:	module-init-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/initng

%description
TODO

%prep
%setup -q -n initng-initscripts-%{_snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -a . $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.runlevel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*/*.i
