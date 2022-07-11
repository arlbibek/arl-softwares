# LINUX TERMINAL CONFIGURATIONS

## Initial

```sh
# update
sudo apt-get update
```

## Add Aliases

```sh
echo """# arl-aliases

alias cls=clear
alias pls=sudo
alias restart='. ~/.bashrc && clear'

apt-updater ()
{
    sudo apt-get update
    sudo apt-get dist-upgrade -Vy
    sudo apt-get autoremove -y
    sudo apt-get autoclean
    sudo apt-get clean
}

mkcd ()
{
  mkdir -p -- \"\$1\" && cd -P -- \"\$1\"
}
""" >> ~/.bash_aliases
```

```sh
# restart for the changes to take effect
. ~/.bash_aliases
```

## Update System

```sh
# update the system using the just created aliases
apt-updater
```

## Install Essential Tools

```sh
# install essential tools
sudo apt-get install curl wget tree git python3 -y

# install yt-dlp
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

# install more tools
sudo apt-get install sl -y
```

## (Optional) Set Up ZSH

```sh
# installing zsh
apt-get install zsh -y
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# changing zhs preferences
echo "# arl-zsh
ZSH_THEME="amuse"
" >> ~/.zshrc
```

---

Made with ❤️ by [Bibek Aryal](https://bibeka.com.np/).
