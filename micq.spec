# $Revision: 1.15 $
Summary:	ICQ Text Based Client
Summary(pl):	Tekstowy klient ICQ
Name:		micq
Version:	0.4.6
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://micq.chatzone.org/pub/micq/V%{version}/%{name}-%{version}.tgz
Patch0:		%{name}-make.patch
Patch1:		%{name}-about_cmd.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-home_data.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text Based ICQ Client.

%description -l pl
Tekstowy klient ICQ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
#%patch3 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install -s micq $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/*
