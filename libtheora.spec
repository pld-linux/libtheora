Summary:	Theora - video codec intended for use within Ogg multimedia streaming system
Summary(pl.UTF-8):	Theora - kodek obrazu do używania w systemie strumieni multimedialnych Ogg
Name:		libtheora
Version:	1.0
%define	subver	RC2
Release:	1.%{subver}.1
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/theora/%{name}-%{version}%{subver}.tar.bz2
# Source0-md5:	e72ea433eb5be8480d458738927c137d
URL:		http://www.theora.org/
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libogg-devel >= 2:1.1
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0.1
BuildRequires:	pkgconfig
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex-bibtex
BuildRequires:	tetex-latex-ltablex
BuildRequires:	transfig
Requires:	libogg >= 2:1.1
Requires:	libvorbis >= 1:1.0.1
Provides:	libtheora-mmx
Obsoletes:	libtheora-mmx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theora is Xiph.Org's first publicly released video codec, intended for
use within the Ogg's project's Ogg multimedia streaming system. Theora
is derived directly from On2's VP3 codec; Currently the two are nearly
identical, varying only in framing headers, but Theora will diverge
and improve from the main VP3 development lineage as time progresses.

%description -l pl.UTF-8
Theora to pierwszy publicznie wypuszczony przez Xiph.Org kodek obrazu,
mający być używany w systemie strumieni multimedialnych Ogg. Theora
wywodzi się bezpośrednio z kodeka VP3 On2. Aktualnie oba są prawie
identyczne, różnią się jedynie nagłówkami ramek, ale Theora będzie się
coraz bardziej rozwijać w stosunku do VP3.

%package devel
Summary:	Header files for Theora library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Theora
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel >= 2:1.1
Provides:	libtheora-mmx-devel
Obsoletes:	libtheora-mmx-devel

%description devel
Header files for Theora library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Theora.

%package static
Summary:	Static Theora library
Summary(pl.UTF-8):	Statyczna biblioteka Theora
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libtheora-mmx-static
Obsoletes:	libtheora-mmx-static

%description static
Static Theora library.

%description static -l pl.UTF-8
Statyczna biblioteka Theora.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}
%{__make} -C doc/spec

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/libtheora-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING LICENSE README
%attr(755,root,root) %{_libdir}/libtheora.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtheora.so.0
%attr(755,root,root) %{_libdir}/libtheoradec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtheoradec.so.1
%attr(755,root,root) %{_libdir}/libtheoraenc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtheoraenc.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/{color.html,draft-ietf-avt-rtp-theora-00.txt,vp3-format.txt} doc/libtheora/html doc/spec/Theora.pdf
%attr(755,root,root) %{_libdir}/libtheora.so
%attr(755,root,root) %{_libdir}/libtheoradec.so
%attr(755,root,root) %{_libdir}/libtheoraenc.so
%{_libdir}/libtheora.la
%{_libdir}/libtheoradec.la
%{_libdir}/libtheoraenc.la
%{_includedir}/theora
%{_pkgconfigdir}/theora.pc
%{_pkgconfigdir}/theoradec.pc
%{_pkgconfigdir}/theoraenc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtheora.a
%{_libdir}/libtheoradec.a
%{_libdir}/libtheoraenc.a
