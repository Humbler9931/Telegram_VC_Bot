HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["27015202"])
    API_HASH = environ["b817ca2d21c5471522ec93b819301d56"]
    SESSION_STRING = environ[
        "BQGcOCIAiYG0zbq7iIKoUCvarFjUwL7iU4IoitKLMwXTcHbXQMg6gkoyfEGszEeX5LzO6VyaAxjNkU7numNNVmUMel-Z0HllWPWMowMu2kFYMSNhL6T_nOHd4o7BPqHv9byZbZHXs8MHip-akQgfIZcF3-L2ln5vdCCaTuPbhXpqRjjy2EKrL_k2a3kZf50slrnupV_N0scjCLpzr35cOOG_GTqgVDJIQc9QbQnjT-raFuDeg51F-oHPtkuh7oHj-5cZtyUGoZvEnztcwA75-d3KMnCweprIBP4YR0JSCCTVRaLkT5r0jKge4OBISbZdfY-UMTKWg9CHHWbunZt9F7wljBs8iwAAAAGYTkO_AA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARJTGY-IXVVUH-LHBMCC-UDBKZD-ARQ"]
    CHAT_ID = int(environ["-1001992548930"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 27015202
    API_HASH = "b817ca2d21c5471522ec93b819301d56"
    ARQ_API_KEY = "ARJTGY-IXVVUH-LHBMCC-UDBKZD-ARQ"
    CHAT_ID = -1001992548930
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://arq.hamker.in"
