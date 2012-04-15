Name:           perl-POE-Component-Client-Ping
Version:        1.171
Release:        1%{?dist}
Summary:        Non-blocking ICMP ping client
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/POE-Component-Client-Ping/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RC/RCAPUTO/POE-Component-Client-Ping-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE) >= 1.007
BuildRequires:  perl(Test::More)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(POE) >= 1.007

%{?perl_default_filter}


%description
POE::Component::Client::Ping is non-blocking ICMP ping client. It lets
several other sessions ping through it in parallel, and it lets them
continue doing other things while they wait for responses.

%prep
%setup -q -n POE-Component-Client-Ping-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
make test


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES README
%{perl_vendorlib}/POE
%{_mandir}/man3/*


%changelog
* Sun Apr 15 2012 Remi Collet <remi@fedoraproject.org> - 1.171-1
- Specfile autogenerated by cpanspec 1.78.
