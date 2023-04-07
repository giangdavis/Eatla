application that takes user input of what they ate in the form of natural language and inputs into fatsecret app for you

INSTALLATION:

FRONTEND
cd frontend/fatbot
npm install

BACKEND
cd backend
source venv/bin/activate
pip3 install -r requirements.txt

RUNNING THE APPLICATION:
In frontend/fatbot
npx expo start

In backend
uvicorn main:app --reload
