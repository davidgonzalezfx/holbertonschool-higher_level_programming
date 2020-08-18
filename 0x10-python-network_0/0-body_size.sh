#!/bin/bash
# body size
curl -sI $1 | grep "content-length:" | cut -d' ' -f2
