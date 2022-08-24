#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oneVPL
Version  : 2022.1.0
Release  : 1
URL      : https://github.com/oneapi-src/oneVPL/archive/refs/tags/v2022.1.0.tar.gz
Source0  : https://github.com/oneapi-src/oneVPL/archive/refs/tags/v2022.1.0.tar.gz
Summary  : oneAPI Video Processing Library
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: oneVPL-bin = %{version}-%{release}
Requires: oneVPL-data = %{version}-%{release}
Requires: oneVPL-lib = %{version}-%{release}
Requires: oneVPL-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(x11)
BuildRequires : pypi(pybind11)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : wayland-dev

%description
# ![oneAPI](assets/oneapi-logo.png "oneAPI") Video Processing Library
The oneAPI Video Processing Library (oneVPL) is a programming interface for video decoding, encoding,
and processing to build portable media pipelines on CPUs, GPUs, and other accelerators.

%package bin
Summary: bin components for the oneVPL package.
Group: Binaries
Requires: oneVPL-data = %{version}-%{release}
Requires: oneVPL-license = %{version}-%{release}

%description bin
bin components for the oneVPL package.


%package data
Summary: data components for the oneVPL package.
Group: Data

%description data
data components for the oneVPL package.


%package dev
Summary: dev components for the oneVPL package.
Group: Development
Requires: oneVPL-lib = %{version}-%{release}
Requires: oneVPL-bin = %{version}-%{release}
Requires: oneVPL-data = %{version}-%{release}
Provides: oneVPL-devel = %{version}-%{release}
Requires: oneVPL = %{version}-%{release}

%description dev
dev components for the oneVPL package.


%package doc
Summary: doc components for the oneVPL package.
Group: Documentation

%description doc
doc components for the oneVPL package.


%package lib
Summary: lib components for the oneVPL package.
Group: Libraries
Requires: oneVPL-data = %{version}-%{release}
Requires: oneVPL-license = %{version}-%{release}

%description lib
lib components for the oneVPL package.


%package license
Summary: license components for the oneVPL package.
Group: Default

%description license
license components for the oneVPL package.


%prep
%setup -q -n oneVPL-2022.1.0
cd %{_builddir}/oneVPL-2022.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661382274
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DBUILD_TESTS=ON
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1661382274
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oneVPL
cp %{_builddir}/oneVPL-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/oneVPL/23bd2c3b0aa961314a708f12595c02e8a1683682
cp %{_builddir}/oneVPL-%{version}/dispatcher/test/ext/googletest/LICENSE %{buildroot}/usr/share/package-licenses/oneVPL/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/oneVPL-%{version}/dispatcher/test/ext/googletest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/oneVPL/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
cp %{_builddir}/oneVPL-%{version}/examples/coreAPI/legacy-decode/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/coreAPI/legacy-encode/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/coreAPI/legacy-vpp/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/hello/hello-createsession/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/hello/hello-decode/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/hello/hello-decvpp/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/hello/hello-encode/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/hello/hello-transcode/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/hello/hello-vpp/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/interop/advanced-decvpp-infer/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/interop/dpcpp-blur/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/interop/hello-decode-infer/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/examples/interop/legacy-decode-infer/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/preview/cplusplus/examples/hello-decode-cpp/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/preview/cplusplus/examples/hello-encode-cpp/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/preview/python/examples/hello-decode-py/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/preview/python/examples/hello-encode-py/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
cp %{_builddir}/oneVPL-%{version}/preview/python/examples/hello-vpp-py/License.txt %{buildroot}/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/decvpp_tool
/usr/bin/hello-decode
/usr/bin/hello-encode
/usr/bin/hello-vpp
/usr/bin/sample_decode
/usr/bin/sample_encode
/usr/bin/sample_multi_transcode
/usr/bin/sample_vpp
/usr/bin/vpl-inspect

