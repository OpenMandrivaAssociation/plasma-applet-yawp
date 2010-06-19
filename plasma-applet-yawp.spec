Summary:	Plasma applet that allow to see the weather
Name:		plasma-applet-yawp
Version:	0.3.3
Release:	%mkrel 1
Source0:	http://www.kde-look.org/CONTENT/content-files/yawp-%{version}.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php?content=94106
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	plasma-devel
BuildRequires:	kdeplasma-addons-devel
Requires:	kdebase4-runtime
Provides:   plasma-applet

%description 
Yet Another Weather Plasmoid
Plasma applet that allow to see the weather. 

%files -f plasma_applet_yawp.lang
%defattr(-,root,root)
%doc CHANGELOG COPYRIGHT LICENSE-BSD LICENSE-GPL2 LICENSE-LGPL-2 README TODO
%_kde_libdir/kde4/*.so
%_kde_appsdir/desktoptheme/default/widgets/*.svg
%_kde_datadir/kde4/services/*.desktop


#--------------------------------------------------------------------

%prep
%setup -q -n yawp-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build
%find_lang	plasma_applet_yawp
%clean
rm -rf %{buildroot}
