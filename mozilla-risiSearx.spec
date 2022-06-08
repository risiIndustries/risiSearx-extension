# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global moz_extensions %{_datadir}/mozilla/extensions

%global ext_id searx@risi.io

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}

Name:           mozilla-risiSearx
Version:        1.0
Release:        1%{?dist}
Summary:        SearXNG instance for risiOS

License:        GPLv3+
URL:            https://searx.risi.io
Source0:        https://github.com/risiOS/risiSearx-extension/releases/download/%{version}/%{version}.xpi
Requires:       mozilla-filesystem
BuildArch:      noarch

%description
Sets default search engine to risiSearx

%prep
%setup

%build
echo Nothing to build

%install
install -Dpm644 %{SOURCE0} %{buildroot}%{firefox_inst_dir}/%{ext_id}.xpi

%files
%license LICENSE
%{firefox_inst_dir}/%{ext_id}.xpi

%changelog
%autochangelog

