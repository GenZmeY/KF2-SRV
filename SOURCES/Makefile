# kf2-srv is a command line tool for managing a set of Killing Floor 2 servers.
# Copyright (C) 2019, 2020 GenZmeY
# mailto: genzmey@gmail.com
# 
# This file is part of kf2-srv.
#
# kf2-srv is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

NAME           := kf2-srv

SOURCEDIR      := .
RELEASEDIR     := $(SOURCEDIR)/release
BUILDROOT       =
PREFIX          = /usr/local

MAINLOGDIR      = $(BUILDROOT)/var/log/$(NAME)
BETALOGDIR      = $(BUILDROOT)/var/log/$(NAME)-beta
CONFDIR         = $(BUILDROOT)/etc/$(NAME)
INSTMAINDIR     = $(CONFDIR)/instances
INSTBETADIR     = $(CONFDIR)/instances-beta
MAPCYCLEDIR     = $(CONFDIR)/mapcycles
CACHEDIR        = $(BUILDROOT)/var/cache/$(NAME)
LOGROTATEDIR    = $(BUILDROOT)/etc/logrotate.d
RSYSLOGDIR      = $(BUILDROOT)/etc/rsyslog.d
UNITDIR         = $(if $(BUILDROOT),$(BUILDROOT)/usr/lib/systemd/system,/etc/systemd/system)
FIREWALLDDIR    = $(if $(BUILDROOT),$(BUILDROOT)/usr/lib/firewalld/services,/etc/firewalld/services)
BINDIR          = $(BUILDROOT)$(PREFIX)/bin
SBINDIR         = $(BUILDROOT)$(PREFIX)/sbin
GAMEDIR         = $(BUILDROOT)$(PREFIX)/games
DATADIR         = $(BUILDROOT)$(PREFIX)/share
LICENSEDIR      = $(DATADIR)/licenses/$(NAME)
KF2MAINDIR      = $(GAMEDIR)/$(NAME)
KF2BETADIR      = $(GAMEDIR)/$(NAME)-beta

BASHCHECK      := bash -n
SYSTEMDCHECK   := systemd-analyze verify
LOGROTATECHECK := logrotate -d
XMLCHECK       := xmllint --noout

.PHONY: build fake-systemd-build install uninstall filesystem test clean all

all: install

build:
	mkdir $(RELEASEDIR)
	
	cp -r $(SOURCEDIR)/main       $(RELEASEDIR)
	cp -r $(SOURCEDIR)/config     $(RELEASEDIR)
	cp -r $(SOURCEDIR)/force-attr $(RELEASEDIR)
	
	find $(RELEASEDIR) -type f -exec sed -i 's|:DEFINE_PREFIX:|$(PREFIX)|g;' {} \;

fake-systemd-build:
	find $(SOURCEDIR)/main       -type f -name '*.service' -exec cp -f {} $(RELEASEDIR)/{} \;
	find $(SOURCEDIR)/force-attr -type f -name '*.service' -exec cp -f {} $(RELEASEDIR)/{} \;
	find $(RELEASEDIR)           -type f -exec sed -i  's|:DEFINE_PREFIX:|$(BUILDROOT)$(PREFIX)|g;' {} \;
	find $(RELEASEDIR)           -type f -exec sed -i -r 's|ExecStart=.+KFGameSteamServer.bin.x86_64|ExecStart=/bin/bash|g;' {} \;

filesystem:
	test -d '$(CONFDIR)'      || install -m 775 -d '$(CONFDIR)'
	test -d '$(INSTMAINDIR)'  || install -m 775 -d '$(INSTMAINDIR)'
	test -d '$(INSTBETADIR)'  || install -m 775 -d '$(INSTBETADIR)'
	test -d '$(MAPCYCLEDIR)'  || install -m 775 -d '$(MAPCYCLEDIR)'
	test -d '$(CACHEDIR)'     || install -m 775 -d '$(CACHEDIR)'
	test -d '$(BINDIR)'       || install -m 755 -d '$(BINDIR)'
	test -d '$(SBINDIR)'      || install -m 755 -d '$(SBINDIR)'
	test -d '$(KF2MAINDIR)'   || install -m 775 -d '$(KF2MAINDIR)'
	test -d '$(KF2BETADIR)'   || install -m 775 -d '$(KF2BETADIR)'
	test -d '$(LICENSEDIR)'   || install -m 755 -d '$(LICENSEDIR)'
	test -d '$(MAINLOGDIR)'   || install -m 770 -d '$(MAINLOGDIR)'
	test -d '$(BETALOGDIR)'   || install -m 770 -d '$(BETALOGDIR)'
	test -d '$(UNITDIR)'      || install -m 755 -d '$(UNITDIR)'
	test -d '$(FIREWALLDDIR)' || install -m 755 -d '$(FIREWALLDDIR)'
	test -d '$(LOGROTATEDIR)' || install -m 755 -d '$(LOGROTATEDIR)'
	test -d '$(RSYSLOGDIR)'   || install -m 755 -d '$(RSYSLOGDIR)'

