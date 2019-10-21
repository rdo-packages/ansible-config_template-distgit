%{!?upstream_version: %global upstream_version %{commit}}
%global commit faf60ddb53dd3d345ea3644f818805a3d356b104
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git
# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global srcname ansible-config_template

Name:           %{srcname}
Version:        1.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        Ansible plugin for config template

License:        ASL 2.0
URL:            https://opendev.org/openstack/%{srcname}
Source0:        https://github.com/openstack/%{srcname}/archive/%{commit}.tar.gz#/%{srcname}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

# Handle python2 exception
%if %{pyver} == 2
Requires:       ansible
%else
Requires:       python3dist(ansible)
%endif

%description

Ansible plugin for config template

%prep
%autosetup -n %{srcname}-%{upstream_version} -S git


%build
%{pyver_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}


%files
%doc README*
%license LICENSE
%{pyver_sitelib}/ansible_config_template*.egg-info
%{_datadir}/ansible/


%changelog
* Mon Oct 21 2019 RDO <dev@lists.rdoproject.org> 1.0.0-1.faf60ddbgit.el7
- Update to post 1.0.0 (faf60ddb53dd3d345ea3644f818805a3d356b104)

