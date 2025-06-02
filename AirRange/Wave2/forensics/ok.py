from Evtx.Evtx import Evtx

with Evtx('flag.evtx') as evtx:
    for record in evtx.records():
        print(record.xml())
