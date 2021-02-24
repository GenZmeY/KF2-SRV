# kf2-srv is a command line tool for managing a set of Killing Floor 2 servers.
# Copyright (C) 2019-2021 GenZmeY
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
DESTDIR         =
PREFIX          = /usr/local

MAINLOGDIR      = $(DESTDIR)/var/log/$(NAME)
BETALOGDIR      = $(DESTDIR)/var/log/$(NAME)-beta
CONFDIR         = $(DESTDIR)/etc/$(NAME)
BASHCOMPDIR     = $(DESTDIR)/etc/bash_completion.d
INSTMAINDIR     = $(CONFDIR)/instances
INSTBETADIR     = $(CONFDIR)/instances-beta
MAPCYCLEDIR     = $(CONFDIR)/mapcycles
CACHEDIR        = $(DESTDIR)/var/cache/$(NAME)
LOGROTATEDIR    = $(DESTDIR)/etc/logrotate.d
RSYSLOGDIR      = $(DESTDIR)/etc/rsyslog.d
UNITDIR         = $(if $(DESTDIR),$(DESTDIR)/usr/lib/systemd/system,/etc/systemd/system)
FIREWALLDDIR    = $(if $(DESTDIR),$(DESTDIR)/usr/lib/firewalld/services,/etc/firewalld/services)
BINDIR          = $(DESTDIR)$(PREFIX)/bin
SBINDIR         = $(DESTDIR)$(PREFIX)/sbin
GAMEDIR         = $(DESTDIR)$(PREFIX)/games
DATADIR         = $(DESTDIR)$(PREFIX)/share
SCRIPTDIR       = $(DATADIR)/$(NAME)
SCRIPTGRPDIR    = $(SCRIPTDIR)/cmdgrp
SCRIPTLIBDIR    = $(SCRIPTDIR)/lib
SCRIPTPATCHDIR  = $(SCRIPTDIR)/patch
LICENSEDIR      = $(DATADIR)/licenses/$(NAME)
KF2MAINDIR      = $(GAMEDIR)/$(NAME)
KF2BETADIR      = $(GAMEDIR)/$(NAME)-beta

BASHCHECK      := bash -n
SYSTEMDCHECK   := systemd-analyze verify
XMLCHECK       := xmllint --noout

.PHONY: build fake-systemd-build install uninstall filesystem test clean all

all: install

build:
	mkdir $(RELEASEDIR)
	
	cp -r $(SOURCEDIR)/main       $(RELEASEDIR)
	cp -r $(SOURCEDIR)/config     $(RELEASEDIR)
	
	find $(RELEASEDIR) -type f -exec sed -i 's|:DEFINE_PREFIX:|$(PREFIX)|g;' {} \;

fake-systemd-build:
	find $(SOURCEDIR)/main       -type f -name '*.service' -exec cp -f {} $(RELEASEDIR)/{} \;
	find $(RELEASEDIR)           -type f -exec sed -i  's|:DEFINE_PREFIX:|$(DESTDIR)$(PREFIX)|g;' {} \;
	find $(RELEASEDIR)           -type f -exec sed -i -r 's|ExecStart=.+KFGameSteamServer.bin.x86_64.*|ExecStart=/bin/bash|g;' {} \;

filesystem:
	test -d '$(CONFDIR)'        || install -m 775 -d '$(CONFDIR)'
	test -d '$(INSTMAINDIR)'    || install -m 775 -d '$(INSTMAINDIR)'
	test -d '$(INSTBETADIR)'    || install -m 775 -d '$(INSTBETADIR)'
	test -d '$(MAPCYCLEDIR)'    || install -m 775 -d '$(MAPCYCLEDIR)'
	test -d '$(CACHEDIR)'       || install -m 775 -d '$(CACHEDIR)'
	test -d '$(BINDIR)'         || install -m 755 -d '$(BINDIR)'
	test -d '$(SBINDIR)'        || install -m 755 -d '$(SBINDIR)'
	test -d '$(KF2MAINDIR)'     || install -m 775 -d '$(KF2MAINDIR)'
	test -d '$(KF2BETADIR)'     || install -m 775 -d '$(KF2BETADIR)'
	test -d '$(LICENSEDIR)'     || install -m 755 -d '$(LICENSEDIR)'
	test -d '$(MAINLOGDIR)'     || install -m 770 -d '$(MAINLOGDIR)'
	test -d '$(BETALOGDIR)'     || install -m 770 -d '$(BETALOGDIR)'
	test -d '$(UNITDIR)'        || install -m 755 -d '$(UNITDIR)'
	test -d '$(FIREWALLDDIR)'   || install -m 755 -d '$(FIREWALLDDIR)'
	test -d '$(LOGROTATEDIR)'   || install -m 755 -d '$(LOGROTATEDIR)'
	test -d '$(RSYSLOGDIR)'     || install -m 755 -d '$(RSYSLOGDIR)'
	test -d '$(SCRIPTGRPDIR)'   || install -m 755 -d '$(SCRIPTGRPDIR)'
	test -d '$(SCRIPTLIBDIR)'   || install -m 755 -d '$(SCRIPTLIBDIR)'
	test -d '$(SCRIPTPATCHDIR)' || install -m 755 -d '$(SCRIPTPATCHDIR)'
	test -d '$(BASHCOMPDIR)'    || install -m 755 -d '$(BASHCOMPDIR)'

