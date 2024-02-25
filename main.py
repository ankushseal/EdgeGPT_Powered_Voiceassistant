import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import re
import whisper
import json
import boto3
import pydub
from pydub import playback
import speech_recognition as sr

file=open("config.json")
config=json.load(file)

recognizer = sr.Recognizer()
wake = "Hi"

def get_wake(trigger):
    if trigger.__contains__(wake):
        trigger=wake
        return wake
    if wake in trigger.lower():
        return wake
    else:
        return None

def genarate_output_audio(text,output_file_name):
    polly = boto3.client(
        'polly',
        region_name = "us-east-1",
        aws_access_key_id = config['aws_access_key_id'],
        aws_secret_access_key = config["aws_secret_access_key"]
    )
    response= polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Kajal",
        Engine="neural"
    )
    with open(output_file_name,'wb') as f:
        f.write(response['AudioStream'].read())

def play_audio(file):
    sound=pydub.AudioSegment.from_file(file,format="mp3")
    playback.play(sound)

async def main():
    end = "i"
    while (end.lower() !="bye"):
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Wating for START COMMAND.....")
            while True:
                audio=recognizer.listen(source)
                try:
                    with open("audio.wav","wb") as f:
                        f.write(audio.get_wav_data())
                    #using whisper preloaded tiny model
                    model=whisper.load_model("base")
                    result=model.transcribe("audio.wav")
                    phrase=result["text"]
                    print(f"You said : {phrase}")
                    trigger=get_wake(phrase)
                    if trigger is not None:
                        break
                    else:
                        print("Not a Start Command..Try again!!!")
                        print("Not a Start Command..Try again!!!")
                except Exception as e:
                    print("Error transcribing audio : "+e)
                    continue
            genarate_output_audio('How can I help you today?', "response.mp3")
            while True:
                print("Speak a prompt....")
                play_audio('response.mp3')
                audio=recognizer.listen(source,15,3)

                try:
                    with open("audio_prompt.wav","wb") as f:
                        f.write(audio.get_wav_data())
                    model=whisper.load_model("tiny")
                    result=model.transcribe("audio_prompt.wav")
                    user_input=result["text"]
                    end=user_input
                    print(f"you said : {user_input}")
                except Exception as e:
                    print("error transcribing audio: "+e)
                    continue
                cookies = json.loads(open("bing_cookies_alternative.json", encoding="utf-8").read())  # might omit cookies option
                bot = await Chatbot.create(cookies=cookies)
                # bot = await Chatbot.create() # Passing cookies is "optional", as explained above
                response = await bot.ask(prompt=user_input, conversation_style=ConversationStyle.precise, simplify_response=True)
                bot_response = str(response['text'])
                bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
                bot_response = re.sub('[*,*]', '', bot_response)
                print(bot_response)
                genarate_output_audio(bot_response,"response.mp3")
                play_audio('response.mp3')

                await bot.close()

if __name__ == "__main__":
    asyncio.run(main())