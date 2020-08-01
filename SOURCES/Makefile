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

BASH         := /bin/bash

NAME         := kf2-srv

SOURCEDIR    := .

MAINLOGDIR   := /var/log/$(NAME)
BETALOGDIR   := /var/log/$(NAME)-beta
CONFDIR      := /etc/$(NAME)
INSTMAINDIR  := $(CONFDIR)/instances
INSTBETADIR  := $(CONFDIR)/instances-beta
MAPCYCLEDIR  := $(CONFDIR)/mapcycles
CACHEDIR     := /var/cache/$(NAME)
LOGROTATEDIR := /etc/logrotate.d
RSYSLOGDIR   := /etc/rsyslog.d
SERVICEDIR    = $(if $(BUILDROOT),/lib/systemd/system,/etc/systemd/system)
FIREWALLDDIR  = $(if $(BUILDROOT),/lib/firewalld/services,/etc/firewalld/services)

BUILDROOT     =
PREFIX        = /usr/local
BINDIR        = $(BUILDROOT)$(PREFIX)/bin
SBINDIR       = $(BUILDROOT)$(PREFIX)/sbin
GAMEDIR       = $(BUILDROOT)$(PREFIX)/games
DATADIR       = $(BUILDROOT)$(PREFIX)/share
LICENSEDIR    = $(DATADIR)/licenses/$(NAME)
KF2MAINDIR    = $(GAMEDIR)/$(NAME)
KF2BETADIR    = $(GAMEDIR)/$(NAME)-beta

.PHONY: all install uninstall filesystem

all: install

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
	test -d '$(SERVICEDIR)'   || install -m 755 -d '$(SERVICEDIR)'
	test -d '$(FIREWALLDDIR)' || install -m 755 -d '$(FIREWALLDDIR)'
	test -d '$(LOGROTATEDIR)' || install -m 755 -d '$(LOGROTATEDIR)'
	test -d '$(RSYSLOGDIR)'   || install -m 755 -d '$(RSYSLOGDIR)'

install: filesystem
	install -m 755 $(SOURCEDIR)/main/$(NAME)                                  $(BINDIR)
	install -m 755 $(SOURCEDIR)/main/$(NAME)-beta                             $(BINDIR)
	
	install -m 644 $(SOURCEDIR)/main/systemd/$(NAME)@.service                 $(SERVICEDIR)
	install -m 644 $(SOURCEDIR)/main/systemd/$(NAME)-beta@.service            $(SERVICEDIR)
	install -m 644 $(SOURCEDIR)/main/systemd/$(NAME)-beta-update.service      $(SERVICEDIR)
	install -m 644 $(SOURCEDIR)/main/systemd/$(NAME)-beta-update.timer        $(SERVICEDIR)
	install -m 644 $(SOURCEDIR)/main/systemd/$(NAME)-update.service           $(SERVICEDIR)
	install -m 644 $(SOURCEDIR)/main/systemd/$(NAME)-update.timer             $(SERVICEDIR)
	
	install -m 644 $(SOURCESIR)/main/firewalld/$(NAME).xml                    $(FIREWALLDDIR)
	install -m 644 $(SOURCESIR)/main/logrotate/$(NAME)                        $(LOGROTATEDIR)
	install -m 644 $(SOURCESIR)/main/rsyslog/$(NAME).conf                     $(RSYSLOGDIR)
	
	install -m 755 $(SOURCEDIR)/force-attr/$(NAME)-force-attr                 $(SBINDIR)
	install -m 755 $(SOURCEDIR)/force-attr/systemd/$(NAME)-force-attr.service $(SERVICEDIR)
	
	install -m 644 $(SOURCEDIR)/conf/bot.conf                                 $(CONFDIR)
	install -m 644 $(SOURCEDIR)/conf/instance.conf.template                   $(CONFDIR)
	install -m 644 $(SOURCEDIR)/conf/$(NAME).conf                             $(CONFDIR)
	
	install -m 644 $(SOURCEDIR)/COPYING                                       $(LICENSEDIR)

uninstall:
	rm -f  $(BINDIR)/$(NAME)
	rm -f  $(BINDIR)/$(NAME)-beta
	
	rm -f  $(SERVICEDIR)/$(NAME)@.service
	rm -f  $(SERVICEDIR)/$(NAME)-beta@.service
	rm -f  $(SERVICEDIR)/$(NAME)-beta-update.service
	rm -f  $(SERVICEDIR)/$(NAME)-beta-update.timer
	rm -f  $(SERVICEDIR)/$(NAME)-update.service
	rm -f  $(SERVICEDIR)/$(NAME)-update.timer
	
	rm -f  $(FIREWALLDDIR)/$(NAME).xml
	rm -f  $(LOGROTATEDIR)/$(NAME)
	rm -f  $(RSYSLOGDIR)/$(NAME).conf
	
	rm -f  $(SBINDIR)/$(NAME)-force-attr
	rm -f  $(SERVICEDIR)/$(NAME)-force-attr.service
	
	rm -rf $(LICENSEDIR)
	rm -rf $(KF2MAINDIR)
	rm -rf $(KF2BETADIR)
	rm -rf $(CACHEDIR)

test:
	$(BASH) -n $(BINDIR)/$(NAME)
	$(BASH) -n $(BINDIR)/$(NAME)-beta
	$(BASH) -n $(SBINDIR)/$(NAME)-force-attr

