import openai 

API_KEY='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'     
media_file_path ='../traductia/audios/creole.mp3'
media_file = open(media_file_path,'rb') 
model_id='whisper-1'
"""
def whisper_trancript(request):
    try:
        media_file = open(media_file_path,'rb') 
        transcript = openai.Audio.transcribe(
            api_key=API_KEY,
            model= model_id,
            file= media_file,
            language = "es",
            response_format='text'
        ) 
        print(transcript)        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
"""
with open("./traductia/audios/creole.mp3", "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        api_key=API_KEY,
        file = audio_file,
        model = "whisper-1",
        response_format="text",
        language="es"
    )
print(transcript)
