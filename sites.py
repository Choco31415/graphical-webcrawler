import requests, bs4

def expand_graph(link, graph):
	# Get a webpage
	res = requests.get(link)
	res.raise_for_status()
	text = res.content

	# Extract the links from it
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	for a in soup.find_all('a', href=True):
			if a['href'][:1] != '/' and a['href'][:1] != '#':
				# Check if a link is already recorded or not
				link = a['href']
				if not link in graph:
					graph.append(link)
					print(graph)
					expand_graph(link, graph)

	return graph

mapped_list = []
expand_graph('https://www.osuaiclub.com',  mapped_list)
