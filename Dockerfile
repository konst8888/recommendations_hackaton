WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.conf.py", "-t","300" ,"-b", ":8000", "app:app"]
