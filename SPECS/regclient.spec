%define debug_package %{nil}

%global gh_user regclient

Name:           regclient
Version:        0.9.0
Release:        1%{?dist}
Summary:        Docker and OCI Registry Client in Go and tooling using those libraries
Group:          Applications/System
License:        Apache-2.0
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Client interface for the registry API. This includes regctl for a
command line interface to manage registries.

%prep
%setup -q -n %{name}-%{version}

%build
make fmt goimports vet test binaries
# go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/%{name}-%{version}/bin/regbot %{buildroot}%{_bindir}/regbot
install -Dm0755 %{_builddir}/%{name}-%{version}/bin/regctl %{buildroot}%{_bindir}/regctl
install -Dm0755 %{_builddir}/%{name}-%{version}/bin/regsync %{buildroot}%{_bindir}/regsync

%files
%{_bindir}/regbot
%{_bindir}/regctl
%{_bindir}/regsync

%changelog
* Tue Jul 1 2025 Jamie Curnow <jc@jc21.com> 0.9.0-1
- https://github.com/regclient/regclient/releases/tag/v0.9.0

* Thu Apr 24 2025 Jamie Curnow <jc@jc21.com> 0.8.3-1
- https://github.com/regclient/regclient/releases/tag/v0.8.3

* Tue Apr 22 2025 Jamie Curnow <jc@jc21.com> 0.8.2-1
- https://github.com/regclient/regclient/releases/tag/v0.8.2
