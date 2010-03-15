%define name	hfsutils
%define version	3.2.6
%define release	%mkrel 23

Summary:	Tools for reading and writing Macintosh HFS volumes
Name:		%{name}
Version:	%{version}
Release:	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:		hfsutils-3.2.6_errno.patch
Patch1:		hfsutils-3.2.6-lib64.patch

BuildRequires:	X11-devel tk tk-devel tcl tcl-devel autoconf2.1
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
