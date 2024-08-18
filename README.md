# ebird-custom-alerts

Custom new bird alerts using data from the ebird api and by scraping the ebird page to get life lists for users with Selenium

## Create virtual environment

1. Create a python virtual environment according to the IDE/OS you're using.
    - [VS Code Docs](https://code.visualstudio.com/docs/python/environments)
2. Install required packages in your virtual environment
    - ```pip install -r requirements.txt```

## Create config files

There are two primary config files you will need to create and place in the project root directory:

**alert-configs.json**: This file contains what hotspots should be monitored for each user.

```json
{
    "dummy_user": {
        "hotspots": [
            "Dummy Hotspot"
        ]
    }
}
```

**secrets.json**: This file contains secrets for the Ebird API & Ebird users.

```json
{
    "ebird": {
        "user_credentials": {
            "dummy_user": "dummy_password"
        },
        "apikey": "dummy-apikey"
    }
}
```

## Usage

1. Create config files
2. Run ```python main.py```
