AI Recipe Generator
Aplikacja chmurowa w architekturze mikroserwisowej generująca przepisy kulinarne na podstawie składników znajdujących się w lodówce użytkownika. System wykorzystuje model AI do tworzenia przepisów oraz kontenery Docker do uruchamiania mikroserwisów.
Projekt powstał w ramach przedmiotu Budowa i administracja aplikacji w chmurze.
________________________________________
Opis aplikacji
Użytkownik może:
•	zarejestrować się i zalogować do systemu
•	dodać składniki do swojej wirtualnej lodówki
•	wygenerować przepis kulinarny na podstawie dostępnych składników
•	zapisać wygenerowany przepis do ulubionych
•	przeglądać zapisane przepisy
Przepis generowany jest przez model AI na podstawie listy składników oraz preferencji użytkownika.
Aplikacje generujące przepisy na podstawie składników wykorzystują modele generatywne, które analizują listę produktów i tworzą instrukcję przygotowania potrawy wraz ze składnikami i krokami wykonania. 
________________________________________
Architektura systemu
Aplikacja została zaprojektowana w architekturze mikroserwisowej.
Frontend (React)
        |
        v
API Gateway
   |     |     |
   v     v     v
Auth  Ingredient  Recipe
Dodatkowo:
Recipe Service -> OpenAI API
Każdy mikroserwis posiada własną bazę danych PostgreSQL.
________________________________________
Mikroserwisy
Auth Service
Serwis odpowiedzialny za zarządzanie użytkownikami.
Funkcjonalności:
•	rejestracja użytkownika
•	logowanie
•	generowanie tokenów JWT
•	weryfikacja tokenów JWT
Baza danych:
users_db
________________________________________
Ingredient Service
Serwis zarządzający składnikami w lodówce użytkownika.
Funkcjonalności:
•	dodawanie składników
•	usuwanie składników
•	pobieranie listy składników
•	czyszczenie lodówki
Baza danych:
ingredients_db
________________________________________
Recipe Service
Serwis odpowiedzialny za generowanie przepisów oraz zarządzanie ulubionymi przepisami.
Funkcjonalności:
•	generowanie przepisu przy użyciu AI
•	generowanie brakujących składników
•	zapisywanie przepisu do ulubionych
•	usuwanie przepisu z ulubionych
•	lista ulubionych przepisów
•	szczegóły przepisu
Baza danych:
recipes_db
Integracja:
OpenAI API
________________________________________
API Gateway
API Gateway jest centralnym punktem wejścia do systemu.
Jego zadaniem jest:
•	przekazywanie zapytań do odpowiednich mikroserwisów
•	obsługa routingu API
•	przekazywanie tokenów JWT
________________________________________
Technologie
Frontend
•	React
•	Axios
Backend
•	Python
•	FastAPI
Baza danych
•	PostgreSQL
AI
•	OpenAI API
Konteneryzacja
•	Docker
•	Docker Compose
Chmura
•	Google Cloud Platform
________________________________________
Struktura projektu
ai-recipe-generator
│
├── frontend
│
├── api-gateway
│
├── services
│   ├── auth-service
│   ├── ingredient-service
│   └── recipe-service
│
├── docker-compose.yml
└── README.md
________________________________________
Uruchomienie projektu lokalnie
Wymagania:
•	Docker
•	Docker Compose
Uruchomienie aplikacji:
docker compose up --build
Po uruchomieniu dostępne będą:
API Gateway
http://localhost:8000
Dokumentacja API:
http://localhost:8000/docs
________________________________________
Przykład generowania przepisu
Request:
{
  "ingredients": ["jajka", "pomidor", "ser"],
  "preferences": ["wegetariańskie", "szybkie"],
  "meal_type": "obiad"
}
AI generuje:
•	tytuł przepisu
•	listę składników
•	instrukcję krok po kroku
________________________________________
Wykorzystanie AI w projekcie
Sztuczna inteligencja została wykorzystana w dwóch obszarach:
1.	Funkcjonalność aplikacji
generowanie przepisów kulinarnych przy użyciu OpenAI API
2.	Proces programowania (Vibe Coding)
wykorzystanie narzędzi AI do:
•	generowania kodu mikroserwisów
•	tworzenia testów
•	refaktoryzacji kodu
________________________________________
Autorzy
Karolina Studzienna, Kamil Jarzyna, Kacper Kulon, Michał Neubauer
Projekt realizowany w ramach przedmiotu:
Budowa i administracja aplikacji w chmurze
