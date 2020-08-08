%global steamuser steam

Name:       kf2-srv
Version:    0.14.0
Release:    1%{dist}
Summary:    Killing Floor 2 server
Group:      Amusements/Games
License:    GNU GPLv3
BuildArch:  noarch

Source0:    %{name}-%{version}.tar.gz 

BuildRequires: systemd-rpm-macros

#BuildRequires(check): xmllint
#BuildRequires(check): systemd >= 219

Requires:   systemd >= 219
Requires:   steamcmd >= 2018.01.05-5
Requires:   libxml2
Requires:   dos2unix
Requires:   curl
Requires:   grep
Requires:   coreutils
Requires:   sed
Requires:   util-linux
Requires:   sudo
Requires:   psmisc
Requires:   gawk
Requires:   multini >= 0.2.3
Requires:   rsyslog >= 8.25.0
Requires:   logrotate
Requires:   inotify-tools

Provides:   %{name}

%description
Command line tool for managing a set of Killing Floor 2 servers.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%check
make test DESTDIR=%{buildroot} PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0775,root,%{steamuser}) %dir               %{_prefix}/games/%{name}
%attr(0775,root,%{steamuser}) %dir               %{_prefix}/games/%{name}-beta
%attr(0775,root,%{steamuser}) %dir               %{_sysconfdir}/%{name}
%attr(0775,root,%{steamuser}) %dir               %{_sysconfdir}/%{name}/instances
%attr(0775,root,%{steamuser}) %dir               %{_sysconfdir}/%{name}/instances-beta
%attr(0775,root,%{steamuser}) %dir               %{_sysconfdir}/%{name}/mapcycles
%attr(0775,root,%{steamuser}) %dir               %{_localstatedir}/log/%{name}
%attr(0775,root,%{steamuser}) %dir               %{_localstatedir}/log/%{name}-beta
%attr(0775,root,%{steamuser}) %dir               %{_localstatedir}/cache/kf2-srv
%attr(0775,root,root)         %dir               %{_datadir}/%{name}
%attr(0775,root,root)         %dir               %{_datadir}/%{name}/cmdgrp
%attr(0755,root,root)         %dir               %{_datadir}/%{name}/cmdgrp/*
%attr(0775,root,root)         %dir               %{_datadir}/%{name}/lib
%attr(0664,root,%{steamuser}) %config(noreplace) %{_sysconfdir}/%{name}/instance.conf.template
%attr(0664,root,%{steamuser}) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0640,root,%{steamuser}) %config(noreplace) %{_sysconfdir}/%{name}/bot.conf
%attr(0644,root,root)         %config(noreplace) %{_prefix}/lib/firewalld/services/%{name}.xml
%attr(0755,root,root)                            %{_bindir}/%{name}
%attr(0755,root,root)                            %{_bindir}/%{name}-beta
%attr(0755,root,root)                            %{_sbindir}/%{name}-force-attr
%attr(0644,root,root)                            %{_unitdir}/*
%attr(0644,root,root)         %doc               %{_datadir}/licenses/%{name}/*
%attr(0644,root,root)                            %{_sysconfdir}/rsyslog.d/%{name}.conf
%attr(0644,root,root)                            %{_sysconfdir}/logrotate.d/%{name}
%attr(0644,root,root)                            %{_datadir}/%{name}/cmdgrp/*/*
%attr(0644,root,root)                            %{_datadir}/%{name}/lib/*

%preun
if [[ $1 -eq 0 ]] ; then # Uninstall
	%{_bindir}/%{name} instance stop
	%{_bindir}/%{name} instance disable
	rm -rf %{_prefix}/games/%{name}/*
	rm -rf %{_prefix}/games/%{name}-beta/*
	rm -rf %{_sysconfdir}/%{name}/instances/default
	rm -rf %{_sysconfdir}/%{name}/instances-beta/default
	rm -rf %{_localstatedir}/cache/kf2-srv/*
fi

%post
if [[ $1 == 1 ]]; then # Install
	systemctl daemon-reload
	systemctl try-restart rsyslog.service
fi

%changelog
* Sat Aug 8 2020 GenZmeY <genzmey@gmail.com> - 0.14.0-1
- new usage (groups/commands);
- new code structure;
- build system;
- tests;
- parallel actions;
- short english description.

* Sun Jul 19 2020 GenZmeY <genzmey@gmail.com> - 0.13.0-1
- /var/cache to store the workshop cache;
- fixed endless downloading of workshop items that tripware gave us in PC Build 1099 patch;
- using ForcePermissions when creating instances;
- add %check section to specfile.

* Mon Jul 13 2020 GenZmeY <genzmey@gmail.com> - 0.12.1-1
- rename main.conf to instance.conf.
 
* Mon Jul 13 2020 GenZmeY <genzmey@gmail.com> - 0.12.0-1
- chat logs without timestamp;
- update rsyslog config - now logs will be create with steam group and 640 permissions;
- update logrotate config (fixed that logrotate does nothing);
- bot password in separate file without read permission to others;
- feat: force attr for log/ini files.

* Thu Jul 9 2020 GenZmeY <genzmey@gmail.com> - 0.11.1-1
- fix syntax error in firewalld service.

* Wed Jul 8 2020 GenZmeY <genzmey@gmail.com> - 0.11.0-1
- logging (rsyslog + logrotate).

* Wed Jul 8 2020 GenZmeY <genzmey@gmail.com> - 0.10.1-1
- add COPYING to distributive;
- add license info to kf2-srv-beta;
- spec fixes;

* Mon Jun 22 2020 GenZmeY <genzmey@gmail.com> - 0.10.0-1
- separate mutators setting;
- mutator column in server list;
- chat notifications on restart for updates;
- unban on working servers;
- refactoring.

* Sun May 31 2020 GenZmeY <genzmey@gmail.com> - 0.9.1-1
- fix realtime -mrl with spaces;
- mapcycles directory.

* Wed May 27 2020 GenZmeY <genzmey@gmail.com> - 0.9.0-1
- new main.conf format;
- multiple WebAdmin and http auth by default;
- online actions;
- chat-bot;
- set password;
- refactoring.

* Mon Apr 27 2020 GenZmeY <genzmey@gmail.com> - 0.8.0-1
- use multini for ini edit;
- add mutators support;
- refactoring;
- returned "reboot-updates".

* Sat Mar 7 2020 GenZmeY <genzmey@gmail.com> - 0.7.0-1
- dual versions support;
- check updates;
- bugfixes.

* Sat Jan 18 2020 GenZmeY <genzmey@gmail.com> - 0.6.0-1
- versions;
- instance conf tweaks;
- extended map list;
- clear cache on delete map;
- removed useless messages.

* Sun Jan 12 2020 GenZmeY <genzmey@gmail.com> - 0.5.0-1
- ban admin;
- map admin;
- multiple args support.

* Sun Sep 29 2019 GenZmeY <genzmey@gmail.com> - 0.4.0-1
- Reworked main.template and kf2-srv@.service;
- Add --restart option;
- --status option shows more info;
- --list option removed.

* Fri Sep 20 2019 GenZmeY <genzmey@gmail.com> - 0.3.0-1
- validate option;
- auto validate on change active branch;
- port info on --status.

* Mon Sep 16 2019 GenZmeY <genzmey@gmail.com> - 0.2.1-1
- --map-sync bugfixes.

* Mon Sep 16 2019 GenZmeY <genzmey@gmail.com> - 0.2.0-1
- Add --map-sync implementation to kf2-srv.

* Sat Sep 14 2019 GenZmeY <genzmey@gmail.com> - 0.1.0-1
- First version of spec.
