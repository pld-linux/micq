# $Revision: 1.1 $
Summary:	micq - ICQ Text Based Client
Name:		micq
Version:	0.4.2
Release:	1
Copyright:	GPL
Group:		Applications/Communication
Group(pl):	Aplikacje/Komunikacja
Source:		%{name}-%{version}.tgz
Patch0:		%{name}-make.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text Based ICQ Client

%prep
%setup -q
%patch0 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install micq	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf {CHANGELOG,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGELOG}.gz
%attr(755,root,root) %{_bindir}/*
