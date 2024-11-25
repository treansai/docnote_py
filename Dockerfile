FROM python:3.12

RUN pip install transformers
RUN pip install torch
RUN pip install flask

COPY . .

CMD ["python", "filigran_app/__main__.py"]
