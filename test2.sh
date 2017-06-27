#!/bin/bash
i=0
while [ $i -lt 10 ]; do echo "hello world!"; i=`expr $i + 1` ; sleep 1s; done
