%define name	hfsutils
%define version	3.2.6
%define release	%mkrel 29

Summary:	Tools for reading and writing Macintosh HFS volumes
Name:		%{name}
Version:	%{version}
Release:	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:		hfsutils-3.2.6_errno.patch
Patch1:		hfsutils-3.2.6-lib64.patch
BuildRequires:	tk tk-devel tcl tcl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
Group:		File tools
URL:		http://www.mars.org/home/rob/proj/hfs/

%package	devel
Summary:	C library for reading and writing Macintosh HFS volumes
Group:		Development/C
Conflicts:	cdrecord-devel

%package xhfs
Summary:	A graphical interface for manipulating HFS volumes
Group:		File tools
Requires:	hfsutils

%description
A portable, free implementation of routines for accessing HFS volumes.
Provides this through several command-line programs, a tk-based front end
for browsing and copying files, and a Tcl package and interface for
scriptable access to volumes.

%description	devel
A portable, free implementation of routines for accessing HFS volumes via a
C library for low-level access to volumes.

%description xhfs
Xhfs presents a graphical front-end for browsing and copying files on
HFS-formatted volumes.

%prep
%setup -q
%patch0 -p1 -b .errno
%patch1 -p1 -b .lib64
autoreconf -v -i

%build
export CFLAGS="%optflags -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DUSE_INTERP_RESULT"
%configure2_5x --with-tcl --with-tk --enable-devlibs --with-lib=%{_lib}

%make

%install
rm -fr %{buildroot}
# (Dadou) Needed...
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}

# (Dadou) Don't use macros here
make install BINDEST=%{buildroot}%_prefix/bin MANDEST=%{buildroot}%_mandir LIBDEST=%{buildroot}%_libdir INCDEST=%{buildroot}%_includedir

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc BLURB CHANGES COPYING COPYRIGHT CREDITS INSTALL README TODO
%config
%{_bindir}/h*
%{_mandir}/man1/h*

%files devel
%defattr (-,root,root)
%{_libdir}/*.a
%{_includedir}/*

%files xhfs
%defattr (-,root,root)
%{_bindir}/xhfs
%{_mandir}/man1/xhfs.*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.6-26mdv2011.0
+ Revision: 665412
- mass rebuild

* Wed Dec 22 2010 Funda Wang <fwang@mandriva.org> 3.2.6-25mdv2011.0
+ Revision: 623785
- tighten BR

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.6-24mdv2011.0
+ Revision: 605857
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.6-23mdv2010.1
+ Revision: 520119
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.6-22mdv2010.0
+ Revision: 425145
- rebuild

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.6-21mdv2009.1
+ Revision: 347742
- rebuild against latest tk libs
- fix build with tcl 8.6

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.2.6-20mdv2009.0
+ Revision: 221175
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 3.2.6-19mdv2008.1
+ Revision: 150255
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Emmanuel Andry <eandry@mandriva.org> 3.2.6-18mdv2008.0
+ Revision: 87140
- use autoreconf

* Sat Sep 15 2007 Emmanuel Andry <eandry@mandriva.org> 3.2.6-17mdv2008.0
+ Revision: 87139
- uncompress patches
- disable autoconf, cannot build with it

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild for new soname of tcl

* Fri May 25 2007 Christiaan Welvaart <spturtle@mandriva.org> 3.2.6-16mdv2008.0
+ Revision: 31214
- rebuild for new tcl
- Import hfsutils




* Sun Sep 10 2006 Stefan van der Eijk <stefan@mandriva.org> 3.2.6-15
- %%mkrel

* Sat May 20 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 3.2.6-14mdk
- split xhfs into a separate package to remove x11 deps from hfsutils

* Mon Jan 02 2006 Oden Eriksson <oeriksson@mandriva.com> 3.2.6-13mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Tue Jun 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.2.6-12mdk
- fix buildrequires

* Fri May 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.2.6-11mdk
- fix buildrequires

* Fri Oct  3 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.2.6-10mdk
- lib64 fixes

* Thu May  9 2003 Stew Benedict <sbenedict@mandrakesoft.com> 3.2.6-9mdk
- devel conflicts with cdrecord-devel: J.A. Magallon <jamagallon@able.es>

* Tue May  6 2003 Stew Benedict <sbenedict@mandrakesoft.com> 3.2.6-8mdk
- large file support

* Wed Apr  9 2003 Stew Benedict <sbenedict@mandrakesoft.com> 3.2.6-7mdk
- rebuild for new Tcl/Tk, errno patch (patch0)

* Sun Jun  2 2002 Stefan van der Eijk <stefan@eijk.nu> 3.2.6-6mdk
- BuildRequires

* Tue May 07 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.2.6-5mdk
- Automated rebuild in gcc3.1 environment

* Wed Feb  6 2002 Stew Benedict <sbenedict@mandrakesoft.com> 3.2.6-4mdk
- remove ExclusiveArch ppc, s/Copyright/License/, add URL

* Sat Sep 17 2000 David BAUDENS <baudens@mandrakesoft.com> 3.2.6-3mdk
- Allow to build (ake big spec clean up, macros, BM & Co.)

* Fri Jul 07 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.2.6-2mdk
- Spec cleanup.
- Adjust groups.

* Thu Feb 24 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build
