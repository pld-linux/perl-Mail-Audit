%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Audit
Summary:	%{pdir}::%{pnam} -- alternative for procmail
Summary(pl):	%{pdir}::%{pnam} -- alternatywa dla procmaila
Name:		perl-%{pdir}-%{pnam}
Version:	2.1
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b52b1142fa9ed7d847c531186f913ea6
BuildRequires:	perl-devel >= 5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Razor::.*)'

%description
Mail::Audit was inspired by Tom Christiansen's audit_mail and deliverlib
programs.  It allows a piece of email to be logged, examined, accepted
into a mailbox, filtered, resent elsewhere, rejected, replied to, and
so on.  It's designed to allow you to easily create filter programs to
stick in a .forward file or similar.

%description -l pl
Inspiracj± dla Mail::Audit by³ audit_mail i programy deliverlib Toma
Christiansena.  Pozwala on na logowanie przychodz±cej poczty, badanie
jej, akceptowanie do skrzynki pocztowej, filtrowanie, przekierowywanie,
odrzucanie, odpowiadanie i tak dalej.  Zosta³ zaprojektowany tak, aby
pozwoliæ Ci na ³atwe tworzenie filtrów, uruchamianych z pliku ~/.forward
lub podobnego miejsca.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README FAQ popread proc2ma
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
