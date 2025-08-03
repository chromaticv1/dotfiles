timedatectl set-local-rtc 1
sudo pacman -Syu
sudo pacman -S stow
if test (pwd) = '/home/chrom/dotfiles'
    echo its stowable
    stow .
else "stow urself bro"
end

sudo pacman -S - --needed < install_list
