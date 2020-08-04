import requests, sys, webbrowser, bs4
class inbound:
	
	def double_verify(self, stage, mappedlist):
		for link in mappedlist:
			if link in stage:
				print(' DELETING .... ' + link)
				stage.remove(link)
				
		for link in mappedlist:
			if link in stage:
				print(' DELETING .... ' + link)
				stage.remove(link)
	
	def getlist(self, weblink, mappedlist):
		res = requests.get(weblink)
		text = res.content
		res.raise_for_status()
		stage = [] # 
		
		counter= 0
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		mappedlist.append(weblink) # here our codes first website is the first link 
		# initalize the first payload
		for a in soup.find_all('a', href=True):
				if a['href'][:1] != '/' and a['href'][:1] != '#' and a['href'] not in mappedlist:
					stage.append(a['href'])
	
		print('STTTTTTTTTTTAGE\n\n\n\n\n')
		print(stage)
		print('##########################################################################################\n\n\n')
		
		print(mappedlist)
		while counter < len(mappedlist):
			print('counter stage' + str(counter))
			
			weblink=stage[counter]
			self.double_verify(self, stage, mappedlist)
			
			#for link in mappedlist:
			#	if link in stage:
			#		print(' DELETING .... ' + link)
			#		stage.remove(link)
			#for link in mappedlist:
			#	if link in stage:
			#		print(' DELETING .... ' + link)
			#		stage.remove(link)
						
			print(' ########## stage # ' + str(counter) + '############' + str(len(stage)))
			print(stage)	
			
			res= requests.get(weblink)
			text = res.content
			res.raise_for_status()
		
			soup = bs4.BeautifulSoup(res.text, 'html.parser')
			for a in soup.find_all('a', href=True):
					if a['href'][:1] != '/' and a['href'][:1] != '#' and a['href'] not in mappedlist: # not in mapped list seems to not be working
						stage.append(a['href'])

			mappedlist.append(weblink)
			counter +=1
			print( 'MAPPPED LISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSST  ' + str(counter)+ ' LENGTH OF : '+ str(len(mappedlist)))
			print(mappedlist)
		print('FINAL STAGGGGGGGGGGGEEEEEEEEEEEE ')
		print(stage)
		
		return stage, mappedlist
mappedlist =[]
inbound.getlist(inbound,'https://en.wikipedia.org/wiki/Main_Page', mappedlist)

