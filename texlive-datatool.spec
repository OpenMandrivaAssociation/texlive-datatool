# revision 31588
# category Package
# catalog-ctan /macros/latex/contrib/datatool
# catalog-date 2013-09-06 14:59:23 +0200
# catalog-license lppl
# catalog-version 2.18
Name:		texlive-datatool
Version:	2.18
Release:	2
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
The tools comprise six packages: - datatool.sty: databases may
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
controllable; - datagidx.sty: provides a way of indexing or
creating glossaries/lists of acronyms that uses TeX to do the
sorting and collating instead of using an external indexing
application, such as xindy or makeindex; - databib.sty: a
bibliography may be loaded into a datatool database, and
manipulated there before being printed (this permits a LaTeX-
based route to printing bibliographies in formats for which no
BibTeX style is available); and - person.sty: provides support
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
%{_texmfdistdir}/bibtex/bst/datatool/databib.bst
%{_texmfdistdir}/tex/latex/datatool/databar.sty
%{_texmfdistdir}/tex/latex/datatool/databib.sty
%{_texmfdistdir}/tex/latex/datatool/datagidx.sty
%{_texmfdistdir}/tex/latex/datatool/datapie.sty
%{_texmfdistdir}/tex/latex/datatool/dataplot.sty
%{_texmfdistdir}/tex/latex/datatool/datatool-base.sty
%{_texmfdistdir}/tex/latex/datatool/datatool-fp.sty
%{_texmfdistdir}/tex/latex/datatool/datatool-pgfmath.sty
%{_texmfdistdir}/tex/latex/datatool/datatool.sty
%{_texmfdistdir}/tex/latex/datatool/person.sty
%doc %{_texmfdistdir}/doc/latex/datatool/CHANGES
%doc %{_texmfdistdir}/doc/latex/datatool/INSTALL
%doc %{_texmfdistdir}/doc/latex/datatool/README
%doc %{_texmfdistdir}/doc/latex/datatool/datatool-code.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/datatool-user.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/datatool-user.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/data-raw-psaved.dbtex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/data-raw-saved.dbtex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/data-raw.dbtex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/data.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/data2.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/exp25a.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/exp25b.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/exp30a.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/fruit.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/groupa.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/groupb.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/index.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/mydata.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/mynewdata.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/onecol.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/plotdata.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/polygon.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/profits.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/rawdata.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/rawdata2.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-barchart.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-barchart.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-datatooltk.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-datatooltk.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-dict.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-dict.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-gidx.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-gidx.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-glossary.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-glossary.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-index.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-index.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-mail-merge.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-mail-merge.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-piechart.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-piechart.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-sort.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-student-records.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-student-scores.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-student-scores.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-two-per-row.pdf
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample-two-per-row.tex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample3.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/sample4.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/scores2.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/semesterscores.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/students.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/studentscores.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/test-export-from-calc.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/test-missing-some-headers.csv
%doc %{_texmfdistdir}/doc/latex/datatool/samples/test-rawtex.dbtex
%doc %{_texmfdistdir}/doc/latex/datatool/samples/test-scores.csv
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
