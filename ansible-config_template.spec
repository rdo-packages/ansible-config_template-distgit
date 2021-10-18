%{!?upstream_version: %global upstream_version %{commit}}
%global commit bd7543a73681f16e20d5562291b8f545fc4fb904
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }

%global srcname ansible-config_template

Name:           %{srcname}
Version:        1.2.1
Release:        1%{?alphatag}%{?dist}
Summary:        Ansible plugin for config template

License:        ASL 2.0
URL:            https://opendev.org/openstack/%{srcname}
Source0:        https://github.com/openstack/%{srcname}/archive/%{commit}.tar.gz#/%{srcname}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       (python3dist(ansible) or ansible-core >= 2.11)

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
* Fri Apr 15 2022 Joel Capitao <jcapitao@redhat.com> - 1.2.1-1.bd7543a7git
- Update to post 1.2.1 (bd7543a73681f16e20d5562291b8f545fc4fb904)
