Kafka RPM build README
Author: Mark Poole <mpoole@apache.org>

If you don't already have development tools installed:
$ yum groupinstall "Development Tools"

You will need to download and install the JDK from the oracle website:
http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html
and install:
$ rpm -ivh jdk-7u17-linux-x64.rpm

Grab the latest Kafka source from github (from within the rpmbuild directory):
$ cd SOURCES
$ ./get_sources.sh

Build the RPM (from within the rpmbuild directory):
$ rpmbuild -bb SPECS/kafka.spec

After the compilation you will have an RPM in rpmbuild/RPMS/$arch/
