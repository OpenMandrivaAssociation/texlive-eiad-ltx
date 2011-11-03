# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eiad
# catalog-date 2007-02-06 22:00:42 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-eiad-ltx
Version:	1.0
Release:	1
Summary:	LaTeX support for the eiad font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eiad
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides macros for use of the eiad fonts in OT1 encoding. Also
offers a couple of MetaFont files described in the font
package, but not provided there.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}