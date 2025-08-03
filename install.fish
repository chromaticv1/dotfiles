timedatectl set-local-rtc 1
sudo pacman -Syu
sudo pacman -S stow
if test (pwd) = '/home/chrom/dotfiles'
    echo its stowable
    stow .
else "stow urself bro"
end

sudo pacman -S --needed - < install_list

cd ~

sudo pacman -S --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si

paru cloudflare-warp-bin
systemctl enable warp-svc
systemctl start warp-svc

flatpak install flathub app.zen_browser.zen
flatpak install flathub dev.vencord.Vesktop
