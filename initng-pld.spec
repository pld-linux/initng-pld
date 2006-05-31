%define		_snap 20060531
%define		_extraver %{nil}
Summary:	initng initscripts for PLD Linux
Summary(de):	Initng Init Skripts für PLD Linux
Summary(pl):	Skrypty inicjalizuj±ce initng dla PLD Linuksa
Name:		initng-pld
Version:	0.6.7
Release:	0.%{_snap}.1
License:	GPL
Group:		Base
Source0:	initng-initscripts-%{version}%{_extraver}-%{_snap}.tar.bz2
# Source0-md5:	11809468d1ed20122df0efc21c3577de
URL:		http://svn.pld-linux.org/initng/
Requires:	agetty
Requires:	initng >= 0.6.1
# initng-tools can be built from initng-ifiles.spec
Requires:	initng-tools
Requires:	rc-scripts
Conflicts:	ApacheJServ < 1.1.2-0.79
Conflicts:	apache < 2.2.0
Conflicts:	courier-imap < 4.0.5
Conflicts:	mDNSResponder < 107-2.1
Conflicts:	spamassassin-spamd < 3.1.0-5.3
Conflicts:	util-linux < 2.12r-2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/initng
%define		_exec_prefix /

%description
initng initscripts for PLD Linux.

%description -l de
Initng Init Skripte für PLD Linux.

%description -l pl
Skrypty inicjalizuj±ce initng dla PLD Linuksa.

%package devel
Summary:	Tools for developing PLD initng scripts
Summary(de):	Tools zur PLD Initng Skripts Entwicklung
Summary(pl):	Narzêdzia do rozwijania skryptów initng dla PLD
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	vim-syntax-initng
#Suggests:	subversion

%description devel
Tools for developing PLD initng scripts.

%description devel -l de
Tools zur PLD Initng Skripts Entwicklung.

%description devel -l pl
Narzêdzia do rozwijania skryptów initng dla PLD.

%prep
%setup -q -n initng-initscripts-%{version}%{_extraver}-%{_snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}
cp -a */ *.runlevel *.virtual $RPM_BUILD_ROOT%{_sysconfdir}
echo 'system' > $RPM_BUILD_ROOT%{_sysconfdir}/default.runlevel
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
		/sbin/ngc -z $s \
	done \
fi \

# Usage:
# _initng_service_hook -p [RPM package/RPM Virtual] [Initng service name(s)]
# please sort the list (in vim: select block with shift+v and :!sort)

