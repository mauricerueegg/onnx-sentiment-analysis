# docker build -t mosazhaw/roberta-onnx .
# docker run --name roberta-onnx -p 9000:5000 -d mosazhaw/roberta-onnx

FROM python:3.12.7

# Copy Files
WORKDIR /usr/src/app
COPY . .

# Install
RUN pip install -r requirements.txt

# Docker Run Command
EXPOSE 5000
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]