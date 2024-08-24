   name: Run Python Script

   on:
     push:
       branches: [main]

   jobs:
     zip-and-send:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.x'

         - name: Install dependencies 
           run: pip install -r requirements.txt

         - name: run script
           run: python main.py
