FROM python:3.7
EXPOSE 8501
WORKDIR mydir
COPY . .
RUN pip install streamlit
RUN python setup.py install 
CMD streamlit run src/reflect/app/streamlit_app.py