install: filesystem build
	install -m 755 $(RELEASEDIR)/main/$(NAME)                                  $(BINDIR)
	install -m 755 $(RELEASEDIR)/main/$(NAME)-beta                             $(BINDIR)
	
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)@.service                 $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-beta@.service            $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-beta-update.service      $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-beta-update.timer        $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-update.service           $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-update.timer             $(UNITDIR)
	
	install -m 644 $(RELEASEDIR)/main/firewalld/$(NAME).xml                    $(FIREWALLDDIR)
	install -m 644 $(RELEASEDIR)/main/logrotate/$(NAME)                        $(LOGROTATEDIR)
	install -m 644 $(RELEASEDIR)/main/rsyslog/$(NAME).conf                     $(RSYSLOGDIR)
	
	install -m 755 $(RELEASEDIR)/force-attr/$(NAME)-force-attr                 $(SBINDIR)
	install -m 644 $(RELEASEDIR)/force-attr/systemd/$(NAME)-force-attr.service $(UNITDIR)
	
	install -m 640 $(RELEASEDIR)/config/bot.conf                               $(CONFDIR)
	install -m 644 $(RELEASEDIR)/config/instance.conf.template                 $(CONFDIR)
	install -m 644 $(RELEASEDIR)/config/$(NAME).conf                           $(CONFDIR)
	
	install -m 644 $(SOURCEDIR)/COPYING                                        $(LICENSEDIR)

uninstall:
	rm -f  $(BINDIR)/$(NAME)
	rm -f  $(BINDIR)/$(NAME)-beta
	
	rm -f  $(UNITDIR)/$(NAME)@.service
	rm -f  $(UNITDIR)/$(NAME)-beta@.service
	rm -f  $(UNITDIR)/$(NAME)-beta-update.service
	rm -f  $(UNITDIR)/$(NAME)-beta-update.timer
	rm -f  $(UNITDIR)/$(NAME)-update.service
	rm -f  $(UNITDIR)/$(NAME)-update.timer
	
	rm -f  $(FIREWALLDDIR)/$(NAME).xml
	rm -f  $(LOGROTATEDIR)/$(NAME)
	rm -f  $(RSYSLOGDIR)/$(NAME).conf
	
	rm -f  $(SBINDIR)/$(NAME)-force-attr
	rm -f  $(UNITDIR)/$(NAME)-force-attr.service
	
	rm -rf $(LICENSEDIR)
	rm -rf $(KF2MAINDIR)
	rm -rf $(KF2BETADIR)
	rm -rf $(CACHEDIR)

test: fake-systemd-build
    ifeq ($(shell $(LOGROTATECHECK) $(RELEASEDIR)/main/logrotate/$(NAME) 2>&1 | grep -qi 'error'; echo $$?), 0)
		$(LOGROTATECHECK) $(RELEASEDIR)/main/logrotate/$(NAME)
    endif
	
	$(XMLCHECK)       $(RELEASEDIR)/main/firewalld/$(NAME).xml
	
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)@.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-beta@.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-beta-update.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-beta-update.timer
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-update.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-update.timer
	$(SYSTEMDCHECK)   $(RELEASEDIR)/force-attr/systemd/$(NAME)-force-attr.service
	
	$(BASHCHECK)      $(RELEASEDIR)/main/$(NAME)
	$(BASHCHECK)      $(RELEASEDIR)/main/$(NAME)-beta
	$(BASHCHECK)      $(RELEASEDIR)/force-attr/$(NAME)-force-attr

clean:
	rm -rf $(RELEASEDIR)

