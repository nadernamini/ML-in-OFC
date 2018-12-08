#!/bin/sh

cd ofc-1 && \
gunzip -c data.tar.gz | tar xopf - && \
cd ../ofc-2 && \
gunzip -c data.tar.gz | tar xopf - && \
cd ../ofc-3 && \
unzip -a data.zip
