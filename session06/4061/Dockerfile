FROM pytorch/pytorch:2.8.0-cuda12.9-cudnn9-runtime

WORKDIR /app
COPY train.py .

RUN pip install --no-cache-dir matplotlib scikit-learn

CMD ["python", "train.py"]