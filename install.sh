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
echo "Compiling application with PEX to ${DIST}."
pex -r requirements.txt . -e lib.app -o ${DIST} --disable-cache
chmod +x ${DIST}
echo "Linking executable to ${SYS}."
ln -s ${DIST} ${SYS}
echo "Success. Installation complete."