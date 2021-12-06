# SIPbuilderGUI
1. [Installation](#installation)
2. [Deploying](#tdeploying)
3. [Errors and Notes](#errors-and-notes)
## Instalation
***
some preinstalled libraries are required.
To install python libraries go to  command line (cmd)
```
cd Y:\ndha\pre-deposit_prod\SIPbuilderGUI 
```
(This folder could be different depends on how it is mapped)
It is also could be cloned from GitHub repository:
```
git clone https://github.com/nlnzcollservices/SIPbuilderGUI
```
Then enter repository and via the command line type
```
pip install -r requirements.txt
```

## Deploying
***

To run the app just go to  the “script” folder and run the “SIP_GUI.py” script. 
It will open the submission form.

![SIP_builder1](/documentation/SIP_builder1.PNG)

### “Main details” tab fields description:
This data populates the dc and mets.xml files.
1.	Library system:
The default setting is Alma you can switch the radio button for Tiaki.
Enter your system record ID number in the corresponding field.
2.	DC title:
 Will be displayed in the dc.xml.
3.	SIP title:
Will be displayed as name of your SIP folder.
4.	Entity type:
You can use small arrows “up” and ”down” to scrall entity types and then click to select and you will ick the appropriate entity type for your submission.
(New ones can be added. Open the script in an editor. Find this line value_list  = ["WebHarvestIE","OneOffIE","AudioIE","PeriodicIE",
"VideoIE","HTMLSerialIE","HTMLMonoIE","UnpublishedIE",""]
And add your entity type inside squared brackets, after coma and in quotes, save and it will appear the next time the app is run.
5.	Policy ID:
Policy rights access code - change to 100, 200,300,400 as required
6.	 File or Folder:
If  your SIP will have one file use “Single file” radio button and select your file using the “FileBrowse” button
If your SIP will have multiple files in a folder switch the radio button to “folder” and use  “FolderBrowse” button to select the folder
7.	Output folder:
Use the “FolderBrowse” button to select the folder where you want your SIP to be built.
8.	Designation field:
Used for non web-archive publications – It you are creating a one-time IEs or a web archives these field can be empty and will be ignored.


![SIP_builder1](/documentation/SIP_builder1.PNG)

### “Web and User” tab fields description:
Used for building SIPs for Web archives or specifying the user or project name in METS.  

1.	Web Archive – should be ticked! if you building a SIP for a web archive
2.	Harvest date – should be entered in the format as in example (Example shows time when app was run)
3.	Seed url – seed url for your web archive.
4.	Use this filed – should be ticked if you would like to specify user or project in METS
5.	If it is ticked please switch the radio button to your option and enter your username or project name in corresponding text field.

Check the form before pressing the “submit” button. From either tabs  the window will disappear and script will give you the message “SIP was created in ”   and show the folder with your SIP.
Check the mets.xml file for metadata you entered and when the SIP is ready:
Place it to:
 - Rosetta automated folder for production or
 - Rosetta UAT folder and contact the PRC team to arrange the Rosetta ingest job.

Done!

## 	Errors and notes:
***
 - Object identifier, entity type, input (either file or folder) and output folder are mandatory.
If you miss one of them the script will not build SIP and give you a message.
 - Object identifier, entity type, sip title, DC title, policy id will be kept the same for next submission while the window is open. However, path to source and output should be chosen again.



