#Quickly converts a switchbru chunk to a package entry.
import json, os, sys

input = {
            "category": "tool", 
            "binary": "/switch/SimpleModManager/SimpleModManager.nro", 
            "updated": "25/10/2019", 
            "name": "SimpleModManager", 
            "license": "GPLv3", 
            "title": "SimpleModManager", 
            "url": "https://github.com/nadrino/SimpleModManager/releases", 
            "author": "nadrino", 
            "changelog": "1.3.0\\n\\nAdding multiple presets in config file\\nPossibility to swap preset during the app execution with \"Y\"\\n\\n1.2.0\\n\\nAdding the possibility to change destination folder (Feature Request)\\nAdding parameter file reading (Initiated by kowbot, thanks !)\\nChanging keybinding\\nFixing bugs\\nCosmetics changes\\n\\n1.1.0\\n\\nCompiled with latest libnx (Compatible with 9.0.0)\\nFew changes in the ui\\nMinor bug fix\\n\\n1.0.0\\n\\nTested on Nintendo Switch Firmware : 8.1.0 and 9.0.0", 
            "extracted": 985, 
            "version": "1.3.0", 
            "filesize": 372, 
            "web_dls": 9, 
            "details": "SimpleModManager is an homebrew app for the Nintendo Switch CFW : Atmosphere. It allows to manage your mods (via LayeredFS).\\n\\nAt the ROOT of your SDcard, there is a /mods/ folder.\\n\\nTree structure :\\n\\n/mods/<NameOfTheGame>/<NameOfTheMod>/<ModTreeStructureFromAtmosphereFolder>\\n\\nExample :\\n\\n /mods/The Legend of Zelda - Breath of the Wild/First Person View/titles/01007EF00011E000/romfs/Actor/Pack/GameRomCamera.sbactorpack", 
            "description": "A Simple Game Mod Manager"
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

with open(os.path.join(pkgdir, "package.json"), mode='w+') as packagefile:
	json.dump(output, packagefile, indent=4)

print(json.dumps(output, indent =4))