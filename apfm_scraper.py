import requests
import bs4

def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))

def pageRequests():
    r = requests.get('https://www.aplaceformom.com/community/merrill-gardens-at-first-hill-71358')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup

def getPageTitle(soup):
    return soup.title.string.strip()

def getCommunityName(soup):
    return soup.find(class_='community-desc').h1.text

def getMetaDescription(soup):
    meta = soup.find_all('meta')
    return listToString([meta.attrs['content'] for meta in meta if 'name' in meta.attrs and meta.attrs['name'] == 'description'])

def getCommunityStreetAddress(soup):
    return soup.find( class_='community-desc').p.text

def getCommunityCity(CommunityStreetAddress):
    city= CommunityStreetAddress.split()
    return city[-3]

def getCommunityState(CommunityStreeAddress):
    state=CommunityStreeAddress.split()
    return state[-2]

def getCommunityZipCode(CommunityStreeAddress):
    state = CommunityStreeAddress.split()
    return state[-1]

def getCommunityImages(soup):
    print(soup.text)
    return 0

def getCommunityContent(soup):
    content= soup.find('div',class_='community-detail').get_text().strip()
    return content.replace('Now offering virtual tours. Call us now to schedule.','')

def getNumberofReviews(soup):
    return soup.find(class_='reviews-count-container').find("span").text.strip()

def getAverageReviewScore(soup):
    return soup.find(class_='score-container').find("span").text.strip()

def getCommunityAmenities(soup):
    amenities=[]
    str=""
    for i in soup.find(class_='List-order').findAll('li')[1:]:
        amenities.append(i.get_text())

    for i in amenities:
        str+=i+","

    return str[:-1]

def getCareTypesProvided(soup):
    caretype = []
    str = ""
    for i in soup.find_all(class_='on'):
        caretype.append(i.get_text())

    for i in caretype:
        str += i + ","

    return str[:-1]