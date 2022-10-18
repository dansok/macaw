export PYTHONPATH=$(pwd):$(echo $PYTHONPATH);
python3 -m venv venv
source venv/bin/activate;
pip3 install -r requirements.txt;
docker compose -f docker/postgres/docker-compose.yml up -d;
