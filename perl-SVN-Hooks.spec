#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	SVN
%define		pnam	Hooks
%include	/usr/lib/rpm/macros.perl
Summary:	SVN::Hooks - A framework for implementing Subversion hooks
Name:		perl-SVN-Hooks
Version:	0.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GN/GNUSTAVO/modules/SVN-Hooks-%{version}.tar.gz
# Source0-md5:	8a9768120374a41eeb1f5386e69cf209
URL:		http://search.cpan.org/dist/SVN-Hooks/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Send
BuildRequires:	perl-Email-Simple
BuildRequires:	perl-JIRA-Client
BuildRequires:	perl-SOAP-Lite
BuildRequires:	perl-SVN-Look
BuildRequires:	perl-SVN-Notify
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A single, simple script can be used as any kind of Subversion hook.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{_mandir}/man3/SVN::Hooks*.3pm*
%{perl_vendorlib}/SVN/Hooks.pm
%{perl_vendorlib}/SVN/Hooks
