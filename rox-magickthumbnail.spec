%define name rox-magickthumbnail
%define oname MagickThumbnail
%define version 0.5.1
%define release %mkrel 6

Summary: Thumbnail image generator for the ROX desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://roxos.sunsite.dk/dev-contrib/guido/%{oname}.tar.bz2
Patch: rox-magickthumbnail-first-frame.patch
License: GPL
Group: Graphical desktop/Other
Url: http://roxos.sunsite.dk/dev-contrib/guido/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: rox-lib >= 1.9.12
Requires: rox >= 2.1.1
Requires: ImageMagick
BuildArch: noarch

%description
This application can generate thumbnails of the various filetypes,
readable by ImageMagick, for display by ROX-Filer.

%prep
%setup -q -n %oname
%patch -p1
rm -f Help/.README.swp

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_prefix/lib/apps/%oname
cp -r .DirIcon * %buildroot%_prefix/lib/apps/%oname

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %_prefix/lib/apps/%oname/Help/
%dir %_prefix/lib/apps/%oname/
%_prefix/lib/apps/%oname/.DirIcon
%_prefix/lib/apps/%oname/*.xml
%_prefix/lib/apps/%oname/*.py
%_prefix/lib/apps/%oname/AppRun

