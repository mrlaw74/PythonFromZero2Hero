#!/usr/bin/env python
#* ***************************************************************************************
# FILE: TMLResutReport.py
# AUTHOR: Nguyen Van Luat
# DESCRIPTION: This script purposes to report daily TML TCs on 3 Jenkins servers
#*****************************************************************************************

import os
import re
import argparse
from datetime import date
import shutil
import smtplib
from email.mime.text import MIMEText
import email.utils

TODAY = date.today()
MAX_ACCEPT_FAILED = 15
MAX_ACCEPT_LOGIN_FAILED = 3
NAME_OVERVIEW_FILE = "HmiBase_TMLTest_overview.html"

# HI Server
DOMAIN_MAINPAGE_HI = "https://rbcm-jen-hmib.hi.de.bosch.com:8443/"
DOMAIN_G3G_HI = DOMAIN_MAINPAGE_HI + "userContent/nightly_builds/nb_w_cmdgen3_tmlmain_check/"
DOMAIN_G4G_HI = DOMAIN_MAINPAGE_HI + "userContent/nightly_builds/nb_w_cmdgen4_tmlmain_check/"
URL_G3G_HI = DOMAIN_G3G_HI
URL_G4G_HI = DOMAIN_G4G_HI
URL_TML_OVERVIEW_G3G_HI = DOMAIN_G3G_HI + NAME_OVERVIEW_FILE
URL_TML_OVERVIEW_G4G_HI = DOMAIN_G4G_HI + NAME_OVERVIEW_FILE

# HI2 Server
DOMAIN_G3G_HI2 = "https://hi-z0iv1.hi.de.bosch.com:8443/userContent/nightly_builds/nb_w_cmdgen3_tmlmain_check/"
DOMAIN_G4G_HI2 = "https://hi-z0iv1.hi.de.bosch.com:8443/job/nb_w_cmdgen4_tmlmain_check/ws/"
URL_G3G_HI2 = DOMAIN_G3G_HI2
URL_G4G_HI2 = DOMAIN_G4G_HI2
URL_TML_OVERVIEW_G3G_HI2 = DOMAIN_G3G_HI2 + NAME_OVERVIEW_FILE
URL_TML_OVERVIEW_G4G_HI2 = DOMAIN_G4G_HI2 + NAME_OVERVIEW_FILE

# India Server
DOMAIN_G3G_INDI = "https://rbcm-jen-hmib.kor.apac.bosch.com:8443/job/nb_w_cmdgen3_tmlmain_check/ws/"
DOMAIN_G4G_INDI = "https://rbcm-jen-hmib.kor.apac.bosch.com:8443/job/nb_w_cmdgen4_tmlmain_check/ws/"
URL_G3G_INDI = DOMAIN_G3G_INDI
URL_G4G_INDI = DOMAIN_G4G_INDI
URL_TML_OVERVIEW_G3G_INDI = DOMAIN_G3G_INDI + NAME_OVERVIEW_FILE
URL_TML_OVERVIEW_G4G_INDI = DOMAIN_G4G_INDI + NAME_OVERVIEW_FILE

# TODO: Config the absolute path to directory of these config file
CONFIG_RECEIVER = "/home/nul3hc/Personal/TML_TCs_Report/TMLReportScript/Configure_Receiver.txt"
DEFAULT_RECEIVER = "/home/nul3hc/Personal/TML_TCs_Report/TMLReportScript/Default_Receiver.txt"

class URL():
    def init(self, userName, password, url, server, gentype):
        self.password = password # Password e.g: xxxxx
        self.url = url # Url of the file link to download
        self.server = server # Jenkins servers e.g India, Hi, ...
        self.userName = userName # User name e.g: pvh3hc
        self.gentype = gentype # e.g gen 3 or gen 4

