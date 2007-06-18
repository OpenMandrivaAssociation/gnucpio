Summary:	A GNU archiving program
Name:		cpio
Version:	2.8
Release:	%mkrel 1
License:	GPL
Group:		Archiving/Backup
URL:		http://www.gnu.org/software/cpio/
Source:		ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
Patch3:		cpio-2.7-svr4compat.patch
Requires(post):	/sbin/install-info
Requires(preun):/sbin/install-info
Requires:	rmt
BuildRequires:	texinfo
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch3 -p1 -b .svr4compat

%build
%configure2_5x --bindir=/bin --with-rmt=/sbin/rmt CPPFLAGS=-DHAVE_LSTAT=1
%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

# remove unpackaged file
rm -f %{buildroot}%{_mandir}/man1/mt.*

%clean
rm -rf %{buildroot}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
/bin/cpio
%{_infodir}/cpio.*
%{_mandir}/man1/cpio.1*
