#!/bin/bash
# Script to create kafka-0.8.0.tar.gz for rpm build
echo "This script requires: unzip, git, wget and tar"
echo "[*] Removing existing.."
rm kafka-0.8.0.tar.gz tmp3212312 &>/dev/null
mkdir tmp3212312
cd tmp3212312
echo "[*] Getting copy of release from dist.apache.org"
wget -L https://dist.apache.org/repos/dist/release/kafka/kafka_2.8.0-0.8.0-beta1.tgz -O kafka_2.8.0-0.8.0-beta1.tar.gz
echo "[*] Untaring tar file"
tar zxf kafka_2.8.0-0.8.0-beta1.tar.gz
echo "[*] Creating .tar.gz"
mv kafka_2.8.0-0.8.0-beta1 kafka-0.8.0
tar -czf ../kafka-0.8.0.tar.gz kafka-0.8.0
cd .. && rm -rf tmp3212312
