FROM python:latest

COPY . ./tbot
WORKDIR ./tbot

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "bot.py" ]