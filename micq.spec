Summary:	ICQ Text Based Client
Summary(pl):	Tekstowy klient ICQ
Name:		micq
%define patchlevel p1
Version:	0.4.6
Release:	2
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://micq.ukeer.de/source/%{name}-%{version}.%{patchlevel}.tgz
Patch0:		%{name}-make.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-home_data.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text Based ICQ Client.

%description -l pl
Tekstowy klient ICQ.

%prep
%setup -q -n %{name}-%{version}-%{patchlevel}
%patch0 -p1
#%patch2 -p1
#%patch3 -p1

%build
cd src
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/micq $RPM_BUILD_ROOT%{_bindir}
install micq.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
