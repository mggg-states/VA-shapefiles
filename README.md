# Virginia Election Shapefile
This shapefile was compiled by the Princeton Gerrymandering Project and edited by the Metric Geometry and Gerrymandering Group (MGGG).

## Sources
The precinct shapefile with election results comes from the Princeton Gerrymandering Project (available here https://github.com/PrincetonUniversity/VA-gerrymander/tree/master/Maps/VA%20Precincts/Precincts%20with%20CD/Elections). Demographic data at the block level are from IPUMS NHGIS (available here https://www.nhgis.org). Shapefiles for Virginia’s congressional, delegate, and senate districts were downloaded from the Commonwealth of Virginia’s Division of Legislative Services (available here http://redistricting.dls.virginia.gov/2010/RedistrictingPlans.aspx).

## Processing
Demographic data were aggregated from the block level to precincts using MGGG’s proration software (available here https://github.com/mggg/maup). Congressional, house, and senate district IDs were assigned to precincts also using this package.

## Metadata
* `precinct`: Precinct name
* `locality`: Locality name
* `loc_prec`: Locality and precinct names
* `district`: Congressional district name
* `G18DHOR`: Number of votes for 2018 Democratic US House candidate
* `G18DSEN`: Number of votes for 2018 Democratic senate candidate
* `G18OSEN`: Number of votes for 2018 other senate candidates
* `G18RHOR`:  Number of votes for 2018 Republican US House candidate
* `G18RSEN`: Number of votes for 2018 Republican senate candidate
* `G17DGOV`: Number of votes for 2017 Democratic gubernatorial candidate
* `G17DLTG`: Number of votes for 2017 Democratic lieutenant governor candidate
* `G17DATG`: Number of votes for 2017 Republican attorney general candidate
* `G17DHOD`: Number of votes for 2017 Democratic House of Delegates candidate
* `G17RGOV`: Number of votes for 2017 Republican gubernatorial candidate
* `G17RLTG`: Number of votes for 2017 Republican lieutenant governor candidate
* `G17RATG`: Number of votes for 2017 Republican attorney general candidate
* `G17RHOD`: Number of votes for 2017 Republican House of Delegates candidate
* `G17OGOV`:  Number of votes for 2017 other gubernatorial candidates
* `G16DPRS`: Number of votes for 2016 Democratic presidential candidate
* `G16RPRS`: Number of votes for 2016 Republican presidential candidate
* `G16OPRS`: Number of votes for 2016 other presidential candidates
* `G16DHOR`: Number of votes for 2016 Democratic US House candidate
* `G16RHOR`: Number of votes for 2016 Republican US House candidate
* `G16OHOR`: Number of votes for 2016 other US House candidates
* `TOTPOP`: Total population 
* `NH_WHITE`: White, non-hispanic, population
* `NH_BLACK`: Black, non-hispanic, population
* `NH_AMIN`: American Indian and Alaska Native, non-hispanic, population
* `NH_ASIAN`: Asian, non-hispanic, population
* `NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population
* `NH_OTHER`: Other race, non-hispanic, population
* `NH_2MORE`: Two or more races, non-hispanic, population
* `HISP`: Hispanic population
* `H_WHITE`: White, hispanic, population
* `H_BLACK`: Black, hispanic, population
* `H_AMIN`: American Indian and Alaska Native, hispanic, population
* `H_ASIAN`: Asian, hispanic, population
* `H_NHPI`: Native Hawaiian and Pacific Islander, hispanic, population
* `H_OTHER`: Other race, hispanic, population
* `H_2MORE`: Two or more races, hispanic, population
* `VAP`: Total voting age population
* `HVAP`: Hispanic voting age population
* `WVAP`: White, non-hispanic, voting age population
* `BVAP`: Black, non-hispanic, voting age population
* `AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population
* `ASIANVAP`: Asian, non-hispanic, voting age population
* `NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population
* `OTHERVAP`: Other race, non-hispanic, voting age population
* `2MOREVAP`: Two or more races, non-hispanic, voting age population
* `CD_12`: 2012 enacted congressional district ID
* `CD_16`: 2016 enacted congressional district ID
* `HDIST_11`: 2011 enacted House of Delegates district ID
* `HDIST_REM`: 2019 remedial House of Delegates district ID
* `SENDIST`: 2011 enacted state senate district ID

## Projection
This shapefile uses a NAD83/Virginia Lambert projection or EPSG: 3968.

## Rating
We give this shapefile an A rating. It was compiled by the Princeton Gerrymandering Project with demographic information added from the 2010 Decennial Census by MGGG. For more information about its creation visit https://openprecincts.org/va/. 
