Summary:	ICQ Text Based Client
Summary(pl):	Tekstowy klient ICQ
Summary(ru):	micq - текстовый клиент icq
Name:		micq
Version:	0.4.10.4
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.micq.org/source/%{name}-%{version}.tgz
# Source0-md5:	abbcf17d1feaf61a8e453d180d559e3c
Patch0:		%{name}-nolibgnutls.patch
URL:		http://www.micq.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Micq is an ICQ client for text mode unix that is not in any way supported
by Mirabilis.  This was done for two reasons :  author wanted to see if he
could and Mirabilis has been slow ( at best ) in releasing a unix port.

%description -l pl
Micq jest tekstowym klientem ICQ, ktСry nie jest w ©aden sposСb supportowany
przez Mirabilis. ZostaЁ stworzony z dwСch powodСw: autor chciaЁ zobaczyФ
czy potrafi oraz Mirabilis powoli wypuszczaЁo port linuksowy.

%description -l ru
Micq - ICQ клиент, работающий в текстовой консоли, никоим образом не
поддерживаемый компанией Mirabilis.

%prep
%setup -q
%patch0 -p0

%build
rm -f missing
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO ChangeLog doc/icq*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%lang(de) %{_mandir}/de/man?/*
%lang(es) %{_mandir}/es/man?/*
%lang(fr) %{_mandir}/fr/man?/*
%lang(ru) %{_mandir}/ru_RU.KOI8-R/man?/*
%lang(sr) %{_mandir}/sr_YU@cyrillic/man?/*
%lang(uk) %{_mandir}/uk_UA/man?/*
%lang(pt_BR) %{_mandir}/pt_BR/man?/*
%lang(bg) %{_datadir}/micq/bg.i18n
%lang(zh_CN) %{_datadir}/micq/zh_CN.i18n
%{_datadir}/micq/en.i18n
%{_datadir}/micq/en@fun.i18n
%{_datadir}/micq/C.i18n
%lang(de) %{_datadir}/micq/de.i18n
%lang(de) %{_datadir}/micq/de@fun.i18n
%lang(de) %{_datadir}/micq/de_CH.i18n
%lang(ja) %{_datadir}/micq/ja.i18n
%lang(ja) %{_datadir}/micq/ja.UTF-8.i18n
%lang(ro) %{_datadir}/micq/ro.i18n
%lang(sr) %{_datadir}/micq/sr.UTF-8.i18n
%lang(sr) %{_datadir}/micq/sr.i18n
%lang(es) %{_datadir}/micq/es.i18n
%lang(fi) %{_datadir}/micq/fi.i18n
%lang(fr) %{_datadir}/micq/fr.i18n
%lang(hr) %{_datadir}/micq/hr.i18n
%lang(id) %{_datadir}/micq/id.i18n
%lang(it) %{_datadir}/micq/it.i18n
%lang(nl) %{_datadir}/micq/nl.i18n
%lang(pl) %{_datadir}/micq/pl.i18n
%lang(pt) %{_datadir}/micq/pt.i18n
%lang(ru) %{_datadir}/micq/ru.i18n
%lang(sv) %{_datadir}/micq/se.i18n
%lang(uk) %{_datadir}/micq/uk.i18n
%lang(sr) %{_datadir}/micq/yu.i18n
