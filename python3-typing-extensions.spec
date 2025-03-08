Name:           python3-typing-extensions
Version:        4.12.2
Release:        1
Summary:        Typing Extensions for Python
License:        Python Software Foundation License
Group:          Development/Languages/Python
BuildArch:	noarch
Requires:	python3-base
Url:            https://pypi.org/project/typing-extensions/#files
Source:         https://files.pythonhosted.org/packages/26/9f/ad63fc0248c5379346306f8668cda6e2e2e9c95e01216d2b8ffd9ff037d0/typing_extensions-4.12.2-py3-none-any.whl

%description
The typing_extensions module serves two related purposes:

Enable use of new type system features on older Python versions. For example, typing.TypeGuard is new in Python 3.10, but typing_extensions allows users on previous Python versions to use it too
Enable experimentation with new type system PEPs before they are accepted and added to the typing module.

%prep

%build

%install
# install whl file into python dir
mkdir -p %{buildroot}/usr/lib/python3.8/site-packages
unzip -d %{buildroot}/usr/lib/python3.8/site-packages %{_sourcedir}/typing_extensions-%{version}-py3-none-any.whl

%files
%defattr(-,root,root)
/usr/lib/python3.8/site-packages/*

%changelog
