Name:		plasma-applet-yawp
Version:	0.4.5
Release:	1
Summary:	Plasma applet that allow to see the weather
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php?content=94106
Source0:	http://downloads.sourceforge.net/project/yawp/yawp/%{version}/yawp-%{version}.tar.bz2
Patch0:		yawp-0.4.5-rus.patch
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

