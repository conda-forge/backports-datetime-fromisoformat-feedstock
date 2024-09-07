#!/usr/bin/env python
import sys
from datetime import date, datetime, time

if sys.version_info <= (3, 11, 0):
    from backports.datetime_fromisoformat import MonkeyPatch
    MonkeyPatch.patch_fromisoformat()

print(datetime.fromisoformat("2014-01-09T21:48:00-05:30"))

print(date.fromisoformat("2014-01-09"))

print(time.fromisoformat("21:48:00-05:30"))
