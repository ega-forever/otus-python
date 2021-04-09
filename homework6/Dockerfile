FROM python:3.8-buster

WORKDIR /var/app

COPY . .
RUN ls
RUN pip install pipenv && \
    pipenv install --system --deploy

EXPOSE 8080

CMD ["python", "app.py"]
# to run container on port 8080 do: docker run -p 8080:8080 <container_name>