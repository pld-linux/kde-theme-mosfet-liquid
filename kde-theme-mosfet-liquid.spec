Summary:	High Performance Liquid
Summary(pl):	Wysoko wydajny Liquid
Name:		kde-theme-mosfet-liquid
Version:	0.9.5
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.mosfet.org/mosfet-liquid%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.mosfet.org/liquid.html
BuildRequires:	qt-devel >= 3.0.3
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
High Performance Liquid is an efficent and streamlined version of a
liquid style UI. It makes use of KDE/Qt's widget styling engine, which
uses custom C++ code to render the widgets. To meet the high
performance objectives, the style is made of tileable components
rather than pixmaps (which would need to be scaled).

%description -l pl
Efektywna wersja popularnego stylu interfejsu u¿ytkownika - liquid.

%prep
%setup  -q -n mosfet-liquid%{version}

%build
%configure \
	--enable-objprelink
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/LookNFeel

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/LookNFeel/liquid.desktop

# splash screens conflict
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/ksplash

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%dir %{_libdir}/kde3
%attr(755,root,root) %{_libdir}/kde3/*.so
%attr(755,root,root) %{_libdir}/kde3/*.la
%dir %{_libdir}/kde3/plugins
%dir %{_libdir}/kde3/plugins/styles
%{_libdir}/kde3/plugins/styles/*.so
%{_applnkdir}/Settings/KDE/LookNFeel/liquid.desktop
%{_datadir}/apps/*/*.*
%{_datadir}/apps/*/*/*.*
