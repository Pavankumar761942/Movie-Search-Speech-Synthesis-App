Movie Search & Speech Synthesis App
This application allows users to search for movie information using text input and speech recognition. It integrates Azure Cognitive Services for text-to-speech functionality and IMDbPy for retrieving movie details.

Features
Text Input Search: Users can enter a movie name to search for its details such as title, year, rating, and plot.
Speech Input: Alternatively, users can use voice commands to search for movies.
Speech Output: The application provides audio feedback using Azure Text-to-Speech, announcing the found movie details.

Technologies Used
Flask: Web framework used for building the application backend.
Azure Cognitive Services: Specifically, the Speech SDK for speech recognition and synthesis.
IMDbPy: Python package to fetch movie details from IMDb.
