# Muslim API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)

## 📖 Overview
Muslim API provides a RESTful interface to access Islamic content including Asmaul Husna (99 Names of Allah) and Quran Surahs. Built with FastAPI for high performance and ease of use, this API serves data from JSON sources making it lightweight and efficient.

## ✨ Features
- Fast and lightweight API using FastAPI
- Access to complete Asmaul Husna data
- Access to Quran Surah information
- Random Asmaul Husna endpoint
- Detailed error handling

## 🛠️ Tech Stack
- Python 3.8+
- FastAPI
- Uvicorn ASGI server
- JSON for data storage

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MuslimApi.git
   cd MuslimApi
   ```

2. Install required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

3. Prepare your JSON data files:
   - Place your `asmaul-husna.json` file in the project directory
   - Place your `quran.json` file in the project directory

4. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation at: `http://localhost:8000/docs`

## 📡 API Endpoints

### Base Endpoint
- **GET /** - Welcome message and API information

### Asmaul Husna Endpoints
- **GET /asmaul-husna** - Retrieve all 99 Names of Allah
- **GET /asmaul-husna/{id}** - Get specific Asmaul Husna by ID (1-99)
- **GET /asmaul-husna/random** - Get a random Name from Asmaul Husna

### Quran Endpoints
- **GET /quran** - Retrieve information about all Surahs
- **GET /quran/{nomor}** - Get specific Surah details by number

## 📝 Response Examples

### Asmaul Husna Response
```json
{
  "urutan": 1,
  "latin": "Ar Rahman",
  "arab": "الرحمن",
  "arti": "Yang Maha Pengasih"
}
```

### Quran Surah Response
```json
{
  "nomor": 1,
  "nama": "الفاتحة",
  "nama_latin": "Al-Fatihah",
  "jumlah_ayat": 7,
  "tempat_turun": "mekah",
  "arti": "Pembukaan"
}
```

## 🔮 Future Plans
- Add ayat-by-ayat Quran endpoint
- Include hadith collection API
- Add prayer times calculation
- Multi-language support
- Authentication for premium features

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact
For questions or feedback, please open an issue in the GitHub repository.