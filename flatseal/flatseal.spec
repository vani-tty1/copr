Name:           flatseal
Version:        2.4.1
Release:        1%{?dist}
Summary:        A permissions manager for Flatpak

License:        GPL-3.0-or-later
URL:            https://github.com/tchx84/Flatseal
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils
BuildRequires:	pkgconfig(webkitgtk-6.0)
BuildRequires:  libappstream-glib
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(flatpak)
BuildRequires:	pkgconfig(appstream)
BuildRequires:	gettext gjs

Requires:	flatpak gjs libadwaita webkitgtk6.0 appstream

%description
A graphical utility to review and modify permissions of Flatpak applications.

%prep
%autosetup -n Flatseal-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%{_bindir}/com.github.tchx84.Flatseal
%license COPYING
%{_datadir}/applications/*.desktop
%{_datadir}/flatseal/
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/symbolic/apps/*.svg
%{_datadir}/metainfo/*.xml


%changelog
* Tue Jun 16 2026 Giovanni Rafanan <giovannirafanan609@gmail.com> - 2.4.1-1
- initial build