%files data
%defattr(-,root,root,-)
/usr/share/oneVPL/env/vars.sh
/usr/share/oneVPL/examples/content/cars_128x96.h265
/usr/share/oneVPL/examples/content/cars_128x96.i420
/usr/share/oneVPL/examples/content/cars_128x96.mjpeg
/usr/share/oneVPL/examples/content/cars_128x96.nv12
/usr/share/oneVPL/examples/content/cars_320x240.i420
/usr/share/oneVPL/examples/content/cars_320x240.nv12
/usr/share/oneVPL/examples/coreAPI/legacy-decode/CMakeLists.txt
/usr/share/oneVPL/examples/coreAPI/legacy-decode/License.txt
/usr/share/oneVPL/examples/coreAPI/legacy-decode/README.md
/usr/share/oneVPL/examples/coreAPI/legacy-decode/sample.json
/usr/share/oneVPL/examples/coreAPI/legacy-decode/src/legacy-decode.cpp
/usr/share/oneVPL/examples/coreAPI/legacy-decode/src/util.h
/usr/share/oneVPL/examples/coreAPI/legacy-encode/CMakeLists.txt
/usr/share/oneVPL/examples/coreAPI/legacy-encode/License.txt
/usr/share/oneVPL/examples/coreAPI/legacy-encode/PreLoad.cmake
/usr/share/oneVPL/examples/coreAPI/legacy-encode/README.md
/usr/share/oneVPL/examples/coreAPI/legacy-encode/sample.json
/usr/share/oneVPL/examples/coreAPI/legacy-encode/src/legacy-encode.cpp
/usr/share/oneVPL/examples/coreAPI/legacy-encode/src/util.h
/usr/share/oneVPL/examples/coreAPI/legacy-vpp/CMakeLists.txt
/usr/share/oneVPL/examples/coreAPI/legacy-vpp/License.txt
/usr/share/oneVPL/examples/coreAPI/legacy-vpp/README.md
/usr/share/oneVPL/examples/coreAPI/legacy-vpp/sample.json
/usr/share/oneVPL/examples/coreAPI/legacy-vpp/src/legacy-vpp.cpp
/usr/share/oneVPL/examples/coreAPI/legacy-vpp/src/util.h
/usr/share/oneVPL/examples/hello/hello-createsession/CMakeLists.txt
/usr/share/oneVPL/examples/hello/hello-createsession/License.txt
/usr/share/oneVPL/examples/hello/hello-createsession/PreLoad.cmake
/usr/share/oneVPL/examples/hello/hello-createsession/README.md
/usr/share/oneVPL/examples/hello/hello-createsession/sample.json
/usr/share/oneVPL/examples/hello/hello-createsession/src/hello-createsession.cpp
/usr/share/oneVPL/examples/hello/hello-createsession/src/util.h
/usr/share/oneVPL/examples/hello/hello-decode/CMakeLists.txt
/usr/share/oneVPL/examples/hello/hello-decode/License.txt
/usr/share/oneVPL/examples/hello/hello-decode/PreLoad.cmake
/usr/share/oneVPL/examples/hello/hello-decode/README.md
/usr/share/oneVPL/examples/hello/hello-decode/sample.json
/usr/share/oneVPL/examples/hello/hello-decode/src/hello-decode.cpp
/usr/share/oneVPL/examples/hello/hello-decode/src/util.h
/usr/share/oneVPL/examples/hello/hello-decvpp/CMakeLists.txt
/usr/share/oneVPL/examples/hello/hello-decvpp/License.txt
/usr/share/oneVPL/examples/hello/hello-decvpp/PreLoad.cmake
/usr/share/oneVPL/examples/hello/hello-decvpp/README.md
/usr/share/oneVPL/examples/hello/hello-decvpp/sample.json
/usr/share/oneVPL/examples/hello/hello-decvpp/src/hello-decvpp.cpp
/usr/share/oneVPL/examples/hello/hello-decvpp/src/util.h
/usr/share/oneVPL/examples/hello/hello-encode/CMakeLists.txt
/usr/share/oneVPL/examples/hello/hello-encode/License.txt
/usr/share/oneVPL/examples/hello/hello-encode/PreLoad.cmake
/usr/share/oneVPL/examples/hello/hello-encode/README.md
/usr/share/oneVPL/examples/hello/hello-encode/sample.json
/usr/share/oneVPL/examples/hello/hello-encode/src/hello-encode.cpp
/usr/share/oneVPL/examples/hello/hello-encode/src/util.h
/usr/share/oneVPL/examples/hello/hello-transcode/CMakeLists.txt
/usr/share/oneVPL/examples/hello/hello-transcode/License.txt
/usr/share/oneVPL/examples/hello/hello-transcode/README.md
/usr/share/oneVPL/examples/hello/hello-transcode/sample.json
/usr/share/oneVPL/examples/hello/hello-transcode/src/hello-transcode.cpp
/usr/share/oneVPL/examples/hello/hello-transcode/src/util.h
/usr/share/oneVPL/examples/hello/hello-vpp/CMakeLists.txt
/usr/share/oneVPL/examples/hello/hello-vpp/License.txt
/usr/share/oneVPL/examples/hello/hello-vpp/PreLoad.cmake
/usr/share/oneVPL/examples/hello/hello-vpp/README.md
/usr/share/oneVPL/examples/hello/hello-vpp/sample.json
/usr/share/oneVPL/examples/hello/hello-vpp/src/hello-vpp.cpp
/usr/share/oneVPL/examples/hello/hello-vpp/src/util.h
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/CMakeLists.txt
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/CPPLINT.cfg
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/License.txt
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/PreLoad.cmake
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/README.md
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/docker/Dockerfile
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/sample.json
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/src/advanced-decvpp-infer.cpp
/usr/share/oneVPL/examples/interop/advanced-decvpp-infer/src/util.h
/usr/share/oneVPL/examples/interop/dpcpp-blur/CMakeLists.txt
/usr/share/oneVPL/examples/interop/dpcpp-blur/License.txt
/usr/share/oneVPL/examples/interop/dpcpp-blur/PreLoad.cmake
/usr/share/oneVPL/examples/interop/dpcpp-blur/README.md
/usr/share/oneVPL/examples/interop/dpcpp-blur/sample.json
/usr/share/oneVPL/examples/interop/dpcpp-blur/src/dpcpp-blur.cpp
/usr/share/oneVPL/examples/interop/dpcpp-blur/src/util.h
/usr/share/oneVPL/examples/interop/hello-decode-infer/CMakeLists.txt
/usr/share/oneVPL/examples/interop/hello-decode-infer/CPPLINT.cfg
/usr/share/oneVPL/examples/interop/hello-decode-infer/License.txt
/usr/share/oneVPL/examples/interop/hello-decode-infer/PreLoad.cmake
/usr/share/oneVPL/examples/interop/hello-decode-infer/README.md
/usr/share/oneVPL/examples/interop/hello-decode-infer/docker/Dockerfile
/usr/share/oneVPL/examples/interop/hello-decode-infer/sample.json
/usr/share/oneVPL/examples/interop/hello-decode-infer/src/hello-decode-infer.cpp
/usr/share/oneVPL/examples/interop/hello-decode-infer/src/util.h
/usr/share/oneVPL/examples/interop/legacy-decode-infer/CMakeLists.txt
/usr/share/oneVPL/examples/interop/legacy-decode-infer/CPPLINT.cfg
/usr/share/oneVPL/examples/interop/legacy-decode-infer/License.txt
/usr/share/oneVPL/examples/interop/legacy-decode-infer/README.md
/usr/share/oneVPL/examples/interop/legacy-decode-infer/docker/Dockerfile
/usr/share/oneVPL/examples/interop/legacy-decode-infer/sample.json
/usr/share/oneVPL/examples/interop/legacy-decode-infer/src/legacy-decode-infer.cpp
/usr/share/oneVPL/examples/interop/legacy-decode-infer/src/util.h
/usr/share/oneVPL/examples/preview/cplusplus/hello-decode-cpp/CMakeLists.txt
/usr/share/oneVPL/examples/preview/cplusplus/hello-decode-cpp/License.txt
/usr/share/oneVPL/examples/preview/cplusplus/hello-decode-cpp/README.md
/usr/share/oneVPL/examples/preview/cplusplus/hello-decode-cpp/src/hello-decode.cpp
/usr/share/oneVPL/examples/preview/cplusplus/hello-decode-cpp/src/util.hpp
/usr/share/oneVPL/examples/preview/cplusplus/hello-encode-cpp/CMakeLists.txt
/usr/share/oneVPL/examples/preview/cplusplus/hello-encode-cpp/License.txt
/usr/share/oneVPL/examples/preview/cplusplus/hello-encode-cpp/README.md
/usr/share/oneVPL/examples/preview/cplusplus/hello-encode-cpp/src/hello-encode.cpp
/usr/share/oneVPL/examples/preview/cplusplus/hello-encode-cpp/src/util.hpp
/usr/share/oneVPL/modulefiles/vpl

