

list1 =  ["192.168.50.1","192.168.50.2","192.168.50.3","192.168.50.4","192.168.50.5","192.168.50.6","192.168.50.7","192.168.50.10","192.168.50.11","192.168.50.12","192.168.50.13","192.168.50.14","192.168.50.15","192.168.50.16","192.168.50.17","192.168.50.18","192.168.50.20","192.168.50.21","192.168.50.22","192.168.50.22","192.168.50.23","192.168.50.25","192.168.50.26","192.168.50.27","192.168.50.29","192.168.50.31","192.168.50.34","192.168.50.41","192.168.50.42","192.168.50.43","192.168.50.44","192.168.50.47","192.168.50.49","192.168.50.50","192.168.50.51","192.168.50.54","192.168.50.67","192.168.50.102","192.168.50.103","192.168.50.104","192.168.50.105","192.168.50.106","192.168.50.124","192.168.50.125","192.168.50.126","192.168.50.132","192.168.50.134","192.168.50.135","192.168.50.157","192.168.50.171","192.168.50.173","192.168.50.181","192.168.50.182",'192.168.50.183','192.168.50.184','192.168.50.185','192.168.50.186','192.168.50.187','192.168.50.191',"192.168.50.203","192.168.50.204","192.168.50.205","192.168.50.207","192.168.50.208","192.168.50.209","192.168.50.210","192.168.50.216","192.168.50.217","192.168.50.219","192.168.50.226","192.168.50.227","192.168.50.228","192.168.50.239","192.168.50.240","192.168.50.242","192.168.50.245","192.168.50.246","192.168.50.253","192.168.51.2","192.168.51.46","192.168.51.48"] 
list2 =  ["192.168.52.2","192.168.52.221","192.168.52.222","192.168.52.223","192.168.52.229","192.168.70.2","192.168.70.3","192.168.70.4","192.168.70.6","192.168.70.7","192.168.70.8","192.168.70.9","192.168.70.10","192.168.70.24","192.168.70.44","192.168.70.132","192.168.70.200","192.168.70.201","192.168.70.243","192.168.70.244","192.168.80.251"]
print(len(list1), len(list2))
list1.extend(list2)
list1 = list(set(list1))
list1.sort()
print(list1)



