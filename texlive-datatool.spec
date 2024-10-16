Name:		texlive-datatool
Version:	52663
Release:	2
Summary:	Tools to load and manipulate data
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datatool
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datatool.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datatool.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datatool.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tools comprise six packages: datatool.sty: databases may be
created using LaTeX commands or by importing external files;
they may be sorted numerically or alphabetically; repetitive
operations (such as mail merging) may be performed on each row
of a database, subject to conditions to exclude particular
rows; commands are provided to examine database elements, and
to convert formats (for example, to convert a numeric element
to a format compatible with the fp package; datapie.sty: a
database may be represented as a pie chart; flexible options
allow colouring of the chart, and annotation hooks are
available; dataplot.sty: a database may be represented as a 2-
dimensional scatter or line plot; flexible options control of
the plot's overall appearance, and of legends and other extra
information; databar.sty: a database may be represented as a
bar chart; overall appearance, colouring and annotation are
controllable; datagidx.sty: provides a way of indexing or
creating glossaries/lists of acronyms that uses TeX to do the
sorting and collating instead of using an external indexing
application, such as xindy or makeindex; databib.sty: a
bibliography may be loaded into a datatool database, and
manipulated there before being printed (this permits a LaTeX-
based route to printing bibliographies in formats for which no
BibTeX style is available); and person.sty: provides support
for displaying a person's name and pronoun in a document, thus
avoiding cumbersome use of "he/she", etc. The drawing packages
make use of PGF/TikZ for their output. The bundle replaces and
supersedes the author's csvtools bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/datatool
%{_texmfdistdir}/tex/latex/datatool
%doc %{_texmfdistdir}/doc/latex/datatool
#- source
%doc %{_texmfdistdir}/source/latex/datatool

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
