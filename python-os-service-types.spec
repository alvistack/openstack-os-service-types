# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-os-service-types
Epoch: 100
Version: 1.7.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python library for consuming OpenStack sevice-types-authority data
License: Apache-2.0
URL: https://github.com/openstack/os-service-types/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The OpenStack Service Types Authority contains information about
official OpenStack services and their historical service-type aliases.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-os-service-types
Summary: Python library for consuming OpenStack sevice-types-authority data
Requires: python3
Requires: python3-pbr >= 2.0.0
Provides: python3-os-service-types = %{epoch}:%{version}-%{release}
Provides: python3dist(os-service-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-os-service-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(os-service-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-os-service-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(os-service-types) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-os-service-types
The OpenStack Service Types Authority contains information about
official OpenStack services and their historical service-type aliases.

%files -n python%{python3_version_nodots}-os-service-types
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-os-service-types
Summary: Python library for consuming OpenStack sevice-types-authority data
Requires: python3
Requires: python3-pbr >= 2.0.0
Provides: python3-os-service-types = %{epoch}:%{version}-%{release}
Provides: python3dist(os-service-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-os-service-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(os-service-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-os-service-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(os-service-types) = %{epoch}:%{version}-%{release}

%description -n python3-os-service-types
The OpenStack Service Types Authority contains information about
official OpenStack services and their historical service-type aliases.

%files -n python3-os-service-types
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-os-service-types
Summary: Python library for consuming OpenStack sevice-types-authority data
Requires: python3
Requires: python3-pbr >= 2.0.0
Provides: python3-os-service-types = %{epoch}:%{version}-%{release}
Provides: python3dist(os-service-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-os-service-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(os-service-types) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-os-service-types = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(os-service-types) = %{epoch}:%{version}-%{release}

%description -n python3-os-service-types
The OpenStack Service Types Authority contains information about
official OpenStack services and their historical service-type aliases.

%files -n python3-os-service-types
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
