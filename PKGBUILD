# Maintainer: NoahC500
pkgname=habbo-launcher-launcher
pkgver=1.0.0
pkgrel=1
pkgdesc="Launcher for Habbo AirPlus, Habbo for Windows, and the website."
arch=('any')
url="https://github.com/NoahC500/habbo-launcher-launcher"
license=('GPL')
source=(
	"Script.py"
	"habbo-launcher-launcher.desktop"
	"icon.png"
)
sha256sums=(
	"5caf4d6ccef5b04bac1f03db41c746e5e5febd752fdee202690e1531edb5ab49"
	"485f2756bc8b433145dcab986ef39e21ab14477b1113ee66e1c54a34f7815189"
	"514f589871d59a91365c80938eb92b16d8898b3d9c1a31ef8398ab9a4d0aca7e"
)

package() {
	mkdir -p "$pkgdir/usr/bin/habbo-launcher-launcher/"
	install -m 0755 "$srcdir/Script.py" "$pkgdir/usr/bin/habbo-launcher-launcher/"
	install -m 0744 "$srcdir/icon.png" "$pkgdir/usr/bin/habbo-launcher-launcher/"
	mkdir -p "$pkgdir/usr/share/applications/"
	install -m 0744 "$srcdir/habbo-launcher-launcher.desktop" "$pkgdir/usr/share/applications/"
}
