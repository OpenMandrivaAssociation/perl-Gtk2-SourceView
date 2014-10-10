%define upstream_name    Gtk2-SourceView
%define upstream_version 1.000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	14

Summary:	Perl upstream_name for the gtksourceview library
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Gtk2-SourceView-1.000-port-to-api2.patch

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	pkgconfig(gtksourceview-1.0)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib)                 >  1.00
BuildRequires:	perl(Gnome2)               >= 0.30
BuildRequires:	perl(Gnome2::Print)
BuildRequires:	perl-devel 

# for data files:
Requires:	gtksourceview1
Requires:	gtk+2

%description
This module provides perl access to the libgtksourceview library, a library
that adds syntax highlighting, line numbers, and other programming-editor
features.
GtkSourceView specializes these features for a code editor.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# (tv) disabled (not enought to build with gtksourceview-2):
#%patch -p0
find -type d -name CVS | xargs rm -rf 
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="%{optflags}"
#%make test || :

%install
%makeinstall_std

%files
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*

%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Sun Feb 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.0.0-11mdv2010.1
+ Revision: 505749
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.000-10mdv2010.0
+ Revision: 426493
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.000-9mdv2009.1
+ Revision: 351811
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.000-8mdv2009.0
+ Revision: 223782
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.000-7mdv2008.1
+ Revision: 152150
- rebuild for new perl
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 5mdv2008.1-current
+ Revision: 134180
- requires gtksourceview1 for data files
- disable patch 0 (not enought to build with gtksourceview-2)
- BR libgtksourceview-1.0-devel instead of latest one
- kill re-definition of %%buildroot on Pixel's request
- readd missing patch
- rebuild


* Mon Feb 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.000-3mdv2007.0
+ Revision: 122789
- rebuild in order to get the same extension on x86_64
- Import perl-Gtk2-SourceView

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.000-2mdk
- Fix BuildRequires

* Tue Oct 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.000-1mdk
- new release

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.0-4mdk
- buildrequires fix

* Tue Feb 08 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.0-3mdk
- rebuild for new perl and for nice number of version

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0-2mdk
- rebuild for perl-5.8.5
- fix too long description
- really remove CVS directories
- remove explicit requires on libgtk+2

* Fri Apr 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0-1mdk
- initial release

