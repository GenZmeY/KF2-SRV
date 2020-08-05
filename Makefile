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

NAME          := kf2-srv

RPMBUILDDIR   := $$HOME/rpmbuild
ACTIVEDIR     := $(shell readlink -e $$HOME/rpmbuild)
WORKDIR       := $(shell readlink -e .)

BUILDDIR      := $(WORKDIR)/BUILD
BUILDROOTDIR  := $(WORKDIR)/BUILDROOT
RPMSDIR       := $(WORKDIR)/RPMS
SOURCESDIR    := $(WORKDIR)/SOURCES
SPECSDIR      := $(WORKDIR)/SPECS
SRPMSDIR      := $(WORKDIR)/SRPMS

SPEC          := $(SPECSDIR)/$(NAME).spec
VERSION       := $(shell grep -Fi 'Version:' $(SPEC) | awk '{ print $$2 }')
SOURCETARBALL := $(SOURCESDIR)/$(NAME)-$(VERSION).tar.gz

.PHONY: all prep rpm srpm activate active check-activate clean-tmp clean-pkg clean

all: check-activate prep
	rpmbuild -ba $(SPEC)
	$(MAKE) clean-tmp

prep: clean-tmp
	cd $(SOURCESDIR) && tar czf $(SOURCETARBALL) \
		config     \
		force-attr \
		main       \
		COPYING    \
		Makefile

rpm: check-activate prep
	rpmbuild -bb $(SPEC)
	$(MAKE) clean-tmp

srpm: check-activate prep
	rpmbuild -bs $(SPEC)
	$(MAKE) clean-tmp

active: activate

activate:
    ifeq ($(shell test -d $(RPMBUILDDIR); echo $$?), 0)
		mv -f $(RPMBUILDDIR) $(RPMBUILDDIR).old
    else
		rm -f $(RPMBUILDDIR)
    endif
	ln -s $(WORKDIR) $(RPMBUILDDIR)

check-activate:
    ifneq ($(ACTIVEDIR), $(WORKDIR))
		$(error project is not active)
    endif

clean-tmp:
	rm -rf $(BUILDDIR)
	rm -rf $(BUILDROOTDIR)
	rm -rf $(SOURCETARBALL)
	
clean-pkg:
	rm -rf $(RPMSDIR)
	rm -rf $(SRPMSDIR)

clean: clean-tmp clean-pkg

