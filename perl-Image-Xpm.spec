%define upstream_name	 Image-Xpm
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Load, create, manipulate and save xpm image files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SU/SUMMER/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl-Image-Base
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This class module provides basic load, manipulate and save functionality for
the xpm file format. It inherits from Image::Base which provides additional
manipulation functionality, e.g. new_from_image(). See the Image::Base pod for
information on adding your own functionality to all the Image::Base derived
classes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
