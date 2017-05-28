#make sure change these variables to suit your language
%define CONFLANG pt_BR
%define LOCNAME pt_BR
%define RPM_SUFFIX pt_br
%define QM_SUFFIX pt_BR

Name: unofficial-jolla-language-pack-%{RPM_SUFFIX}
Version:	2.1.0
Release:	0.0.1
Summary:	Unofficial community Portuguese (Brazil) translation for Jolla

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/pt_BR
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Wed Mar 01 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.1
- First RPM build from partially completed Pootle project
