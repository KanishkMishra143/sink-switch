Name:           sink-switch
Version:        1.0
Release:        1%{?dist}
Summary:        Switch audio sinks easily (PulseAudio / PipeWire)

License:        MIT
URL:            https://github.com/KanishkMishra143/sink-switch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash, pulseaudio-utils?pipewire-pulseaudio, which

%description
Simple Bash script to switch audio sinks from the command line.

%prep
%setup -q

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 0755 sink-switch.sh %{buildroot}%{_bindir}/sink-switch

%files
Name:           sink-switch
Version:        1.0
Release:        1%{?dist}
Summary:        Switch audio sinks easily (PulseAudio / PipeWire)

License:        MIT
URL:            https://github.com/KanishkMishra143/sink-switch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash, pulseaudio-utils?pipewire-pulseaudio, which

%description
Simple Bash script to switch audio sinks from the command line.

%prep
%setup -q

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 0755 sink-switch.sh %{buildroot}%{_bindir}/sink-switch

%files
%license LICENSE
%doc README.md
%{_bindir}/sink-switch

%changelog
* Mon Oct 20 2025 Kanishk Mishra kanishk.kumar412@gmail.com - 1.0-1
- Fedora 43 release

