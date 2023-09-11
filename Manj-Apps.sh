#!/bin/bash/root



# Update repository:
sudo pacman -Sqyu

# Install aur package manager
sudo pacman -Sq yay pamac

# Base system applications
sudo pacman -Sq git screenfetch zsh gparted net-tools copyq htop appimagelauncher latte-dock
yay -Sq nerdfetch pantheon-terminal translate-Sqhell http gitflow stacer powerline-fonts-git

# Icon set
wget -qO- https://git.io/papirus-icon-theme-install | DESTDIR="$HOME/.local/share/icons" sh

# Programming language

## python
sudo pacman -Sq python ipython python-pip virtualbox

### base python modules
sudo pip install -U pip
sudo pip install -U django flask sanic gunicorn pyfiglet shecan

## node.js
sudo pacman -Sq nodejs npm

# ClamAV antivirus
sudo pacman -Sq clamav clamtk

# Graphic tools
sudo pacman -Sq krita gimp
yay -Sq lorien-bin rnote



echo "--- Postgres ---"
sudo -u postgres -b 'initdb --locale $LANG -E UTF8 -D "/var/lib/postgres/data/"'
sudo systemctl start postgresql.service
sudo systemctl enable postgresql.service



echo "--- Mongodb ---" 
yay -Sq mongodb-bin mongodb-compass
sudo systemctl start mongodb.service
sudo systemctl enable mongodb.service

echo "--- Redis ---" 
sudo pacman -Sq redis
sudo systemctl start redis
sudo systemctl enable redis

echo "--- Sqlite ---" 
sudo pacman -Sq sqlite



echo "--- Browsers: Firefox | Chrome | Brave ---" 
sudo pacman -Sq firefox
yay -Sq google-chrome
sudo pamac install brave-browser



echo "--- Docker ---" 
sudo pacman -Sq docker docker-compose
sudo systemctl start docker
sudo systemctl enable docker

echo "--- Virtualbox ---" 
sudo pacman -Sq virtualbox linux515-virtualbox-host-modules
sudo vboxreload

echo "--- Remina ---" 
sudo pacman -Sq remmina
yay -Sq wrk

echo "--- Insomnia ---" 
yay -Sq insomnia

echo "--- Kate ---" 
sudo pacman -S kate

echo "--- Clementine ---" 
sudo pacman -S clementine

echo "--- Elisa ---" 
sudo pacman -S elisa

echo "--- Pycharm-community ---" 
sudo pacman -S pycharm-community-edition

echo "--- VLC ---" 
sudo pacman -S vlc

echo "--- Flameshot ---" 
sudo pacman -S flameshot

echo "--- Kazam ---" 
sudo yay -S kazam

echo "--- Sublime4 ---" 
sudo yay -S sublime-text-4

echo "--- Onlyoffice ---" 
sudo yay -S onlyoffice-bin

echo "--- sshpass ---"
sudo pacman -S sshpass

echo "--- alacarte ---"
sudo pacman -S alacarte

echo "--- Visual Studio Code ---"
sudo pacman -S --needed git base-devel
yay -S visual-studio-code-bin

echo "--- Visual Studio Code Insiders ---"
sudo pamac install visual-studio-code-insiders-bin

echo "--- Telegram Desktop ---"
sudo pacman -S telegram-desktop
