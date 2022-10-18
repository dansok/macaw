# macaw
ML deployment tool, currently only deploys logistic regressions :-)

NOTES
-----
All code has been tested on MacOS Monterey 12.6,
running Python 3.10.6, and Docker Desktop 4.12.0.

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
See the contents of these scripts for specifics.

---
**NOTE** that if you want to run python scripts from a new
terminal session, you must run the first command in the
`setup.sh` script in that session from inside of `macaw/`:

```
export PYTHONPATH=$(pwd):$(echo $PYTHONPATH)
```

RUNNING
-------
From inside of `macaw/`, run

```
python3 modeling/create_test_models.py
```
then
```
python3 model_service/run.py
```
to run the model service server
