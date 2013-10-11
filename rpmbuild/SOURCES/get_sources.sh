#!/bin/bash
# Script to create kafka-0.8.0.tar.gz for rpm build
echo "This script requires: unzip, git, wget and tar"
echo "[*] Removing existing.."
rm kafka-0.8.0.tar.gz tmp3212312 &>/dev/null
mkdir tmp3212312
cd tmp3212312
echo "[*] Getting copy of trunk from github"
wget -L https://github.com/apache/kafka/archive/trunk.zip -O trunk.zip
echo "[*] Unzipping zip file"
unzip trunk.zip
echo "[*] Creating .tar.gz"
mv kafka-trunk kafka-0.8.0
tar -czf ../kafka-0.8.0.tar.gz kafka-0.8.0
cd .. && rm -rf tmp3212312
