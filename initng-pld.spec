Summary:	initng initscripts for PLD
Summary(pl):	Skrypty inicjalizuj±ce initng dla PLD
Name:		initng-pld
Version:	0.0.1
%define		_snap 20051017
Release:	0.%{_snap}.1
License:	GPL
Group:		Base
Source0:	http://glen.alkohol.ee/pld/initng/initscripts/initng-initscripts-%{_snap}.tar.bz2
# Source0-md5:	dfb13a5e96c8e7cb546794da2b77d3e6
Requires:	initng
Requires:	module-init-tools
Requires:	mount
Requires:	net-tools
Requires:	util-linux
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/initng
%define		_exec_prefix /

%description
initng initscripts for PLD.

%description -l pl
Skrypty inicjalizuj±ce initng dla PLD.

%prep
%setup -q -n initng-initscripts-%{_snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}
cp -a */ *.i *.runlevel $RPM_BUILD_ROOT%{_sysconfdir}
install shutdown_script $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.runlevel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*/*.i
%{_sbindir}/*
