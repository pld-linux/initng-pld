Summary:	initng initscripts for PLD Linux
Summary(pl):	Skrypty inicjalizuj�ce initng dla PLD Linuksa
Name:		initng-pld
Version:	0.5.0
%define		_snap 20051225
Release:	0.%{_snap}.3
License:	GPL
Group:		Base
Source0:	initng-initscripts-%{version}-%{_snap}.tar.bz2
# Source0-md5:	09ecc4399a5a0f304a21c28373763a55
URL:		http://svn.pld-linux.org/initng/
Requires:	agetty
Requires:	initng >= %{version}
Requires:	rc-scripts
Conflicts:	mDNSResponder < 107-2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/initng
%define		_exec_prefix /

%description
initng initscripts for PLD Linux.

%description -l pl
Skrypty inicjalizuj�ce initng dla PLD Linuksa.

%package devel
Summary:	Tools for developing PLD initng scripts
Summary(pl):	Narz�dzia do rozwijania skrypt�w initng dla PLD
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	vim-syntax-initng
#Suggests:	subversion

%description devel
Tools for developing PLD initng scripts.

%description devel -l pl
Narz�dzia do rozwijania skrypt�w initng dla PLD.

%prep
%setup -q -n initng-initscripts-%{version}-%{_snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}
cp -a */ *.runlevel $RPM_BUILD_ROOT%{_sysconfdir}
install shutdown_script $RPM_BUILD_ROOT%{_sbindir}
install migrate_rc.d-initng.i.sh test-syntax.sh $RPM_BUILD_ROOT%{_sysconfdir}

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
%_initng_service_hook -p acpid daemon/acpid
%_initng_service_hook -p alsa-utils-init daemon/alsasound
%_initng_service_hook -p anacron daemon/anacron
%_initng_service_hook -p ap-fcgi daemon/ap-fcgi
%_initng_service_hook -p apache daemon/httpd
%_initng_service_hook -p apache1 daemon/apache
%_initng_service_hook -p autofs daemon/autofs
%_initng_service_hook -p bind daemon/named
%_initng_service_hook -p bluez-utils-init daemon/bluetooth
%_initng_service_hook -p bnc-init daemon/bnc
%_initng_service_hook -p bopm daemon/bopm
%_initng_service_hook -p clamav daemon/clamd
%_initng_service_hook -p courier-authlib daemon/courier-authlib
%_initng_service_hook -p courier-imap daemon/courier-imap daemon/courier-imap-ssl
%_initng_service_hook -p cups daemon/cupsd
%_initng_service_hook -p cyrus-imapd daemon/cyrus-imapd
%_initng_service_hook -p cyrus-sasl-saslauthd daemon/saslauthd
%_initng_service_hook -p daemontools daemon/svscan
%_initng_service_hook -p dbus daemon/messagebus
%_initng_service_hook -p dhcp daemon/dhcpd
%_initng_service_hook -p dspam daemon/dspam
%_initng_service_hook -p eventum-irc daemon/eventum-irc
%_initng_service_hook -p exim daemon/exim
%_initng_service_hook -p fam-standalone daemon/famd
%_initng_service_hook -p freevo-boot daemon/freevo daemon/freevo_dep daemon/freevo_recordserver daemon/freevo_webserver
%_initng_service_hook -p gnustep-base daemon/gnustep
%_initng_service_hook -p gpm daemon/gpm
%_initng_service_hook -p hal daemon/haldaemon
%_initng_service_hook -p hc-cron daemon/crond
%_initng_service_hook -p hdparm system/hdparm
%_initng_service_hook -p hotplug daemon/hotplug
%_initng_service_hook -p imapproxy daemon/imapproxy
%_initng_service_hook -p iptables-init daemon/iptables daemon/ip6tables
%_initng_service_hook -p ism-cli daemon/dpcproxy
%_initng_service_hook -p issue-fancy daemon/issue-fancy
%_initng_service_hook -p kbd daemon/console
%_initng_service_hook -p kdenetwork-lanbrowser daemon/lisa
%_initng_service_hook -p kdm daemon/kdm
%_initng_service_hook -p klogd daemon/klogd
%_initng_service_hook -p lighttpd daemon/lighttpd
%_initng_service_hook -p mDNSResponder daemon/mdns
%_initng_service_hook -p mdadm daemon/mdadm
%_initng_service_hook -p mldonkey daemon/mldonkey
%_initng_service_hook -p monit daemon/monit
%_initng_service_hook -p mysql daemon/mysql
%_initng_service_hook -p mythtv-backend daemon/mythbackend
%_initng_service_hook -p nagios daemon/nagios
%_initng_service_hook -p nagios-nrpe daemon/nrpe
%_initng_service_hook -p nessusd daemon/nessusd
%_initng_service_hook -p net-snmp daemon/snmpd
%_initng_service_hook -p nfs-utils-clients daemon/nfsfs
%_initng_service_hook -p ntp daemon/ntpd
%_initng_service_hook -p oidentd-standalone daemon/oidentd
%_initng_service_hook -p openct daemon/openct
%_initng_service_hook -p openldap-servers daemon/slapd
%_initng_service_hook -p openssh-server daemon/sshd
%_initng_service_hook -p openvpn daemon/openvpn
%_initng_service_hook -p polipo daemon/polipo
%_initng_service_hook -p portmap daemon/portmap
%_initng_service_hook -p postfix daemon/postfix
%_initng_service_hook -p pound daemon/pound
%_initng_service_hook -p preload daemon/preload
%_initng_service_hook -p pure-ftpd daemon/pure-ftpd
%_initng_service_hook -p rc-inetd daemon/rc-inetd
%_initng_service_hook -p rc-scripts daemon/cpusets daemon/network daemon/timezone daemon/random daemon/sys-chroots
%_initng_service_hook -p rdate daemon/rdate
%_initng_service_hook -p samba daemon/samba
%_initng_service_hook -p smartsuite daemon/smartd
%_initng_service_hook -p spamassassin-spamd daemon/spamd
%_initng_service_hook -p squid daemon/squid
%_initng_service_hook -p sqwebmail daemon/sqwebmail
%_initng_service_hook -p syslog daemon/syslog
%_initng_service_hook -p syslog-ng daemon/syslog-ng
%_initng_service_hook -p sysstat daemon/sysstat
%_initng_service_hook -p tenshi daemon/tenshi
%_initng_service_hook -p tuxaator-init daemon/tuxaator
%_initng_service_hook -p umlinux-init daemon/uml
%_initng_service_hook -p util-linux daemon/blockdev
%_initng_service_hook -p util-vserver-init daemon/vprocunhide daemon/vservers
%_initng_service_hook -p vixie-cron daemon/crond
%_initng_service_hook -p wine daemon/wine
%_initng_service_hook -p xen daemon/xend daemon/xendomains
%_initng_service_hook -p yum daemon/yum

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.runlevel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*/*.i
%attr(755,root,root) %{_sbindir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/migrate_rc.d-initng.i.sh
%attr(755,root,root) %{_sysconfdir}/test-syntax.sh
