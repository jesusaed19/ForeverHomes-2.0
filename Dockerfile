# 
FROM python:3.9

#
# ENV PYTHONPATH "${PYTHONPATH}:/code/app"
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
# 

COPY . /code/

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]