#Quickly converts a switchbru chunk to a package entry.
import json, os, sys

input = {
            "category": "tool", 
            "binary": "/switch/ScreenTester-NX/ScreenTester-NX.nro", 
            "updated": "16/07/2018", 
            "name": "ScreenTester", 
            "license": ".", 
            "title": "ScreenTester-NX", 
            "url": "https://github.com/Marice/ScreenTester-NX/releases", 
            "author": "marice", 
            "changelog": "n/a", 
            "extracted": 2128, 
            "version": "0.2", 
            "filesize": 493, 
            "web_dls": 143, 
            "details": "This program displays different colors to detect dead/stuck pixels on your Nintendo-Switch screen.It can cycle colors on your Switch screen very rapidly to try and repair stuck/dead pixels.", 
            "app_dls": 1030, 
            "description": "Screen Testing App"
        }



output = {
			"name": "",
			"author": "",
			"description": "",
			"install_subfolder": None,
			"pattern": [
				[
					""
				],
				""
			],
			"license": "",
			"package": "",
			"release_api": "https://api.github.com/repos//releases",
			"website": "",
			"category": "",
			"tags": [
			]
		}

table = [
		["title", "name"],
		["author", "author"],
		["details", "description"],
		["category", "category"],
		["license", "license"],
		["name", "package"],
		["url", "website"],
		["category", "category"],
	]

for pair in table:
	output[pair[1]] = input[pair[0]]

output["tags"].append(input["category"])

pkgdir = os.path.join(sys.path[0], output["package"])
if not os.path.isdir(pkgdir):
	os.mkdir(pkgdir)

with open(os.path.join(pkgdir, "package.json"), mode='w+', encoding = "utf-8") as packagefile:
	json.dump(output, packagefile, indent=4)

print(json.dumps(output, indent =4))

packages = []
for package in os.listdir(sys.path[0]):
	if os.path.isfile(os.path.join(sys.path[0], os.path.join(package, "package.json"))):
		packages.append(package)

print(json.dumps(packages, indent = 4))
with open("packages.json", mode='w+') as packagefile:
	json.dump(packages, packagefile, indent=4)

print("Found {} packages".format(len(packages)))