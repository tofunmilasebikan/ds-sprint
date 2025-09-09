** Goal:** build a recommendation baseline you can run on student laptop in minutes, then improve it a little
**why:** recommendation is core to streaming (data -> split -> metrics -> result)

#what I built
**Baseline** recommend the most popular movies overall excluding items a user already watched
**evaluation** MAP@10 and NDCG@10 on a hold out of each user's interaction (a realistic 'what will they watch next?' setup)

##DATA
**MovieLens `ml-latest-small`** (free, public): `ratings.csv`, `movies.csv`
Files live locally at: `data/raw/ml-latest-small/`
