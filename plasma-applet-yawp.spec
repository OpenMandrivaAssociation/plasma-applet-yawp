Summary:        Plasma applet that allow to see the weather	
Name:		plasma-applet-yawp
Version: 	0.2.3
Release: 	%mkrel 1
Source0: 	http://www.kde-look.org/CONTENT/content-files/yawp-%{version}.tar.bz2
Patch0:     yawp-fix-cmake.patch
# SVN patches
#Patch100:	yawp-0.2.1-icon_size.patch
License: 	GPLv2+
Group: 		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php?content=94106
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	plasma-devel
Requires:       kdebase4-runtime

%description 
Yet Another Weather Plasmoid
Plasma applet that allow to see the weather. 

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_yawp.so
%_kde_appsdir/desktoptheme/default/widgets/yawp_theme13.svg
%_kde_datadir/kde4/services/plasma_yawp.desktop
%_kde_datadir/locale/*/LC_MESSAGES/*.mo

#--------------------------------------------------------------------

%prep
%setup -q -n yawp-%{version}  
#%patch0 -p1
#%patch100 -p0 -b .icon_size

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build
%clean
rm -rf %{buildroot}
