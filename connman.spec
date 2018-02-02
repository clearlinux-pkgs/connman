#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : connman
Version  : 1.35
Release  : 24
URL      : https://www.kernel.org/pub/linux/network/connman/connman-1.35.tar.gz
Source0  : https://www.kernel.org/pub/linux/network/connman/connman-1.35.tar.gz
Summary  : Connection Manager
Group    : Development/Tools
License  : GPL-2.0
Requires: connman-bin
Requires: connman-config
Requires: connman-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : openconnect-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnftnl)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(xtables)
BuildRequires : readline-dev
BuildRequires : wpa_supplicant
Patch1: 0001-create-resolv.conf-link-when-lauched.patch

%description
Connection Manager
******************
Functionality and features
==========================

%package bin
Summary: bin components for the connman package.
Group: Binaries
Requires: connman-config

%description bin
bin components for the connman package.


%package config
Summary: config components for the connman package.
Group: Default

%description config
config components for the connman package.


%package dev
Summary: dev components for the connman package.
Group: Development
Requires: connman-bin
Provides: connman-devel

%description dev
dev components for the connman package.


%package doc
Summary: doc components for the connman package.
Group: Documentation

%description doc
doc components for the connman package.


%prep
%setup -q -n connman-1.35
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502420774
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1502420774
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/connmanctl
/usr/bin/connmand
/usr/bin/connmand-wait-online

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/connman-resolvconf.service
/usr/lib/systemd/system/connman-wait-online.service
/usr/lib/systemd/system/connman.service
/usr/lib/tmpfiles.d/connman_resolvconf.conf

%files dev
%defattr(-,root,root,-)
/usr/include/connman/agent.h
/usr/include/connman/device.h
/usr/include/connman/inet.h
/usr/include/connman/inotify.h
/usr/include/connman/ipaddress.h
/usr/include/connman/ipconfig.h
/usr/include/connman/log.h
/usr/include/connman/machine.h
/usr/include/connman/network.h
/usr/include/connman/notifier.h
/usr/include/connman/peer.h
/usr/include/connman/plugin.h
/usr/include/connman/provision.h
/usr/include/connman/resolver.h
/usr/include/connman/service.h
/usr/include/connman/session.h
/usr/include/connman/storage.h
/usr/include/connman/version.h
/usr/lib64/pkgconfig/connman.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
