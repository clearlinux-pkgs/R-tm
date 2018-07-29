#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tm
Version  : 0.7.5
Release  : 15
URL      : https://cran.r-project.org/src/contrib/tm_0.7-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tm_0.7-5.tar.gz
Summary  : Text Mining Package
Group    : Development/Tools
License  : GPL-3.0
Requires: R-tm-lib
Requires: R-BH
Requires: R-NLP
Requires: R-SnowballC
Requires: R-slam
Requires: R-xml2
BuildRequires : R-BH
BuildRequires : R-NLP
BuildRequires : R-SnowballC
BuildRequires : R-slam
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-tm package.
Group: Libraries

%description lib
lib components for the R-tm package.


%prep
%setup -q -c -n tm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532892844

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1532892844
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tm/CITATION
/usr/lib64/R/library/tm/DESCRIPTION
/usr/lib64/R/library/tm/INDEX
/usr/lib64/R/library/tm/Meta/Rd.rds
/usr/lib64/R/library/tm/Meta/data.rds
/usr/lib64/R/library/tm/Meta/features.rds
/usr/lib64/R/library/tm/Meta/hsearch.rds
/usr/lib64/R/library/tm/Meta/links.rds
/usr/lib64/R/library/tm/Meta/nsInfo.rds
/usr/lib64/R/library/tm/Meta/package.rds
/usr/lib64/R/library/tm/Meta/vignette.rds
/usr/lib64/R/library/tm/NAMESPACE
/usr/lib64/R/library/tm/NEWS.Rd
/usr/lib64/R/library/tm/R/tm
/usr/lib64/R/library/tm/R/tm.rdb
/usr/lib64/R/library/tm/R/tm.rdx
/usr/lib64/R/library/tm/data/acq.rda
/usr/lib64/R/library/tm/data/crude.rda
/usr/lib64/R/library/tm/doc/extensions.R
/usr/lib64/R/library/tm/doc/extensions.Rnw
/usr/lib64/R/library/tm/doc/extensions.pdf
/usr/lib64/R/library/tm/doc/index.html
/usr/lib64/R/library/tm/doc/tm.R
/usr/lib64/R/library/tm/doc/tm.Rnw
/usr/lib64/R/library/tm/doc/tm.pdf
/usr/lib64/R/library/tm/ghostscript/pdf_info.ps
/usr/lib64/R/library/tm/help/AnIndex
/usr/lib64/R/library/tm/help/aliases.rds
/usr/lib64/R/library/tm/help/paths.rds
/usr/lib64/R/library/tm/help/tm.rdb
/usr/lib64/R/library/tm/help/tm.rdx
/usr/lib64/R/library/tm/html/00Index.html
/usr/lib64/R/library/tm/html/R.css
/usr/lib64/R/library/tm/libs/symbols.rds
/usr/lib64/R/library/tm/stopwords/SMART.dat
/usr/lib64/R/library/tm/stopwords/catalan.dat
/usr/lib64/R/library/tm/stopwords/danish.dat
/usr/lib64/R/library/tm/stopwords/dutch.dat
/usr/lib64/R/library/tm/stopwords/english.dat
/usr/lib64/R/library/tm/stopwords/finnish.dat
/usr/lib64/R/library/tm/stopwords/french.dat
/usr/lib64/R/library/tm/stopwords/german.dat
/usr/lib64/R/library/tm/stopwords/hungarian.dat
/usr/lib64/R/library/tm/stopwords/italian.dat
/usr/lib64/R/library/tm/stopwords/norwegian.dat
/usr/lib64/R/library/tm/stopwords/portuguese.dat
/usr/lib64/R/library/tm/stopwords/romanian.dat
/usr/lib64/R/library/tm/stopwords/russian.dat
/usr/lib64/R/library/tm/stopwords/spanish.dat
/usr/lib64/R/library/tm/stopwords/swedish.dat
/usr/lib64/R/library/tm/texts/acq/reut-00001.xml
/usr/lib64/R/library/tm/texts/acq/reut-00002.xml
/usr/lib64/R/library/tm/texts/acq/reut-00003.xml
/usr/lib64/R/library/tm/texts/acq/reut-00004.xml
/usr/lib64/R/library/tm/texts/acq/reut-00005.xml
/usr/lib64/R/library/tm/texts/acq/reut-00006.xml
/usr/lib64/R/library/tm/texts/acq/reut-00007.xml
/usr/lib64/R/library/tm/texts/acq/reut-00008.xml
/usr/lib64/R/library/tm/texts/acq/reut-00009.xml
/usr/lib64/R/library/tm/texts/acq/reut-00010.xml
/usr/lib64/R/library/tm/texts/acq/reut-00011.xml
/usr/lib64/R/library/tm/texts/acq/reut-00012.xml
/usr/lib64/R/library/tm/texts/acq/reut-00013.xml
/usr/lib64/R/library/tm/texts/acq/reut-00014.xml
/usr/lib64/R/library/tm/texts/acq/reut-00015.xml
/usr/lib64/R/library/tm/texts/acq/reut-00016.xml
/usr/lib64/R/library/tm/texts/acq/reut-00017.xml
/usr/lib64/R/library/tm/texts/acq/reut-00018.xml
/usr/lib64/R/library/tm/texts/acq/reut-00020.xml
/usr/lib64/R/library/tm/texts/acq/reut-00021.xml
/usr/lib64/R/library/tm/texts/acq/reut-00022.xml
/usr/lib64/R/library/tm/texts/acq/reut-00023.xml
/usr/lib64/R/library/tm/texts/acq/reut-00024.xml
/usr/lib64/R/library/tm/texts/acq/reut-00025.xml
/usr/lib64/R/library/tm/texts/acq/reut-00026.xml
/usr/lib64/R/library/tm/texts/acq/reut-00027.xml
/usr/lib64/R/library/tm/texts/acq/reut-00028.xml
/usr/lib64/R/library/tm/texts/acq/reut-00029.xml
/usr/lib64/R/library/tm/texts/acq/reut-00030.xml
/usr/lib64/R/library/tm/texts/acq/reut-00031.xml
/usr/lib64/R/library/tm/texts/acq/reut-00032.xml
/usr/lib64/R/library/tm/texts/acq/reut-00034.xml
/usr/lib64/R/library/tm/texts/acq/reut-00035.xml
/usr/lib64/R/library/tm/texts/acq/reut-00036.xml
/usr/lib64/R/library/tm/texts/acq/reut-00039.xml
/usr/lib64/R/library/tm/texts/acq/reut-00040.xml
/usr/lib64/R/library/tm/texts/acq/reut-00042.xml
/usr/lib64/R/library/tm/texts/acq/reut-00043.xml
/usr/lib64/R/library/tm/texts/acq/reut-00045.xml
/usr/lib64/R/library/tm/texts/acq/reut-00046.xml
/usr/lib64/R/library/tm/texts/acq/reut-00047.xml
/usr/lib64/R/library/tm/texts/acq/reut-00048.xml
/usr/lib64/R/library/tm/texts/acq/reut-00049.xml
/usr/lib64/R/library/tm/texts/acq/reut-00050.xml
/usr/lib64/R/library/tm/texts/acq/reut-00051.xml
/usr/lib64/R/library/tm/texts/acq/reut-00052.xml
/usr/lib64/R/library/tm/texts/acq/reut-00053.xml
/usr/lib64/R/library/tm/texts/acq/reut-00054.xml
/usr/lib64/R/library/tm/texts/acq/reut-00055.xml
/usr/lib64/R/library/tm/texts/acq/reut-00056.xml
/usr/lib64/R/library/tm/texts/crude/reut-00001.xml
/usr/lib64/R/library/tm/texts/crude/reut-00002.xml
/usr/lib64/R/library/tm/texts/crude/reut-00004.xml
/usr/lib64/R/library/tm/texts/crude/reut-00005.xml
/usr/lib64/R/library/tm/texts/crude/reut-00006.xml
/usr/lib64/R/library/tm/texts/crude/reut-00007.xml
/usr/lib64/R/library/tm/texts/crude/reut-00008.xml
/usr/lib64/R/library/tm/texts/crude/reut-00009.xml
/usr/lib64/R/library/tm/texts/crude/reut-00010.xml
/usr/lib64/R/library/tm/texts/crude/reut-00011.xml
/usr/lib64/R/library/tm/texts/crude/reut-00012.xml
/usr/lib64/R/library/tm/texts/crude/reut-00013.xml
/usr/lib64/R/library/tm/texts/crude/reut-00014.xml
/usr/lib64/R/library/tm/texts/crude/reut-00015.xml
/usr/lib64/R/library/tm/texts/crude/reut-00016.xml
/usr/lib64/R/library/tm/texts/crude/reut-00018.xml
/usr/lib64/R/library/tm/texts/crude/reut-00019.xml
/usr/lib64/R/library/tm/texts/crude/reut-00021.xml
/usr/lib64/R/library/tm/texts/crude/reut-00022.xml
/usr/lib64/R/library/tm/texts/crude/reut-00023.xml
/usr/lib64/R/library/tm/texts/custom.xml
/usr/lib64/R/library/tm/texts/loremipsum.txt
/usr/lib64/R/library/tm/texts/rcv1_2330.xml
/usr/lib64/R/library/tm/texts/reuters-21578.xml
/usr/lib64/R/library/tm/texts/txt/ovid_1.txt
/usr/lib64/R/library/tm/texts/txt/ovid_2.txt
/usr/lib64/R/library/tm/texts/txt/ovid_3.txt
/usr/lib64/R/library/tm/texts/txt/ovid_4.txt
/usr/lib64/R/library/tm/texts/txt/ovid_5.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tm/libs/tm.so
/usr/lib64/R/library/tm/libs/tm.so.avx2
/usr/lib64/R/library/tm/libs/tm.so.avx512
