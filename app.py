import os
from flask import Flask, render_template, jsonify, request
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioDataStream, ResultReason
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import imdb
import speech_recognition as sr
import tempfile

# Azure Text-to-Speech configuration
azure_key = "88f27e0fe0a745fb9d4dc98ebd5f41f5"  # Replace with your Azure subscription key
azure_region = "eastus"  # Replace with your Azure region

# Configure speech synthesis
speech_config = SpeechConfig(subscription=azure_key, region=azure_region)
audio_config = AudioOutputConfig(use_default_speaker=True)
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Initialize IMDb instance
moviesdb = imdb.IMDb()

# Function to convert text to speech using Azure Text-to-Speech
def speak(text):
    try:
        result = synthesizer.speak_text_async(text).get()
        if result.reason == ResultReason.SynthesizingAudioCompleted:
            # Use a temporary file for storing audio
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
                temp_audio_file_path = temp_audio_file.name
                audio_data_stream = AudioDataStream(result)
                audio_data_stream.save_to_wav_file(temp_audio_file_path)
                return temp_audio_file_path  # Return the file path to the saved audio
        else:
            print(f"Speech synthesis failed: {result.reason}")
            return None
    except Exception as ex:
        print(f"Exception during speech synthesis: {ex}")
        return None

# Function to get audio input using microphone
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        return said.lower()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_audio')
def get_audio_route():
    movie_name = get_audio()
    if movie_name:
        audio_file = speak(f"You said: {movie_name}")
        if audio_file:
            return jsonify({"movie_name": movie_name, "audio_file": audio_file})
    return jsonify({"movie_name": movie_name, "audio_file": None})

@app.route('/search_movie', methods=['GET', 'POST'])
def search_movie():
    if request.method == 'POST':
        movie_name = request.form['movie_name']
    else:
        movie_name = request.args.get('movie_name')

    if not movie_name:
        return jsonify({"error": "No movie name provided"})

    movies = moviesdb.search_movie(movie_name)
    
    if len(movies) == 0:
        return jsonify({"error": "No result found"})
    
    movie = movies[0]
    info = movie.getID()
    movie = moviesdb.get_movie(info)

    title = movie.get('title', 'N/A')
    year = movie.get('year', 'N/A')
    rating = movie.get('rating', 'N/A')
    plot = movie.get('plot outline', 'N/A')
    image_url = movie.get('full-size cover url', None)

    audio_text = f"Movie found: {title}. Year: {year}. Rating: {rating}. Plot: {plot}"
    audio_file = speak(audio_text)

    return jsonify({
        "title": title,
        "year": year,
        "rating": rating,
        "plot": plot,
        "image_url": image_url,
        "audio_file": audio_file
    })

if __name__ == '__main__':
    app.run(debug=True)
