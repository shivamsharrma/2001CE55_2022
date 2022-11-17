
from datetime import datetime
start_time = datetime.now()
import pandas as pd #importing pandas
import sys
from csv import writer


def scorecard():
	pass

	text=open('pak_inns1.txt','r').read()
	fun= open('Scorecard.txt','a')
	document=[]
	for i in text.split('\n\n'):
		document.append(i)
	line=[]
	for i in range(len(document)):
		line.append(document[i].split(','))
	lx=len(document)
	
	batsman=[]
	bowlers=[]
	balls=[]
	for i in range(len(line)):
		players= line[i][0].split('to')
		player=players[0].split(' ')
		
		batsman.append(players[1])
		s=''
		for j in range(len(player)-1):
			if j==0:
				continue
			else:
				s=s+player[j]+" "
		bowlers.append(s)
		balls.append(player[0])
	
	unique_batsman= list(dict.fromkeys(batsman))
	unique_ballers= list(dict.fromkeys(bowlers))
	Batter=pd.DataFrame()
	Batter['BATTER']=unique_batsman
	Batter['status']='Not Out'
	Batter['R']=Batter['B']=Batter['4s']=Batter['6s']=Batter['SR']=0

	MyBowlers=pd.DataFrame()
	MyBowlers['BOWLER']=unique_ballers
	MyBowlers['O']=MyBowlers['M']=MyBowlers['R']=MyBowlers['W']=MyBowlers['NB']=MyBowlers['WD']=MyBowlers['EC']=MyBowlers['B']=0
	
	# print(bowlers)
	extra=wide=score=wickets=NoBall=b=lb=0
	fall=[]
	for i in range(len(line)):
		line[i][1]=line[i][1].lower()
		bowlername=bowlers[i]
		batsmanName=batsman[i]
		ball_no=balls[i]
		row1=0
		row2=0

		for k in range(len(unique_ballers)):
			if unique_ballers[k]==bowlers[i]:
				row1=k
				break

		for k in range(len(unique_batsman)):
			if unique_batsman[k]==batsman[i]:
				row2=k
				break
		
		if line[i][1]==' wide':
			wide=wide+1
			score=score+1
			MyBowlers.at[row1,'WD']=MyBowlers.at[row1,'WD']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+1

		elif line[i][1]==' no run':
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1

		elif line[i][1]==' 2 wides':
			wide=wide+2
			score=score+2
			MyBowlers.at[row1,'WD']=MyBowlers.at[row1,'WD']+2
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+2

		elif line[i][1]==' 3 wides':
			wide=wide+3
			score=score+3
			MyBowlers.at[row1,'WD']=MyBowlers.at[row1,'WD']+3
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+3

		elif line[i][1]==' no ball':
			NoBall=NoBall+1
			score=score+1
			
			MyBowlers.loc[row1,'R']=MyBowlers.loc[row1,'R']+1
			MyBowlers.loc[row1,'NB']=MyBowlers.loc[row1,'NB']+1
		
		elif line[i][1]==' four':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+4
			Batter.loc[row2,'4s']=Batter.loc[row2,'4s']+1
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+4
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+4

		elif line[i][1]==' six':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+6
			Batter.loc[row2,'6s']=Batter.loc[row2,'6s']+1
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+6
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+6

		elif line[i][1]==' 1 run':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+1
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+1
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+1

		elif line[i][1]==' 2 runs':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+2
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+2
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+2
		
		elif line[i][1]==' 3 runs':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+3
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+3
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+3

		
		elif line[i][1]==' byes':
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			if line[i][2]==' 1 run':
				MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+1
				score=score+1

			elif line[i][2]==' 2 runs':
				MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+2
				score=score+2
			elif line[i][2]==' 3 runs':
				MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+3
				score=score+3
			elif line[i][2]==' 4 run' or line[i][2]==' FOUR':
				MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+4
				score=score+4

		elif line[i][1]==' leg byes':
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			lg=lg+1
			if line[i][2]==' 1 run':
				score=score+1
			elif line[i][2]==' 2 runs':
				score=score+2
			elif line[i][2]==' 3 runs':
				score=score+3
			elif line[i][2]==' 4 runs' or line[i][2]==' FOUR':
				score=score+4

		# elif line[i][1]==

		else:
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			add= str(score)+'-'+str(wickets)+'('+ batsmanName +','+ball_no+')'
			fall.append(add)
			if len(fall)%4==0:
				fall.append('\n') 

			content=line[i][1].split('!')
			if content[0]==' out lbw':
				Batter.loc[row2,'status']='lbw b '+bowlername
				MyBowlers.at[row1,'W']=MyBowlers.at[row1,'W']+1
				wickets=wickets+1
			else:	
				if content[0]==' out bowled':
					Batter.loc[row2,'status']='b'+bowlername
					MyBowlers.at[row1,'W']=MyBowlers.at[row1,'W']+1
					wickets=wickets+1
				elif content[0]==' run out':
					Batter.loc[row2,'status']='run out'
					wickets=wickets+1
				else:
					content2=content[0].split('by')
					Batter.loc[row2,'status']='c'+content2[1]+' b '+bowlername
					MyBowlers.at[row1,'W']=MyBowlers.at[row1,'W']+1
					wickets=wickets+1

	for i in range (len(Batter)):
		
		Batter.loc[i,'SR']=round((Batter.loc[i,'R']/Batter.loc[i,'B'])*100,2)	

	for i in range (len(MyBowlers)):
		rem=(MyBowlers.at[i,'B']%6)/10	
		val=int(MyBowlers.at[i,'B']/6)	
		MyBowlers.at[i,'O']=round(val+rem,1)
		MyBowlers.at[i,'EC']=round(MyBowlers.at[i,'R']/MyBowlers.at[i,'O'],2)
	del MyBowlers['B']
	
	extra=wide+NoBall+lb+b
	Batter.loc[len(Batter)+1,'BATTER']=''
	Batter.loc[len(Batter)+1,'BATTER']=('Extras\t\t'+str(extra)+'(b '+str(b)+', lb '+str(lb)+', w '+str(wide)+', nb '+str(NoBall)+')')
	Batter.loc[len(Batter)+1,'BATTER']=('\nTotal\t\t'+str(score)+' ('+str(wickets)+' wkts, '+ str(MyBowlers['O'].sum())+' Ov)')
	
	Batter.to_csv('Scorecard.txt')
	with open('Scorecard.txt','a') as f:
		writer_object=writer(f)
		writer_object.writerow(fall)
	MyBowlers.loc[len(MyBowlers)+1,'BATTER']=''
	MyBowlers.loc[len(MyBowlers)+1,'BATTER']=''
	MyBowlers.loc[len(MyBowlers)+1,'BATTER']='Pakistan innings over\n'
	MyBowlers.loc[len(MyBowlers)+1,'BATTER']=''
	MyBowlers.loc[len(MyBowlers)+1,'BATTER']=''
	MyBowlers.loc[len(MyBowlers)+1,'BATTER']='India inning started\n'
	MyBowlers.to_csv('Scorecard.txt',mode='a')

	

	text=open('india_inns2.txt','r').read()
	
	document=[]
	for i in text.split('\n\n'):
		document.append(i)
	line=[]
	for i in range(len(document)):
		line.append(document[i].split(','))
	lx=len(document)
	
	batsman=[]
	bowlers=[]
	balls=[]
	for i in range(len(line)):
		players= line[i][0].split('to')
		player=players[0].split(' ')
		
		batsman.append(players[1])
		s=''
		for j in range(len(player)-1):
			if j==0:
				continue
			else:
				s=s+player[j]+" "
		bowlers.append(s)
		balls.append(player[0])
	
	unique_batsman= list(dict.fromkeys(batsman))
	unique_ballers= list(dict.fromkeys(bowlers))
	Batter=pd.DataFrame()
	Batter['BATTER']=unique_batsman
	Batter['status']='Not Out'
	Batter['R']=Batter['B']=Batter['4s']=Batter['6s']=Batter['SR']=0

	MyBowlers=pd.DataFrame()
	MyBowlers['BOWLER']=unique_ballers
	MyBowlers['O']=MyBowlers['M']=MyBowlers['R']=MyBowlers['W']=MyBowlers['NB']=MyBowlers['WD']=MyBowlers['EC']=MyBowlers['B']=0
	
	# print(bowlers)
	extra=wide=score=wickets=NoBall=b=lb=0
	fall=[]
	for i in range(len(line)):
		line[i][1]=line[i][1].lower()
		bowlername=bowlers[i]
		batsmanName=batsman[i]
		ball_no=balls[i]
		row1=0
		row2=0

		for k in range(len(unique_ballers)):
			if unique_ballers[k]==bowlers[i]:
				row1=k
				break

		for k in range(len(unique_batsman)):
			if unique_batsman[k]==batsman[i]:
				row2=k
				break
		
		if line[i][1]==' wide':
			wide=wide+1
			score=score+1
			MyBowlers.at[row1,'WD']=MyBowlers.at[row1,'WD']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+1

		elif line[i][1]==' no run':
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1

		elif line[i][1]==' 2 wides':
			wide=wide+2
			score=score+2
			MyBowlers.at[row1,'WD']=MyBowlers.at[row1,'WD']+2
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+2

		elif line[i][1]==' 3 wides':
			wide=wide+3
			score=score+3
			MyBowlers.at[row1,'WD']=MyBowlers.at[row1,'WD']+3
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+3

		elif line[i][1]==' no ball':
			NoBall=NoBall+1
			score=score+1
			
			MyBowlers.loc[row1,'R']=MyBowlers.loc[row1,'R']+1
			MyBowlers.loc[row1,'NB']=MyBowlers.loc[row1,'NB']+1
		
		elif line[i][1]==' four':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+4
			Batter.loc[row2,'4s']=Batter.loc[row2,'4s']+1
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+4
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+4

		elif line[i][1]==' six':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+6
			Batter.loc[row2,'6s']=Batter.loc[row2,'6s']+1
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+6
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+6

		elif line[i][1]==' 1 run':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+1
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+1
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+1

		elif line[i][1]==' 2 runs':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+2
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+2
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+2
		
		elif line[i][1]==' 3 runs':
			Batter.loc[row2,'R']=Batter.loc[row2,'R']+3
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+3
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			score=score+3

		
		elif line[i][1]==' byes':
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			if line[i][2]==' 1 run':
				MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+1
				score=score+1

			elif line[i][2]==' 2 runs':
				MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+2
				score=score+2
			elif line[i][2]==' 3 runs':
				MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+3
				score=score+3
			elif line[i][2]==' 4 run' or line[i][2]==' FOUR':
				MyBowlers.at[row1,'R']=MyBowlers.at[row1,'R']+4
				score=score+4

		elif line[i][1]==' leg byes':
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			lb=lb+1
			if line[i][2]==' 1 run':
				score=score+1
			elif line[i][2]==' 2 runs':
				score=score+2
			elif line[i][2]==' 3 runs':
				score=score+3
			elif line[i][2]==' 4 runs' or line[i][2]==' FOUR':
				score=score+4

		# elif line[i][1]==

		else:
			Batter.loc[row2,'B']=Batter.loc[row2,'B']+1
			MyBowlers.at[row1,'B']=MyBowlers.at[row1,'B']+1
			add= str(score)+'-'+str(wickets)+'('+ batsmanName +','+ball_no+')'
			fall.append(add)
			if len(fall)%4==0:
				fall.append('\n') 

			content=line[i][1].split('!')
			if content[0]==' out lbw':
				Batter.loc[row2,'status']='lbw b '+bowlername
				MyBowlers.at[row1,'W']=MyBowlers.at[row1,'W']+1
				wickets=wickets+1
			else:	
				if content[0]==' out bowled':
					Batter.loc[row2,'status']='b'+bowlername
					MyBowlers.at[row1,'W']=MyBowlers.at[row1,'W']+1
					wickets=wickets+1
				elif content[0]==' run out':
					Batter.loc[row2,'status']='run out'
					wickets=wickets+1
				else:
					content2=content[0].split('by')
					Batter.loc[row2,'status']='c'+content2[1]+' b '+bowlername
					MyBowlers.at[row1,'W']=MyBowlers.at[row1,'W']+1
					wickets=wickets+1

	for i in range (len(Batter)):
		
		Batter.loc[i,'SR']=round((Batter.loc[i,'R']/Batter.loc[i,'B'])*100,2)	

	for i in range (len(MyBowlers)):
		rem=(MyBowlers.at[i,'B']%6)/10	
		val=int(MyBowlers.at[i,'B']/6)	
		MyBowlers.at[i,'O']=round(val+rem,1)
		MyBowlers.at[i,'EC']=round(MyBowlers.at[i,'R']/MyBowlers.at[i,'O'],2)
	del MyBowlers['B']
	
	extra=wide+NoBall+lb+b
	Batter.loc[len(Batter)+1,'BATTER']=''
	Batter.loc[len(Batter)+1,'BATTER']=('Extras\t\t'+str(extra)+'(b '+str(b)+', lb '+str(lb)+', w '+str(wide)+', nb '+str(NoBall)+')')
	Batter.loc[len(Batter)+1,'BATTER']=('\nTotal\t\t'+str(score)+' ('+str(wickets)+' wkts, '+ str(MyBowlers['O'].sum())+' Ov)')
	
	Batter.to_csv('Scorecard.txt',mode='a')
	with open('Scorecard.txt','a') as f:
		writer_object=writer(f)
		writer_object.writerow(fall)
	
	MyBowlers.to_csv('Scorecard.txt',mode='a')
	# del MyBowlers['B']
	
	

###Code
# print("Correct Version Installed")


scorecard()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
