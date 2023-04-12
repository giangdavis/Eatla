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
PORT=8001
echo "PWD is: ${PWD}"
echo "ROOTDIR PATH SET TO: ${ROOTDIR}"
echo "FRONTENDAPPDIR PATH SET TO: ${FRONTENDAPPDIR}"
echo "BACKENDAPPDIR PATH SET TO: ${BACKENDAPPDIR}"


echo "Checking if port ${PORT} is already in use..."

if lsof -Pi :${PORT} -sTCP:LISTEN -t >/dev/null ; then
    echo "Port ${PORT} is already in use. Killing the process..."
    lsof -t -i :${PORT} | xargs kill -9
fi

# Detect the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux OS
    cd $BACKENDAPPDIR && uvicorn main:app --host 0.0.0.0 --port $PORT &
    cd $FRONTENDAPPDIR && npx expo start
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    cd $BACKENDAPPDIR && uvicorn main:app --host 0.0.0.0 --port $PORT &
    osascript -e 'tell app "Terminal" to do script "cd '$FRONTENDAPPDIR' && npx expo start"'
else
    echo "Unsupported operating system: $OSTYPE"
    exit 1
fi


