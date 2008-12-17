Summary:        Plasma applet that allow to see the weather	
Name:		plasma-applet-yawp
Version: 	0.0.6
Release: 	%mkrel 1
Source0: 	http://www.kde-look.org/CONTENT/content-files/94106-yawp-0.0.6.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.kde-look.org/content/show.php/yaWP+(Yet+Another+Weather+Plasmoid)?content=94106
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-workspace-devel >= 2:4.1.3

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

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}


