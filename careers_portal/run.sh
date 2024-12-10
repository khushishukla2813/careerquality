
#!/bin/bash

# Hardcoded port number 5000
PORT=8000

# Find the PID of the process using port 5000
PID=$(lsof -t -i :$PORT)

# Check if the PID ißs found
if [ -z "$PID" ]; then
    echo "No process is using port $PORT."
    
else
    # Kill the process using the PID
    echo "Killing process with PID $PID on port $PORT..."
    kill -9 $PID
    echo "Process with PID $PID has been terminated."
fi
[ -z "$VIRTUAL_ENV" ] && source ../env/bin/activate
pip install -r req.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
