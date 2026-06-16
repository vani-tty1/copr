Name:           impression
Version:        3.7.0
Release:        1%{?dist}
Summary:        Application to create bootable drives from disk images
License:        GPL-3.0-only
URL:            https://apps.gnome.org/Impression/
Source0:        https://gitlab.com/adhami3310/Impression/-/archive/v%{version}/Impression-v%{version}.tar.gz
BuildRequires:  meson gcc blueprint-compiler cargo rust gettext desktop-file-utils libappstream-glib
BuildRequires:  pkgconfig(gtk4) pkgconfig(libadwaita-1) pkgconfig(glib-2.0)
BuildRequires:  openssl-devel libudisks2-devel
Requires:       dconf glib2 glibc gtk4 hicolor-icon-theme libadwaita openssl-libs udisks2


%description
Impression is a useful tool for both avid distro-hoppers and casual computer
users. Write disk images onto your drives with ease. Select an image, insert
your drive, and you're good to go!


%prep
%autosetup -n Impression-v%{version}
CARGO_HOME="%{_builddir}/cargo-home" \
    cargo fetch --locked --target "$(rustc --print host-tuple)"


%build
%meson --buildtype=release
CARGO_HOME="%{_builddir}/cargo-home" \
CARGO_PROFILE_RELEASE_LTO=true \
CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1 \
CARGO_PROFILE_RELEASE_DEBUG=2 \
CARGO_PROFILE_RELEASE_STRIP=false \
    %meson_build



%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/impression
%{_metainfodir}/io.gitlab.adhami3310.Impression.metainfo.xml
%{_datadir}/dbus-1/services/io.gitlab.adhami3310.Impression.service
%{_datadir}/impression/resources.gresource 
%{_datadir}/applications/io.gitlab.adhami3310.Impression.desktop
%{_datadir}/glib-2.0/schemas/io.gitlab.adhami3310.Impression.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.gitlab.adhami3310.Impression.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.gitlab.adhami3310.Impression-symbolic.svg


%changelog
%autochangelog
