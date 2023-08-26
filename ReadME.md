# Audio Extraction Django Project

This is a Django project that allows users to upload audio files, extract audio features, and stream audio files.

## Getting Started

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the project dependencies using the command: `pip install -r requirements.txt`
4. Make database migrations: `python manage.py makemigrations` and `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`

## Usage

- Visit `http://localhost:8000/admin` to log in to the admin panel and manage audio features.
- Visit `http://localhost:8000/audioFeatures` to upload audio files and view extracted features.

## Dependencies

- Python (>=3.6)
- Django
- mutagen
- pydub

