%define		_prenum		pre1
%define		_version	0.9.6
Summary:	High Performance Liquid
Summary(pl):	Wysoko wydajny Liquid
Name:		kde-theme-mosfet-liquid
Version:	%{_version}%{_prenum}
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.mosfet.org/mosfet-liquid%{_version}-%{_prenum}.tar.gz
# Source0-md5:	b307becc99285f4463c65703622ed859
Source1:	%{name}.desktop
URL:		http://www.mosfet.org/liquid.html
BuildRequires:	kdebase-devel >= 3.1.1
BuildRequires:	kdelibs-devel >= 3.1.1
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	rpmbuild(macros) >= 1.176
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
High Performance Liquid is an efficent and streamlined version of a
liquid style UI. It makes use of KDE/Qt's widget styling engine, which
uses custom C++ code to render the widgets. To meet the high
performance objectives, the style is made of tileable components
rather than pixmaps (which would need to be scaled).

%description -l pl
Efektywna wersja popularnego stylu interfejsu u�ytkownika - liquid.
Wykorzystuje silnik styli widget�w KDE/Qt, kt�ry u�ywa w�asnego kodu
C++ do renderowania widget�w. Aby sprosta� wymaganiu du�ej wydajno�ci,
styl jest tworzony z powtarzalnych komponent�w zamiast pixmap (kt�re
musia�yby by� skalowane).

%prep
%setup -q -n mosfet-liquid%{_version}%{_prenum}

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/LookNFeel

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/LookNFeel/liquid.desktop

# splash screens conflict
rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/ksplash

%post
/sbin/ldconfig
%banner %{name} -e <<EOF
You may have to run kinstalltheme for this theme to become available
in currently opened sessions.
EOF
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la
%{_applnkdir}/Settings/KDE/LookNFeel/liquid.desktop
%{_datadir}/apps/*/*.*
%{_datadir}/apps/*/*/*.*
