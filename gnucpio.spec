Summary:	A GNU archiving program
Name:		gnucpio
Version:	2.13
Release:	1
License:	GPLv2+
Group:		Archiving/Backup
Url:		http://www.gnu.org/software/cpio/
Source0:	ftp://ftp.gnu.org/pub/gnu/cpio/cpio-%{version}.tar.bz2
Patch0:		cpio-2.13-fix-clang.patch
Patch1:		0001-Fix-cpio-header-verification.patch
Patch2:		0002-Improve-684b7ac5.patch
# fix mga#25698
Patch10:	revert-upstream-CVE-2015-1197.patch
Patch11:	suse-CVE-2015-1197.patch
Patch20:	cpio-2.12-svr4compat.patch
Patch21:	cpio-2.13-git-multiple-defs.patch
Patch22:	cpio-2.13-CVE-2021-38185.patch
Patch23:	dfc801c44a93bed7b3951905b188823d6a0432c8.patch
Patch24:	236684f6deb3178043fe72a8e2faca538fa2aae1.patch

BuildRequires:	bison
BuildRequires:	texinfo
Requires:	rmt

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

OpenMandriva Lx uses bsdcpio by default -- install gnucpio if you need
the GNU implementation of cpio.

%prep
%autosetup -n cpio-%{version} -p1

%build
export CPPFLAGS="%{optflags} -DHAVE_LSTAT=1"
%configure \
	--with-rmt=%{_bindir}/rmt

%make_build

%check
%make check

%install
%make_install

%find_lang cpio

# remove unpackaged file
rm -f %{buildroot}%{_mandir}/man1/mt.*

mv %{buildroot}%{_bindir}/cpio %{buildroot}%{_bindir}/gcpio
mv %{buildroot}%{_mandir}/man1/cpio.1 %{buildroot}%{_mandir}/man1/gcpio.1

%files -f cpio.lang
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/gcpio
%doc %{_infodir}/cpio.*
%doc %{_mandir}/man1/gcpio.1*
