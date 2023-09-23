from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import pandas as pd

# create an instance of a web browser (in this case, chrome)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

#arrays for the different parameters to extract data
salud=[]
ataque=[]
curacion=[]
defensa=[]
tribu1=[]
tribu2=[]
tipo=[]
ID=[]
nombre=[]
coste=[]
estrellas=[]
nHability=[]

nSkills=[]
nEffectSkill1=[]
CDSkill1=[]

nEffectSkill2=[]
CDSkill2=[]

nEffectSkill3=[]
CDSkill3=[]

nEffectCrashSkill=[]

numeroCargas=[]
chargeITurns=[]
nEffectCharge1=[]

chargeIITurns=[]
nEffectCharge2=[]

chargeIIITurns=[]
nEffectCharge3=[]



damageBreak=[]
antiHacking=[]
antiVirus=[]
poisonBreak=[]
antiSkillBind=[]
junkBreak=[]
timerBreak=[]
wormBreak=[]

blastreducion=[]

anticooldawnincrease=[]
anticoolpercetnage=[]

ATKboost=[]
ATKboosttotal=[]
ATKboostpercentage=[]

DEFboost=[]
DEFboosttotal=[]
DEFboostpercentage=[]

RECboost=[]
RECboosttotal=[]
RECboostpercentage=[]

HPboost=[]
HPboosttotal=[]
HPboostpercentage=[]

overHeal=[]
OverHealValue=[]

panelDrop=[]  #drop as
multiChain=[]

Barrier=[]

blastRadius=[]
blastRadiusPercent=[]

bombDrop=[]
CPDrop=[]
convertPanels=[] #to

counter=[]
counterValue=[]

damageReduction=[]
damageReductionperc=[]

directDamage=[]
directDamageIgnore=[]
directDamagecategorical=[]
diretDamageTotalValue=[]
directDamagePer=[]

easyCPSpawn=[]

joinAttack=[]
joinAttackpercen=[]

provoke=[]

skillTurnsReduce=[]

boardExtend=[]
boardExtendValue=[]


#especify the number to acces to the web page
x=range(15467,15468,1)
#x=[20046,15654]

