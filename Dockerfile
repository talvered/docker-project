FROM python
COPY ./app.py .
EXPOSE 8080
RUN pip3 install -U Flask
CMD flask run --port=8080