cal = Calendar()
from datetime import datetime

cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

import pytz
event = Event()
event.add('summary', 'Python meeting about calendaring')
event.add('dtstart', datetime(2005,4,4,8,0,0,tzinfo=pytz.utc))
event.add('dtend', datetime(2005,4,4,10,0,0,tzinfo=pytz.utc))
event.add('dtstamp', datetime(2005,4,4,0,10,0,tzinfo=pytz.utc))

from icalendar import vCalAddress, vText
organizer = vCalAddress('MAILTO:noone@example.com')

organizer.params['cn'] = vText('Max Rasmussen')
organizer.params['role'] = vText('CHAIR')
event['organizer'] = organizer
event['location'] = vText('Odense, Denmark')

event['uid'] = '20050115T101010/27346262376@mxm.dk'
event.add('priority', 5)

attendee = vCalAddress('MAILTO:maxm@example.com')
attendee.params['cn'] = vText('Max Rasmussen')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

attendee = vCalAddress('MAILTO:the-dude@example.com')
attendee.params['cn'] = vText('The Dude')
attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
event.add('attendee', attendee, encode=0)

cal.add_component(event)

import tempfile, os
directory = tempfile.mkdtemp()
f = open(os.path.join(directory, 'example.ics'), 'wb')
f.write(cal.to_ical())
f.close()