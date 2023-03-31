%define modname	File-Tail

Summary:	File::Tail module for Perl
Name:		perl-%{modname}
Version:	1.3
Release:	2
License:	GPLv2 or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MG/MGRABNAR/%{modname}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{modname}/
Requires:	perl
BuildRequires:	perl-devel perl-Time-HiRes
BuildArch:	noarch

%description
This Perl modules allows to read from continously updated files.

%prep
%autosetup -p1 -n File-Tail-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*
