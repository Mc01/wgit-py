#!/bin/bash
DIST="$PWD/dist/wgit"
SYS="/usr/local/bin/wgit"
rm -f ${SYS}
rm -f ${DIST}
pex -r requirements.txt . -e lib.app -o ${DIST} --disable-cache
chmod +x ${DIST}
ln -s ${DIST} ${SYS}
