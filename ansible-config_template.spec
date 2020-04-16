
%global srcname ansible-config_template

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{srcname}
Version:        XXX
Release:        XXX
Summary:        Ansible plugin for config template

License:        ASL 2.0
URL:            https://opendev.org/openstack/%{srcname}
Source0:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3dist(ansible)

%description

Ansible plugin for config template

%prep
%autosetup -n %{srcname}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/ansible_config_template*.egg-info
%{_datadir}/ansible/


%changelog
