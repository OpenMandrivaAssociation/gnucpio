Summary:	A GNU archiving program
Name:		cpio
Version:	2.11
Release:	7
License:	GPLv2+
Group:		Archiving/Backup
URL:		http://www.gnu.org/software/cpio/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
Patch0:		cpio-2.11-no-gets.patch
Patch1:		cpio-2.11-non-gnu-compilers.patch
Patch2:		cpio-2.11-stat.patch
Patch3:		cpio-2.7-svr4compat.patch
BuildRequires:	bison
Requires:	rmt
BuildRequires:	texinfo

%description
GNU cpio copies files into or out of a cpio or tar archive.  Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions.  The archive can be another file on the disk, a magnetic
tape, or a pipe.  GNU cpio supports the following archive formats:  binary,
old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar and POSIX.1
tar.  By default, cpio creates binary format archives, so that they are
compatible with older cpio programs.  When it is extracting files from
archives, cpio automatically recognizes which kind of archive it is reading
and can read archives created on machines with a different byte-order.

Install cpio if you need a program to manage file archives.
archives

%prep

%setup -q
%patch0 -p1 -b .gets
%patch1 -p0 -b .gnu
%patch2 -p1 -b .stat
%patch3 -p1 -b .svr4compat

%build
export CPPFLAGS="%{optflags} -DHAVE_LSTAT=1"
%configure2_5x \
	--bindir=/bin \
	--with-rmt=/sbin/rmt \
	--disable-rpath

%make

%check
make check

%install
%makeinstall_std

%find_lang %{name}

# remove unpackaged file
rm -f %{buildroot}%{_mandir}/man1/mt.*


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
/bin/cpio
%{_infodir}/cpio.*
%{_mandir}/man1/cpio.1*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.11-3mdv2011.0
+ Revision: 663400
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2.11-2mdv2011.0
+ Revision: 603851
- rebuild

* Fri Mar 12 2010 Oden Eriksson <oeriksson@mandriva.com> 2.11-1mdv2010.1
+ Revision: 518397
- 2.11

* Wed Jun 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.10-1mdv2010.0
+ Revision: 388893
- update to new version 2.10
- drop patches 4 and 6
- add buildrequires on bison
- kill rpath

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.9-6mdv2009.1
+ Revision: 316516
- rediffed one fuzzy patch

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 2.9-5mdv2009.0
+ Revision: 264358
- rebuild early 2009.0 package (before pixel changes)

* Wed May 21 2008 Oden Eriksson <oeriksson@mandriva.com> 2.9-4mdv2009.0
+ Revision: 209708
- added a gcc43 patch from fedora

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Funda Wang <fwang@mandriva.org> 2.9-3mdv2008.1
+ Revision: 120544
- fix CVE-2007-4476

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 2.9-2mdv2008.0
+ Revision: 69900
- kill file require on info-install

* Wed Jul 11 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9-1mdv2008.0
+ Revision: 51382
- new version

* Mon Jun 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.8-1mdv2008.0
+ Revision: 40641
- new version
- remove patches 10,11 and 12 (has been fixed upstream)
- add %%check
- spec file clean


* Tue Jan 23 2007 Stew Benedict <sbenedict@mandriva.com> 2.7-3mdv2007.0
+ Revision: 112577
- Fix issue with bad symlinks in archive (#28369)

* Wed Nov 15 2006 Stew Benedict <sbenedict@mandriva.com> 2.7-2mdv2007.1
+ Revision: 84328
- fix P11 (copypass perms fix)
- add patch for copypass bug #27143

* Fri Nov 10 2006 Stew Benedict <sbenedict@mandriva.com> 2.7-1mdv2007.0
+ Revision: 80499
- Import cpio

* Fri Nov 10 2006 Stew Benedict <sbenedict@mandriva.com> 2.7-1mdv2007.1
- 2.7
- drop P2 (mtime)
- rediff, bunzip P3 (svr4compat)
- drop P4 (no-libnsl)
- bunzip P10
- drop P11 (CAN-199-1572) - merged upstream
- drop P12 (gcc4 compile) - not needed
- drop P13 (CVE-2005-4268) - merged upstream
- import into svn

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 2.6-7mdk
- rebuild for sparc

* Thu Dec 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.6-6mdk
- Patch 13: security fix for CVE-2005-4268

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.6-5mdk
- Require rmt directly
- Fix compilation with gcc 4 (patch 12)

* Thu Apr 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.6-4mdk
- Add -DHAVE_LSTAT=1 to the C flags (bug #12970)

* Wed Mar 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.6-3mdk
- Add patch 11, security fix for CAN-1999-1572

* Thu Jan 06 2005 Stew Benedict <sbenedict@mandrake.org> 2.6-2mdk
- re-patch for LSB compliance 
-   subpatch of one provided by Mitsuru Chinen of OpenI18N (P10)
-   http://www.openi18n.org/subgroups/utildev/dli18npatch2.html

* Wed Dec 22 2004 Abel Cheung <deaddog@mandrake.org> 2.6-1mdk
- Drop P1 (errno), P10 (manpage location), P12 (i18n), fixed upstream
- Merge P11 into P3
- cpio is not using bundled error handling routine, so P9 is not useful now,
  but keep it in case somebody want to take a look
- Other spec cleanup
- P4 (fedora), no need to link with libnsl
- make check