install: filesystem build
	install -m 755 $(RELEASEDIR)/main/$(NAME)                                  $(BINDIR)
	install -m 755 $(RELEASEDIR)/main/$(NAME)-beta                             $(BINDIR)
	
	# ugly, but works
	find $(RELEASEDIR)/main/cmdgrp                    \
		-mindepth 1                                   \
		-maxdepth 1                                   \
		-type d                                       \
		-printf "%f\n" |                              \
	while read CmdGrp;                                \
	do                                                \
		pushd   $(RELEASEDIR)/main/cmdgrp/$$CmdGrp;   \
		install -m 755 -d $(SCRIPTGRPDIR)/$$CmdGrp;   \
		install -m 644  * $(SCRIPTGRPDIR)/$$CmdGrp;   \
		popd;                                         \
	done
	
	install -m 644 $(RELEASEDIR)/main/lib/*                                    $(SCRIPTLIBDIR)
	
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)@.service                 $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-orig@.service            $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-beta@.service            $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-beta-orig@.service       $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-beta-update.service      $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-beta-update.timer        $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-update.service           $(UNITDIR)
	install -m 644 $(RELEASEDIR)/main/systemd/$(NAME)-update.timer             $(UNITDIR)
	
	install -m 644 $(RELEASEDIR)/main/firewalld/$(NAME).xml                    $(FIREWALLDDIR)
	install -m 644 $(RELEASEDIR)/main/logrotate/$(NAME)                        $(LOGROTATEDIR)
	install -m 644 $(RELEASEDIR)/main/rsyslog/$(NAME).conf                     $(RSYSLOGDIR)
	
	install -m 640 $(RELEASEDIR)/config/bot.conf                               $(CONFDIR)
	install -m 644 $(RELEASEDIR)/config/instance.conf.template                 $(CONFDIR)
	install -m 644 $(RELEASEDIR)/config/$(NAME).conf                           $(CONFDIR)
	
	install -m 644 $(SOURCEDIR)/COPYING                                        $(LICENSEDIR)
	
	install -m 644 $(RELEASEDIR)/main/bash_completion/$(NAME)                  $(BASHCOMPDIR)

uninstall:
	rm -f  $(BINDIR)/$(NAME)
	rm -f  $(BINDIR)/$(NAME)-beta
	
	rm -f  $(UNITDIR)/$(NAME)@.service
	rm -f  $(UNITDIR)/$(NAME)-orig@.service
	rm -f  $(UNITDIR)/$(NAME)-beta@.service
	rm -f  $(UNITDIR)/$(NAME)-beta-orig@.service
	rm -f  $(UNITDIR)/$(NAME)-beta-update.service
	rm -f  $(UNITDIR)/$(NAME)-beta-update.timer
	rm -f  $(UNITDIR)/$(NAME)-update.service
	rm -f  $(UNITDIR)/$(NAME)-update.timer
	
	rm -f  $(FIREWALLDDIR)/$(NAME).xml
	rm -f  $(LOGROTATEDIR)/$(NAME)
	rm -f  $(RSYSLOGDIR)/$(NAME).conf
	
	rm -rf $(LICENSEDIR)
	rm -rf $(KF2MAINDIR)
	rm -rf $(KF2BETADIR)
	rm -rf $(CACHEDIR)

test: fake-systemd-build
	$(XMLCHECK)       $(RELEASEDIR)/main/firewalld/$(NAME).xml
	
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)@.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-orig@.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-beta@.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-beta-orig@.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-beta-update.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-beta-update.timer
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-update.service
	$(SYSTEMDCHECK)   $(RELEASEDIR)/main/systemd/$(NAME)-update.timer
	
	$(BASHCHECK)      $(RELEASEDIR)/main/$(NAME)
	$(BASHCHECK)      $(RELEASEDIR)/main/$(NAME)-beta
	
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/ban/list
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/ban/add
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/ban/delete
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/ban/sync
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/game/update
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/game/validate
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/game/fix-permissions
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/game/run
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/list
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/add
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/delete
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/enable
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/disable
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/start
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/stop
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/restart
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/instance/chat
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/maprotate/save
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/maprotate/load
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/password/game
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/password/admin
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/workshop/list
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/workshop/add
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/workshop/delete
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/workshop/sync
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/log/cat
	$(BASHCHECK)      $(RELEASEDIR)/main/cmdgrp/log/tail
	
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/ban.lib
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/game.lib
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/instance.lib
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/maprotate.lib
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/password.lib
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/playerids.lib
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/webadmin.lib
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/workshop.lib
	$(BASHCHECK)      $(RELEASEDIR)/main/lib/log.lib
	
	$(BASHCHECK)      $(RELEASEDIR)/main/bash_completion/$(NAME)

clean:
	rm -rf $(RELEASEDIR)

