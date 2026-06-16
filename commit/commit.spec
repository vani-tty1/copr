Name:           commit
Version:        4.5
Release:        1%{?dist}
Summary:        Editor that helps you write better Git and Mercurial commit messages
License:        GPL-3.0-or-later

URL:            https://apps.gnome.org/Commit/
Source0:        https://github.com/sonnyp/Commit/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/sonnyp/troll/archive/refs/heads/main/troll-main.tar.gz

BuildArch:      noarch
%global debug_package %{nil}
BuildRequires:  meson blueprint-compiler gettext desktop-file-utils libappstream-glib gjs
BuildRequires:  pkgconfig(gtk4) pkgconfig(libadwaita-1) pkgconfig(gtksourceview-5) pkgconfig(libspelling-1) pkgconfig(libportal-gtk4)
Requires:       dconf gjs glib2 gtk4 gtksourceview5 hicolor-icon-theme libadwaita libportal libspelling
Recommends:     git
Recommends:     mercurial


%description
Commit is an editor that helps you write better Git and Mercurial commit
messages. It opens automatically when you run git commit or hg commit from
the terminal.


%prep
%autosetup -n Commit-%{version} -N
tar -xf %{SOURCE1}
rm -rf troll
mv troll-main troll


%build
%meson --buildtype=release
%meson_build


%install
%meson_install
ln -s re.sonny.Commit %{buildroot}%{_bindir}/commit
%find_lang re.sonny.Commit



%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop





%files -f re.sonny.Commit.lang
%license COPYING
%{_bindir}/re.sonny.Commit
%{_bindir}/commit
%{_metainfodir}/re.sonny.Commit.metainfo.xml
%{_datadir}/applications/re.sonny.Commit.desktop
%{_datadir}/glib-2.0/schemas/re.sonny.Commit.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/re.sonny.Commit.svg
%{_datadir}/icons/hicolor/symbolic/apps/re.sonny.Commit-symbolic.svg
%{_datadir}/re.sonny.Commit/re.sonny.Commit.src.gresource



%changelog
%autochangelog
