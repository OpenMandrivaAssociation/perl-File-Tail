%define module File-Tail

Summary:	File::Tail module for Perl
Name:		perl-%module
Version:	0.99.3
Release:	%mkrel 9
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
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/*/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.99.3-9mdv2012.0
+ Revision: 765274
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.99.3-8
+ Revision: 763767
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.99.3-7
+ Revision: 667146
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.99.3-6mdv2010.1
+ Revision: 426445
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.99.3-5mdv2009.1
+ Revision: 351766
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.99.3-4mdv2009.0
+ Revision: 223755
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.99.3-3mdv2008.1
+ Revision: 180397
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.99.3-2mdv2007.0
+ Revision: 108534
- rebuild

  + Michael Scherer <misc@mandriva.org>
    - Import perl-File-Tail

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.99.3-1mdk
- New release 0.99.3
- make rpmbuildupdate-able

* Thu Jun 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.99.1-2mdk
- Rebuild

* Wed Jan 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.99.1-1mdk
- New version
- Update description
- Remove MANIFEST

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.98-5mdk
- rebuild

