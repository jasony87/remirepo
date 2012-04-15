Name:           perl-FusionInventory-Agent-Task-NetDiscovery
Version:        2.1
Release:        1%{?dist}
Summary:        Network discovery support for FusionInventory Agent
License:        GPLv2+
Group:          Development/Libraries

URL:            http://forge.fusioninventory.org/projects/fusioninventory-agent-task-netdiscovery
Source0:        http://search.cpan.org/CPAN/authors/id/F/FU/FUSINV/FusionInventory-Agent-Task-NetDiscovery-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Module::Install)
# For tests
BuildRequires:  perl(FusionInventory::Agent) >= 2.2.0
BuildRequires:  perl(Net::SNMP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Compile)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(FusionInventory::Agent) >= 2.2.0
Requires:       perl(XML::SAX)
# Optional (but recommended) dependencies
Requires:       perl(Net::SNMP)
Requires:       perl(Net::NBName)
Requires:       nmap

%{?perl_default_filter}


%description
This module scans your networks to get information from devices with
SNMP protocol.


%prep
%setup -q -n FusionInventory-Agent-Task-NetDiscovery-%{version}


%build
perl Makefile.PL \
     PREFIX=%{_prefix} \
     SYSCONFDIR=%{_sysconfdir}/fusioninventory \
     LOCALSTATEDIR=%{_localstatedir}/lib/%{name}

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README THANKS
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/SNMP.pm
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/NetDiscovery.pm
%{_datadir}/fusioninventory/lib/FusionInventory/Agent/Task/NetDiscovery
%{_mandir}/man3/FusionInventory*


%changelog
* Sun Apr 15 2012 Remi Collet <remi@fedoraproject.org> - 2.1-1
- update to 2.1 for agent 2.2.0
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-Task-NetDiscovery-2.1/Changes

* Sat May 28 2011 Remi Collet <Fedora@famillecollet.com> 1.5-2
- add dependency on perl(XML::SAX)

* Mon May  9 2011 Remi Collet <Fedora@famillecollet.com> 1.5-1
- update to 1.5
  http://cpansearch.perl.org/src/FUSINV/FusionInventory-Agent-Task-NetDiscovery-1.5/Changes

* Wed Mar 30 2011 Remi Collet <Fedora@famillecollet.com> 1.4-1
- update to 1.4

* Wed Mar 30 2011 Remi Collet <Fedora@famillecollet.com> 1.3-1
- update to 1.3

* Mon Aug 16 2010 Remi Collet <Fedora@famillecollet.com> 1.2-1
- update to 1.2

* Mon May 17 2010 Remi Collet <Fedora@famillecollet.com> 1.1-1
- Specfile autogenerated by cpanspec 1.78.
- spec cleanup

