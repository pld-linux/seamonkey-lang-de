%define	_lang	de
%define	_reg	AT
%define	_lare	%{_lang}-%{_reg}
Summary:	German resources for SeaMonkey
Summary(pl):	Niemieckie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-%{_lang}
Version:	1.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	4f5f5dea2bfe18e84a80657152e1ef20
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-%{_lang}-0.9x.xpi
# Source1-md5:	a6d521392385d55d9de6dbe093def72c
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
%setup -q -c
%{__unzip} -o -qq %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-DE}.jar \
	> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{%{_reg},%{_lare},%{_lang}-unix,enigmail-DE}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults dictionaries searchplugins $RPM_BUILD_ROOT%{_datadir}/seamonkey
rm $RPM_BUILD_ROOT%{_datadir}/seamonkey/dictionaries/LICENSE.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_reg}.jar
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-DE.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/messenger/%{_reg}
%{_datadir}/seamonkey/defaults/profile/%{_reg}
%{_datadir}/seamonkey/dictionaries/*
