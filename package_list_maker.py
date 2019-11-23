import os, sys, json

packages = []
for package in os.listdir(sys.path[0]):
	if os.path.isfile(os.path.join(sys.path[0], os.path.join(package, "package.json"))):
		packages.append(package)

print(json.dumps(packages, indent = 4))
with open("packages.json", mode='w+') as packagefile:
	json.dump(packages, packagefile, indent=4)

print("Found {} packages".format(len(packages)))