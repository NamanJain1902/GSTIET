from bs4 import BeautifulSoup
import requests

def fetch(id):
    url = f"https://scholar.google.co.in/citations?user={id}&hl=en"
    
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")

    scholar = soup.title.text[:-17]
    scholar_post = soup.find('div', attrs={'class':'gsc_prf_il'}).text
    designation =  scholar_post.split(",")[0].strip()
    department = scholar_post.split(",")[1].strip()

    print(designation, "at", department)

    d = {}
    total_publications = 0

    text = soup.find('div', attrs={'id': 'gsc_prf_pua'})

    pmi = text.find('img', attrs={'id': 'gsc_prf_pup-img'})
    pmisrc = pmi.src

    profile_img_url = f"{url}/{soup.findAll('img', attrs={'id', 'gsc_prf_pup-img'})}"
    labels = [] 
    
    for label in soup.findAll("a", attrs={'class' : 'gsc_prf_inta gs_ibl'}):
        labels.append(label.text)
    print(labels)

    for citation in soup.findAll('tr', attrs={'class': 'gsc_a_tr'}):
        cite = citation.find('td', attrs={'class': 'gsc_a_t'})
        title = cite.find('a', attrs={'class': 'gsc_a_at'}).text
        coauthor = list(cite.find('div', attrs={'class': 'gs_gray'}).text.strip().split(","))
        yr = int(citation.find('td', attrs={'class': 'gsc_a_y'}).text)

        val = (title, coauthor)

        if d.get(yr):
            d[yr].append(val)
        else:
            d[yr] = list([val])

        total_publications += 1

    context = {
        "scholar" : scholar,
        "content" : soup.prettify(),
        "d" : d,
        "labels" : labels,
        "img_url" : pmisrc,
    }


id = "MNj1Dw4AAAAJ"
fetch(id)