%global steamuser steam

Name:      kf2-srv
Version:   0.5.0
Release:   1%{dist}
Summary:   Killing Floor 2 server
Group:     Amusements/Games
License:   GNU GPLv3
BuildArch: noarch

Source1:   %{name}
Source2:   %{name}.conf
Source3:   %{name}.xml
Source4:   %{name}@.service
Source5:   %{name}-update.service
Source6:   %{name}-update.timer
Source7:   main.conf.template

Requires:  systemd >= 219
Requires:  steamcmd
Requires:  libxml2

Provides:  %{name}

%description
Command line tool for managing a set of Killing Floor 2 servers.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 -d %{buildroot}/%{_prefix}/lib/systemd/system
install -m 755 -d %{buildroot}/%{_prefix}/lib/firewalld/services
install -m 755 -d %{buildroot}/%{_sysconfdir}/%{name}/instances
install -m 644 -d %{buildroot}/%{_prefix}/games/%{name}

install -m 755 %{SOURCE1} %{buildroot}/%{_bindir}
install -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}
install -m 644 %{SOURCE3} %{buildroot}/%{_prefix}/lib/firewalld/services
install -m 644 %{SOURCE4} %{buildroot}/%{_prefix}/lib/systemd/system
install -m 644 %{SOURCE5} %{buildroot}/%{_prefix}/lib/systemd/system
install -m 644 %{SOURCE6} %{buildroot}/%{_prefix}/lib/systemd/system
install -m 644 %{SOURCE7} %{buildroot}/%{_sysconfdir}/%{name}

sed -i -r "s|^(InstallDir=).*$|\1\"%{_prefix}/games/%{name}\"|g" %{buildroot}/%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(775,root,%{steamuser}) %dir       %{_prefix}/games/%{name}
%attr(775,root,%{steamuser}) %dir       %{_sysconfdir}/%{name}
%attr(775,root,%{steamuser}) %dir       %{_sysconfdir}/%{name}/instances
%attr(644,root,root)                    %{_sysconfdir}/%{name}/main.conf.template
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(644,root,root) %config(noreplace) %{_prefix}/lib/firewalld/services/%{name}.xml
%attr(755,root,root)                    %{_bindir}/%{name}
%attr(644,root,root)                    %{_prefix}/lib/systemd/system/*

%post
#/bin/env bash
#if [[ $1 -eq 1 ]]; then # First installation
#	
#fi
#exit 0

%preun
#/bin/env bash
if [[ $1 -eq 0 ]] ; then # Uninstall
	%{_bindir}/%{name} --stop
	%{_bindir}/%{name} --disable
	rm -rf %{_prefix}/games/%{name}/*
fi

%changelog
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
