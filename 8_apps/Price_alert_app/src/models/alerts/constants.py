__author__ = "esobolie"


URL = "https://api.mailgun.net/v3/sandbox64ae580e2e65a4956ea85.mailgun.org"
API_KEY = "key-081424db580be4552196f5"
FROM = "Mailgun Sandbox <postmaster@sandbox6870580e2e65a4956ea85.mailgun.org"
ALERT_TIMEOUT = 10
COLLECTION = "alerts"

"""
    'requests.post(
    "https://api.mailgun.net/v3/sandbox6870e258e2e65a4956ea85.mailgun.org/messages",
    auth=("api", "key-081424db580be2e196f5"),
    data={"from": "Mailgun Sandbox <postmaster@sandbox68700e2e65a4956ea85.mailgun.org>",
          "to": "E <r4@gm>",
          "subject": "Hello E",
          "text": "Congratulations E, you just sent an email with Mailgun!  You are truly awesome!"})'
"""
