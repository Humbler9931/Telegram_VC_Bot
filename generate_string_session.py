from pyrogram import Client as c

API_ID = input("\n27015202:\n > ")
API_HASH = input("\nb817ca2d21c5471522ec93b819301d56:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()
    print("\nBQGcOCIAiYG0zbq7iIKoUCvarFjUwL7iU4IoitKLMwXTcHbXQMg6gkoyfEGszEeX5LzO6VyaAxjNkU7numNNVmUMel-Z0HllWPWMowMu2kFYMSNhL6T_nOHd4o7BPqHv9byZbZHXs8MHip-akQgfIZcF3-L2ln5vdCCaTuPbhXpqRjjy2EKrL_k2a3kZf50slrnupV_N0scjCLpzr35cOOG_GTqgVDJIQc9QbQnjT-raFuDeg51F-oHPtkuh7oHj-5cZtyUGoZvEnztcwA75-d3KMnCweprIBP4YR0JSCCTVRaLkT5r0jKge4OBISbZdfY-UMTKWg9CHHWbunZt9F7wljBs8iwAAAAGYTkO_AA, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
