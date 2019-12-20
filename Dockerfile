FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY container-entrypoint.sh / 
RUN git clone --single-branch -b mimic-csv2 -- https://github.com/mfens98/mimic.git

RUN pip3 install --no-cache-dir ./mimic

EXPOSE 8900
ENTRYPOINT ["/container-entrypoint.sh"]
CMD ["twistd", "-n", "mimic"]
