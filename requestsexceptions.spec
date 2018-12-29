#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x421E6472811F9A81 (infra-root@openstack.org)
#
Name     : requestsexceptions
Version  : 1.4.0
Release  : 14
URL      : http://tarballs.openstack.org/requestsexceptions/requestsexceptions-1.4.0.tar.gz
Source0  : http://tarballs.openstack.org/requestsexceptions/requestsexceptions-1.4.0.tar.gz
Source99 : http://tarballs.openstack.org/requestsexceptions/requestsexceptions-1.4.0.tar.gz.asc
Summary  : Import exceptions from potentially bundled packages in requests.
Group    : Development/Tools
License  : Apache-2.0
Requires: requestsexceptions-python3
Requires: requestsexceptions-license
Requires: requestsexceptions-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==================
        
        The python requests library bundles the urllib3 library, however, some
        software distributions modify requests to remove the bundled library.
        This makes some operations, such as supressing the "insecure platform
        warning" messages that urllib emits difficult.  This is a simple
        library to find the correct path to exceptions in the requests library
        regardless of whether they are bundled.

%package license
Summary: license components for the requestsexceptions package.
Group: Default

%description license
license components for the requestsexceptions package.


%package python
Summary: python components for the requestsexceptions package.
Group: Default
Requires: requestsexceptions-python3

%description python
python components for the requestsexceptions package.


%package python3
Summary: python3 components for the requestsexceptions package.
Group: Default
Requires: python3-core

%description python3
python3 components for the requestsexceptions package.


%prep
%setup -q -n requestsexceptions-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532270956
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/requestsexceptions
cp LICENSE %{buildroot}/usr/share/doc/requestsexceptions/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/requestsexceptions/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
