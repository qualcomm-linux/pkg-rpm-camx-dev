%global debug_package %{nil}
%global __os_install_post %{nil}
%global _build_id_links none

%global upstream_tag 260925

# The publisher uses arm64 in the tarball filename. The RPM remains noarch
# because the payload contains headers only.
%global upstream_arch arm64

Name:           camx-dev
Version:        1.1.1
Release:        1%{?dist}
Summary:        Qualcomm CamX usermode headers consumed by camera service

License:        LicenseRef-Qualcomm-Proprietary
URL:            http://support.cdmatech.com

Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/camx.qclinux.0.0/%{upstream_tag}/prebuilt_rpm/camx-headers_%{version}_%{upstream_arch}.tar.gz

BuildArch:      noarch

%description
Qualcomm CamX usermode headers consumed by camera service.

Target-agnostic header-only package providing the CamX camera API under
/usr/include/camx-v1. Contains no libraries and no
compiled code; it exists so camera-service and GStreamer-side consumers can
build against the CamX API without depending on a per-target CamX build.

%package -n libcamx-dev
Summary:        Qualcomm CamX usermode headers consumed by camera service

# Keep the libcamx-dev binary name used by Stage 1 and existing RPM consumers.
%description -n libcamx-dev
Qualcomm CamX usermode headers consumed by camera service.

Target-agnostic header-only package providing the CamX camera API under
/usr/include/camx-v1. The package also provides compatibility headers under
/usr/include/hardware and /usr/include/system.

%prep
%autosetup -n camx-headers_%{version}

%build
# Intentionally empty: header-only payload, nothing to compile.

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}/

# camera-service and GStreamer include these compatibility headers using the
# standard Android-style hardware/ and system/ include paths.
install -d %{buildroot}%{_includedir}/hardware
install -d %{buildroot}%{_includedir}/system
cp -a %{buildroot}%{_includedir}/camx-v1/camx-api/camx/service/hardware/. \
    %{buildroot}%{_includedir}/hardware/
cp -a %{buildroot}%{_includedir}/camx-v1/camx-api/camx/service/system/. \
    %{buildroot}%{_includedir}/system/

%files -n libcamx-dev
%license %{_defaultlicensedir}/libcamx-dev/LICENSE.qcom-2
%license %{_defaultlicensedir}/libcamx-dev/LICENSE
%doc %{_docdir}/libcamx-dev/NOTICE
%{_includedir}/camx-v1
%{_includedir}/hardware
%{_includedir}/system

%changelog
* Mon Sep 28 2026 Qualcomm Camera Team <camx.deb.maintainers@qti.qualcomm.com> - 1.1.1-1
- Initial RPM package for the CamX API headers.
