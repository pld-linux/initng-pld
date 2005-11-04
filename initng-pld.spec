Summary:	initng initscripts for PLD
Summary(pl):	Skrypty inicjalizuj±ce initng dla PLD
Name:		initng-pld
Version:	0.0.6
%define		_snap 20051104
Release:	0.%{_snap}.2
License:	GPL
Group:		Base
Source0:	http://glen.alkohol.ee/pld/initng/initscripts/initng-initscripts-%{_snap}.tar.bz2
# Source0-md5:	09366ccbf6cd02e700efeb0e7ce16f2a
Requires:	initng
Requires:	module-init-tools
Requires:	mount
Requires:	net-tools
Requires:	util-linux
Requires:	agetty
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

%define	_initng_service_hook(p:) \
%triggerin -- %{-p*} \
%{?debug:set -x; echo triggerin %{name}-%{version}-%{release} of %{-p*}}\
if [ "$1" = "1" ] && [ "$2" = "1" ]; then \
	for s in %*; do \
		/sbin/ng-update add $s default \
	done \
fi \
\
%triggerun -- %{-p*} \
%{?debug:set -x; echo triggepostun %{name}-%{version}-%{release} of %{-p*}}\
if [ "$1" = "0" ] || [ "$2" = "0" ]; then \
	for s in %*; do \
		/sbin/ng-update del $s \
	done \
fi \

# Usage:
# _initng_service_hook -p [RPM package/RPM Virtual] [Initng service name(s)]

%_initng_service_hook -p ApacheJServ-init daemon/jserv
%_initng_service_hook -p X11-xfs daemon/xfs
%_initng_service_hook -p alsa-utils-init daemon/alsasound
%_initng_service_hook -p ap-fcgi daemon/ap-fcgi
%_initng_service_hook -p apache daemon/httpd
%_initng_service_hook -p apache1 daemon/apache
%_initng_service_hook -p autofs daemon/autofs
%_initng_service_hook -p bind daemon/named
%_initng_service_hook -p bnc-init daemon/bnc
%_initng_service_hook -p bopm daemon/bopm
%_initng_service_hook -p clamav daemon/clamd
%_initng_service_hook -p courier-authlib daemon/courier-authlib
%_initng_service_hook -p courier-imap daemon/courier-imap daemon/courier-imap-ssl
%_initng_service_hook -p crondaemon daemon/crond
%_initng_service_hook -p cups daemon/cupsd
%_initng_service_hook -p cyrus-sasl-saslauthd daemon/saslauthd
%_initng_service_hook -p dbus daemon/messagebus
%_initng_service_hook -p dhcp daemon/dhcpd
%_initng_service_hook -p dspam daemon/dspam
%_initng_service_hook -p eventum-irc daemon/eventum-irc
%_initng_service_hook -p freevo-boot daemon/freevo daemon/freevo_dep daemon/freevo_recordserver daemon/freevo_webserver
%_initng_service_hook -p gpm daemon/gpm
%_initng_service_hook -p hotplug daemon/hotplug
%_initng_service_hook -p imapproxy daemon/imapproxy
%_initng_service_hook -p iptables-init net/iptables daemon/ip6tables
%_initng_service_hook -p ism-cli daemon/dpcproxy
%_initng_service_hook -p kbd daemon/console
%_initng_service_hook -p kdenetwork-lanbrowser daemon/lisa
%_initng_service_hook -p kdm daemon/kdm
%_initng_service_hook -p klogd daemon/klogd
%_initng_service_hook -p lighttpd daemon/lighttpd
%_initng_service_hook -p mDNSResponder daemon/mdns
%_initng_service_hook -p mldonkey daemon/mldonkey
%_initng_service_hook -p mysql daemon/mysql
%_initng_service_hook -p mythtv-backend daemon/mythbackend
%_initng_service_hook -p nessusd daemon/nessusd
%_initng_service_hook -p net-snmp daemon/snmpd
%_initng_service_hook -p nfs-utils-clients daemon/nfsfs
%_initng_service_hook -p ntp daemon/ntpd
%_initng_service_hook -p openldap-servers daemon/slapd
%_initng_service_hook -p openssh-server daemon/sshd
%_initng_service_hook -p openvpn daemon/openvpn
%_initng_service_hook -p polipo daemon/polipo
%_initng_service_hook -p portmap daemon/portmap
%_initng_service_hook -p postfix daemon/postfix
%_initng_service_hook -p pound daemon/pound
%_initng_service_hook -p pure-ftpd daemon/pure-ftpd
%_initng_service_hook -p rc-inetd daemon/rc-inetd
%_initng_service_hook -p rc-scripts daemon/cpusets daemon/network daemon/timezone
%_initng_service_hook -p rdate daemon/rdate
%_initng_service_hook -p samba daemon/samba
%_initng_service_hook -p spamassassin-spamd daemon/spamd
%_initng_service_hook -p squid daemon/squid
%_initng_service_hook -p syslog daemon/syslog
%_initng_service_hook -p syslog-ng daemon/syslog-ng
%_initng_service_hook -p sysstat daemon/sysstat
%_initng_service_hook -p tenshi daemon/tenshi
%_initng_service_hook -p tuxaator-init daemon/tuxaator
%_initng_service_hook -p umlinux-init daemon/uml
%_initng_service_hook -p util-vserver-init daemon/vprocunhide daemon/vservers-default
%_initng_service_hook -p xen daemon/xend daemon/xendomains
%_initng_service_hook -p yum daemon/yum
%_initng_service_hook -p hdparm system/hdparm

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.runlevel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*/*.i
%attr(755,root,root) %{_sbindir}/*
