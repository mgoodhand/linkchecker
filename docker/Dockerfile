FROM python:2.7

RUN pip install linkchecker==9.3
RUN sed -i.bak '/2.2.0/,+1 d' /usr/local/lib/python2.7/site-packages/linkcheck/__init__.py

ENTRYPOINT ["linkchecker"]

