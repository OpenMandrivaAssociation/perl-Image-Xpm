%define module	Image-Xpm
%define name	perl-%{module}
%define version 1.09
%define release %mkrel 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Load, create, manipulate and save xpm image files
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/S/SU/SUMMER/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl-Image-Base
Buildarch:	noarch

%description
This class module provides basic load, manipulate and save functionality for
the xpm file format. It inherits from Image::Base which provides additional
manipulation functionality, e.g. new_from_image(). See the Image::Base pod for
information on adding your own functionality to all the Image::Base derived
classes.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Image
%{_mandir}/*/*

