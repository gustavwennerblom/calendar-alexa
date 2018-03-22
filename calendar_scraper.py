from bs4 import BeautifulSoup
import requests
from pprint import pprint


class CalendarParser():
    def __init__(self):
        html = requests.get('https://www.business-sweden.se/en/Trade/Seminars-and-events/')
        self.soup = BeautifulSoup(html.text, 'html.parser')

    def get_events(self):
        events = []
        all_events_soup = self.soup.find_all("div", class_="eventdetails")
        for event_soup in all_events_soup:
            event_dict = dict(
                title = event_soup.find("a").get_text(),
                date_and_place = event_soup.find("h2", class_="eventDesc").get_text().strip(),
                description_trunc = event_soup.find("p").get_text()
            )
            events.append(event_dict)
        return events


if __name__ == '__main__':
    parser = CalendarParser()
    events = parser.get_events()
    print(", ".join(event.get('title') for event in events))
