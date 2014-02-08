Summary:	A GNU archiving program
Name:		cpio
Version:	2.11
Release:	13
License:	GPLv2+
Group:		Archiving/Backup
Url:		http://www.gnu.org/software/cpio/
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
Patch0:		cpio-2.11-no-gets.patch
Patch1:		cpio-2.11-non-gnu-compilers.patch
Patch2:		cpio-2.11-stat.patch
Patch3:		cpio-2.7-svr4compat.patch
Patch4:		cpio-aarch64.patch
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

Install cpio if you need a program to manage file archives.
archives

%prep
%setup -q
%apply_patches

%build
export CPPFLAGS="%{optflags} -DHAVE_LSTAT=1"
%configure2_5x \
	--bindir=/bin \
	--with-rmt=/sbin/rmt

%make

%check
make check

%install
%makeinstall_std

%find_lang %{name}

# remove unpackaged file
rm -f %{buildroot}%{_mandir}/man1/mt.*


%files -f %{name}.lang
%doc AUTHORS ChangeLog README NEWS
/bin/cpio
%{_infodir}/cpio.*
%{_mandir}/man1/cpio.1*

