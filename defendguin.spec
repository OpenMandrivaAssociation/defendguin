%define name	defendguin
%define version	0.0.12
%define release	%mkrel 3
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
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL-devel
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



%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.0.12-3mdv2011.0
+ Revision: 635155
- tighten BR

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.12-2mdv2011.0
+ Revision: 610226
- rebuild

* Tue Dec 08 2009 Jérôme Brenier <incubusss@mandriva.org> 0.0.12-1mdv2010.1
+ Revision: 474630
- new version 0.0.12
- fix source url

* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 0.0.11-6mdv2010.0
+ Revision: 384579
- rediff and don't compress CFLAGS patch
- add patch number
- fix license
- clean spec file

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.0.11-5mdv2009.0
+ Revision: 244024
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.0.11-3mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import defendguin


* Thu Aug 24 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.0.11-3mdv2007.0
- fix summary macro used in menu item
- don't bzip2 icons

* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 0.0.11-2mdv2007.0
- switch to XDG menu

* Mon Jan 30 2006 Lenny Cartier <lenny@mandriva.com> 0.0.11-1mdk
- 0.0.11

* Tue Oct 11 2005 Pixel <pixel@mandriva.com> 0.0.10-5mdk
- rebuild

* Fri Jan  2 2004 Pixel <pixel@mandrakesoft.com> 0.0.10-4mdk
- rebuild

* Tue Nov 12 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.0.10-3mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Opps, forgot to specify full datapath in build stage
	- Use correct macro; _datadir/games -> _gamesdatadir

* Mon Nov 11 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 0.0.10-2mdk
- Fix icons, did'nt show up, made them transparent
- Put stuff in the right places
- Removed obsolete Prefix tag
- Cleanups

* Wed Sep 18 2002 Götz Waschk <waschk@linux-mandrake.com> 0.0.10-1mdk
- fix menu group
- fix file permissions for rpmlint
- quiet tar
- used spec file from Charles A Edwards <eslrahc@bellsouth.net>
  - 0.0.10
  - Remove requires for TiMidity++
  - Add Mandrake menu
  - Add icons

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.0.9-4mdk
- rebuild

* Sun Jul 21 2002 Pixel <pixel@mandrakesoft.com> 0.0.9-3mdk
- recompile against new vorbis stuff

* Mon Apr 29 2002 Pixel <pixel@mandrakesoft.com> 0.0.9-2mdk
- rebuild for new libasound (alsa)

* Sat Feb  2 2002 Pixel <pixel@mandrakesoft.com> 0.0.9-1mdk
- new release

* Sat Jan 19 2002 Stefan van der Eijk <stefan@eijk.nu> 0.0.6-8mdk
- BuildRequires

* Thu Sep 13 2001 Stefan van der Eijk <stefan@eijk.nu> 0.0.6-7mdk
- BuildRequires: libSDL-devel XFree86-devel

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 0.0.6-6mdk
- add requires TiMidity++

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 0.0.6-5mdk
- rebuild

* Mon May 14 2001 Pixel <pixel@mandrakesoft.com> 0.0.6-4mdk
- rebuild with new SDL

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0.0.6-3mdk
- rebuild for new libSDL_mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0.0.6-2mdk
- rebuild, build req

* Sun Nov 26 2000 Pixel <pixel@mandrakesoft.com> 0.0.6-1mdk
- new version

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.0.5-3mdk
- capitalize summary

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.0.5-2mdk
- rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.0.5-1mdk
- initial spec
