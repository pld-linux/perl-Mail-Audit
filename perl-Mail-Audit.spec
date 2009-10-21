#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Audit
Summary:	Mail::Audit - alternative for procmail
Summary(pl.UTF-8):	Mail::Audit - alternatywa dla procmaila
Name:		perl-Mail-Audit
Version:	2.224
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/R/RJ/RJBS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3118c0514ff6d7f3aff8a32cfd36791f
URL:		http://search.cpan.org/dist/Mail-Audit/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::HomeDir) >= 0.61
BuildRequires:	perl(File::Tempdir)
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-MailTools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::Audit was inspired by Tom Christiansen's audit_mail and deliverlib
programs.  It allows a piece of email to be logged, examined, accepted
into a mailbox, filtered, resent elsewhere, rejected, replied to, and
so on.  It's designed to allow you to easily create filter programs to
stick in a .forward file or similar.

%description -l pl.UTF-8
Inspiracją dla Mail::Audit był audit_mail i programy deliverlib Toma
Christiansena.  Pozwala on na logowanie przychodzącej poczty, badanie
jej, akceptowanie do skrzynki pocztowej, filtrowanie, przekierowywanie,
odrzucanie, odpowiadanie i tak dalej.  Został zaprojektowany tak, aby
pozwolić Ci na łatwe tworzenie filtrów, uruchamianych z pliku ~/.forward
lub podobnego miejsca.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README FAQ
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/Audit
%{_mandir}/man3/*
