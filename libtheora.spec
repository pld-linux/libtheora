Summary:	Theora - video codec intended for use within Ogg multimedia streaming system
Summary(pl.UTF-8):	Theora - kodek obrazu do używania w systemie strumieni multimedialnych Ogg
Name:		libtheora
Version:	1.0
%define	bver	beta1
Release:	0.%{bver}.1
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/theora/%{name}-%{version}%{bver}.tar.bz2
# Source0-md5:	e2ff1996c5a9fadd0df1025aa10bc35e
URL:		http://www.theora.org/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libogg-devel >= 2:1.1
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0.1
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex-bibtex
BuildRequires:	transfig
Requires:	libogg >= 2:1.1
Requires:	libvorbis >= 1:1.0.1
Obsoletes:	libtheora-mmx
Provides:	libtheora-mmx
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
Obsoletes:	libtheora-mmx-devel
Provides:	libtheora-mmx-devel

%description devel
Header files for Theora library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Theora.

%package static
Summary:	Static Theora library
Summary(pl.UTF-8):	Statyczna biblioteka Theora
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libtheora-mmx-static
Provides:	libtheora-mmx-static

%description static
Static Theora library.

%description static -l pl.UTF-8
Statyczna biblioteka Theora.

%prep
%setup -q -n %{name}-%{version}%{bver}

%build
%{__sed} -i 's,CFLAGS="-g -O2 ,CFLAGS=",' configure.ac

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
	docdir=%{_builddir}/%{buildsubdir}/__docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/{color.html,vp3-format.txt} doc/libtheora/html doc/spec/Theora_I_spec.pdf
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/theora
%{_pkgconfigdir}/theora.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
