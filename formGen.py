formName = raw_input("Enter Form Name: ")
xmlFile = open(formName, 'w')
xmlFile.write("<html><head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css'><link rel='stylesheet'href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css'><script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js'></script></head>")
xmlFile.write("<form>")
xmlFile.close()
	
while 1==1:		
		
		print("Select input type \n")
		print("1 text \n")
		print("2 password \n")
		print("3 Radio buttons \n")
		print("4 checkbox \n")
		print("5 buttons \n")
		print("6 Selection List \n")
		print("7 Textarea \n")
		print("8 submit \n")
		print("0 to exit \n")
		global inputType
		inputType = raw_input("Enter your choice : ")
		print(inputType)
		if inputType == '1':
			labelName = raw_input("Label Name ")
			with open(formName, 'a') as formBody:
				formBody.write("<div class='form-group'>")
				formBody.write("<label for='%s'> %s </label> \n" % (labelName,labelName) )
				formBody.write("<input type='text' class='form-control' id= %s /> " % labelName)
				formBody.write("</div>")
				formBody.close()
					
				
		elif inputType == '2':
			labelName = raw_input("Label Name ")
		        with open(formName, 'a') as formBody:
				formBody.write("<div class='form-group'>")
				formBody.write("<label for='%s'> %s </label> \n" % (labelName,labelName) )
				formBody.write("<input type='password' class='form-control' id= '%s' /> " % labelName)
				formBody.write("</div>")
				formBody.close()
		elif inputType == '3':
			numRadioButtons = raw_input("How many radio buttons do you want ?")
			for i in numRadioButtons:
				nameRadioBtn = input("Please enter Name of radio button")
				valueRadioBtn = input("Please enter value of radio button")
				with open(formName, 'a') as formBody:
					formBody.write("<div class='radio'>")
					formBody.write("<label><input type='radio' name='%s'>%s</label>"% (nameRadioBtn,valueRadioBtn))
					formBody("</div>")
					formBody.close()
			
		elif inputType == '4':
			numOfCheckBox = raw_input("How many checkboxes do you want? ")
			for c in numOfCheckBox:	
				chkValue = raw_input("Value for checkbox ")
				with open(formName, 'a') as formBody:
					formBody.write("<div class='checkbox'> ")
					formBody.write("<label><input type='checkbox' value="">%s</label>"% chkValue)
					formBody("</div>")
					formBody.close()
		elif inputType == '5':
			print("1 White \n")
			print("2 green \n")
			print("3 Orange \n")
			print("4 Red \n")
			btnColor = raw_input("Please select a color")
			if btnColor == '1':
					btnName = raw_input("Please enter Button Name")
					with open(formName,'a') as formBody:
						formBody.write("<button type='button' class='btn btn-default'>%s</button>"% btnName)
						formBody.close()
			elif btnColor == '2':	
					btnName = raw_input("Please enter Button Name")
					with open(formName,'a') as formBody:
						formBody.write("<button type='button' class='btn btn-success'>%s</button>" % btnName)
						formBody.close()
			elif btnColor == '3':	
					btnName = raw_input("Please enter Button Name")
					with open(formName,'a') as formBody:
						formBody.write("<button type='button' class='btn btn-warning'>%s</button>"% btnName)
						formBody.close()
			elif btnColor == '4':	
					btnName = raw_input("Please enter Button Name")
					with open(formName,'a') as formBody:
						formBody.write("<button type='button' class='btn btn-danger'>%s</button>" % btnName)
						formBody.close()	
			else:
					print("Please Choose a given number")		
		elif inputType == '6':
			nameOfSelectionList = raw_input("Name of selection list")
			numOfOptions = raw_input("Number of option do you want?")
			script = open(formName,'a')
			script.write("<label for='%s'> %s </label>"% (nameOfSelectionList,nameOfSelectionList))
			script.write(" <select class='form-control' id='%s'>"% nameOfSelectionList)
			for d in numOfOptions:
				optionName = raw_input("Please enter option name")
				script.write("<option>%s</option>"% optionName)
			script.write("</select>")
			script.write("</div>")
			script.close()
		elif inputType == '7':
			nameTextArea = raw_input("Name for text area")
			rowForTextArea = raw_input("Enter Number of Rows")
			script = open(formName,'a')
			script.write("<label for='%s'>%s</label>"% (nameTextArea,nameTextArea))
			script.write("<textarea class='form-control' rows='%s' id='%s'></textarea>"% (rowForTextArea,nameTextArea))	
			script.close()
		elif inputType == '8':
			submitTitle = raw_input("Title for submit button")
			script = open(formName,'a')
			script.write("<input type='submit' value='%s'>"% submitTitle)
			script.close()
		elif inputType == '0':
			xmlFile = open(formName, 'a')
			xmlFile.write("</form>")
			xmlFile.write("</body></html>")
			xmlFile.close()		
			break
		
		else: 		
			print("Please enter it again")
		


