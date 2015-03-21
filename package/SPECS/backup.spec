Name: Backup
Version: 1.0 
Release: 1 
License: GPL 
Summary: A simple backup program 

%description 
Copyright (c) 2015 Dana R Connors

%install 
mkdir -p %{_buildrootdir}/usr/local/bin
mkdir -p %{_buildrootdir}/etc
cp ../../backup.py %{_buildrootdir}/usr/local/bin/backup.py
cp ../../backup.config %{_buildrootdir}/etc/backup.config

%files 
%defattr(-,root,root) 

/usr/local/bin/backup.py
/etc/backup.config

%post
echo "56 19 * * * root /usr/bin/backup.py &" >> /var/spool/cron/root

%changelog 
* Fri Mar 20 2015 Dana R Connors <dana.connors@my.cs.coloradotech.edu>
- Original RPM build.
