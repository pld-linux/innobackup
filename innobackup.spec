%include	/usr/lib/rpm/macros.perl
Summary:	InnoDB Hot Backup
Summary(pl):	Gor±cy backup InnoDB
Name:		ibbackup
Version:	3.0.0
Release:	1.1
License:	restricted (http://www.innodb.com/hotbackuplicense.php) / GPL v2 (innobackup)
Group:		Applications/Databases
# Source0Download:	http://www.innodb.com/order.php
Source0:	%{name}.gz
# NoSource0-md5:	dc2c361ed2c9af01b189e3b11b9d3bc2
NoSource:	0
Source1:	http://www.innodb.com/innobackup.txt
# Source1-md5:	50c91492fd85838598761476712dea3b
Source2:	%{name}.conf
URL:		http://www.innodb.com/
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl
InnoDB Hot Backup to idealne rozwi±zanie dla tworzenia w czasie
rzeczywistym kopii zapasowych tabel w MySQL oraz zestawiania
replikacji. Umo¿liwia tworzenie kopii zapasowych dzia³aj±cej bazy
danych InnoDB pod MySQL-em bez ustawiania ¿adnych blokad czy
przeszkadzania w normalnym przetwarzaniu baz danych. Otrzymuje siê
spójn± kopiê bazy danych, tak, jakby by³a wykonana w dok³adnym punkcie
w czasie. InnoDB Hot Backup to tak¿e idealna metoda zestawiania nowych
serwerów podrzêdnych w przypadku u¿ywania replikacji MySQL-a na
tabelach InnoDB.

Dokumentacja programu dostêpna jest pod
<http://www.innodb.com/manual.php>.

%prep
%setup -q -c -T
gzip -dc %{SOURCE0} > %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}/ibbackup
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/innobackup
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ibbackup
%attr(755,root,root) %{_bindir}/innobackup
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ibbackup.conf
