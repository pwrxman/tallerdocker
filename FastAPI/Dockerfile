FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim
WORKDIR /myapp
COPY . /myapp
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "fastapi", "dev", "main.py" ]