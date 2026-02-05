#!/bin/bash

echo -en "Hostname, O.S, CPU, Mem, A.S, Apache,\n"  >> inventory.csv
echo -en "$(hostname),  " >> inventory.csv;
echo -en "$(cat /etc/issue|sed 's/\\n.*/\ /'), " >> inventory.csv; 
echo -en "$(cat /proc/cpuinfo| grep processor |wc -l),  " >> inventory.csv 
echo -en "$(grep MemTotal /proc/meminfo | sed 's/.*://'),  "  >> inventory.csv

AS=$(ps aux | grep -v "grep"| grep -c "jboss\|tomcat")
Apache=$(ps aux | grep -v "grep"| grep -c "apache2")

	if [ $AS -ne 0  ]; then # Check if tomcat running
		app="$(ps aux | grep java | grep -v "grep" | grep -o "tomcat\|jboss" | tail -1)"
		if test -z $app ; then
					echo -en ", "  >> inventory.csv
			else	
			if [ $app = "tomcat" ] ; then
						echo -en " tomcat, "  >> inventory.csv
			else
					echo -en "Jboss, "  >> inventory.csv
			fi
		fi
	fi
		if [ $Apache -ne 0  ]; then # Is Apache Running 
				echo -en " Y,\n" >> inventory.csv
			else
			echo -en " N,\n"  >> inventory.csv
		fi

