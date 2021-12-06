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

To run the app just go to  the “script” folder and run the “SIP_GUI.py” script
It will open the submission form.

![SIP_builder1](/documentation/SIP_builder1.PNG)

###“Main details” tab fields description:
This data populates the dc and mets.xml files.
1.Library system:
The default setting is Alma you can switch the radio button for Tiaki.
Enter your system record ID number in the corresponding field.
2. DC title will be displayed in the dc.xml.
3. SIP title – this names the SIP folder.
4. Entity type – you can use small arrows “up” and ”down” to scrall entity types and then click to select and you will pick the appropriate entity type for your submission.
(New ones can be added. Open the script in an editor. Find this line
```
value_list  = ["WebHarvestIE","OneOffIE","AudioIE","PeriodicIE",
"VideoIE","HTMLSerialIE","HTMLMonoIE","UnpublishedIE",""]
```
And add your entity type inside squared brackets, after coma and in quotes, save and it will appear the next time the app is run.
5. Policy ID – policy rights access code - change to 100, 200,300,400 as required
6. File or Folder:
If  your SIP will have one file use “Single file” radio button and select your file using the “FileBrowse” button
If your SIP will have multiple files in a folder switch the radio button to “folder” and use  “FolderBrowse” button to select the folder
7.Output folder:
Use the “FolderBrowse” button to select the folder where you want your SIP to be built.
8.Designation fields, for serial publications – It you are creating a one-time IEs or a web archives these field can be empty and will be ignored.




## Errors and notes
***

