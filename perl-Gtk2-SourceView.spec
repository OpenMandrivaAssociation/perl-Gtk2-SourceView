%define upstream_name    Gtk2-SourceView
%define upstream_version 1.000

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	12

Summary:    Perl upstream_name for the gtksourceview library
License:    GPL or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
Source0:    %{upstream_name}-%{upstream_version}.tar.bz2
Patch0:     Gtk2-SourceView-1.000-port-to-api2.patch

BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libgnomeprintui-2.2)
BuildRequires: pkgconfig(gtksourceview-1.0)
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib)                 >  1.00
BuildRequires: perl(Gnome2)               >= 0.30
BuildRequires: perl(Gnome2::Print)
BuildRequires: perl-devel 

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

# for data files:
Requires: gtksourceview1
Requires: gtk+2

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
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/*
