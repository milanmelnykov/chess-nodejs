import os,subprocess, json
data = subprocess.check_output("aws elb describe-load-balancers", shell=True)
json_data = json.loads(data)
for lb in json_data['LoadBalancerDescriptions']:
    if(lb['ListenerDescriptions'][0]['Listener']['LoadBalancerPort'] == 8081):
        print(lb['DNSName'])
