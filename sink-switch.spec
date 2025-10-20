Name:           sink-switch
Version:        1.0
Release:        1%{?dist}
Summary:        Switch audio sinks (PulseAudio / PipeWire) from command line
License:        MIT
URL:            https://github.com/KanishkMishra143/sink-switch
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash, pulseaudio-utils?pipewire-pulseaudio, which

%description
Small bash utility to switch audio sinks.

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
* $(date +"%a %b %d %Y") Kanishk Mishra kanishk.kumar412@gmail.com - 1.0-1
- Update for Fedora 43

