#!/bin/bash

echo "Instalando dependencias..."
pip3 install -r requirements.txt

echo "Lanzando aplicación..."
python3 src/main.py