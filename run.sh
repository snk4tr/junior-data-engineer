#!/usr/bin/env bash

####################################  SCRIPT ARGUMENTS  ####################################
port=$1
testing=${2:-0}

####################################  LOCAL VARIABLES  ####################################

containerName=junior-data-engineer-$RANDOM
projectDir=$(pwd)
imageName=pilrus-kastryulin-interview
imageTag=v19.09

####################################  BUILD / LOAD IMAGE  ####################################

# If there is no image on current node
if [[ "$(docker images -q ${imageName}:${imageTag} 2> /dev/null)" == "" ]]; then
  echo "Image does not exist. Building image from Dockerfile..."
  docker build \
    -t ${imageName}:${imageTag} \
    -f Dockerfile .
fi

echo "The image was built. Running container..."

####################################  RUN CONTAINER  ####################################

runCommand='flask run --host=0.0.0.0'
if [[ "${testing}" == "Test" ]]; then
  runCommand='python -m pytest tests/'
fi

docker run \
  --runtime=nvidia \
  --rm \
  --name ${containerName} \
  -v "${projectDir}":"${projectDir}" \
  -p "${port}":5000 \
  --user "$(id -u)":"$(id -g)" \
  --ipc=host \
  ${imageName}:${imageTag} \
  ${runCommand}
