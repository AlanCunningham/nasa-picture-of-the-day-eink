# Nasa picture of the day eink

Displays the NASA picture of the day on a Pimoroni Inky Impression (7.3") eink display.

## API keys
This project requires a NASA developer API key, [available here](https://api.nasa.gov/).
Add your API key to `nasa_api_key` in settings.py.

## Installation and running
Clone the project and install the dependencies into a python virtual environment:
```
# Clone the repository
$ git clone git@github.com:AlanCunningham/nasa-picture-of-the-day-eink.git

# Create a python virtual environment
$ python3 -m venv venv

# Activate the virtual environment
$ source venv/bin/activate

# Install the python dependencies using the requirements.txt file provided
(venv) $ pip install -r requirements.txt
```

You can now run main.py to fetch today's image of the day onto the display:
```
(venv) $ python main.py
```
