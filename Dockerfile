FROM caida/bgpstream
COPY . /app/
WORKDIR /app
RUN apt install python3-pip -y && \
    python3 -m pip install -r requirements.txt


ENTRYPOINT ["bash"]
