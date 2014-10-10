%define upstream_name	 Image-Xpm
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Load, create, manipulate and save xpm image files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SU/SUMMER/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Image::Base)
BuildArch:	noarch

%description
This class module provides basic load, manipulate and save functionality for
the xpm file format. It inherits from Image::Base which provides additional
manipulation functionality, e.g. new_from_image(). See the Image::Base pod for
information on adding your own functionality to all the Image::Base derived
classes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Image
%{_mandir}/*/*


%changelog
* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 596560
- update to new version 1.12

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 471053
- update to 1.11

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 466456
- update to 1.10

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.0
+ Revision: 402545
- rebuild using %%perl_convert_version

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.09-12mdv2009.0
+ Revision: 290410
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-9mdv2008.0
+ Revision: 86477
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-8mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-7mdk
- better summary and description
- spec cleanup
- better URL
- %%mkrel

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-6mdk 
- remove MANIFEST

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-5mdk
- fix buildrequires in a backward compatible way

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-4mdk 
- fix directory ownership (distlint)
- make test

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-3mdk 
- rpmbuildupdate aware

