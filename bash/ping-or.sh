#!/bin/bash
# https://szerverlabor.hu/ - roland@szerverlabor.hu
HOST="google.com"
ping -c 1 $HOST || echo "$HOST unreachable."
