FROM python:3.8
RUN mkdir -p /app/
WORKDIR /app/
COPY * /app/
RUN pip3 install -r requirements.txt
CMD python app.py
