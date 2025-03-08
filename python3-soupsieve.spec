Name:           python3-soupsieve
Version:        2.6
Release:        1
Summary:        CSS selector library for BeautifulSoup4
License:        MIT
Group:          Development/Languages/Python
BuildArch:	noarch
Requires:	python3-base
Url:            https://pypi.org/project/soupsieve/#files
Source:         https://files.pythonhosted.org/packages/d1/c2/fe97d779f3ef3b15f05c94a2f1e3d21732574ed441687474db9d342a7315/soupsieve-2.6-py3-none-any.whl

%description
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4. It aims to provide selecting, matching, and filtering using modern CSS selectors. Soup Sieve currently provides selectors from the CSS level 1 specifications up through the latest CSS level 4 drafts and beyond (though some are not yet implemented).

%prep

%build

%install
# install whl file into python dir
mkdir -p %{buildroot}/usr/lib/python3.8/site-packages
unzip -d %{buildroot}/usr/lib/python3.8/site-packages %{_sourcedir}/soupsieve-%{version}-py3-none-any.whl

%files
%defattr(-,root,root)
/usr/lib/python3.8/site-packages/*

%changelog
