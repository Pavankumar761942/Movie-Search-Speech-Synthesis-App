Movie Search & Speech Synthesis App
This application allows users to search for movie information using text input and speech recognition. It integrates Azure Cognitive Services for text-to-speech functionality and IMDbPy for retrieving movie details.

Features
Movie Search: Allows users to search for movies by name using IMDb's database.
Speech Synthesis: Converts movie details into speech using Azure Text-to-Speech service.
Real-Time Speech Interaction: Users can interact with the application using speech input via microphone.
Text-Based Interaction: Users can also input movie names via text input for search and speech synthesis.
Display Movie Information: Provides details such as title, year, rating, and plot summary of the searched movies.
Integrated AI Voice: Uses Azure's AI capabilities to provide synthesized speech output.

Requirements
Python 3.6+
Flask
IMDbPY
SpeechRecognition
Azure Cognitive Services (Text-to-Speech)
Requests

Installation
Clone the repository:
git clone https://github.com/Pavankumar761942/Movie-Search-Speech-Synthesis-App.git
cd Movie-Search-Speech-Synthesis-App

Create a virtual environment and activate it:
Windows:
python -m venv myenv
myenv\Scripts\activate

macOS/Linux:
python -m venv myenv
source myenv/bin/activate

Install the required packages:
pip install IMDbPY
pip install pyttsx3
pip install SpeechRecognition
pip install DateTime
pip install pyaudio
pip install flask
pip install azure-cognitiveservices-speech
pip install msrest
pip install azure-cognitiveservices-vision-computervision
pip install azure-storage-blob
pip install azure-keyvault-secrets
pip install Flask azure-cognitiveservices-speech imdbpy SpeechRecognition

Run the Flask application 
python app.py

Access the Application:
Open your web browser and go to http://127.0.0.1:5000 to interact with the application.

Using the Application:
Text Input: Enter the movie name in the text input field and click on the search button to get movie details.
Speech Input: Click on the microphone icon to use speech recognition for searching movies.
Speech Synthesis: Once movie details are retrieved, click on the "Read Aloud" button to hear the movie details.



