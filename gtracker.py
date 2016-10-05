from bs4 import BeautifulSoup
import cfscrape


def getTracker():
    list_url = "https://torrentproject.se/trackers/"

    scraper = cfscrape.create_scraper()
    resp = scraper.get(list_url)
    resp.encoding = "utf-8"
    parser = BeautifulSoup(resp.text, "html.parser")
    tds = parser.find_all("td", attrs={"class": "trackers_l"})
    return [td.a.get_text() for td in tds]


def main():
    for trackers in getTracker():
        print(trackers)
        print()


if __name__ == "__main__":
    main()
