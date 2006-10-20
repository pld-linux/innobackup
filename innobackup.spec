Summary:	InnoDB Hot Backup
Name:		ibbackup
Version:	3.0.0
Release:	1
License:	restricted (http://www.innodb.com/hotbackuplicense.php)
Group:		Applications/Databases
Source0:	%{name}.gz
# Source0-md5:	dc2c361ed2c9af01b189e3b11b9d3bc2
URL:		http://www.innodb.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
InnoDB Hot Backup is the ideal solution for online backups of InnoDB
tables in MySQL - and for setting up replication. It allows you to
back up a running InnoDB database under MySQL without setting any
locks or disturbing normal database processing. You get a consistent
copy of your database, as if the copy were taken at a precise point in
time. InnoDB Hot Backup is also the ideal method of setting up new
slaves if you use the MySQL replication on InnoDB tables.

The program documentation is available at
<http://www.innodb.com/manual.php>.

%prep
%setup -q -c -T
gzip -dc %{SOURCE0} > %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ibbackup
