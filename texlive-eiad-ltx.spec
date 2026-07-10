%global tl_name eiad-ltx
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	LaTeX support for the eiad font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eiad
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros to support use of the eiad fonts in OT1
encoding. Also offered are a couple of Metafont files described in the
font package, but not provided there.

