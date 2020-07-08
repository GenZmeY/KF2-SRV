#!/bin/bash

ScriptFullname=$(readlink -e "$0")
SrpmProjectDir=$(dirname "$ScriptFullname")
RpmBuild="$HOME/rpmbuild"

if [[ -d "$RpmBuild" ]]; then
	rm -rf "$RpmBuild"
else
	rm -f "$RpmBuild"
fi

ln -s "$SrpmProjectDir" "$RpmBuild"