# Parse log file to get all TCs and their status
def parseLogFile(resultLogFile):
    dictOfTCs = {}
    dictIssue = {}
    isIssueDetail = False
    cSearchTestName = re.compile(r'.<td\sclass="tdTestName">(.)</td>.')
    cSearchTestStatus = re.compile(r'.<td\sclass="(tdPassed|tdFailed|tdUnknown)">(passed|failed|aborted|unknown)</td>.')
    cSearchBlockFailure = re.compile(r'.RefStep.endconditions.failure'')
    cSearchScreenshotCompareIssue = re.compile(r'.AppHmi_Test_04#.__C__diff.png.')
    cSearchPreconditionIssue = re.compile(r'.[ERROR] The as precondition required App:.')
    cSearchConnectionIssue = re.compile(r'.[WARNING] Connection failed:.')
    cSearchGetAndVerifyIssue = re.compile(r'.Error: For widget property.')
    cSearchReachSceneIssue = re.compile(r'.*[ViewVerifyStep] 'current view is AppHmi_Test_.Failed.')
    cSearchGetScreenshotIssue = re.compile(r'.*getScreenShotWidget01' : Failed')
    cSearchMissingTraceIssue = re.compile(r'.ERROR] Message 'SBTestAppClient.')
    try:
        with open(resultLogFile, encoding='windows-1252') as f:
            TCStatus = ''
            TCName = ''
            for line in f:
                match = cSearchTestName.search(line)
                if match is not None:
                    TCName = str(match.group(1))
                    continue
                match = cSearchTestStatus.search(line)
                if match is not None:
                    TCStatus = str(match.group(2))
                    dictOfTCs[TCName] = TCStatus
                    continue
                ######### TODO: Add more type of issue inside block here #####
                match = cSearchScreenshotCompareIssue.search(line)
                if match is not None:
                    isIssueDetail = True
                    dictIssue[TCName] = "Screenshot compare issue"
                    continue
                match = cSearchPreconditionIssue.search(line)
                if match is not None:
                    isIssueDetail = True
                    dictIssue[TCName] = "The as precondition required App: '/opt/bosch/base/bin/apphmi_tuner_reference-g3g_out.out' is not running"
                    continue
                match = cSearchConnectionIssue.search(line)
                if match is not None:
                    isIssueDetail = True
                    dictIssue[TCName] = "Connection failed issue"
                    continue
                match = cSearchGetAndVerifyIssue.search(line)
                if match is not None:
                    isIssueDetail = True
                    dictIssue[TCName] = "Get and verify property issue"
                    continue
                match = cSearchReachSceneIssue.search(line)
                if match is not None:
                    isIssueDetail = True
                    dictIssue[TCName] = "Reaching scene issue"
                    continue
                match = cSearchGetScreenshotIssue.search(line)
                if match is not None:
                    isIssueDetail = True
                    dictIssue[TCName] = "Getting screenshot issue"  
                    continue
                match = cSearchMissingTraceIssue.search(line)
                if match is not None:
                    isIssueDetail = True
                    dictIssue[TCName] = "Missing trace message from Screen Broker"
                    continue
                ######### End Block Issue ##############
                match = cSearchBlockFailure.search(line)
                if match is not None and isIssueDetail is True:
                    isIssueDetail = False
                elif match is not None and isIssueDetail is False:
                    dictIssue[TCName] = "Cannot define issue"
        f.close()
    except OSError:
        print('cannot open', resultLogFile)
        print("Can not open result log file here, Check download step !!!")
        exit()
    return dictOfTCs, dictIssue

def collectTMLResultContent(listFailedTCs, listAbortedTCs, listUnknownTCs, urlObj, isTMLRun, dayStopRun, listReportIssue,
isPassWord, isDownload):
content = f"In {urlObj.server} Jenkins, "
if isPassWord is False:
content += f"{urlObj.gentype} did not have result because of a login error, check user and password again.
"
return content
if isDownload is False:
content += f"{urlObj.gentype} did not have result because of an error related to downloading the log file on the server.
"
return content
if isTMLRun is False:
content += f"{urlObj.gentype} did not have result from {dayStopRun}.
"
return content
content += f"there is/are {str(len(listFailedTCs))} failed test case(s) for {urlObj.gentype}. "
if len(listFailedTCs) >= MAX_ACCEPT_FAILED:
content += f"
So many failed TCs. Please help check and analyze the main issue. ({urlObj.url} )"
elif len(listFailedTCs) > 0 and len(listFailedTCs) < MAX_ACCEPT_FAILED:
for i in range(len(listFailedTCs)):
content += f"
- {str(listFailedTCs[i])}: {listReportIssue[i]}"
content += f"
Please help check: ({urlObj.url} )"
if listAbortedTCs:
content += f"
There is/are {str(len(listAbortedTCs))} aborted test case(s) for {urlObj.gentype}.
"
content += " - "
for i in range(len(listAbortedTCs)):
content += str(listAbortedTCs[i]) + ", "
content += f"
Please help check: ({urlObj.url} )"
if listUnknownTCs:
content += f"
There is/are {str(len(listUnknownTCs))} unknown test case(s) for {urlObj.gentype}."
content += "
- "
for i in range(len(listUnknownTCs)):
content += str(listUnknownTCs[i]) + ", "
content += f"
Please help check: ({urlObj.url} )"
content += "
"
return content

def groupTCsByStatusFromDict(dictSource, status):
listResult = []
listOfItems = dictSource.items() # return an iterable sequence of all key value pairs in dictionary
for item in listOfItems:
if item[1] == status:
listResult.append(item[0])
return listResult

def collectDetailIssue(listNameFailedTCS, dictIssue):
listIssue = []
listOfItems = dictIssue.items()
for i in listNameFailedTCS:
for item in listOfItems:
if item[0] == i:
listIssue.append(item[1])
break
return listIssue

def downloadZipResultFile(urlObj):
pathToServer = os.path.join("/tmp/", urlObj.server)
if os.path.isdir(pathToServer) is False:
os.mkdir(pathToServer)
# Clean dir and make new dir
shutil.rmtree(pathToServer)
os.mkdir(pathToServer)
tar_dir = f"{pathToServer}/log{urlObj.gentype}.zip"
command = f"curl -u {urlObj.userName}:'{urlObj.password}' --insecure {urlObj.url} --output {tar_dir}"
print(urlObj.url)
try:
os.system(command)
except OSError as error:
print(error.message)
exit()
## unzip all .zip file
commandExtract = f"7z x /tmp/{urlObj.server}/log{urlObj.gentype}.zip -y -o{pathToServer}"
os.system(commandExtract)

def sendMail(userID, password, content, isReceiverConfig):
# TODO: update DEFAULT_RECEIVE file if there is any change in your team.
receiver = []
if isReceiverConfig:
for line in open(CONFIG_RECEIVER).readlines():
receiver.append(line.strip())
else:
for line in open(DEFAULT_RECEIVER).readlines():
receiver.append(line.strip())
mailobj = smtplib.SMTP('rb-owa.apac.bosch.com', 587)
mailobj.ehlo()
mailobj.starttls()
mailobj.login(userID + '@bosch.com', password)
msg = MIMEText(content, 'html')
msg['Subject'] = '[HMIB][TEST] TML run failed; ' + str(TODAY)
msg['To'] = '; '.join(receiver)
msg['From'] = email.utils.formataddr(('Jenkins HMIBase', 'HMIBase.Jenkins@bcn.bosch.com'))
## TODO: This hardcode for the sender is our HMIBase server, need to config this first argument as needed
mailobj.sendmail('HMIBase.Jenkins@bcn.bosch.com', receiver, msg.as_string())
mailobj.quit()

def initUrlLogFile(urlObj):
version, isTMLRun, dayGetReport = parseOverviewFile(f"/tmp/overview_file/{urlObj.server}TMLoverview{urlObj.gentype}.html")
url = urlObj.url
url += f"{version}/tml_logfiles.zip"
return isTMLRun, url, dayGetReport

def downloadOverviewFile(urlObj, option = ""):
pathToDir = os.path.join("/tmp/", "overview_file")
if os.path.isdir(pathToDir) is False:
os.mkdir(pathToDir)
# Clean Dir before download new files
for f in os.listdir(pathToDir):
os.remove(os.path.join(pathToDir, f))
# command = f"curl -u {urlObj.userName}:'{urlObj.password}'{option} {urlObj.url}
# --output /tmp/overview_file/{urlObj.server}TMLoverview{urlObj.gentype}.html"
command = f"curl -u {urlObj.userName}:'{urlObj.password}'{option} {urlObj.url}
--output /tmp/overview_file/{urlObj.server}TMLoverview{urlObj.gentype}.html"
print(urlObj.url)
try:
os.system(command)
except OSError as error:
print(error.message)
exit()
for filename in os.listdir(pathToDir):
html = os.path.join(pathToDir, filename)
return html

This function will return if genX of serverX is run or not via isRun.
def parseOverviewFile(overViewFile):
searchTestName = r'^.tr> (\d.)\s((\d{4}-\d{2}-\d{2}).*'
versonResult = ''
isTMLRun = False
dayGetReport = ''
# pathToDir = os.path.join("/tmp/", "overview_file")
# for f in os.listdir(pathToDir):
# os.remove(os.path.join(pathToDir, f))
try:
with open(overViewFile, 'r') as f:
for line in f:
match = re.search(searchTestName, line)
if match is not None:
if str(match.group(2)) == str(TODAY):
versonResult += str(match.group(1))
isTMLRun = True
break
else:
dayGetReport = str(match.group(2))
break
# If it still do not get any TML result or has not finish running yet,
# it will return did not have result from lastest day of result.
if isTMLRun == False:
print("There is no new verson from " + dayGetReport)
f.close()
except:
print("Can not open overview log file here. Check download step !!!")
exit()
return versonResult, isTMLRun, dayGetReport

def checkOverviewFile(overviewFile):
checkCredential = r'.(Error 401 Unauthorized).' # Check user and password of local computer.
checkContent = r'.tr> (\d.)\s((.)).' # Check if files downloaded have necessary content.
noContent = 0
isPassWord = True
isDownload = True
with open(overviewFile, 'r') as f:
for line in f:
match = re.search(checkCredential, line)
if match is not None:
print("User or Password is wrong! Please check: " + overviewFile)
isPassWord = False
break
match = re.search(checkContent, line)
if match is not None:
noContent += 1
f.close()
if isPassWord is True and noContent is 0:
print("Content of overview file is Null !! Check download step file: " + overviewFile)
isDownload = False
# isDownload = False
return isPassWord, isDownload

def parserArgument():
parser = argparse.ArgumentParser()
parser.add_argument('--p', type=str, help='Password of your userid computer', required=True)
parser.add_argument('--u', type=str, help='UserID of your computer', required=True)
parser.add_argument('-a', '--all', help='Download zip file and HTML of 3 servers', action="store_true")
parser.add_argument('-g', '--hi', help='Download zip file from HI Jenkins', action="store_true")
parser.add_argument('-l', '--hi2', help='Download zip file from HI2 Jenkins', action="store_true")
parser.add_argument('-i', '--indi', help='Download HTML file from India Jenkins', action="store_true")
parser.add_argument('-r', '--receiver', help='Use Config_Receiver.txt for configuring receiver', action="store_true")
return parser.parse_args()

def getEmailContent(urlLog, urlOverview):
listOfFailedTCs = []
listOfAbortedTCs = []
listOfUnknownTCs = []
dictAllIssue = {}
listIssue = []
numberOfLogin = 0
html = downloadOverviewFile(urlOverview, ' --insecure')
isPassWord, isDownload = checkOverviewFile(html)
# Try to log in 3 times more if the login to the Jenkins server issue occurs
while isPassWord is False and numberOfLogin < MAX_ACCEPT_LOGIN_FAILED:
html = downloadOverviewFile(urlOverview, ' --insecure')
isPassWord, isDownload = checkOverviewFile(html)
print(f"Login failed, try again: {numberOfLogin+1}. \n")
numberOfLogin += 1
pathToLogFile = f"/tmp/{urlLog.server}/{urlLog.gentype}_AutoTestSummary.log.html"
isTMLRun, url, dayGetReport = initUrlLogFile(urlLog)
urlLog.url = url
if isTMLRun is True:
downloadZipResultFile(urlLog)
dictAllTCs, dictAllIssue = parseLogFile(pathToLogFile)
listOfFailedTCs = groupTCsByStatusFromDict(dictAllTCs, 'failed')
listOfAbortedTCs = groupTCsByStatusFromDict(dictAllTCs, 'aborted')
listOfUnknownTCs = groupTCsByStatusFromDict(dictAllTCs, 'unknown')
listIssue = collectDetailIssue(listOfFailedTCs, dictAllIssue)
content = collectTMLResultContent(listOfFailedTCs, listOfAbortedTCs, listOfUnknownTCs, urlLog, isTMLRun, dayGetReport,
listIssue, isPassWord, isDownload)
return content

if name == "main":
content = ""
gen_3 = 'G3G'
gen_4 = 'G4G'
try:
args = parserArgument()
except Exception as error:
print(error.message)
exit()
userName = args.u
password = args.p
# HI Jenkins
urlLogG3GHi = URL(userName, password, URL_G3G_HI, 'HI', gen_3)
urlOverviewG3GHi = URL(userName, password, URL_TML_OVERVIEW_G3G_HI, 'HI', gen_3)
urlLogG4GHi = URL(userName, password, URL_G4G_HI, 'HI', gen_4)
urlOverviewG4GHi = URL(userName, password, URL_TML_OVERVIEW_G4G_HI, 'HI', gen_4)
# HI2 Jenkins
urlLogG3GHi2 = URL(userName, password, URL_G3G_HI2, 'HI2', gen_3)
urlOverviewG3GHi2 = URL(userName, password, URL_TML_OVERVIEW_G3G_HI2, 'HI2', gen_3)
urlLogG4GHi2 = URL(userName, password, URL_G4G_HI2, 'HI2', gen_4)
urlOverviewG4GHi2 = URL(userName, password, URL_TML_OVERVIEW_G4G_HI2, 'HI2', gen_4)
# INDIA Jenkins
urlLogG3GIn = URL(userName, password, URL_G3G_INDI, 'INDIA', gen_3)
urlOverviewG3GIn = URL(userName, password, URL_TML_OVERVIEW_G3G_INDI, 'INDIA', gen_3)
urlLogG4GIn = URL(userName, password, URL_G4G_INDI, 'INDIA', gen_4)
urlOverviewG4GIn = URL(userName, password, URL_TML_OVERVIEW_G4G_INDI, 'INDIA', gen_4)
print("Start main job!")
if args.hi:
content += getEmailContent(urlLogG3GHi, urlOverviewG3GHi)
content += getEmailContent(urlLogG4GHi, urlOverviewG4GHi)
elif args.hi2:
content += getEmailContent(urlLogG3GHi2, urlOverviewG3GHi2)
content += getEmailContent(urlLogG4GHi2, urlOverviewG4GHi2)
elif args.indi:
content += getEmailContent(urlLogG3GIn, urlOverviewG3GIn)
content += getEmailContent(urlLogG4GIn, urlOverviewG4GIn)
elif args.all:
content += getEmailContent(urlLogG3GHi, urlOverviewG3GHi)
content += getEmailContent(urlLogG4GHi, urlOverviewG4GHi)
content += '
'
content += getEmailContent(urlLogG3GHi2, urlOverviewG3GHi2)
content += getEmailContent(urlLogG4GHi2, urlOverviewG4GHi2)
content += '
'
content += getEmailContent(urlLogG3GIn, urlOverviewG3GIn)
content += getEmailContent(urlLogG4GIn, urlOverviewG4GIn)
else:
print("run 'python TMLResultReport.py -h' for more instructions!")
# Please check carefuly the "mail.To" step to send to the right people
sendMail(userName, password, content, args.receiver)

Created by: HMI Base Script TMLResultReport.py, Version: 1.0