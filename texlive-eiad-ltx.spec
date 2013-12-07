# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eiad
# catalog-date 2007-02-06 22:00:42 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-eiad-ltx
Version:	1.0
Release:	6
Summary:	LaTeX support for the eiad font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eiad
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eiad-ltx.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751388
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718315
- texlive-eiad-ltx
- texlive-eiad-ltx
- texlive-eiad-ltx
- texlive-eiad-ltx

