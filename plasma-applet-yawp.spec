Summary:        Plasma applet that allow to see the weather	
Name:		plasma-applet-yawp
Version: 	0.0.6
Release: 	%mkrel 2
Source0: 	http://www.kde-look.org/CONTENT/content-files/94106-yawp-%{version}.tar.gz
Patch0:     yawp-fix-cmake.patch
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
%_kde_appsdir/desktoptheme/default/widgets/yawp_theme05.svg
%_kde_datadir/kde4/services/plasma_yawp.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n yaWP-%{version}  
%patch0 -p1
%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
