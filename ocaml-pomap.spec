Name:		ocaml-pomap
Version:	2.9.9
Release:        4
Summary:        Library for maintaining partially ordered maps
License:        LGPL
Group:          Development/Other
URL:		http://www.ocaml.info/home/ocaml_sources.html#pomap
Source0:	http://hg.ocaml.info/release/pomap/archive/pomap-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/pomap/archive/release-%{version}.tar.bz2 > pomap-release-%{version}.tar.bz2
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
BuildRequires:  texlive
BuildRequires:  gzip

%description
The Pomap-library implements an ADT that maintains maps of partially
ordered elements. Whereas a total order allows you to say whether some
element is lower, equal or greater than another one, partial orders also
allow for a "don't know"-case.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n pomap-release-%{version}

%build
make
make doc
gzip --best doc/pomap/latex/doc.ps

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/pomap
make install

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{_libdir}/ocaml/pomap
%{_libdir}/ocaml/pomap/META
%{_libdir}/ocaml/pomap/*.cma
%{_libdir}/ocaml/pomap/*.cmi

%files devel
%defattr(-,root,root)
%doc LICENSE Changes README.txt
%doc examples
%doc lib/doc/pomap/html
%doc lib/doc/pomap/latex/*.{dvi,ps.gz,pdf}
%{_libdir}/ocaml/pomap/*.a
%{_libdir}/ocaml/pomap/*.cmxa
%{_libdir}/ocaml/pomap/*.mli



%changelog
* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.9.9-2mdv2010.0
+ Revision: 390299
- rebuild

* Thu Jan 29 2009 Florent Monnier <blue_prawn@mandriva.org> 2.9.9-1mdv2009.1
+ Revision: 335200
- requires latex
- import ocaml-pomap


