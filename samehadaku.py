from bs4 import BeautifulSoup
import requests

def samehadaku(URL):
   page = requests.get(URL)
   soup = BeautifulSoup(page.content, 'html.parser')
   listAnimeTebaru = soup.main.find_all('div', 'widget_senction')

   # Mencari Widget section episode terbaru-nya
   for idx,widget_title in enumerate(listAnimeTebaru):
      if(widget_title.find('div','widget-title').text == 'Episode Terbaru'):
         break
   
   # Semua list anime episode terbaru
   listAnimeTebaru = listAnimeTebaru[idx].find('div', 'post-show').ul.find_all('li')
   links = []
   for i, anime in enumerate(listAnimeTebaru):
      # gambarAnime = anime.find('div', 'thumb').a.img['src']
      infoAnime = anime.find('div', 'dtla').h2.a
      title = infoAnime['title']
      link = infoAnime['href']
      print('{:-^100s}'.format(''))
      print(i, title)
      links.append(link)
   print('{:-^100s}'.format(''))

   noAnimeDownload = int(input('pilih anime yang mau didownload ? '))
   return links[noAnimeDownload]

def links_download_samehadaku(URL):
   page = requests.get(URL)
   soup = BeautifulSoup(page.content, 'html.parser')
   downloadEps = soup.find_all('div', 'download-eps')
   for link in downloadEps:
      formatVideo = link.p.text
      linksDownload = link.ul.find_all('li')
      for linkDownload in linksDownload:
         print(f'{formatVideo} \t\t: {linkDownload.strong.text}')
         for i in linkDownload.find_all('span'):
            if (i.a) != None:
               print(f"{i.a.string} \t: {i.a['href']}")
         print('{:-^100s}'.format(''))
      print('{:=^100s}'.format(''))


def main():
   URL = 'https://samehadaku.vip'
   links_download_samehadaku(samehadaku(URL))
   # links_download_samehadaku('https://samehadaku.vip/hanyou-no-yashahime-sengoku-otogizoushi-episode-14/')


if __name__ == "__main__":
    main()

