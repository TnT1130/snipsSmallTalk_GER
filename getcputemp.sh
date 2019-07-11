#!/bin/bash
tm=`/opt/vc/bin/vcgencmd measure_temp` 
tc=`echo $tm| cut -d '=' -f2 | sed 's/..$//'` 
echo $tc