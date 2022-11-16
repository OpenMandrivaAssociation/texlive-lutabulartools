Name:		texlive-lutabulartools
Version:	64780
Release:	1
Summary:	Some useful LuaLaTeX-based tabular tools
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lutabulartools
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lutabulartools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lutabulartools.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some useful commands for tabular matter.
It uses LuaLaTeX and offers the ability to combine the
facilities of multirow and makecell with an easy to use syntax.
It also adds some enhanced rules for the booktabs package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/lutabulartools
%doc %{_texmfdistdir}/doc/luatex/lutabulartools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
