. venv/bin/activate;
pip3 install -r requirements.txt;
export PYTHONPATH=$(pwd):$(echo $PYTHONPATH);
docker compose -f docker/postgres/docker-compose.yml up -d;
python3 db/migrations/model_service.py;
