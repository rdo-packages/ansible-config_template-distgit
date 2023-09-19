%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087

%global srcname ansible-config_template

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{srcname}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Ansible plugin for config template

License:        ASL 2.0
URL:            https://opendev.org/openstack/%{srcname}
Source0:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  ansible-packaging

Requires:       (python3dist(ansible) or ansible-core >= 2.11)

%description

Ansible plugin for config template

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n ansible-config_template-%{upstream_version}
sed -i -e 's/version:.*/version: %{version}/' galaxy.yml
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
rm -vrf releasenotes/ examples/ tests/ .gitreview .gitignore doc/

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%doc README*
%license LICENSE

%changelog
* Tue Sep 19 2023 RDO <dev@lists.rdoproject.org> 2.0.0-1
- Update to 2.0.0


