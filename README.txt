------------------------------------------------------------------------------------------------
	ONLY WORKS FOR MacOS | Full history can be seen in 'version_history.txt'
------------------------------------------------------------------------------------------------
v.1.1.4		- Small bug fixes with negative or zero values showing up because of high terminal growth rates in 'PocketDCF.py'
		- Small updates to 'Numbers.toolkit'
------------------------------------------------------------------------------------------------

	READ ME

1.0. 	Please have all prerequisite libraries for Python installed— see imports in .py files.
1.1.	Enter terminal and input:
		pip install -r requirements.txt
1.1.	It is recommended to rename parent folder to something simple like 'PocketAnalyst'

2.0. 	Populate yellow boxes in Numbers file.
2.1. 	For growth rate, if you do not have an exact value it’s recommended to look at industry wide averages. I recommend Dr. Damodaran’s sector CAGRS: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafilehistgr.html
2.2 	Please use figures in millions where requested to.

3.0. 	Export to CSV when finished with Numbers file.
3.1. 	Create a file for each table when prompted.
3.2. 	DO NOT include table names when exporting to CSV.

4.0.	For PocketAnalyst.sh to work you must follow a few steps:
4.1.	You must enter Terminal and type in (ensure you type in your PATH location):
		cd /YOUR_PATH/PocketAnalyst
		chmod +x PocketAnalyst.sh
4.2.	In case of malfunctioning, check PocketAnalyst.sh contains this:
		#!/bin/bash
		cd "$(dirname "$0")"  # Navigate to the script's directory
		open -a Terminal ./PocketAnalyst.py
4.3.	If MacOS won't let you open PocketAnalyst.sh, Right-click + Open.
4.4.	PocketAnalyst does not take into consideration forecasted values.

5.0.	For PocketDCF.sh to work you must follow a few steps:
5.1.	You must enter Terminal and type in (ensure you type in your PATH location):
		>> cd /YOUR_PATH/PocketAnalyst
		>> chmod +x PocketDCF.sh
5.2.	In case of malfunctioning, check PocketDCF.sh contains this:
		#!/bin/bash
		cd "$(dirname "$0")"  # Navigate to the script's directory
		open -a Terminal ./PocketDCF.py
5.3.	If MacOS won't let you open PocketDCF.sh, Right-click + Open.
5.4.	You can use the forecasted values from Toolkit.numbers or your own.
5.5.	Do not use comma separators in PocketDCF

6.0.	DISCLOSURE
6.1.	'Toolkit.numbers' encompasses information, data, and numerical values for equity securities. Some of this spreadsheet’s values are forward-looking and derive from a statistical model based on quantitative data. From here onwards 'Toolkit.numbers' will be referred to as the 'spreadsheet', 'PocketAnalyst.py', 'PocketAnalyst.sh', 'PocketDCF.py', and 'PocketDCF.sh' will be referred to as the 'application/s' or 'app/s'.

6.2.	Kindly be aware that engaging in securities investments entails exposure to market and various risks. It’s important to note that there is no certainty or guarantee that the desired investment objectives will be realised. The previous performance of a security does not necessarily indicate its future performance, as it may or may not be sustained. The return on a security investment and the principal value of an investor may fluctuate, resulting in the potential for the redeemed shares to be valued either higher or lower than their initial cost. The current investment performance of a security may differ from the performance mentioned in the spreadsheet and applications.

6.3.	The completeness or accuracy of the assumptions and models used in determining certain forward-facing values is not guaranteed by the spreadsheet and apps or by Mr. Voloaca. Moreover, there is a risk that the investor’s target/s may not be achieved due to unforeseen changes, such as shifts in demand for the company's products, alterations in management, technology, economic development, interest rates, operational or material costs, competitive pressures, supervisory laws, exchange rates, tax rates, and the aforementioned risks within the report. Investments in foreign markets carry additional risks, typically tied to changes in exchange rates or shifts in political and social conditions. Any alteration in the fundamental factors underlying the quantitative equity values can result in subsequent inaccuracies in the valuation.

6.4.	This spreadsheet and apps are provided for informational purposes only and should not be the sole basis for making investment decisions. It does not take into account the specific investment objectives, financial situation, or individual needs of any particular recipient. The intention of this publication is to offer information to assist investors in making their own decisions rather than providing specific investment advice. Consequently, the discussed investments may not be suitable for all investors. Individuals are advised to exercise independent judgment regarding the suitability of such investments and recommendations based on their own investment objectives, experience, taxation status, and financial position.

6.5.	Mr. Voloaca encourages recipients of these apps and spreadsheet to thoroughly review all relevant issue documents, such as the prospectus, related to the security in question. This includes, but is not limited to, information regarding investment objectives, risks, and costs. Before making any investment decisions, and when necessary, it is recommended to seek the guidance of a financial, legal, tax, and/or accounting professional.

6.6.	Unless required by law or outlined in a separate agreement, Mr. Voloaca disclaims any responsibility or liability for trading decisions, damages, or other losses arising from or connected to the information, data, analyses, or opinions presented in the spreadsheet and/or apps. It is strongly advised that recipients of these apps and spreadsheet thoroughly review all pertinent issue documents, such as the prospectus, associated with the relevant security. This includes, but is not limited to, information concerning its investment objectives, risks, and costs. Before making any investment decisions, and as deemed necessary, individuals are encouraged to seek the guidance of legal, tax, and/or accounting professionals.

6.7.	The spreadsheet and apps and its contents are not aimed at, nor intended for the distribution to or utilisation by, any individual or entity who is a citizen, resident, or situated in any region, state, country, or other jurisdiction where such distribution, publication, availability, or utilisation would violate laws or regulations or impose registration or licensing obligations on Mr. Voloaca in that jurisdiction.

6.8.	Downloading the folder containing the spreadsheet and apps from GitHub entails that you have read and agreed to the Disclosure above.