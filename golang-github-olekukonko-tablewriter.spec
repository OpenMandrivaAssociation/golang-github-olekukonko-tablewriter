# http://github.com/olekukonko/tablewriter

%global goipath         github.com/olekukonko/tablewriter
%global commit          a0225b3f23b5ce0cbec6d7a66a968f8a59eca9c4


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.11%{?dist}
Summary:        ASCII table in golang
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/mattn/go-runewidth)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENCE.md
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.gita0225b3
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gita0225b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.gita0225b3
- Bump to upstream a0225b3f23b5ce0cbec6d7a66a968f8a59eca9c4
  related: #1320304

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitcca8bbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitcca8bbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitcca8bbc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.4.gitcca8bbc
- Polish the spec file
  resolves: #1320304

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitcca8bbc
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 0-0.2.gitcca8bbc
- Bump to upstream cca8bbc0798408af109aaaa239cbd2634846b340
  resolves: #1320304

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gita5eefc2
- First package for Fedora
  resolves: #1315099

