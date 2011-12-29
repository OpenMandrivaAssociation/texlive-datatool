# revision 16023
# category Package
# catalog-ctan /macros/latex/contrib/datatool
# catalog-date 2009-11-15 19:44:35 +0100
# catalog-license lppl
# catalog-version 2.03
Name:		texlive-datatool
Version:	2.03
Release:	1
Summary:	Tools to load and manipulate data
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datatool
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datatool.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datatool.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datatool.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides six packages: - datatool.sty: databases may
be created using LaTeX commands or by importing external files;
they may be sorted numerically or alphabetically; repetitive
operations (such as mail merging) may be performed on each row
of a database, subject to conditions to exclude particular
rows; commands are provided to examine database elements, and
to convert formats (for example, to convert a numeric element
to a format compatible with the fp package; - datapie.sty: a
database may be represented as a pie chart; flexible options
allow colouring of the chart, and annotation hooks are
available; - dataplot.sty: a database may be represented as a
2-dimensional scatter or line plot; flexible options control of
the plot's overall appearance, and of legends and other extra
information; - databar.sty: a database may be represented as a
bar chart; overall appearance, colouring and annotation are
controllable; - databib.sty: a bibliography may be loaded into
a datatool database, and manipulated there before being printed
(this permits a LaTeX-based route to printing bibliographies in
formats for which no BibTeX style is available); and -
person.sty: provides support for displaying a person's name and
pronoun in a document, thus avoiding cumbersome use of
"he/she", etc. The drawing packages make use of PGF/TikZ for
their output. The bundle replaces and supersedes the author's
csvtools bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/datatool/databib.bst
%{_texmfdistdir}/tex/latex/datatool/databar.sty
%{_texmfdistdir}/tex/latex/datatool/databib.sty
%{_texmfdistdir}/tex/latex/datatool/datapie.sty
%{_texmfdistdir}/tex/latex/datatool/dataplot.sty
%{_texmfdistdir}/tex/latex/datatool/datatool.sty
%{_texmfdistdir}/tex/latex/datatool/person.sty
%doc %{_texmfdistdir}/doc/latex/datatool/CHANGES
%doc %{_texmfdistdir}/doc/latex/datatool/README
%doc %{_texmfdistdir}/doc/latex/datatool/datatool.pdf
#- source
%doc %{_texmfdistdir}/source/latex/datatool/datatool.dtx
%doc %{_texmfdistdir}/source/latex/datatool/datatool.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
