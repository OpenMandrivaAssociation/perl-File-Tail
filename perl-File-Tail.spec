%define modname	File-Tail

Summary:	File::Tail module for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version 1.0
Release:	1
License:	GPLv2 or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MG/MGRABNAR/%{modname}-1.0.tar.gz
Url:		http://search.cpan.org/dist/%{modname}/
Requires:	perl
BuildRequires:	perl-devel perl-Time-HiRes
BuildArch:	noarch

%description
This Perl modules allows to read from continously updated files.

%prep
%setup -qn File-Tail-1.0

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*
