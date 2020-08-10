#!/bin/sh -l

make active && make builddep && make -j$(nproc) "$1"

RC=$?

echo "::set-output name=rpm_name::$(find /github/workspace/RPMS   -type f -name '*.rpm' -printf '%f\n')"
echo "::set-output name=srpm_name::$(find /github/workspace/SRPMS -type f -name '*.src.rpm' -printf '%f\n')"

exit $RC
