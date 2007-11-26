%define name	defendguin
%define version	0.0.11
%define release	%mkrel 3
%define	Summary	A Defender Clone

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/defendguin/defendguin-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	GPL 
Url:		http://newbreedsoftware.com/defendguin
Group:		Games/Arcade 
BuildRequires:	SDL_mixer-devel X11-devel alsa-lib-devel esound-devel 
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Patch:		%{name}-0.0.5-fix-CFLAGS.patch.bz2

%description
Defendguin is going to be a clone of the arcade game "Defender," but with a
Linux theme. Your mission is to defend little penguinoids from being captured
and mutated by... well, you know who.

%prep
%setup -q
%patch0 -p1

%build
%make CFLAGS="%{optflags}" PREFIX=%{_prefix} BIN_PREFIX=%{_gamesbindir} DATA_PREFIX=%{_gamesdatadir}/%{name}/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_gamesbindir},%{_mandir}/man6}
%make install PREFIX=$RPM_BUILD_ROOT%{_prefix} BIN_PREFIX=$RPM_BUILD_ROOT%{_gamesbindir} \
DATA_PREFIX=$RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/ MAN_PREFIX=$RPM_BUILD_ROOT%{_datadir}

install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
needs="x11" \
section="More Applications/Games/Arcade" \
title="Defendguin" \
longtitle="%{Summary}" \
command="%{_gamesbindir}/%{name}" \
icon="%{name}.png" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Defendguin
Comment=%{Summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%post
%{update_menus}

%postun
%{clean_menus} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/*/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*
%{_menudir}/%{name}
