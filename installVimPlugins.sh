#!/bin/bash
#
# Description: Quick WSL2 Ubuntu setup script to update required developer packages and setup the dev environment
#
# Usage: ./installVimPlugins.sh
#

# SECTION BEGIN ----- OPTIONAL commands for personal dev environment setup
# Install Vim-Plug
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# Install plugins using Vim-Plug
vim -E -s -c "PlugInstall" -c "qa"
# SECTION END ----- OPTIONAL commands for personal dev environment setup
