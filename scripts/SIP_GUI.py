import PySimpleGUI as sg
import os
from pathlib import Path

from datetime import datetime as dt
from rosetta_sip_factory.sip_builder import build_sip_from_json, build_single_file_sip, build_sip



def my_gui():

	form = sg.FlexForm('Simple SIP form')
	value_list  = ["WebHarvestIE","OneOffIE","AudioIE","PeriodicIE","VideoIE","HTMLSerialIE","HTMLMonoIE","UnpublishedIE",""]
	layout1 = [
			[sg.Text('Library system:')],
			[sg.Radio('Alma', "RADIO1", default=True,key='alma'),sg.Text('Alma MMS', size=(8, 1)), sg.InputText('',key='alma_mms',size=(35, 1))],
			[sg.Radio('Tiaki', "RADIO1", default=False,key='tiaki'),sg.Text('Tiaki EMU', size=(8, 1)), sg.InputText('',key = 'tiaki_emu',size=(35, 1))],
			[sg.Text('dc title', size=(10, 1)), sg.InputText('my title',key='dc_title', size=(40, 1))],
			[sg.Text('SIP title', size=(10, 1)), sg.InputText('my_sip_title',key='sip_title',size=(40, 1))],
			[sg.Text('Entity type',size=(10, 1)), sg.Listbox(values=value_list, size=(30, 1), default_values=(value_list[0],), key='entity_type')],
			[sg.Text('policyId', size=(10, 1)), sg.InputText('100',key='access',size=(5, 1))],
			[sg.Text('File or folder:')],
			[sg.Radio('Single file      ', "RADIO2", default=True, key = 'file_flag'),sg.Text('File Browse result', size=(30, 1)),sg.FileBrowse('FileBrowse',key='filename')],
			[sg.Radio('Folder           ', "RADIO2", default=False, key = 'fold_flag'),sg.Text('Folder Browse result', size=(30, 1)),sg.FolderBrowse('FolderBrowse',key='foldername')],
			[sg.Text('', size=(1, 1)),sg.Text('Output folder', size=(10, 1)), sg.Text('Folder Browse result', size=(30, 1)), sg.FolderBrowse('FolderBrowse',key='output_dir')],
			[sg.Text('For non WEB only:')],
			[sg.Text('year', size=(5, 1)), sg.InputText(dt.now().strftime("%Y"),key="year",size=(5, 1)),sg.Text('month', size=(5, 1)), sg.InputText(dt.now().strftime(""),key="month",size=(5, 1)),sg.Text('day', size=(5, 1)), sg.InputText(dt.now().strftime(""),key="day",size=(5, 1))],
			[sg.Text('volume', size=(5, 1)), sg.InputText("",key="volume",size=(5, 1)),sg.Text('issue', size=(5, 1)), sg.InputText("",key="issue",size=(5, 1)),sg.Text('number', size=(5, 1)), sg.InputText("",key="number",size=(5, 1))],
			]
	layout2 = [
			[sg.Checkbox('Web Archive', default=False,key='if_web')],
			[sg.Radio('Webrecorder', "RADIO3", default=True, key='webrecorder'),sg.Radio('ArchiveIt', "RADIO3", default=False, key = 'ArchiveIt')],
			[sg.Text('Harvest date', size=(15, 1)), sg.InputText(dt.now().strftime("%d/%m/%Y %H:%M:%S"),key="harvest_date",size=(15, 1))],
			[sg.Text('Seed url', size=(15, 1)), sg.InputText('https://',key="seed_url")],
			[sg.Text('NEW! user or project (please ignore if do not need it)',text_color = "dark red")],
			[sg.Checkbox('Use This Filed', default=False,key='if_user_project')],
			[sg.Radio('Project', "RADIO4", default=True,key='project'), sg.InputText('',key='projectname',size=(20, 1))],
			[sg.Radio('User   ', "RADIO4", default=False,key='user'), sg.InputText('',key = 'username',size=(20, 1))]
			]
	tabgrp = [[sg.TabGroup([[sg.Tab('Main details', layout1, border_width =10),
               sg.Tab('Web and User', layout2,title_color='Blue')]],
 					tab_location='centertop', border_width=5), sg.Button('Submit')]]  
        
	#Define Window
	window =sg.Window("Tabs",tabgrp)
	#Read  values entered by user
	event,values=window.read()
	#access all the values and if selected add them to a string
	window.close() 
	print(values)  

	# window=sg.Window('SIP Maker', layout1,grab_anywhere=True)

	# button, values = window.Read()

	# window.Close() # added to fix downstream problem
	return values
	#{'alma': True, 'alma_mms': '999999999999999', 'tiaki': False, 'tiaki_emu': '', 'dc_title': 'my title test1', 'sip_title': 'my_sip_title_test1', 'entity_type': ['HTMLMonoIE'], 'policy_id': '100', 0: True, 'filename': 'D:/5427e475-120e-4bcf-9f26-b15362c0a7c6.pdf', 1: False, 'foldername': '', 'output_dir': 'D:/', 'if_web': False, 'webrecorder': True, 'ArchiveIt': False, 'harvest_date': '25/11/2021 15:41:55', 'seed_url': 'https://'}
