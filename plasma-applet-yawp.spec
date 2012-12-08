Name:		plasma-applet-yawp
Version:	0.4.3
Release:	1
Summary:	Plasma applet that allow to see the weather
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php?content=94106
Source0:	http://downloads.sourceforge.net/project/yawp/yawp/%{version}/yawp-%{version}.tar.bz2
Patch0:		yawp-0.4.3-rus.patch
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description
Yet Another Weather Plasmoid
Plasma applet that allow to see the weather.

%files -f plasma_applet_yawp.lang
%doc CHANGELOG COPYRIGHT LICENSE-BSD LICENSE-GPL2 LICENSE-LGPL-2 README TODO
%{_kde_libdir}/kde4/*.so
%{_kde_appsdir}/desktoptheme/default/widgets/*.svg
%{_kde_services}/*.desktop


#--------------------------------------------------------------------

%prep
%setup -q -n yawp-%{version}
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang plasma_applet_yawp

%changelog
* Mon Jul 23 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.4.3-1
- New version 0.4.3

* Mon Feb 13 2012 Andrey Bondrov <abondrov@mandriva.org> 0.4.2-2
+ Revision: 773746
- Update russian translation

* Sat Jan 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.4.2-1
+ Revision: 760809
- New version 0.4.2, add patch with russian translation, spec cleanup

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-2
+ Revision: 667781
- mass rebuild

* Fri Dec 17 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.6-1mdv2011.0
+ Revision: 622663
- new version
- drop P0 (upstream)

* Fri Oct 15 2010 Funda Wang <fwang@mandriva.org> 0.3.5-2mdv2011.0
+ Revision: 585751
- rebuild

* Sat Oct 09 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.5-1mdv2011.0
+ Revision: 584476
- new version
  patch0: remove obsolete include (may be upstream)

* Wed Sep 08 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.4-2mdv2011.0
+ Revision: 576795
- patch0: update to current SVN for 4.6 support

* Sat Jul 10 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.4-1mdv2011.0
+ Revision: 550012
- new version

* Sat Jun 19 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.3-1mdv2010.1
+ Revision: 548336
- update snapshot to final release

* Sat May 22 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.3-0.svn376.1mdv2010.1
+ Revision: 545710
- update to svn376 to fix mdv#59326; delete patch1 (upstream)

* Fri Dec 11 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.2-2mdv2010.1
+ Revision: 476389
- revive patch1 again (thanks to John)

* Mon Dec 07 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 474304
- new version 0.3.2

* Mon Sep 14 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.2.3-3mdv2010.0
+ Revision: 440683
- update to svn182, mostly to get updated trasnations
  remove patch1 (pushed upstream) - thanks, John

* Mon Sep 14 2009 John Balcaen <mikala@mandriva.org> 0.2.3-2mdv2010.0
+ Revision: 440174
- Add Provides
- Fix plasma applet category

* Thu May 07 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.2.3-1mdv2010.0
+ Revision: 372992
- new version

* Wed Apr 01 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 363117
- new version 0.2.2
  * remove upstream patch100

* Mon Mar 30 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.2.1-3mdv2009.1
+ Revision: 362450
- patch100: patch from SVN (r133) to fix icon size under KDE4.2.2 and above

* Mon Mar 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2.1-2mdv2009.1
+ Revision: 362232
- Rebuild against new KDE 4.2.2

* Sat Mar 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2.1-1mdv2009.1
+ Revision: 360064
- Update to 0.2.1

* Tue Feb 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.65-1mdv2009.1
+ Revision: 337033
- Update to 0.1.65 version

* Sun Feb 01 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.0.6-3mdv2009.1
+ Revision: 335921
- rebuild with KDE 4.2

* Sat Jan 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0.6-2mdv2009.1
+ Revision: 328100
- Fix compilation against kde 4.2

  + Funda Wang <fwang@mandriva.org>
    - update url

* Wed Dec 17 2008 Funda Wang <fwang@mandriva.org> 0.0.6-1mdv2009.1
+ Revision: 315041
- only plasma is required
- import plasma-applet-yawp


* Tue Dec 16 2008 John Balcaen <john.balcaen@littleboboy.net> 0.0.6-1mdv2009.0
- import yawp
- use plasma-applet-weather spec from neoclust@mandriva.org.

