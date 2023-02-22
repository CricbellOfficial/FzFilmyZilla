if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Ganeshmrxx/FzFilmyZilla.git /FzFilmyZilla
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /FzFilmyZilla
fi
cd /FzFilmyZilla
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
echo "Starting Bot...."
nohup python3 bot.py &
