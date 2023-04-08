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


echo "ENTERING FRONTEND APP DIRECTORY: ${FRONTENDAPPDIR}"
cd ${FRONTENDAPPDIR}; npm install

echo "ENTERING BACKEND APP DIRECTORY: ${FRONTENDAPPDIR}"
cd ${BACKENDAPPDIR}; source venv/bin/activate; pip3 install -r requirements.txt


echo "ENTERING FRONTEND APP DIRECTORY: ${FRONTENDAPPDIR}"
cd ${FRONTENDAPPDIR}; npx expo start

echo "ENTERING BACKEND APP DIRECTORY: ${FRONTENDAPPDIR}"
cd ${BACKENDAPPDIR}; uvicorn main:app --reload


