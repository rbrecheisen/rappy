#!/usr/bin/env bash
pip freeze | xargs pip uninstall -y
