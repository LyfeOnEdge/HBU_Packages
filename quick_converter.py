#Quickly converts a switchbru chunk to a package entry.
import json, os, sys

input = None

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

with open(os.path.join(pkgdir, "package.json"), mode='w+') as packagefile:
	json.dump(output, packagefile, indent=4)

print(json.dumps(output, indent =4))