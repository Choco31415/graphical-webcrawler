import requests
import bs4
import matplotlib.pyplot as plt
import math


def getlist(get_list_web_link, get_list_mapped_list):
    res = requests.get(get_list_web_link)
    stage = []
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        if a['href'][:1] != '/' and a['href'][:1] != '#' and a['href'] not in get_list_mapped_list:
            stage.append(a['href'])
            get_list_mapped_list.append(a['href'])

    return stage, get_list_mapped_list


link = 'https://en.wikipedia.org/wiki/Main_Page'
mapped_list = ['https://en.wikipedia.org/wiki/Main_Page']

website_list, mapped_list = getlist(link, mapped_list)
print(len(mapped_list))

fig, ax = plt.subplots(figsize=(20, 10))

ax.text(
    0,
    0,
    link,
    fontsize=8,
    verticalalignment='center',
    horizontalalignment='center',
    bbox=dict(boxstyle='square', facecolor='white', alpha=1)
)

new_list = []
new_list.append(website_list[0])

for idx, item in enumerate(website_list):
    x = 0 + 1 * math.cos(2 * math.pi * (idx + 1) / len(website_list))
    y = 0 + 1 * math.sin(2 * math.pi * (idx + 1) / len(website_list))

    item_plot = ax.text(
        x,
        y,
        item,
        fontsize=8,
        verticalalignment='center',
        horizontalalignment='center',
        bbox=dict(boxstyle='square', facecolor='white', alpha=1)
    )

    plt.plot([0, x], [0, y], 'k')

plt.xlim(-1, 1)
plt.ylim(-1, 1)

fig.patch.set_visible(False)
ax.axis('off')


plt.show()

# class: filter options... what the alorgitm should grab  Duski Tkinter
#  MAIN Getlist algorithim class    Duski 
# Class: Drawing all the visual elements of web(s) FAWRUXU doing stuff with turtle
#LATER: Database for replacing array

