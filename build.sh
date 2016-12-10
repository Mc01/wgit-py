DIST="$PWD/dist/wgit"
pex -r requirements.txt . -e lib.app -o $DIST
chmod +x $DIST
ln -s $DIST /usr/local/bin/wgit
