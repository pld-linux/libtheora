Summary:	Theora - video codec intended for use within Ogg multimedia streaming system
Summary(pl):	Theora - kodek obrazu do u¿ywania w systemie strumieni multimedialnych Ogg
Name:		libtheora
Version:	1.0
%define	bver	alpha2
Release:	0.%{bver}.1
License:	BSD-like
Group:		Libraries
Source0:	http://www.theora.org/files/%{name}-%{version}%{bver}.tar.gz
# Source0-md5:	8fdeb6fabc7c67598b1031e0a3cb73dd
Patch0:		%{name}-nostatic.patch
Patch1:		%{name}-ogg.patch
URL:		http://www.theora.org/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libogg-devel >= 2:1.1
BuildRequires:	libtool
Requires:	libogg >= 2:1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theora is Xiph.Org's first publicly released video codec, intended for
use within the Ogg's project's Ogg multimedia streaming system. Theora
is derived directly from On2's VP3 codec; Currently the two are nearly
identical, varying only in framing headers, but Theora will diverge
and improve from the main VP3 development lineage as time progresses.

%description -l pl
Theora to pierwszy publicznie wypuszczony przez Xiph.Org kodek obrazu,
maj±cy byæ u¿ywany w systemie strumieni multimedialnych Ogg. Theora
wywodzi siê bezpo¶rednio z kodeka VP3 On2. Aktualnie oba s± prawie
identyczne, ró¿ni± siê jedynie nag³ówkami ramek, ale Theora bêdzie siê
coraz bardziej rozwijaæ w stosunku do VP3.

%package devel
Summary:	Header files for Theora library
Summary(pl):	Pliki nag³ówkowe biblioteki Theora
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Theora library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Theora.

%package static
Summary:	Static Theora library
Summary(pl):	Statyczna biblioteka Theora
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Theora library.

%description static -l pl
Statyczna biblioteka Theora.

%prep
%setup -q -n %{name}-%{version}%{bver}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/theora

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
