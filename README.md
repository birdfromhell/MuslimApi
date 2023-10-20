# Project Title: Muslim API

## Overview
This API provides access to data related to Asmaul Husna and Quran Surah. It's built with FastAPI and reads data from a JSON file. 

## How to Run
1. Install required packages with `pip install fastapi uvicorn`.
2. Replace 'asmaul-husna.json' and 'quran.json' with the path to your JSON files.
3. Save the script as 'main.py' for example.
4. From the terminal, run `uvicorn main:app --reload`.

## Endpoints
There are six available endpoints:

**1. GET /** 
Return a welcome message.

**2. GET /asmaul-husna**
Returns all data inside 'asmaul-husna.json' file.

**3. GET /asmaul-husna/{id}**
Returns specific data based on id from 'asmaul-husna.json' file. If the id does not exist, it will return an HTTPException with status code 404.

**4. GET /asmaul-husna/random**
Returns a random data from 'asmaul-husna.json' file.

**5. GET /quran**
Returns all data inside 'quran.json' file.

**6. GET /quran/{nomor}**
Returns specific Surah based on 'nomor' from 'quran.json' file. If the 'nomor' does not exist, it will return a message "Nomor Surah not found". 

## Future Plans
Add more endpoints in the future to explore other aspects of the data provided in 'asmaul-husna.json' and 'quran.json'.