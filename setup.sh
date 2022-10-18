export PYTHONPATH=$(pwd):$(echo $PYTHONPATH);
source venv/bin/activate;
pip3 install -r requirements.txt;
docker compose -f docker/postgres/docker-compose.yml up -d;
