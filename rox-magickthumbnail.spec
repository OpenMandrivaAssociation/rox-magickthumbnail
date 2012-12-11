%define name rox-magickthumbnail
%define oname MagickThumbnail
%define version 0.5.1
%define release %mkrel 7

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
Requires: imagemagick
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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-7mdv2010.0
+ Revision: 433391
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-6mdv2009.0
+ Revision: 242557
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Jun 03 2006 Götz Waschk <waschk@mandriva.org> 0.5.1-4mdv2007.0
- fix appdir
- use mkrel

* Thu Jun 02 2005 Götz Waschk <waschk@mandriva.org> 0.5.1-3mdk
- Rebuild

* Fri May 28 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5.1-2mdk
- only thumbnail the first frame (usefull for 1000 page pdfs)

* Fri Mar 05 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5.1-1mdk
- new version

* Thu Mar 04 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-2mdk
- add missing icon

* Thu Mar 04 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- initial package