%files dev
%defattr(-,root,root,-)
/usr/include/vpl/mfx.h
/usr/include/vpl/mfxadapter.h
/usr/include/vpl/mfxbrc.h
/usr/include/vpl/mfxcommon.h
/usr/include/vpl/mfxdefs.h
/usr/include/vpl/mfxdispatcher.h
/usr/include/vpl/mfxdispatcherprefixedfunctions.h
/usr/include/vpl/mfximplcaps.h
/usr/include/vpl/mfxjpeg.h
/usr/include/vpl/mfxmvc.h
/usr/include/vpl/mfxpcp.h
/usr/include/vpl/mfxsession.h
/usr/include/vpl/mfxstructures.h
/usr/include/vpl/mfxsurfacepool.h
/usr/include/vpl/mfxvideo++.h
/usr/include/vpl/mfxvideo.h
/usr/include/vpl/mfxvp8.h
/usr/include/vpl/preview/README.txt
/usr/include/vpl/preview/bitstream.hpp
/usr/include/vpl/preview/defs.hpp
/usr/include/vpl/preview/detail/frame_interface.hpp
/usr/include/vpl/preview/detail/sdk_callable.hpp
/usr/include/vpl/preview/detail/string_helpers.hpp
/usr/include/vpl/preview/detail/variant.hpp
/usr/include/vpl/preview/exception.hpp
/usr/include/vpl/preview/extension_buffer.hpp
/usr/include/vpl/preview/extension_buffer_list.hpp
/usr/include/vpl/preview/frame_surface.hpp
/usr/include/vpl/preview/future.hpp
/usr/include/vpl/preview/impl_caps.hpp
/usr/include/vpl/preview/impl_selector.hpp
/usr/include/vpl/preview/option_tree.hpp
/usr/include/vpl/preview/options.hpp
/usr/include/vpl/preview/payload.hpp
/usr/include/vpl/preview/session.hpp
/usr/include/vpl/preview/source_reader.hpp
/usr/include/vpl/preview/stat.hpp
/usr/include/vpl/preview/surface_pool.hpp
/usr/include/vpl/preview/video_param.hpp
/usr/include/vpl/preview/vpl.hpp
/usr/lib64/cmake/vpl/VPLConfig.cmake
/usr/lib64/cmake/vpl/VPLConfigVersion.cmake
/usr/lib64/libvpl.so
/usr/lib64/pkgconfig/vpl.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/oneVPL/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvpl.so.2
/usr/lib64/libvpl.so.2.6
/usr/lib64/oneVPL/libvpl_wayland.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oneVPL/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
/usr/share/package-licenses/oneVPL/23bd2c3b0aa961314a708f12595c02e8a1683682
/usr/share/package-licenses/oneVPL/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/oneVPL/96e27db69e6c1223c23e287a5802383b683382bc