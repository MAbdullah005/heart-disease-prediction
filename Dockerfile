#    0u19820# base image
FROM python:3.13-slim

# woking dir
WORKDIR /app
# copy  
COPY  requirements.txt .
# Run install dependencies
RUN  pip install --no-cache-dir -r requirements.txt
# Copy all project files (including frontend.py and app.py)
COPY  . .
#  Expose FastAPI (8000) and Streamlit (8501) ports
EXPOSE 8000

EXPOSE 8501

# Run both FastAPI and Streamlit using a shell
CMD [ "bash","-c","uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run frontend/app1.py --server.port=8501 --server.address=0.0.0.0" ]