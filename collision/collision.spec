Name:           collision
Version:        3.14.1
Release:        1%{?dist}
Summary:        GUI tool to generate, compare and verify file hashes
License:        BSD-2-Clause
%global archivename Collision-%{version}


URL:            https://apps.gnome.org/Collision/
Source0:        https://github.com/GeopJr/Collision/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  crystal gobject-introspection-devel make git libyaml-devel
BuildRequires:  pkgconfig(gtk4) pkgconfig(libadwaita-1) pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(openssl) pkgconfig(zlib) pkgconfig(libpcre2-8)
Requires:       dconf gc glib2 glibc gtk4 hicolor-icon-theme libadwaita openssl pcre2 zlib
Recommends:     nautilus-python


%description
Collision is a GNOME Circle application for generating, comparing and
verifying file hashes. Supports MD5, SHA-1, SHA-256, SHA-512, Blake3,
CRC32 and Adler32 algorithms.



%prep
%autosetup -n %{archivename}
shards install
sed -i -e '/gtk-update-icon-cache/d' -e '/glib-compile-schemas/d' Makefile



%build
make -j1
make metainfo



%check
make check
make validate-appstream



%install
make PREFIX="%{buildroot}/usr" install
install -Dm644 -t %{buildroot}%{_datadir}/nautilus-python/extensions/ \
    nautilus-extension/collision-extension.py
install -Dm644 -t %{buildroot}%{_metainfodir}/ \
    data/dev.geopjr.Collision.metainfo.xml
    
    
    
%files
%license LICENSE
%{_bindir}/collision
%{_datadir}/applications/dev.geopjr.Collision.desktop
%{_datadir}/glib-2.0/schemas/dev.geopjr.Collision.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/dev.geopjr.Collision.svg
%{_datadir}/icons/hicolor/symbolic/apps/dev.geopjr.Collision-symbolic.svg
%{_datadir}/metainfo/dev.geopjr.Collision.metainfo.xml
%{_datadir}/nautilus-python/extensions/collision-extension.py



%changelog
%autochangelog
