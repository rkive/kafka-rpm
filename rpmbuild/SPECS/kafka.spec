Summary: Kafka is a distributed publish/subscribe messaging system
Name: kafka
Version: 0.8.0
Release: 1
License: Apache (v2)
Group: Applications
Source0: kafka-%{version}.tar.gz
Source1: kafka.init
Source2: zookeeper.init
Patch0: sbt.patch
Patch1: kafka-run-class.patch
URL: http://kafka.apache.org
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Distribution: Mark Poole
Vendor: Mark Poole
Packager: Mark Poole <mark@poole.im>

Prereq: jdk >= 1.6
Requires(pre): shadow-utils

%description
It is designed to support the following

Persistent messaging with O(1) disk structures that provide constant time performance even with many TB of stored messages.
High-throughput: even with very modest hardware Kafka can support hundreds of thousands of messages per second.
Explicit support for partitioning messages over Kafka servers and distributing consumption over a cluster of consumer machines while maintaining per-partition ordering semantics.
Support for parallel data load into Hadoop.
Kafka is aimed at providing a publish-subscribe solution that can handle all activity stream data and processing on a consumer-scale web site. This kind of activity (page views, searches, and other user actions) are a key ingredient in many of the social feature on the modern web. This data is typically handled by "logging" and ad hoc log aggregation solutions due to the throughput requirements. This kind of ad hoc solution is a viable solution to providing logging data to an offline analysis system like Hadoop, but is very limiting for building real-time processing. Kafka aims to unify offline and online processing by providing a mechanism for parallel load into Hadoop as well as the ability to partition real-time consumption over a cluster of machines.

See our web site for more details on the project. (http://kafka.apache.org/)

%pre

# Create user and group
getent group kafka >/dev/null || groupadd -r kafka
getent passwd kafka >/dev/null || \
    useradd -r -g kafka -d /usr/local/kafka -s /bin/bash \
    -c "Kafka Account" kafka


exit 0

%post

# Create symlink for install directory
ln -s /usr/local/%{name}-%{version} /usr/local/kafka
chown -R kafka:kafka /var/log/zookeeper /var/log/kafka /usr/local/%{name}-%{version}



%postun
# Remove symlinks after uninstall
rm /usr/local/kafka

%prep

%setup

%patch0 -p1
%patch1 -p1

%build
# Build package

./sbt update
./sbt +package

%install
pwd
mkdir -p $RPM_BUILD_ROOT/usr/local/%{name}-%{version}
cp -r * $RPM_BUILD_ROOT/usr/local/%{name}-%{version}
cp -r .ivy2 $RPM_BUILD_ROOT/usr/local/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT/var/log/zookeeper
mkdir -p $RPM_BUILD_ROOT/var/log/kafka
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install  -m 755 %{S:1} $RPM_BUILD_ROOT/etc/rc.d/init.d/kafka
install  -m 755 %{S:2} $RPM_BUILD_ROOT/etc/rc.d/init.d/zookeeper

%files
%defattr(-,root,root)

%config %attr(755,root,root) /usr/local/%{name}-%{version}/config

/usr/local/%{name}-%{version}
/var/log/zookeeper
/var/log/kafka
/etc/rc.d/init.d/kafka
/etc/rc.d/init.d/zookeeper

%clean
#used to cleanup things outside the build area and possibly inside.
rm -rf %{buildroot}

%changelog
* Fri Mar 15 2013 Mark Poole <mpoole@apache.org>
- First build
