%global packname  ipred
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.1
Release:          1
Summary:          Improved Predictors
Group:            Sciences/Mathematics
License:          GPL
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/ipred_0.9-1.tar.gz

Requires:         R-rpart R-MASS R-mlbench R-survival R-nnet R-class 
Requires:         R-mvtnorm 
Requires:         R-prodlim
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-rpart R-MASS R-mlbench R-survival R-nnet R-class
BuildRequires:    R-mvtnorm 
BuildRequires:    R-prodlim

%description
Improved predictive models by indirect classification and bagging for
classification, regression and survival problems as well as resampling
based estimators of prediction error.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.8_11-1
+ Revision: 775920
- Import R-ipred
- Import R-ipred


