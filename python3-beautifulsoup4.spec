Name:           python3-beautifulsoup4
Version:        4.13
Release:        1
Summary:        HTML/XML Parser for Quick-Turnaround Applications Like Screen-Scraping
License:        MIT
Group:          Development/Languages/Python
BuildArch:	noarch
Requires:	python3-base
Url:            http://www.crummy.com/software/BeautifulSoup/
Source:         https://www.crummy.com/software/BeautifulSoup/bs4/download/%{version}/beautifulsoup4-%{version}.3-py3-none-any.whl

%description
Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

%prep

%build

%install
# install whl file into python dir
mkdir -p %{buildroot}/usr/lib/python3.8/site-packages
unzip -d %{buildroot}/usr/lib/python3.8/site-packages %{_sourcedir}/beautifulsoup4-%{version}.3-py3-none-any.whl

%files
%defattr(-,root,root)
/usr/lib/python3.8/site-packages/*

%changelog

