Summary:	ICQ Text Based Client
Summary(pl):	Tekstowy klient ICQ
Summary(ru):	micq - текстовый клиент icq
Name:		micq
Version:	0.4.9
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.micq.org/source/%{name}-%{version}.tgz
Url:		http://www.micq.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Micq is an ICQ client for text mode unix that is not in any way supported
by Mirabilis.  This was done for two reasons :  author wanted to see if he
could and Mirabilis has been slow ( at best ) in releasing a unix port.

%description -l pl
Tekstowy klient ICQ.

%description -l ru
Micq - ICQ клиент, работающий в текстовой консоли, никоим образом не
поддерживаемый компанией Mirabilis.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -D doc/micq.1 $RPM_BUILD_ROOT/%{_mandir}/man1/micq.1
install -D doc/micq.7 $RPM_BUILD_ROOT/%{_mandir}/man7/micq.7
install -D doc/micqrc.5 $RPM_BUILD_ROOT/%{_mandir}/man5/micqrc.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%lang(bg) %{_datadir}/micq/bg.i18n
%lang(pt_BR) %{_datadir}/micq/br.i18n
%lang(zh) %{_datadir}/micq/cn.i18n
%lang(de) %{_datadir}/micq/de.i18n
%{_datadir}/micq/en.i18n
%{_datadir}/micq/en_fun.i18n
%lang(es) %{_datadir}/micq/es.i18n
%lang(fi) %{_datadir}/micq/fi.i18n
%lang(fr) %{_datadir}/micq/fr.i18n
%lang(hr) %{_datadir}/micq/hr.i18n
%lang(id) %{_datadir}/micq/id.i18n
%lang(it) %{_datadir}/micq/it.i18n
%lang(nl) %{_datadir}/micq/nl.i18n
%lang(pl) %{_datadir}/micq/pl.i18n
%lang(ru) %{_datadir}/micq/ru.i18n
%lang(sv) %{_datadir}/micq/se.i18n
%lang(uk) %{_datadir}/micq/uk.i18n
%lang(sr,sh) %{_datadir}/micq/yu.i18n
