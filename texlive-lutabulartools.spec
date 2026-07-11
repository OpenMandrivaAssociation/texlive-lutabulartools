%global tl_name lutabulartools
%global tl_revision 73345

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Some useful LuaLaTeX-based tabular tools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/lutabulartools
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lutabulartools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lutabulartools.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides some useful commands for tabular matter. It uses
LuaLaTeX and offers the ability to combine the facilities of multirow
and makecell with an easy to use syntax. It also adds some enhanced
rules for the booktabs package.