for i in x:
	print(i)
	numero=str(i)
	# open the web page and add the number modifier to extract from different pages from the web
	browser.get('https://crashlibrary.com/unit/'+numero)

	# wait until some element would be in the HTML code
	#try:
	    #element_present = EC.presence_of_all_elements_located((By.XPATH, "//*[@class='my-5 d-flex flex-row justify-content-evenly align-items-center' and @id='root']"))
	    #element_present = EC.presence_of_element_located((By.ID, "root"))
	    #WebDriverWait(browser, 200)#.until(element_present)
	#except TimeoutError:
	    #print("Timed out waiting for page to load")

	time.sleep(6)

	## obtain the JavaScript codde form the web as a string
	html_text = browser.page_source

	# save the JavaScript code in a text file
	with open("html_code.txt", "w", errors='ignore') as f:
	    f.write(html_text)

	with open("html_code.txt", "r", errors='ignore') as f:
	    html_text = f.read()

	#SALUD
	# search the pattern in the HTML code
	match = re.search(r'HP: <b>(\d+)</b>', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    salud.append(hp_value)
	else:
		salud.append("error en "+numero)


	#ATAQUE
	# search the pattern in the HTML code
	match = re.search(r'ATK: <b>(\d+)</b>', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    ataque.append(hp_value)
	else:
		ataque.append("error en "+numero)



	#CURACION
	# search the pattern in the HTML code
	match = re.search(r'REC: <b>(\d+)</b>', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    curacion.append(hp_value)
	else:
		curacion.append("error en "+numero)


	#DEFENSA
	# search the pattern in the HTML code
	match = re.search(r'DEF: <b>(\d+)</b>', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    defensa.append(hp_value)
	else:
		defensa.append("error en "+numero)


	#NOMBRE
	# search the pattern in the HTML code
	match = re.search(r'="font-weight: bold;">(.*)</span><div class="d-flex', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    nombre.append(hp_value)
	else:
		nombre.append("error en "+numero)

	#ID
	# search the pattern in the HTML code
	match = re.search(r'ID: (\d+)</span>', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    ID.append(hp_value)
	else:
		ID.append("error en "+numero)



	#coste
	# search the pattern in the HTML code
	match = re.search(r'<span>Cost (\d+)<', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    coste.append(hp_value)
	else:
		coste.append("error en "+numero)


	#tipo
	# search the pattern in the HTML code
	match = re.search(r'<span>([a-zA-Z]+) Type', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    tipo.append(hp_value)
	else:
		tipo.append("error en "+numero)


	#tribu 1
	# search the pattern in the HTML code
	match = re.search(r'd-flex flex-row justify-content-between align-items-center text-center"><span>([a-zA-Z]+),', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    tribu1.append(hp_value)
	else:
		match = re.search(r'd-flex flex-row justify-content-between align-items-center text-center"><span>([a-zA-Z]+)<', html_text)
		if match:
			    hp_value = match.group(1)
			    tribu1.append(hp_value)
		else:
			tribu1.append("error en "+numero)
		
		


	#tribu 2
	# search the pattern in the HTML code
	match = re.search(r', ([a-zA-Z]+)</span>', html_text)

	# Extract the value if is in the text
	if match:
	    hp_value = match.group(1)
	    tribu2.append(hp_value)
	else:
		tribu2.append("error en "+numero)


	#Rareza
	
	# Search all times that appears the string
	result = re.findall(r'ico_Star.png', html_text)

	# Count
	if result:
		count = len(result)
		estrellas.append(count)
	else:
		estrellas.append("error en "+numero)

	#nHability
	#check how many times appears ability 
	result = re.findall(r'>Ability',html_text)
	count = len(result)
	nHability.append(count)
	
	#nSkills
	#check how many times appears skills
	result = re.findall(r'>Skill',html_text)
	count = len(result)
	nSkills.append(count)
	
	#nEffectSkill1
	#check how many effects have each skill using '+' as separator
	if count==1:
		match = re.search(r'>Skill(.*?)>Charge', html_text)
		if match:
			match2 = match.group(1)
			result = re.findall(r'\+', match2)
			counttemp=len(result)
			nEffectSkill1.append(counttemp+1)
		else:
			match = re.search(r'>Skill(.*?)>Crash', html_text)
			match2 = match.group(1)
			result = re.findall(r'\+', match2)
			counttemp=len(result)
			nEffectSkill1.append(counttemp+1)
	else:
		match = re.search(r'>Skill 1(.*?)>Skill 2', html_text)
		if match:
			match2 = match.group(1)
			result = re.findall(r'\+', match2)
			counttemp=len(result)
			nEffectSkill1.append(counttemp+1)
		else:
			nEffectSkill1.append(0)
	
	#CDSkill1
	#check what is the cooldown of each skill searching CD between each sequence of HTML code depending on the number of skills
	if count==1:
		match = re.search(r'>Skill(.*?)>Charge', html_text)
		if match:
			match2 = match.group(1)
			result = re.search(r'CD (\d+)', match2)
			CD = result.group(1)
			CDSkill1.append(CD)
		else:
			match = re.search(r'>Skill(.*?)>Crash', html_text)
			match2 = match.group(1)
			result = re.search(r'CD (\d+)', match2)
			CD = result.group(1)
			CDSkill1.append(CD)
	else:
		match = re.search(r'>Skill 1(.*?)>Skill 2', html_text)
		if match:
			match2 = match.group(1)
			CD = re.search(r'CD (\d+)', match2)
			CDSkill1.append(CD.group(1))
		else: 
			CDSkill1.append(0)

	#nEffectSkill2
	
	if count<2:
		nEffectSkill2.append(0)
	else:
		match = re.search(r'>Skill 2(.*?)>Skill 3', html_text)
		match2 = match.group(1)
		result = re.findall(r'\+', match2)
		counttemp=len(result)
		nEffectSkill2.append(counttemp+1)

	#CDSkill2
	if count<2:
		CDSkill2.append(0)
	else:
		match = re.search(r'>Skill 2(.*?)>Skill 3', html_text)
		match2 = match.group(1)
		CD = re.search(r'CD (\d+)', match2)
		CDSkill2.append(CD.group(1))

	#nEffectSkill3
	if count<3:
		nEffectSkill3.append(0)
	else:
		match = re.search(r'>Skill 3(.*?)>Crash', html_text)
		match2 = match.group(1)
		result = re.findall(r'\+', match2)
		counttemp=len(result)
		nEffectSkill3.append(counttemp+1)

	#CDSkill3
	if count<3:
		CDSkill3.append(0)
	else:
		match = re.search(r'>Skill 3(.*?)>Crash', html_text)
		match2 = match.group(1)
		CD = re.search(r'CD (\d+)', match2)
		CDSkill3.append(CD.group(1))

	
	#numeroCargas
	#check if the skill has a charge and how many charges
	result = re.findall(r'>Charge',html_text)
	count = len(result)
	numeroCargas.append(count)

	#chargeITurns
	#check the number of turns thar requires each charge
	if count>0:
		match = re.search(r'>Charge 1(.*?)>Charge 2', html_text)
		if match:
			match2 = match.group(1)
			CD = re.search(r'CD (\d+)', match2)
			chargeITurns.append(CD.group(1))
		else:
			match = re.search(r'>Charge 1(.*?)>Crash ', html_text)
			match2 = match.group(1)
			CD = re.search(r'CD (\d+)', match2)
			chargeITurns.append(CD.group(1))
	else:
		chargeITurns.append(0)

	#nEffectCharge1
	if count>0:
		match = re.search(r'>Charge 1(.*?)>Charge 2', html_text)
		if match:
			match2 = match.group(1)
			result = re.findall(r'\+', match2)
			counttemp=len(result)
			nEffectCharge1.append(counttemp+1)
		else :
			match = re.search(r'>Charge 1(.*?)>Crash', html_text)
			match2 = match.group(1)
			result = re.findall(r'\+', match2)
			counttemp=len(result)
			nEffectCharge1.append(counttemp+1)
	else:
		nEffectCharge1.append(0)

	#chargeIITurns
	if count>1:
		match = re.search(r'>Charge 2(.*?)>Charge 3', html_text)
		if match:
			match2 = match.group(1)
			CD = re.search(r'CD (\d+)', match2)
			chargeIITurns.append(CD.group(1))
		else:
			match = re.search(r'>Charge 2(.*?)>Crash', html_text)
			match2 = match.group(1)
			CD = re.search(r'CD (\d+)', match2)
			chargeIITurns.append(CD.group(1))
	else:
		chargeIITurns.append(0)
	
	#nEffectCharge2
	if count>1:
		match = re.search(r'>Charge 2(.*?)>Charge 3', html_text)
		if match:
			match2 = match.group(1)
			result = re.findall(r'\+', match2)
			counttemp=len(result)
			nEffectCharge2.append(counttemp+1)
		else :
			match = re.search(r'>Charge 2(.*?)>Crash', html_text)
			match2 = match.group(1)
			result = re.findall(r'\+', match2)
			counttemp=len(result)
			nEffectCharge2.append(counttemp+1)
	else:
		nEffectCharge2.append(0)

	#chargeIIITurns
	if count>2:
		match = re.search(r'>Charge 3(.*?)>Crash', html_text)
		match2 = match.group(1)
		CD = re.search(r'CD (\d+)', match2)
		chargeIIITurns.append(CD.group(1))
	else:
		chargeIIITurns.append(0)

	#nEffectCharge3
	if count>2:
		match = re.search(r'>Charge 3(.*?)>Crash', html_text)
		match2 = match.group(1)
		result = re.findall(r'\+', match2)
		counttemp=len(result)
		nEffectCharge1.append(counttemp+1)
	else:
		nEffectCharge3.append(0)
	
	#nEffectCrashSkill
	match = re.search(r'>Crash(.*?)>Ability', html_text)
	if match:
		match2 = match.group(1)
		result = re.findall(r'\+', match2)
		counttemp=len(result)
		nEffectCrashSkill.append(counttemp+1)
	else:
		nEffectCrashSkill.append(0)

	#damageBreak
	#check if appear that effect
	if len(re.findall(r'break Damage Panels',html_text))>0 or len(re.findall(r'destroy Damage Panels',html_text))>0:
		damageBreak.append(1)
	else:
		damageBreak.append(0)
	

	#antiHacking
	#check if appear that effect
	if len(re.findall(r'Hacking',html_text))>0:
		antiHacking.append(1)
	else:
		antiHacking.append(0)


	#antiVirus
	#check if appear that effect
	if len(re.findall(r'Virus',html_text))>0:
		antiVirus.append(1)
	else:
		antiVirus.append(0)


	#poisonBreak
	#check if appear that effect
	if len(re.findall(r'can break Poison Panels',html_text))>0:
		poisonBreak.append(1)
	else:
		poisonBreak.append(0)

		
	
	#antiSkillBind
	#check if appear that effect
	if len(re.findall(r'Skill Bind',html_text))>0 or len(re.findall(r'SkillBind',html_text))>0:
		antiSkillBind.append(1)
	else:
		antiSkillBind.append(0)

		
	#junkBreak
	#check if appear that effect
	if len(re.findall(r'Junk',html_text))>0:
		junkBreak.append(1)
	else:
		junkBreak.append(0)
	
	
	#wormBreak
	#check if appear that effect
	if len(re.findall(r'Worm',html_text))>0:
		wormBreak.append(1)
	else:
		wormBreak.append(0)
		
	
	#anticooldawnincrease
	#check if appear that effect
	if len(re.findall(r'Anti-cooldown',html_text))>0:
		anticooldawnincrease.append(1)
	else:
		anticooldawnincrease.append(0)
			
	#anticoolpercetnage
	#check if appear that effect
	if len(re.findall(r'Anti-cooldown',html_text))>0:
		CD = re.search(r'(\d+)% Anti-cooldown',html_text)
		anticoolpercetnage.append(CD.group(1))
	else: 
		anticoolpercetnage.append(0)
	
		# in proccess
	#ATKboost

	#ATKboosttotal
	
	#ATKboostpercentage
	
	#DEFboost
	
	#DEFboosttotal
	
	#DEFboostpercentage
	
	#RECboost
	
	#RECboosttotal
	
	#RECboostpercentage

	#HPboost
	
	#HPboosttotal
	
	#HPboostpercentage
	
	#overHeal
	
	#OverHealValue
	
	#panelDrop
	
	#multiChain
	
	#Barrier
	
	#blastRadius
	
	#blastRadiusPercent
	
	#bombDrop
	
	#CPDrop
	
	#convertPanels
	
	#counter
	
	#counterValue
	
	#damageReduction
	
	#damageReductionperc
	
	#directDamage
	
	#directDamageIgnore
	
	#directDamagecategorical
	
	#diretDamageTotalValue
	
	#directDamagePer
	
	#easyCPSpawn
	
	#joinAttack
	
	#joinAttackpercen
	
	#provoke
	
	#skillTurnsReduce
	
	#boardExtend
	
	#boardExtendValue










#print the parameters to check that all is correct
print(ID)
print(nombre)   
print(coste)
print(estrellas)
print(salud)
print(ataque)
print(curacion)
print(defensa)
print(tipo)
print(tribu1)
print(tribu2)
print(nHability)
print(nSkills)
print(nEffectSkill1)
print(CDSkill1)
print(nEffectSkill2)
print(CDSkill2)
print(nEffectSkill3)
print(CDSkill3)
print(numeroCargas)
print(chargeITurns)
print(nEffectCharge1)
print(chargeIITurns)
print(nEffectCharge2)
print(chargeIIITurns)
print(nEffectCharge3)
print(nEffectCrashSkill)

#store in a data frame
data={'ID':ID,'Name':nombre,'Cost':coste,'Rare':estrellas,'Type':tipo, 'Tribe1':tribu1, 'Tribe2':tribu2, 'HP':salud,'ATK':ataque,'REC':curacion,'DEF':defensa,
'nHability':nHability,
'nSkills':nSkills,
'nEffectSkill1':nEffectSkill1,
'CDSkill1':CDSkill1,
'nEffectSkill2':nEffectSkill2,
'CDSkill2':CDSkill2,
'nEffectSkill3':nEffectSkill3,
'CDSkill3':CDSkill3,
'numeroCargas':numeroCargas,
'chargeITurns':chargeITurns,
'nEffectCharge1':nEffectCharge1,
'chargeIITurns':chargeIITurns,
'nEffectCharge2':nEffectCharge2,
'chargeIIITurns':chargeIIITurns,
'nEffectCharge3':nEffectCharge3,
'nEffectCrashSkill':nEffectCrashSkill}

# Create a DataFrame
df = pd.DataFrame(data)

# Export to Excel
df.to_excel('crashfever2.xlsx', index=False)
print(html_text)

browser.quit()