%_initng_service_hook -p ApacheJServ daemon/jserv
%_initng_service_hook -p Canna daemon/canna
%_initng_service_hook -p LPRng daemon/lpd
%_initng_service_hook -p X11-xdm daemon/xdm
%_initng_service_hook -p X11-xfs daemon/xfs
%_initng_service_hook -p Zope daemon/z2.py
%_initng_service_hook -p Zope3 daemon/zope3
%_initng_service_hook -p acpid daemon/acpid
%_initng_service_hook -p alsa-utils-init daemon/alsasound
%_initng_service_hook -p anacron daemon/anacron
%_initng_service_hook -p anubis daemon/anubis
%_initng_service_hook -p ap-fcgi daemon/ap-fcgi
%_initng_service_hook -p apache-base daemon/httpd
%_initng_service_hook -p apache1 daemon/apache
%_initng_service_hook -p apcupsd daemon/apcupsd daemon/halt
%_initng_service_hook -p apinger daemon/apinger
%_initng_service_hook -p apmd daemon/apmd
%_initng_service_hook -p arpd daemon/arpd
%_initng_service_hook -p arpwatch daemon/arpwatch
%_initng_service_hook -p asterisk daemon/asterisk
%_initng_service_hook -p at daemon/atd
%_initng_service_hook -p athcool daemon/athcool
%_initng_service_hook -p atsar daemon/atsar
%_initng_service_hook -p audit daemon/auditd
%_initng_service_hook -p aumix-preserve-settings daemon/aumix
%_initng_service_hook -p autofs daemon/autofs
%_initng_service_hook -p autolog daemon/autolog
%_initng_service_hook -p bigsister daemon/bigsister
%_initng_service_hook -p bind daemon/named
%_initng_service_hook -p bircd daemon/ircd
%_initng_service_hook -p bird-ipv4 daemon/bird-ipv4
%_initng_service_hook -p bird-ipv6 daemon/bird-ipv6
%_initng_service_hook -p blockdev daemon/blockdev
%_initng_service_hook -p bluez-utils-init daemon/bluetooth
%_initng_service_hook -p bnc-init daemon/bnc
%_initng_service_hook -p boa daemon/boa
%_initng_service_hook -p bootparamd daemon/rpc.bootparamd
%_initng_service_hook -p bopm daemon/bopm
%_initng_service_hook -p camserv-relay daemon/camserv-relay
%_initng_service_hook -p cancd daemon/cancd
%_initng_service_hook -p capi4k-utils daemon/capi
%_initng_service_hook -p cherokee daemon/cherokee
%_initng_service_hook -p clamav daemon/clamd
%_initng_service_hook -p clamsmtp daemon/clamsmtpd
%_initng_service_hook -p conserver daemon/conserver
%_initng_service_hook -p courier-authlib daemon/courier-authlib
%_initng_service_hook -p courier-imap daemon/courier-imap daemon/courier-imap-ssl
%_initng_service_hook -p courier-imap-pop3 daemon/courier-pop3
%_initng_service_hook -p cpudyn daemon/cpudynd
%_initng_service_hook -p cpufreqd daemon/cpufreqd
%_initng_service_hook -p cups daemon/cups
%_initng_service_hook -p cyrus-imapd daemon/cyrus-imapd
%_initng_service_hook -p cyrus-sasl-saslauthd daemon/saslauthd
%_initng_service_hook -p daemontools daemon/svscan
%_initng_service_hook -p dbus daemon/messagebus
%_initng_service_hook -p dcd daemon/dcd
%_initng_service_hook -p ddclient daemon/ddclient
%_initng_service_hook -p dgee daemon/dgee
%_initng_service_hook -p dhcp daemon/dhcpd
%_initng_service_hook -p dhcp-relay daemon/dhcp-relay
%_initng_service_hook -p discover daemon/discover
%_initng_service_hook -p distcc-standalone daemon/distcc
%_initng_service_hook -p dkms daemon/dkms_autoinstaller
%_initng_service_hook -p dnsmasq daemon/dnsmasq
%_initng_service_hook -p drbdsetup daemon/drbd
%_initng_service_hook -p dspam daemon/dspam
%_initng_service_hook -p ejabberd daemon/ejabberd
%_initng_service_hook -p eventum-irc daemon/eventum-irc
%_initng_service_hook -p exim daemon/exim
%_initng_service_hook -p eximstate-client daemon/eximstate
%_initng_service_hook -p ez-ipupdate daemon/ez-ipupdate
%_initng_service_hook -p fakebo daemon/fakebo
%_initng_service_hook -p fam-standalone daemon/famd
%_initng_service_hook -p fbset daemon/fbset
%_initng_service_hook -p fetchmail-daemon daemon/fetchmail
%_initng_service_hook -p filtergen daemon/filtergen
%_initng_service_hook -p firestarter daemon/firestarter
%_initng_service_hook -p firewall-init daemon/firewall daemon/firewall-pre
%_initng_service_hook -p freeradius daemon/freeradius
%_initng_service_hook -p freevo-boot daemon/freevo daemon/freevo_dep daemon/freevo_recordserver daemon/freevo_webserver
%_initng_service_hook -p frox daemon/frox
%_initng_service_hook -p gkrellm-gkrellmd daemon/gkrellmd
%_initng_service_hook -p gnustep-base daemon/gnustep
%_initng_service_hook -p gpm daemon/gpm
%_initng_service_hook -p hal daemon/haldaemon
%_initng_service_hook -p hc-cron daemon/crond
%_initng_service_hook -p hddtemp-hddtempd daemon/hddtempd
%_initng_service_hook -p hdparm daemon/hdparm
%_initng_service_hook -p heimdal-server daemon/kdc daemon/kpasswdd
%_initng_service_hook -p hotplug daemon/hotplug
%_initng_service_hook -p htb.init daemon/htb
%_initng_service_hook -p htpdate daemon/htpdate
%_initng_service_hook -p httptunnel-server daemon/httptunnel
%_initng_service_hook -p icecast daemon/icecast
%_initng_service_hook -p idled daemon/idled
%_initng_service_hook -p imapproxy daemon/imapproxy
%_initng_service_hook -p inn daemon/inn
%_initng_service_hook -p ipac-ng daemon/ipac-ng
%_initng_service_hook -p ipband daemon/ipband
%_initng_service_hook -p ipfm daemon/ipfm
%_initng_service_hook -p iplog daemon/iplog
%_initng_service_hook -p ippl daemon/ippl
%_initng_service_hook -p iptables-init daemon/iptables daemon/ip6tables
%_initng_service_hook -p ipxripd daemon/ipxripd
%_initng_service_hook -p ipxtund daemon/ipxtund
%_initng_service_hook -p irqbalance daemon/irqbalance
%_initng_service_hook -p ism-cli daemon/dpcproxy
%_initng_service_hook -p issue-fancy daemon/issue-fancy
%_initng_service_hook -p jabber-aim-transport daemon/jabber-aimtrans
%_initng_service_hook -p jabber-msn-transport daemon/jabber-msntrans
%_initng_service_hook -p jabber-mu-conference daemon/jabber-muc
%_initng_service_hook -p jabberd daemon/jabberd
%_initng_service_hook -p janchor daemon/janchor
%_initng_service_hook -p jit daemon/jit
%_initng_service_hook -p kbd daemon/console
%_initng_service_hook -p kdenetwork-lanbrowser daemon/lisa
%_initng_service_hook -p kdm daemon/kdm
%_initng_service_hook -p klogd daemon/klogd
%_initng_service_hook -p kudzu-rc daemon/kudzu
%_initng_service_hook -p laptop-mode-tools daemon/laptop-mode
%_initng_service_hook -p lighttpd daemon/lighttpd
%_initng_service_hook -p linux-atm-rc-scripts daemon/atm
%_initng_service_hook -p linux-wlan-ng daemon/wlan
%_initng_service_hook -p lirc daemon/lircmd
%_initng_service_hook -p lm_sensors-sensord daemon/sensors
%_initng_service_hook -p lms-lmsd daemon/lmsd
%_initng_service_hook -p lstat daemon/lstatd
%_initng_service_hook -p lsvpd daemon/lsvpd
%_initng_service_hook -p lvcool daemon/lvcool
%_initng_service_hook -p mDNSResponder daemon/mdns
%_initng_service_hook -p mailgraph daemon/mailgraph
%_initng_service_hook -p mailman daemon/mailman
%_initng_service_hook -p maradns daemon/maradns
%_initng_service_hook -p maradns-zoneserver daemon/zoneserver
%_initng_service_hook -p mars_nwe daemon/ncpserv
%_initng_service_hook -p mcserv daemon/mcserv
%_initng_service_hook -p mdadm daemon/mdadm
%_initng_service_hook -p memcached daemon/memcached
%_initng_service_hook -p metalog daemon/metalog
%_initng_service_hook -p microcode_ctl daemon/microcode_ctl
%_initng_service_hook -p mini_httpd daemon/mini_mini_httpd
%_initng_service_hook -p mksd daemon/mksd
%_initng_service_hook -p mldonkey daemon/mldonkey
%_initng_service_hook -p mmtcpfwd daemon/mmtcpfwd
%_initng_service_hook -p monit daemon/monit
%_initng_service_hook -p monkey daemon/monkeyd
%_initng_service_hook -p mrt daemon/mrtd
%_initng_service_hook -p mserver daemon/mserver
%_initng_service_hook -p muddleftpd daemon/muddleftpd
%_initng_service_hook -p munin-node daemon/munin-node
%_initng_service_hook -p mysql daemon/mysql
%_initng_service_hook -p mythtv-backend daemon/mythbackend
%_initng_service_hook -p nagios daemon/nagios
%_initng_service_hook -p nagios-nrpe daemon/nrpe
%_initng_service_hook -p nessusd daemon/nessusd
%_initng_service_hook -p net-snmp daemon/snmpd
%_initng_service_hook -p net-snmp-snmptrapd daemon/snmptrapd
%_initng_service_hook -p netconsole daemon/netconsole
%_initng_service_hook -p netplug daemon/netplugd
%_initng_service_hook -p nfs-utils daemon/nfs
%_initng_service_hook -p nfs-utils-clients daemon/nfsfs
%_initng_service_hook -p nfs-utils-lock daemon/nfslock
%_initng_service_hook -p niceshaper daemon/niceshaper
%_initng_service_hook -p noip daemon/noip
%_initng_service_hook -p nscd daemon/nscd
%_initng_service_hook -p ntop daemon/ntop
%_initng_service_hook -p ntp daemon/ntpd
%_initng_service_hook -p nut daemon/upsd
%_initng_service_hook -p nut-client daemon/upsmon
%_initng_service_hook -p oidentd-standalone daemon/oidentd
%_initng_service_hook -p onetkonekt daemon/onetkonekt.pl
%_initng_service_hook -p openct daemon/openct
%_initng_service_hook -p openldap-servers daemon/slapd
%_initng_service_hook -p openslp-server daemon/slpd
%_initng_service_hook -p openssh-server daemon/sshd
%_initng_service_hook -p openswan daemon/ipsec
%_initng_service_hook -p openvpn daemon/openvpn
%_initng_service_hook -p p0f daemon/p0f
%_initng_service_hook -p p3scan daemon/p3scan
%_initng_service_hook -p pbbuttonsd daemon/pbbuttonsd
%_initng_service_hook -p pcmcia-cs daemon/pcmcia
%_initng_service_hook -p pcsc-lite daemon/pcscd
%_initng_service_hook -p pdns daemon/pdns
%_initng_service_hook -p pdnsd daemon/pdnsd
%_initng_service_hook -p php-fcgi-init daemon/php-fcgi
%_initng_service_hook -p plptools daemon/psion
%_initng_service_hook -p polipo daemon/polipo
%_initng_service_hook -p pop-before-smtp daemon/popbsmtp
%_initng_service_hook -p portfwd daemon/portfwd
%_initng_service_hook -p portmap daemon/portmap
%_initng_service_hook -p portsentry daemon/portsentry
%_initng_service_hook -p postfix daemon/postfix
%_initng_service_hook -p postgresql daemon/postmaster
%_initng_service_hook -p pound daemon/pound
%_initng_service_hook -p poweracpid daemon/poweracpid
%_initng_service_hook -p preload daemon/preload
%_initng_service_hook -p privoxy daemon/privoxy
%_initng_service_hook -p proftpd-standalone daemon/proftpd
%_initng_service_hook -p protolog daemon/protolog
%_initng_service_hook -p pulsard daemon/pulsard
%_initng_service_hook -p pure-ftpd daemon/pure-ftpd
%_initng_service_hook -p pyrss daemon/pyrss
%_initng_service_hook -p qpopper-ssl-standalone daemon/qpoppersd
%_initng_service_hook -p qpopper-standalone daemon/qpopperd
%_initng_service_hook -p quagga daemon/zebra
%_initng_service_hook -p quake2-server daemon/quake2-server
%_initng_service_hook -p quake3-server daemon/q3ded
%_initng_service_hook -p quakeforge-servers daemon/nq-serverd daemon/qw-serverd
%_initng_service_hook -p quota-rquotad daemon/rquotad
%_initng_service_hook -p radvd daemon/radvd
%_initng_service_hook -p rarpd daemon/rarpd
%_initng_service_hook -p rawdevices daemon/rawdevices
%_initng_service_hook -p rbldnsd daemon/rbldnsd
%_initng_service_hook -p rc-inetd daemon/rc-inetd
%_initng_service_hook -p rc-scripts daemon/allowlogin daemon/cpusets daemon/network daemon/timezone daemon/random daemon/sys-chroots
%_initng_service_hook -p rdate daemon/rdate
%_initng_service_hook -p routed daemon/routed
%_initng_service_hook -p rp-pppoe-relay daemon/pppoe-relay
%_initng_service_hook -p rp-pppoe-server daemon/pppoe-server
%_initng_service_hook -p rpasswdd daemon/rpasswdd
%_initng_service_hook -p rpld daemon/rpld
%_initng_service_hook -p rstatd daemon/rpc.rstatd
%_initng_service_hook -p rusersd daemon/rpc.rusersd
%_initng_service_hook -p rwalld daemon/rpc.rwalld
%_initng_service_hook -p rwho daemon/rwhod
%_initng_service_hook -p samba daemon/smb
%_initng_service_hook -p sendmail daemon/sendmail
%_initng_service_hook -p shaperd.2 daemon/shaperd
%_initng_service_hook -p smartsuite daemon/smartd
%_initng_service_hook -p smokeping daemon/smokeping
%_initng_service_hook -p smstools daemon/smsd
%_initng_service_hook -p snort daemon/snort
%_initng_service_hook -p spamassassin-spamd daemon/spamd
%_initng_service_hook -p spfd daemon/spfd
%_initng_service_hook -p splashutils splashutils
%_initng_service_hook -p squid daemon/squid
%_initng_service_hook -p sqwebmail daemon/sqwebmail
%_initng_service_hook -p srsd daemon/srsd
%_initng_service_hook -p subversion-svnserve daemon/svnserve
%_initng_service_hook -p swapd daemon/swapd
%_initng_service_hook -p sympa daemon/sympa
%_initng_service_hook -p syslog daemon/syslog
%_initng_service_hook -p syslog-ng daemon/syslog-ng
%_initng_service_hook -p sysstat daemon/sysstat
%_initng_service_hook -p tac_plus daemon/tac_plus
%_initng_service_hook -p tenshi daemon/tenshi
%_initng_service_hook -p thttpd daemon/thttpd
%_initng_service_hook -p tpop3d daemon/tpop3d
%_initng_service_hook -p tuxaator-init daemon/tuxaator
%_initng_service_hook -p ulogd daemon/ulogd
%_initng_service_hook -p umlinux-init daemon/uml
%_initng_service_hook -p util-vserver-init daemon/vprocunhide daemon/vservers daemon/vrootdevices
%_initng_service_hook -p vfmg daemon/vfmg
%_initng_service_hook -p vixie-cron daemon/crond
%_initng_service_hook -p vm-pop3d-standalone daemon/pop3d
%_initng_service_hook -p vsftpd-standalone daemon/vsftpd
%_initng_service_hook -p vtun daemon/vtund
%_initng_service_hook -p wanpipe daemon/wanrouter
%_initng_service_hook -p watchdog daemon/watchdog
%_initng_service_hook -p wccpd daemon/wccpd
%_initng_service_hook -p webmin daemon/webmin
%_initng_service_hook -p whoson-server daemon/whosond
%_initng_service_hook -p wine daemon/wine
%_initng_service_hook -p wwwoffle daemon/wwwoffle
%_initng_service_hook -p xen daemon/xend daemon/xendomains
%_initng_service_hook -p ypbind-mt daemon/ypbind
%_initng_service_hook -p ypserv daemon/rpc.yppasswdd daemon/ypserv daemon/ypxfrd
%_initng_service_hook -p yum daemon/yum
%_initng_service_hook -p zmailer daemon/zmailer

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.runlevel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.virtual
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/system
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/net

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/migrate_rc.d-initng.i.sh
%attr(755,root,root) %{_sysconfdir}/test-syntax.sh
