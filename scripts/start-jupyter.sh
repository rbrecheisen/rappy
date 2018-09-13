#!/bin/bash

docker run -it --name jupyter --rm \
  -p 8888:8888 -v $(pwd)/notebooks:/notebooks jupyter/datascience-notebook start-notebook.sh \
    --NotebookApp.token='' \
    --NotebookApp.notebook_dir=/notebooks