def main():

	values = my_gui()
	if "alma" in values.keys():
		mms_id = values["alma_mms"]
		emu = None
	elif "tiaki" in values.keys():
		emu = values["emu"]
		mms_id = None
	if values["file_flag"]:
		filename = values["filename"]
		foldername = None
	elif values["fold_flag"]:
		print("here0")
		foldername = values["foldername"]
		filename = None
	entity = values["entity_type"][0]
	access = values["access"]
	dc_title = values["dc_title"]
	sip_title = values["sip_title"]
	print(values["output_dir"])
	output_dir = Path(values["output_dir"],sip_title)
	print(output_dir)
	if values["if_web"]== False:
		year = values["year"]
		month = values["month"]
		day = values["day"]
		volume = values["volume"]
		issue = values["issue"]
		number = values["number"]
	if values["if_web"] == True:
		harvest_date = values["harvest_date"]
		seed_url = values ["seed_url"]
		dcdate = dt.strptime(harvest_date,"%d/%m/%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
		if "webrecorder" in values.keys():
			harvester = "Webrecorder"
		elif "archiveit" in values.keys():
			harvester = "ArchiveIt"
	if values["if_user_project"] == True:
		if "user" in values.keys():
			username = values["username"]
			projectname = None
		elif "project" in values.keys():
			projectname = values["projectname"]
			username = None
	if not values["if_web"]:
		ie_dc_dict = [{"dcterms:bibliographicCitation":volume,"dcterms:accrualPeriodicity":number,"dcterms:issued":issue,"dc:date":year,"dcterms:available":month,"dc:coverage": day,"dc:title":dc_title}]
	elif values["if_web"]:
		ie_dc_dict = [{"dc:date":dcdate,"dc:title":dc_title}]	
	general_ie_chars=[{'IEEntityType':entity}]
	if values["if_user_project"]:
		if username:
				general_ie_chars[0]["UserDefinedB"]=username
		elif projectname:
				general_ie_chars[0]["UserDefinedB"]=projectname
	kwargs = {  'ie_dmd_dict':ie_dc_dict, 
				'generalIECharacteristics':general_ie_chars,
				'accessRightsPolicy':[{'policyId': access}],
				'digital_original':True,
				'sip_title':sip_title,
				'output_dir':output_dir,
				'encoding':'utf-8'}
	if mms_id:
		kwargs['objectIdentifier'] = [{'objectIdentifierType': 'ALMAMMS', 'objectIdentifierValue': mms_id}] 
	elif emu:
		kwargs['cms'] = [{'system': 'emu','recordId':emu}]
	if values["if_web"]:
		kwargs["webHarvesting"]= [{"primarySeedURL":seed_url,"harvestDate":harvest_date,"WCTIdentifier":harvester}]

	if filename:

		kwargs["filepath"] = filename
		build_single_file_sip(**kwargs)


	elif foldername:
		print("here")
		kwargs["input_dir"]  = foldername
		kwargs["pres_master_dir"]=foldername
		print(kwargs)
		build_sip(**kwargs)
		print("Done")

if __name__ == '__main__':
	main()