#mcandrew

import numpy as np
import pandas as pd

def listPACounties():
    fips2name = {42001:"Adams",42003:"Allegheny",42005:"Armstrong",42007:"Beaver",42009:"Bedford",42011:"Berks",42013:"Blair",42015:"Bradford",
                 42017:"Bucks",42019:"Butler",42021:"Cambria",42023:"Cameron",42025:"Carbon",42027:"Centre",42029:"Chester",42031:"Clarion",
                 42033:"Clearfield",42035:"Clinton",42037:"Columbia",42039:"Crawford",42041:"Cumberland",42043:"Dauphin",42045:"Delaware",
                 42047:"Elk",42049:"Erie",42051:"Fayette",42053:"Forest",42055:"Franklin",42057:"Fulton",42059:"Greene",42061:"Huntingdon",
                 42063:"Indiana",42065:"Jefferson",42067:"Juniata",42069:"Lackawanna",42071:"Lancaster",42073:"Lawrence",42075:"Lebanon"	,
                 42077:"Lehigh",42079:"Luzerne",42081:"Lycoming",42083:"McKean",42085:"Mercer",42087:"Mifflin",42089:"Monroe",42091:"Montgomery",
                 42093:"Montour",42095:"Northampton",42097:"Northumberland",42099:"Perry",42101:"Philadelphia",42103:"Pike",42105:"Potter",
                 42107:"Schuylkill",42109:"Snyder",42111:"Somerset",42113:"Sullivan",42115:"Susquehanna",42117:"Tioga",42119:"Union",
                 42121:"Venango",42123:"Warren",42125:"Washington",42127:"Wayne",42129:"Westmoreland",42131:"Wyoming",42133:"York"}
    return fips2name

if __name__ == "__main__":

    d = pd.read_csv("https://raw.githubusercontent.com/MEDSL/2018-elections-unoffical/master/raw-returns/Pennsylvania.CSV") # from MIT labs election website
    d = d[['Election Name','County Name','Office Name','Party Name','Votes']] # subset to columns i care about

    d["Votes"] = [ int(x.replace(",","")) for x in d.Votes.values] 
    d.Votes = d.Votes.astype(int)
    def propOfVotes(x):
        ttlVotes = x.Votes.sum()
        x['prop'] = x.Votes/ttlVotes
        return x
    d = d.groupby(["County Name",'Office Name']).apply(propOfVotes)

    fromFIPS2countyName  = listPACounties()
    fromname2fips = {v.title():k for k,v in fromFIPS2countyName.items()}

    FIPS = []
    for x in d["County Name"]:
        x = x.title()
        FIPS.append( fromname2fips[x] )
    d['fips'] = FIPS
    d.to_csv("PA_prop_of_votes_2018.csv")
