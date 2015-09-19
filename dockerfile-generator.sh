#!/usr/bin/env bash
# Generate Dockerfile file for different git project

# Need a dockerfile-template.txt file to start
PRJ_NAME=$(git remote -v  | grep fetch | sed "s#^.*/\(.*\).git (fetch)#\1#")
export CODEPATH="$(dirname $(dirname $(readlink -f $0)))/$PRJ_NAME"

# local machine pip from Aliyun CDN
if [ "$USER" = "neo" -o "$USER" = "liao" ]; then
    export PIP_INSTALL_SUFFIX="--index-url http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com"
fi

# Single quotes here to prevent expanding varaibles
VARS='$CODEPATH:$PIP_INSTALL_SUFFIX'

OUTPUT="Dockerfile"
echo "# Generated by $0" > "$OUTPUT"
envsubst "$VARS" < dockerfile-template.txt >> "$OUTPUT"

echo "Generate new file: $OUTPUT"
