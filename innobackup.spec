%include	/usr/lib/rpm/macros.perl
Summary:	Perl script which automates the backup of both MyISAM and InnoDB tables
Summary(pl.UTF-8):	Skrypt Perla automatyzujący tworzenie kopii zapasowych tabel MyISAM i InnoDB
Name:		innobackup
Version:	1.5.2
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://www.innodb.com/download/%{name}-%{version}
# Source0-md5:	859eda702913228709c0f843c2884405
URL:		http://www.innodb.com/hot-backup/
# http://bugs.mysql.com/bug.php?id=40351
Patch0:		%{name}-engine-archive.patch
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	ibbackup
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
InnoDB Hot Backup is the ideal solution for online backups of InnoDB
tables in MySQL - and for setting up replication. It allows you to
back up a running InnoDB database under MySQL without setting any
locks or disturbing normal database processing. You get a consistent
copy of your database, as if the copy were taken at a precise point in
time. InnoDB Hot Backup is also the ideal method of setting up new
slaves if you use the MySQL replication on InnoDB tables.

innobackup is a Perl script which automates the backup of both MyISAM
and InnoDB type tables and .frm files. It is an adaptable front-end
for ibbackup.

%description -l pl.UTF-8
InnoDB Hot Backup to idealne rozwiązanie dla tworzenia w czasie
rzeczywistym kopii zapasowych tabel w MySQL oraz zestawiania
replikacji. Umożliwia tworzenie kopii zapasowych działającej bazy
danych InnoDB pod MySQL-em bez ustawiania żadnych blokad czy
przeszkadzania w normalnym przetwarzaniu baz danych. Otrzymuje się
spójną kopię bazy danych, tak, jakby była wykonana w dokładnym punkcie
w czasie. InnoDB Hot Backup to także idealna metoda zestawiania nowych
serwerów podrzędnych w przypadku używania replikacji MySQL-a na
tabelach InnoDB.

innobackup to skrypt Perla automatyzujący tworzenie kopii zapasowych
tabel typu MyISAM i InnoDB oraz plików .frm. Jest to adaptowalny
frontend dla programu ibbackup.

%prep
%setup -q -c -T
cp -a %{SOURCE0} %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/innobackup
