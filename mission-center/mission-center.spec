Name:           mission-center
Version:        1.1.0
Release:        1%{?dist}
Summary:        Monitor your CPU, Memory, Disk, Network and GPU usage
License:        GPL-3.0-or-later
URL:            https://missioncenter.io
Source0:        https://gitlab.com/mission-center-devs/mission-center/-/archive/v%{version}/mission-center-v%{version}.tar.gz
Source1:        https://gitlab.com/mission-center-devs/gng/-/archive/main/gng-main.tar.gz
ExclusiveArch:  x86_64
BuildRequires:  git meson cmake blueprint-compiler cargo rust gcc gettext desktop-file-utils libappstream-glib
BuildRequires:  pkgconfig(dconf) pkgconfig(gdk-pixbuf-2.0) pkgconfig(glib-2.0) pkgconfig(graphene-1.0)
BuildRequires:  pkgconfig(gtk4) pkgconfig(libadwaita-1) pkgconfig(protobuf) pkgconfig(libsystemd)
BuildRequires:  mesa-libGL-devel
Requires:       dconf dmidecode gdk-pixbuf2 glib2 glibc graphene gtk4 libadwaita mesa-libGL nvtop protobuf systemd-libs


%description
Mission Center is a GTK4/Libadwaita application that lets you monitor
your CPU, Memory, Disk, Network and GPU usage.



%prep
%autosetup -n mission-center-v%{version} -N
tar -xf %{SOURCE1}
mv gng-main subprojects/magpie
CARGO_HOME="%{_builddir}/cargo-home" \
    cargo fetch --target "$(rustc --print host-tuple)"
cd subprojects/magpie
CARGO_HOME="%{_builddir}/subprojects/magpie/cargo-home" \
    cargo fetch --locked --target "$(rustc --print host-tuple)"



%build
export CFLAGS="%{optflags} -ffat-lto-objects"
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
%{_bindir}/mission-center
%{_libexecdir}/mission-center/
%{_metainfodir}/*.xml
%{_datadir}/applications/io.missioncenter.MissionCenter.desktop
%{_datadir}/glib-2.0/schemas/io.missioncenter.MissionCenter.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.missioncenter.MissionCenter.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.missioncenter.MissionCenter-symbolic.svg


%changelog
%autochangelog
