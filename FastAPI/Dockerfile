FROM python:3.11
WORKDIR /myapp
COPY . /myapp
RUN pip install -r requirements.txt
RUN pip install "fastapi[standard]"
EXPOSE 8000
CMD [ "fastapi", "dev", "main.py" ]