#!/bin/bash

HOSTNAME=localhost
SCRIPT="/usr/local/hadoop/bin/hdfs namenode -format; /usr/local/hadoop/sbin/start-dfs.sh"

ssh ${HOSTNAME} "${SCRIPT}"
