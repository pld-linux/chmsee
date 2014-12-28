Summary:	HTML Help viewer for Unix/Linux
Summary(pl.UTF-8):	Przeglądarka plików HTML Help dla systemów Unix/Linux
Name:		chmsee
Version:	1.3.0
Release:	3
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://chmsee.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	5ba68ccee32ba782486badc025842ccf
URL:		http://code.google.com/p/chmsee/
BuildRequires:	chmlib-devel >= 0.39
BuildRequires:	cmake >= 2.8
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	gtk+2-devel >= 2:2.20
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	nspr-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xulrunner-devel >= 1.9
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	chmlib >= 0.39
Requires:	glib2 >= 1:2.22
Requires:	gtk+2 >= 2:2.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ChmSee is an HTML Help viewer for Unix/Linux. It is based on CHMLIB
and use GTK+ as its frontend toolkit. Because of using gecko HTML
rendering engine, ChmSee can support rich features of modern HTML
page, specially CSS.

%description -l pl.UTF-8
ChmSee jest przeglądarką plików HTML Help dla systemów Unix/Linux.
Oparta jest na bibliotece CHMLIB oraz używa biblioteki GTK+ jako
frontend. Dzięki użyciu silnika renderującego HTML gecko, ChmSee
wspiera bogatą funkcjonalność nowoczesnych stron HTML, w szczególności
CSS.

%prep
%setup -q

%build
%cmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/mime-info

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.js
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.ui
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/mimetypes/chm.png
%{_iconsdir}/hicolor/scalable/mimetypes/chm.svg
%{_pixmapsdir}/%{name}-icon.png
