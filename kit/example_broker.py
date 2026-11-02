"""Example broker spec with listings and the payment estimate. Copy, replace with verified facts, run: python3 example_broker.py"""
import sys
from helpers import P, broker, broker_nav as nav, listing, areas, write_all

specs = dict([
broker('twaddle-realty-maryville', dict(
    name='Twaddle Realty', short='Twaddle',
    title='Twaddle Realty | Homes in Maryville, MO and southwest Iowa',
    desc='Twaddle Realty on S Main in Maryville, Missouri. Licensed in Missouri and Iowa, current listings with a payment estimate.',
    theme=dict(bg='#f4f1ea', surface='#e6e0d4', ink='#1c2430', muted='#5d6572', accent='#2b5d8a', accent_ink='#f6f3ed', band='#1c2430', band_ink='#f4f1ea'),
    font='clash',
    photos=dict(h=P('1565829262357-bf9669de2295'), menu=P('1600382421534-01865c8877cb'), about=P('1651407825801-eec2dcbd86bd'),
                strip=[P('1675178415839-27d20d76275a'), P('1616593871468-2a9452218369'), P('1641357435350-39483f1e15ac')],
                s2a=P('1596725217685-1315a39b80d4'), visit=P('1625602812206-5ec545ca1231'), foot=P('1655478157959-3fcfc543c1a2')),
    nav=nav(), primary=('Call 660 224 0743', 'tel:+16602240743'), secondary=('Email Bryan', 'mailto:TwaddleRealty@gmail.com'),
    status_default='916 S Main St, Maryville',
    lead='Homes and land around Maryville and into southwest Iowa, with same day service from a team of 10.',
    facts=['<b>30+ years</b> of experience', 'Licensed in Missouri and Iowa'],
    services=dict(id='listings', h2='On the market', sub='Current Twaddle Realty listings. Set a down payment and rate to see a monthly estimate.',
                  groups=[dict(rows=[
                      listing('314 E Thompson St', 'Maryville', '$339,000', '4 bed, 3 bath, 2,708 sq ft'),
                      listing('30449 Hillside Dr, 3.14 acres', 'Maryville', '$327,000', 'Land'),
                      listing('627 W Edwards St', 'Maryville', '$248,000', '4 bed, 2 bath'),
                      listing('327 E 7th St', 'Maryville', '$115,000', '3 bed, 2 bath'),
                  ])],
                  note='Listings as of October 2026. Same day service, just call.'),
    about=dict(h2='Same day service since 1995', ps=['Bryan Twaddle is the broker and owner of Twaddle Realty on South Main in Maryville. He earned his broker’s license in 1995.', 'Before the brokerage he founded Professional Property Management, and today the office is licensed in Missouri and Iowa with 10 agents.', 'The promise is simple: same day service.']),
    band=dict(fig='10', bx='agents covering Nodaway County and southwest Iowa.', small='Licensed in Missouri and Iowa.'),
    areas_html=areas('Where we work', ['Maryville', 'Savannah', 'Graham', 'Barnard', 'Pickering', 'Maitland', 'Ravenwood', 'Burlington Junction', 'Southwest Iowa'], [('Broker and owner', 'Bryan Twaddle'), ('Office', '916 S Main St'), ('Cell', '660 541 0400'), ('Licensed in', 'Missouri and Iowa')]),
    visit=dict(h2='Get in touch', rows=[('Office', '660 224 0743', 'tel:+16602240743'), ('Bryan’s cell', '660 541 0400', 'tel:+16605410400'), ('Email', 'TwaddleRealty@gmail.com', 'mailto:TwaddleRealty@gmail.com', True)],
               go=('Ask about a home', 'mailto:TwaddleRealty@gmail.com')),
    footer=dict(nav=nav(), contact='916 S Main St<br>Maryville, MO 64468<a href="tel:+16602240743">660 224 0743</a>',
                follow=[('Current site', 'https://www.twaddlerealty.com/')],
                legal='Every listing and detail comes from twaddlerealty.com and Bryan’s public Homes.com profile.'),
    dock=[('Call', 'tel:+16602240743'), ('Email', 'mailto:TwaddleRealty@gmail.com')],
), 'Twaddle<br>Realty')
])

if __name__ == '__main__':
    write_all(specs, sys.argv[1:])
