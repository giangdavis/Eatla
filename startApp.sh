#!/bin/bash
#
#
# Description: Use this script to quickly startup the application once the dev env is setup
#
# Usage: ./startApp.sh
# If necessary, do chmod +x ./startApp.sh
#
#
ROOTDIR=${PWD}
FRONTENDAPPDIR=${ROOTDIR}/frontend/fatbot
BACKENDAPPDIR=${ROOTDIR}/backend
echo "PWD is: ${PWD}"
echo "ROOTDIR PATH SET TO: ${ROOTDIR}"
echo "FRONTENDAPPDIR PATH SET TO: ${FRONTENDAPPDIR}"
echo "BACKENDAPPDIR PATH SET TO: ${BACKENDAPPDIR}"


#!/bin/bash

# Detect the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux OS
    cd $BACKENDAPPDIR && uvicorn main:app --host 0.0.0.0 --port 8001 &
    cd $FRONTENDAPPDIR && npx expo start
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    cd $BACKENDAPPDIR && uvicorn main:app --host 0.0.0.0 --port 8001 &
    osascript -e 'tell app "Terminal" to do script "cd '$FRONTENDAPPDIR' && npx expo start"'
else
    echo "Unsupported operating system: $OSTYPE"
    exit 1
fi


