from os import getenv

from dotenv import load_dotenv

load_dotenv()
# Mandatory VARS
API_ID = int(getenv("API_ID", "1480988"))
API_HASH = getenv("API_HASH", "be76b2fd25b50222b0e1eee141d6a259")
BOT_TOKEN = getenv("BOT_TOKEN", "5767549463:AAFpKnXcBSQkq8_scZwG_Wv3k5Twlw744mE")
STRING_SESSION = getenv("STRING_SESSION", "AQCWPW7925QnJEl7uo5rBnnzctHuZwl0X6XkBb2rbhaguA-JV01tqhA0rA50NAporQGP_9Cd5Vx6Bz7CvVjUYhZ6LORkZ86YtnTAJhbPxrfUBeEBKCyoHvUYMV9C2DXDYOS6EXNB918yzJB7nhTWxy_NhYzsB24CRD5pIcX0FV7tmBEpDPeCMCAixGBFYdu0ffWPiFYYP6ozY2J94Rc_vyh9bycBgKiQ8ldOtHsBlAhrxyinq0Y9PbNZpENCXtqjHNbcGDDWW0jUrRSSKnOSa7G2D7o1j8NUlF0FAwo_tgLFblehBippHC5pxS7oiU21WKOVuqraVrNnOCVmItNftP6nAAAAAUp_RwIA")
VIDEO_CHAT_ID = int(getenv("VIDEO_CHAT_ID", "-1001767332965"))
CUSTOM_ICON = getenv("CUSTOM_ICON")
