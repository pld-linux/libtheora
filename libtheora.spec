#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static libraries

Summary:	Theora - video codec intended for use within Ogg multimedia streaming system
Summary(pl.UTF-8):	Theora - kodek obrazu do używania w systemie strumieni multimedialnych Ogg
Name:		libtheora
Version:	1.2.0
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.xz
# Source0-md5:	ec64ed07bffb5f45dca0ae7faa68f814
URL:		https://www.theora.org/
BuildRequires:	SDL-devel
BuildRequires:	libogg-devel >= 2:1.3.4
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libvorbis-devel >= 1:1.0.1
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex-bibtex
BuildRequires:	tetex-latex-ltablex
BuildRequires:	transfig
%endif
Requires:	libogg >= 2:1.3.4
Requires:	libvorbis >= 1:1.0.1
Provides:	libtheora-mmx
Obsoletes:	libtheora-mmx < 1.0-1
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
Requires:	libogg-devel >= 2:1.3.4
Provides:	libtheora-mmx-devel
Obsoletes:	libtheora-mmx-devel < 1.0-1

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
Obsoletes:	libtheora-mmx-static < 1.0-1

%description static
Static Theora library.

%description static -l pl.UTF-8
Statyczna biblioteka Theora.

%package apidocs
Summary:	API documentation for Theora library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Theora
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Theora library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Theora.

%prep
%setup -q

%build
%configure \
	%{__enable_disable static_libs static} \
	--disable-silent-rules

%{__make}
%if %{with apidocs}
%{__make} -C doc/spec
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/libtheora-docs

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtheora*.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libtheora-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING LICENSE README.md
%attr(755,root,root) %{_libdir}/libtheora.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtheora.so.1
%attr(755,root,root) %{_libdir}/libtheoradec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtheoradec.so.2
%attr(755,root,root) %{_libdir}/libtheoraenc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtheoraenc.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtheora.so
%attr(755,root,root) %{_libdir}/libtheoradec.so
%attr(755,root,root) %{_libdir}/libtheoraenc.so
%{_includedir}/theora
%{_pkgconfigdir}/theora.pc
%{_pkgconfigdir}/theoradec.pc
%{_pkgconfigdir}/theoraenc.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtheora.a
%{_libdir}/libtheoradec.a
%{_libdir}/libtheoraenc.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/{color.html,draft-ietf-avt-rtp-theora-00.txt,vp3-format.txt} doc/libtheora/html doc/spec/Theora.pdf
