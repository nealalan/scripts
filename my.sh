#!/bin/bash

freespace=$(df -H / | grep -E "\/$" | awk '{print $4}')
logdate=$(date +"%Y%m%d")
logtime=$(date +"%H%M%S")
logdateUS=$(date +"%m/%d/%y")
logfile=system_report_"$logdate"_"$logtime".log
uptimeArray=$(uptime -p)
filecount=$(ls -R ~ | wc -l)
theIP=$(curl -s ifconfig.co)
GREEN="\033[32m"
BOLD="\033[1m"
NORMAL="\033[0m"


echo -e $BOLD"System report for "$GREEN$HOSTNAME$NORMAL$BOLD "on" $GREEN$logdateUS$NORMAL
printf "\tSystem type:\t%s\n" $MACHTYPE
printf "\tBash Version:\t%s\n" $BASH_VERSION
printf "\tUptime:\t\t%s\n" "${uptimeArray[*]}"
printf "\tFree Space:\t%s\n" $freespace
printf "\tFiles in ~:\t%s\n" $filecount
printf "\tPublic IP:\t%s\n" $theIP
echo -e "\n$BOLD""A summary of this info has been saved to: $GREEN$logfile$NORMAL"

cat <<- EOF > $logfile
	This report was automatically generated by a bash script.
	It contains a brief summary of some system information.

EOF

echo -e "System report for $HOSTNAME on $logdateUS" >> $logfile
printf "\tSystem type:\t%s\n" $MACHTYPE >> $logfile
printf "\tBash Version:\t%s\n" $BASH_VERSION >> $logfile
printf "\tUptime:\t\t%s\n" "${uptimeArray[*]}" >> $logfile
printf "\tFree Space:\t%s\n" $freespace >> $logfile
printf "\tFiles in ~:\t%s\n" $filecount >> $logfile
printf "\tPublic IP:\t%s\n" $theIP >> $logfile

