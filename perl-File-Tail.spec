%define module File-Tail

Summary:	File::Tail module for Perl
Name:		perl-%module
Version:	0.99.3
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MG/MGRABNAR/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%module/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root/
Requires:	perl
BuildRequires:	perl-devel perl-Time-HiRes
BuildArch:	noarch

%description
This Perl modules allows to read from continously updated files.

%prep
%setup -q -n File-Tail-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/*/*


