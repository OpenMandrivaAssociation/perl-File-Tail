%define modname	File-Tail

Summary:	File::Tail module for Perl
Name:		perl-%{modname}
Version:	0.99.3
Release:	11
License:	GPLv2 or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MG/MGRABNAR/%{modname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{modname}/
Requires:	perl
BuildRequires:	perl-devel perl-Time-HiRes
BuildArch:	noarch

%description
This Perl modules allows to read from continously updated files.

%prep
%setup -qn File-Tail-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*

