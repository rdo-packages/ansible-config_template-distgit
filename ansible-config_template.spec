%{!?upstream_version: %global upstream_version %{commit}}
%global commit 8a9b9622d5225177891bf0fa14b4b37b8c5fb379
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }

%global srcname ansible-config_template

Name:           %{srcname}
Version:        1.1.1
Release:        2%{?alphatag}%{?dist}
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
* Mon Oct 18 2021 Joel Capitao <jcapitao@redhat.com> - 1.1.1-2.8a9b9622git
- Update to post 1.1.1 (8a9b9622d5225177891bf0fa14b4b37b8c5fb379)
