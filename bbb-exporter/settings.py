import os
import api_lib
from helpers import validate_api_base_url

MAJOR = 0
MINOR = 2
BUGFIX = 0

VERSION = "{}.{}.{}".format(MAJOR, MINOR, BUGFIX)

debug_env = os.getenv("DEBUG", "false")
DEBUG = True if debug_env.lower() == "true" else False

API_BASE_URL = validate_api_base_url(os.environ["API_BASE_URL"])
# SSH into server and run: `$ bbb-conf --secret` to get secret
API_SECRET = os.environ["API_SECRET"]

API_CLIENT = api_lib.Client(API_BASE_URL, API_SECRET)

PORT = int(os.getenv("PORT", 9688))
BIND_IP = os.getenv("BIND_IP", "0.0.0.0")

# Global (gasp.) variable flag that is used to mark if communicating with BigBlueButton's API is possible.
# Used to set the `bbb_api_up` metric.
_api_up = False
