# LINUX INSTALLATION

## INITIAL

```sh
# Update
sudo apt-get update
sudo apt-get update --fix-missing

# Install essential tools
apt-get install curl wget tree git python python3 -y
```

## SET UP ZSH (Optional)

```sh
# installing zsh
apt-get install zsh -y
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# changing zhs preferences
echo "# arl-zsh
ZSH_THEME="amuse"
" >> ~/.zshrc
```

## ADD ALIASES

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

# Restart the shell for the changes to take effect
. ~/.bash_aliases
```

## UPDATE SYS

```sh
# Update the sys using the just created aliases
apt-updater
```

## OTHERS

```sh
# Install more tools
apt-get install yt-dlp sl -y
```

---

Made with ❤️ by [Bibek Aryal](https://bibeka.com.np/).
