#!/usr/bin/env python

from datetime import date, datetime, time
from backports.datetime_fromisoformat import MonkeyPatch
MonkeyPatch.patch_fromisoformat()

datetime.fromisoformat("2014-01-09T21:48:00-05:30")

date.fromisoformat("2014-01-09")

time.fromisoformat("21:48:00-05:30")
