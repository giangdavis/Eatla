# Application that takes user input of what they ate in the form of natural language and inputs into fatsecret app for you

INSTALLATION:

### FRONTEND
```
  cd frontend/fatbot
  npm install
```
### BACKEND
```
  cd backend
  source venv/bin/activate
  pip3 install -r requirements.txt
```
### RUNNING THE APPLICATION:
In frontend/fatbot
```
  npx expo start
```
In backend
```
  uvicorn main:app --reload
```




# Windows Dev Environment Setup Steps from a fresh windows 10 OS install:

### Here are the steps to set up WSL 2 Ubuntu via Windows Terminal:

  1. Enable WSL 2 on Windows: To use WSL 2, you need to have Windows 10 version 1903 or higher installed on your system. You also need to enable WSL 2 feature on your Windows machine. To do this, open PowerShell as an administrator and run the following command:

  ```
  dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
  dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
  ```
  
  2. Download and install the Linux kernel update package: To use WSL 2, you need to download and install the Linux kernel update package. You can download it from the official Microsoft website.

  3. Download and install Ubuntu from the Microsoft Store: To download and install Ubuntu on your Windows machine, open the Microsoft Store app and search for        "Ubuntu."     Click the "Get" button to download and install it.

  4. Launch Ubuntu and set up your username and password: Once the installation is complete, launch Ubuntu from the Start menu. You will be prompted to set up your username and password.

  5. Install Windows Terminal: Windows Terminal is a new terminal application that allows you to run multiple shells and command-line applications simultaneously. You can download and install it from the Microsoft Store.

  6. Add Ubuntu to Windows Terminal: Open Windows Terminal and click the downward-facing arrow in the tab bar to open the drop-down menu. Click "Settings" to open the settings file in your default text editor. Scroll down to the "profiles" section and add the following to the "list" array:

  ```json
  {
     "guid": "{insert-unique-guid-here}",
     "name": "Ubuntu",
     "commandline": "wsl.exe -d Ubuntu",
     "icon": "path/to/icon"
  }
  ```
Replace "{insert-unique-guid-here}" with a unique identifier, and "path/to/icon" with the path to an icon image you want to use for the Ubuntu profile.

  7. Save the settings file and restart Windows Terminal: Save the settings file and restart Windows Terminal. You should now see the Ubuntu profile in the drop-down menu.
