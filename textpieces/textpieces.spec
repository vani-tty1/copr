Name:           textpieces
Version:        4.3.1
Release:        1%{?dist}
Summary:        Powerful scratchpad with ability to perform a lot of text transformations

License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/TextPieces/
Source0:        https://gitlab.com/liferooter/textpieces/-/archive/%{version}/textpieces-%{version}.tar.gz


BuildRequires:  appstream blueprint-compiler cargo-rpm-macros
BuildRequires:  desktop-file-utils git meson rust-packaging pkgconfig(gtk4) pkgconfig(gtksourceview-5) pkgconfig(libadwaita-1)

Requires:	dconf glib2 gtk4 gtksourceview5 hicolor-icon-theme libadwaita pango

%description
Textpieces is a powerful scratchpad with the ability to perform a lot of
text transformations: encoding/decoding, formatting, hashing, and more,
directly from a GNOME-native interface.

%prep
%autosetup -p1 
%cargo_prep

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/textpieces
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.xml
%{_datadir}/locale/*/LC_MESSAGES/textpieces.mo

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%changelog
%autochangelog
