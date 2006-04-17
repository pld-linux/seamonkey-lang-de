Summary:	German resources for SeaMonkey
Summary(pl):	Niemieckie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-de
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.de-AT.langpack.xpi
# Source0-md5:	4a941dcf13ae315a97293da31ae9cc4e
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-de-0.9x.xpi
# Source1-md5:	bc4a451a0b79cf330111fd4392d93fcf
Source2:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
German resources for SeaMonkey.

%description -l pl
Niemieckie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c -T
unzip %{SOURCE0}
unzip -o %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale chrome/{AT,de-AT,de-unix,enigmail-DE}.jar \
	> lang-de-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{AT,de-AT,de-unix,enigmail-DE}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-de-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults myspell searchplugins $RPM_BUILD_ROOT%{_datadir}/seamonkey
rm $RPM_BUILD_ROOT%{_datadir}/seamonkey/myspell/LICENSE.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/AT.jar
%{_chromedir}/de-AT.jar
%{_chromedir}/de-unix.jar
%{_chromedir}/enigmail-DE.jar
%{_chromedir}/lang-de-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/messenger/AT
%{_datadir}/seamonkey/defaults/profile/AT
%{_datadir}/seamonkey/myspell/*
