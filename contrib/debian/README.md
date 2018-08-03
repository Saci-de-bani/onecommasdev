
Debian
====================
This directory contains files used to package onecommasd/onecommas-qt
for Debian-based Linux systems. If you compile onecommasd/onecommas-qt yourself, there are some useful files here.

## onecommas: URI support ##


onecommas-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install onecommas-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your onecommasqt binary to `/usr/bin`
and the `../../share/pixmaps/onecommas128.png` to `/usr/share/pixmaps`

onecommas-qt.protocol (KDE)

