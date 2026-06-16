Name:           resources
Version:        1.10.2
Release:        1%{?dist}
Summary:        Monitor for system resources and processes
License:        GPL-3.0-or-later


URL:            https://apps.gnome.org/Resources/
Source0:        https://github.com/nokyan/resources/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  meson cargo rust gcc gettext desktop-file-utils libappstream-glib
BuildRequires:  pkgconfig(gtk4) pkgconfig(libadwaita-1) pkgconfig(glib-2.0) pkgconfig(graphene-1.0)
BuildRequires:  pkgconfig(cairo) pkgconfig(polkit-gobject-1)
Requires:       cairo dconf glib2 glibc graphene gtk4 hicolor-icon-theme libadwaita polkit



%description
Resources allows you to check the utilization of your system resources and
control your running processes and apps. It supports monitoring CPU, memory,
GPU, network interfaces, storage devices and batteries.



%prep
%autosetup -n %{name}-%{version}
CARGO_HOME="%{_builddir}/cargo-home" \
    cargo fetch --locked --target "$(rustc --print host-tuple)"



%build
%meson \
    --buildtype=release \
    -Dprofile=default
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
%license LICENSE
%{_bindir}/resources
%{_metainfodir}/net.nokyan.Resources.metainfo.xml
%{_datadir}/applications/net.nokyan.Resources.desktop
%{_datadir}/glib-2.0/schemas/net.nokyan.Resources.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/net.nokyan.Resources.svg
%{_datadir}/icons/hicolor/symbolic/apps/net.nokyan.Resources-symbolic.svg
%{_datadir}/resources/
%{_libexecdir}/resources/resources-adjust
%{_libexecdir}/resources/resources-kill
%{_libexecdir}/resources/resources-processes
%{_datadir}/polkit-1/actions/net.nokyan.Resources.policy


%changelog
%autochangelog
