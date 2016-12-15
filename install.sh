#!/bin/bash
VIRTUAL="virtual"
DIST="$PWD/dist/wgit"
SYS="/usr/local/bin/wgit"
rm -rf ${VIRTUAL}
virtualenv ${VIRTUAL}
source ${VIRTUAL}/bin/activate
pip install -r requirements-install.txt
rm -f ${SYS}
rm -f ${DIST}
pex -r requirements.txt . -e lib.app -o ${DIST} --disable-cache
chmod +x ${DIST}
ln -s ${DIST} ${SYS}
