# macaw
ML deployment tool, currently only deploys logistic regressions :-)

NOTES
-----
All code has been tested on MacOS Monterey 12.6, running Docker Desktop 4.12.0.

REQUIREMENTS
------------

- Python3
- Docker

SETUP
-----

From inside of `macaw/`, run
```
source setup.sh
```
then
```
python3 db/migrations/model_service.py
```

This will install pip requirements,
set up a postgres docker container,
and create the relevant tables in database.

RUNNING
-------
From inside of `macaw/`, run

```
python3 modeling/create_test_models.py
```
then
```
python3 model_service/main.py
```
to run the model service server
