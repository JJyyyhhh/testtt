FROM python:3.10
WORKDIR /app
RUN apt install git
RUN git clone https://github.com/yejif15/my-flask-project.git /app
RUN pip install -r requirements.txt
ENV FLASK_APP "pybo"
ENTRYPOINT ["python3"]
CMD ["-m", "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000/tcp
