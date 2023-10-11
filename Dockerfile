FROM python:3.10-bullseye

WORKDIR /usr/src/app

copy . .

RUN pip install streamlit


CMD [ "bash", "run.sh"]