# PythonFromZero2Hero
#!/bin/sh
export PASSWORD="VNserverHmi)$)%2022"
# output=$(python3 /home/jeh8hc/samba/views/ci_tools/rbcm-jen-hmib/tml/TMLReportScript/TMLResultReport.py --u jeh8hc --p "$PASSWORD" -a)
output=$(python3 /home/nul3hc/Personal/TML_TCs_Report/TMLReportScript/TMLTCsReport.py --u jeh8hc --p "$PASSWORD" -a)
echo $output > /tmp/TML_report_log_`date +\%Y-\%m-\%d_\%H\%M`.log 2>&1
# python3 ./TMLResultReport.py --u jeh8hc --p "VNserverHmi)$)%2022" -a

# m h  dom mon dow   command
#27 14 * * * /usr/bin/python3 /home/jeh8hc/samba/views/ci_tools/rbcm-jen-hmib/tml/TMLReportScript/TMLResultReport.py --u jeh8hc --p "VNserverHmi)$)%2022" -a -r > /tmp/TML_report_log_`date +\%Y-\%m-\%d_\%H\%M`.log 2>&1
#30 09 * * * /usr/bin/python3 /home/jeh8hc/Desktop/TMLResultReport/TMLResultReport.py --u jeh8hc --p "VNserverHmi)$)%2022" -a > /tmp/TML_report_log_`date +\%Y-\%m-\%d_\%H\%M`.log 2>&1
#30 11 * * * rm /tmp/overview_file/*
03 10 * * * /bin/bash /home/jeh8hc/samba/views/ci_tools/rbcm-jen-hmib/tml/TMLReportScript/callCron.sh
30 7 * * * /bin/bash /data/jeh8hc/lsim/callDownloadLsim.sh
