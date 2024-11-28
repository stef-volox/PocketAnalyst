ONLY WORKS FOR MacOS!!!

1.0. 	Please have all prerequisite libraries for Python installed— see imports in .py files.
1.1.	It is recommended to rename folder to something simple like 'PocketAnalyst'

2.0. 	Populate yellow boxes in Numbers file.
2.1. 	For growth rate, if you do not have an exact value it’s recommended to look at industry wide 	averages. I recommend Dr. Damodar’s sector CAGRS: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafilehistgr.html
	2.2 Please use figures in millions where requested to.

3.0. 	Export to CSV when finished with Numbers file.
3.1. 	Create a file for each table when prompted.
3.2. 	DO NOT include table names when exporting to CSV.

4.0. 	Edit .py file with according PATH file locations and save otherwise it will not work.

5.0. 	Open Automator and click ‘Open an Existing Document’ then select valuation.py
5.1. 	Ensure shell is on ‘/bin/zsh’
5.2. 	Write in the field (make sure to change PATH location with yours):z
		pip3 install pandas rich pillow reportlab
		python3 /YOUR_PATH/PocketAnalyst/valuation.py

5.0. 	Click PocketAnalyst and it will print a PDF file with a score and summary for the given stock.
5.1.	Known issue with PocketAnalyst not being allowed by MacOS to open. Try Right-click + Open. If that doesn't work either, you can still print the PDF with the Value Score by opening PocketAnalyst.app in Automator and pressing run.

6.0.	For PocketDCF.sh to work you must follow a few steps:
6.1.	You must enter Terminal and type in (ensure you type in your PATH location):
		>> cd /YOUR_PATH/PocketAnalyst
		>> chmod +x PocketDCF.sh
6.2.	In case of malfunctioning, check PythonDCF.sh contains this:
		#!/bin/bash
		cd "$(dirname "$0")"  # Navigate to the script's directory
		open -a Terminal ./PocketDCF.py  # Open the Python script in Terminal
6.3.	If MacOS won't let you open PocketDCF.sh, Right-click + Open.