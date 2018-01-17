import os
import re
import requests
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
import jenkins
import urllib2

def getHostName(ip):
    base_url = "https://192.168.132.127:9440/PrismGateway/services/rest/v1/vms/"
    requests.packages.urllib3.disable_warnings()
    s = requests.Session()
    s.auth = ('admin', 'Nutanix123!')
    s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
    vm_dict = s.get(base_url, verify=False).json()
    vm_list = list(vm_dict["entities"])
    for vm in vm_list:
        ipAddresses = (vm['ipAddresses'])
        if ip in ipAddresses:
            hostname = str(vm['vmName']).replace(' ', '_')
            return hostname

#print getHostName('192.168.132.81')

j = Jenkins('http://192.168.132.6:8080/jenkins/')


def getJobsByProductName(ProductName):
    jobs = j.get_jobs_list()
    i = 0
    for i in jobs:
        if re.search(ProductName, i, re.I):
            print i


getJobsByProductName('SON_Multibranch')

job = j['SON_Release_17.12']
lgb = job.get_last_good_build()
print lgb

jserver = jenkins.Jenkins('http://192.168.132.6:8080/jenkins/')

buildKeepStateMessage = "http://192.168.132.6:8080/jenkins/view/SON/job/SON_Multibranch/job/"+ProductName+"/"+build_number+"/"
buildKeepSup = urllib2.urlopen(buildKeepStateMessage)
buildKeep = buildKeepSup.read()
if re.search("Don't keep this build forever", buildKeep, re.I):
    print "found Don't keep this build forever, no need to keep it"
else:
    toggleMessage = "http://192.168.132.6:8080/jenkins/view/SON/job/SON_Multibranch/job/"+ProductName+"/"+build_number+"/toggleLogKeep"
    toggleSup = urllib2.urlopen(toggleMessage)
    print "Build Saved"

#v = jserver.get_build_console_output('SON_Release_17.12', 146)
#print v

#t = jserver.get_job_config('SON_Release_17.12')
#print t

# plugins = jserver.get_plugin_info()
# print plugins

#print jserver.jobs_count()