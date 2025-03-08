# python3 packages for sailfishos
Python 3 package for Sailfish OS

- beautifulsoup4
- soupsieve
- typing-extensions

## Building

SSH into SDK Build Engine (Start Build engine in Sailfish SDK)
> ssh mersdk@localhost -p 2222 -i ~/SailfishOS/vmshare/ssh/private_keys/sdk

Packaged in Salifish SDK Build Engine with following command:
> rpmbuild --undefine=_disable_source_fetch -bb python3-<package_name>.spec

Output RPM is a crossplatform noarch package  
You can find the packages <a href="https://openrepos.net/user/18370/programs">here</a>.
