Summary:	initng initscripts for PLD
Summary(pl):	Skrypty inicjalizuj±ce initng dla PLD
Name:		initng-pld
Version:	0.0.3
%define		_snap 20051104
Release:	0.%{_snap}.10
License:	GPL
Group:		Base
Source0:	http://glen.alkohol.ee/pld/initng/initscripts/initng-initscripts-%{_snap}.tar.bz2
# Source0-md5:	e77417df972c02b3fb1a3427ffc22b37
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

%define	_initng_service_hook() \
%triggerin -- %1 \
%{?debug:set -x; echo triggerin %{name}-%{version}-%{release} of %1}\
if [ "$1" = "1" ] && [ "$2" = "1" ]; then \
	/sbin/ng-update add %2 default \
fi \
\
%triggerin -- %1 \
%{?debug:set -x; echo triggepostun %{name}-%{version}-%{release} of %1}\
if [ "$1" = "0" ] || [ "$2" = "0" ]; then \
	/sbin/ng-update del %2 \
fi \

#%triggerun -- %{name} \
#set -x; echo triggepostun %{name}-%{version}-%{release} of %{name}\
#if [ "$1" = 0 ]; then \
#	/sbin/ng-update del %2 \
#fi

# Usage:
# _initng_service_hook [RPM package/RPM Virtual] [Initng service name]

%_initng_service_hook alsa-utils-init daemon/alsasound
%_initng_service_hook apache1 daemon/apache
%_initng_service_hook autofs daemon/autofs
%_initng_service_hook crondaemon daemon/crond
%_initng_service_hook cups daemon/cupsd
%_initng_service_hook dhcp daemon/dhcpd
%_initng_service_hook gpm daemon/gpm
%_initng_service_hook klogd daemon/klogd
%_initng_service_hook lighttpd daemon/lighttpd
%_initng_service_hook mldonkey daemon/mldonkey
%_initng_service_hook mysql daemon/mysql
%_initng_service_hook mythtv-backend daemon/mythbackend
%_initng_service_hook ntp daemon/ntpd
%_initng_service_hook openvpn daemon/openvpn
%_initng_service_hook samba daemon/samba
%_initng_service_hook squid daemon/squid
%_initng_service_hook openssh-server daemon/sshd
%_initng_service_hook syslog-ng daemon/syslog-ng
%_initng_service_hook syslog daemon/syslog
%_initng_service_hook X11-xfs daemon/xfs

%_initng_service_hook iptables-init net/iptables

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.runlevel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*/*.i
%attr(755,root,root) %{_sbindir}/*
