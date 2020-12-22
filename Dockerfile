FROM python:3.8

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/webapp

WORKDIR ${PROJECT_DIR}

COPY Pipfile ${PROJECT_DIR}/

RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "python", "-m", "ManPageBot"]