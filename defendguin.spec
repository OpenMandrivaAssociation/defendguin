%define name	defendguin
%define version	0.0.12
%define release	%mkrel 2
%define	Summary	A Defender Clone

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.tuxpaint.org/unix/x/defendguin/src/%{name}-%{version}.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	GPLv2 
Url:		http://newbreedsoftware.com/defendguin
Group:		Games/Arcade 
BuildRequires:	SDL_mixer-devel X11-devel alsa-lib-devel esound-devel 
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Patch0:		%{name}-0.0.11-fix-CFLAGS.patch

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
rm -rf %{buildroot}
install -d %{buildroot}{%{_gamesbindir},%{_mandir}/man6}
%make install PREFIX=%{buildroot}%{_prefix} BIN_PREFIX=%{buildroot}%{_gamesbindir} \
DATA_PREFIX=%{buildroot}%{_gamesdatadir}/%{name}/ MAN_PREFIX=%{buildroot}%{_datadir}


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus} 
%endif

%clean
rm -rf %{buildroot}

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

