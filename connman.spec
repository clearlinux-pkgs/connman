#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : connman
Version  : 1.30
Release  : 2
URL      : https://www.kernel.org/pub/linux/network/connman/connman-1.30.tar.gz
Source0  : https://www.kernel.org/pub/linux/network/connman/connman-1.30.tar.gz
Summary  : Connection Manager
Group    : Development/Tools
License  : GPL-2.0
Requires: connman-bin
Requires: connman-config
Requires: connman-data
Requires: connman-doc
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(xtables)
BuildRequires : readline-dev
BuildRequires : systemd-dev
BuildRequires : wpa_supplicant

%description
Connection Manager
******************
Functionality and features
==========================

%package bin
Summary: bin components for the connman package.
Group: Binaries
Requires: connman-data
Requires: connman-config

%description bin
bin components for the connman package.


%package config
Summary: config components for the connman package.
Group: Default

%description config
config components for the connman package.


%package data
Summary: data components for the connman package.
Group: Data

%description data
data components for the connman package.


%package dev
Summary: dev components for the connman package.
Group: Development
Requires: connman-bin
Requires: connman-data
Provides: connman-devel

%description dev
dev components for the connman package.


%package doc
Summary: doc components for the connman package.
Group: Documentation

%description doc
doc components for the connman package.


%prep
%setup -q -n connman-1.30

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/connmanctl
/usr/bin/connmand

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/connman.service

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system.d/connman.conf

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
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
