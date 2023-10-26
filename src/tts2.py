import google.cloud.texttospeech as tts
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./src/service.json"


# Create a text-to-speech client.
client = tts.TextToSpeechClient()

# Set the text input to be synthesized.
synthesis_input = tts.SynthesisInput(
    text="మేము ప్రస్తుతం ఆస్ట్రోవర్స్ ప్రాజెక్ట్‌లో పని చేస్తున్నాము. మా ప్రాజెక్ట్ ప్రధానంగా ఒకే భాష వీడియోను భారతీయ భాషల్లోకి అనువదించడంపై దృష్టి పెడుతుంది.")
# Build the voice request, select the language code ("en-US")
# and the gender ("neutral").
voice = tts.VoiceSelectionParams(
    language_code="te",
    ssml_gender=tts.SsmlVoiceGender.MALE,
)

# Select the type of audio file you want returned.
audio_config = tts.AudioConfig(
    audio_encoding=tts.AudioEncoding.MP3,
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type.
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)

# Print the response.
print("Audio content written to output.mp3")