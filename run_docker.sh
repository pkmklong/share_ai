docker run -v ${HOME}/.aws/credentials:/root/.aws/credentials:ro -v ${HOME}/.aws/config:/root/.aws/config:ro -p 8501:8501 app:latest
