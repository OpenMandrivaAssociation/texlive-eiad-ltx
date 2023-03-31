Name:		texlive-eiad-ltx
Version:	15878
Release:	2
Summary:	LaTeX support for the eiad font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eiad
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides macros for use of the eiad fonts in OT1 encoding. Also
offers a couple of MetaFont files described in the font
package, but not provided there.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/eiad-ltx/Fbf10.mf
%{_texmfdistdir}/fonts/source/public/eiad-ltx/Fr10.mf
%{_texmfdistdir}/tex/latex/eiad-ltx/eiad.sty
%doc %{_texmfdistdir}/doc/latex/eiad-ltx/README
#- source
%doc %{_texmfdistdir}/source/latex/eiad-ltx/eiad.dtx
%doc %{_texmfdistdir}/source/latex/eiad-ltx/eiad.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
