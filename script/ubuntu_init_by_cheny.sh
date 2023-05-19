#!/bin/bash
# Author: cheny
# Created Time: 2023-05-18 10:00:00
# This script is used to init ubuntu system by myself. It will automatically install some softwares and configure some settings.
# The script run as normal user, so you should not run it with sudo command. Sometimes the first 'sudo' command need input user's password,
# so before you run this first script, you should run 'sudo echo' to input your password. 
# Remember that you don't run this script with sudo command, because it will install some softwares and configure some settings for rootsudo.

# ENV
SSH_PUBLIC_KEY="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCjabJ4UW8Rx50NChKBoHzfxGPNF/caByQ2RPiZUQ69dAzXSxq63+SUhHho2t31LWq8MWy1FjRGuxJXiSju8NTJk5IPU+CLD6IqttZr/CgvHNbGXlZ/MAMuN68tHqKQag90kZDfBqeNlY2NizuYkhrT1Hvxu65hLZbEOrofFLg1KC82BNKwQqjcoLnbpMVi+8CDnEL9MqDA22St4p4K/X/FvOutsiaJ/+p1yQW+ejD6+AUpKSIZAz4YzqBls4sG8sPPlbYC/WPcupACQziqARXhD7WwrlS7jEgMkwvznhAl3InecsECvOx3K3/1Au4vCAAozAb5vbHVXASeJOVAG44KTx3amCbMhyNzvkFMndzlU8XZYojs8ZoARLQLLNmQHpjsw/T55cmQAtVkI/qUVp+gMoLSmL5tRE7xPDOjI9GuEu4CKFokA0I2quVV54aJ3RjM9TII5Xr+0ofGLwzobIw6Hga2oyfzHMoTnkE9logzIjPJRqi4IKf1UsyKf8KNsc8= cheny@=macbook-pro.local"

# check the apt repository is aliyun or not, if not, change it to aliyun
if [ ! -f /etc/apt/sources.list.bak ]; then
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
fi
sudo sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
sudo sed -i 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
sudo apt update
sudo apt install -y git curl wget


# config ssh with SSH_PUBLIC_KEY
mkdir -p ~/.ssh
# if SSH_PUBLIC_KEY is in authorized_keys, do nothing
if [ -f ~/.ssh/authorized_keys ]; then
    if grep -q "$SSH_PUBLIC_KEY" ~/.ssh/authorized_keys; then
        echo "SSH_PUBLIC_KEY is already in ~/.ssh/authorized_keys"
    else
        echo "$SSH_PUBLIC_KEY" >> ~/.ssh/authorized_keys
    fi
fi

chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

# disenble ssh password permission
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
sudo service sshd restart

# config /etc/sudoers no password for sudo command
sudo sed -i 's/%sudo\tALL=(ALL:ALL) ALL/%sudo\tALL=(ALL:ALL) NOPASSWD:ALL/g' /etc/sudoers

# install zsh and oh-my-zsh
sudo apt install -y zsh
chsh -s /bin/zsh
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


# install vim-runtime with https://github.com/amix/vimrc.git
apt install -y vim
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh

# edit ~/.vim_runtime/vimrcs/plugins_config.vim and commit the 50th line, 解决run_time中的Ctrl+f快捷键与vim默认的向下翻页冲突的问题
sed -ie "s/^let g:ctrlp_map.*/\" &/" .vim_runtime/vimrcs/plugins_config.vim

echo "ALL is done."







