Summary:	3ivX codec for XAnim
Summary(pl.UTF-8):   Kodek 3ivX dla XAnima
Name:		xanim-codec-3ivx
Version:	3.5
Release:	1
License:	unknown
# README mentions http://www.3ivx.com/download.html, but no word about license there
Group:		X11/Applications/Graphics
Source0:	http://www.3ivx.com/codec/unix/3ivxxanim2801ci686lxglibc21.tgz
# NoSource0-md5:	891c36af96d57d860e1178b169e346fe
NoSource:	0
URL:		http://www.3ivx.com/
Requires:	xanim >= 1:2920
ExclusiveArch:	i686 pentium3 pentium4 athlon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3ivX codec decompression DLL for XAnim.

%description -l pl.UTF-8
Biblioteka do dekompresji kodeka 3ivX dla XAnima.

%prep
%setup -q -n 3ivx-xanim2801c-i686linux-glibc21

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

install vid_3ivX.xa $RPM_BUILD_ROOT%{_libdir}/xanim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/xanim/vid_3ivX.xa
