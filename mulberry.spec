%define		svnrev	354
%define		rel		1
Summary:	Mulberry email and calendar client
Name:		mulberry
Version:	4.0.8
Release:	0.%{svnrev}.%{rel}
License:	Apache v2.0
Group:		Applications
# svn co http://svn.mulberrymail.com/mulberry/Mulberry/trunk mulberry
# tar -cjf mulberry-$(svnversion mulberry).tar.bz2 --exclude-vcs mulberry
# ../dropin mulberry-$(svnversion mulberry).tar.bz2
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	a0dcb50b1f35c54a209ae7456097b24d
Patch0:		jxinit-patch.diff
Patch1:		Linux-Make.header-patch.diff
URL:		http://www.mulberrymail.com/
BuildRequires:	aspell-devel
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mulberry email and calendar client.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p0

%build
%{__make} -f Makefile-Linux jxinit

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
