#!/bin/bash
#
#
# Description: Quick WSL2 Ubuntu setup script to update required developer packages and setup the dev environment
#
# Usage: sudo chmod +x ./windowsDevEnvSetup.sh
#        sudo ./windowsDevEnvSetup.sh
#
#
ROOTDIR=${PWD}
echo "PWD is: ${PWD}"
echo "ROOTDIR VARIABLE SET TO: ${ROOTDIR}"



# SECTION BEGIN ----- Install packages and dependencies

InstallPackages () {

    # Install Python and Pip
    sudo apt update -y && sudo apt upgrade -y
    sudo apt install python3 -y
    python3 --version
    sudo apt install python3-pip -y
    pip3 --version
    # Install Npm
    sudo apt install nodejs npm -y
    sudo apt update -y && sudo apt upgrade nodejs -y
    sudo npm install -g npm@latest
    npm --version
    nodejs --version

}

FrontendInstall() {

    echo "FRONTEND INSTALL BEGIN - PWD: ${PWD}"
    cd "${ROOTDIR}/frontend/fatbot"
    npm install

}

BackendInstall() {

    echo "BACKEND INSTALL BEGIN - PWD: ${PWD}"
    cd ${ROOTDIR}/backend
    source venv/bin/activate
    pip3 install -r requirements.txt
    # For WSL2 Ubuntu dev environments, we must export the PATH of the Python package executable scripts installed by pip
    #   or else we will need to specify the full path of these scripts when we want to run it. 
    #   The optional PATH mod command is below:
    echo "HOME DIRECTORY IS: ${HOME}"
    echo "BASHRC FILE PATH IS: ${HOME}/.bashrc"
    if ! grep "export PATH=" "${HOME}/.bashrc"; then
        echo -e "\n\n\n# EXPORT PATH VARIABLE FOR PYTHON PACKAGES WITH EXECUTABLE SCRIPTS (such as uvicorn)\n" \
            >> ${HOME}/.bashrc
        echo "export PATH=\"$HOME/.local/bin:$PATH\"" >> ${HOME}/.bashrc
    fi
    cat ${HOME}/.bashrc
    # Install the Expo CLI globally using npm now that the path variable is updated
    npm install -g expo-cli
    npm install fs.promises

}

# SECTION END ----- Install packages and dependencies



Main() {

    InstallPackages
    FrontendInstall
    BackendInstall

}

Main 

exit 0
