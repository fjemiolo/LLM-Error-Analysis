# Status Projektu: LLM Error Analysis

Ten plik ułatwi współpracę w zespole lub z kolejnymi agentami. Pokazuje on dokładnie, co zostało już zrobione, a co jest dopiero przed Wami.

## 🟢 Etap 1: Przygotowanie Danych (ZAKOŃCZONO)
- **Skrypt:** `01_prepare_dataset.py`
- **Status:** Wygenerowano plik `data/sampled_100_questions.json`.
- Mamy wylosowaną, zbalansowaną i "zamrożoną" próbkę 100 pytań HotpotQA (easy, medium, hard).

## 🟢 Etap 2: Generowanie Odpowiedzi (ZAKOŃCZONO)
- **Skrypt:** `02_generate_responses.py`
- **Status:** Wygenerowano wszystkie 100 pytań! Zapisano potężny plik `data/raw_responses.json`. M5 przetrwał wielogodzinny maraton z Llama 3.1. Praca lokalnego procesora na tak dużą skalę została oficjalnie i z pełnym sukcesem zakończona.

## 🟡 Etap 3: Ewaluacja Odpowiedzi (GOTOWE DO ODPALENIA PRZEZ ZESPÓŁ)
- **Skrypt:** `03_evaluate_metrics.py`
- **Status logiki:** Zaktualizowano API z przestarzałego `gemini-1.5` na nowiutkie, oficjalnie wspierane `gemini-2.5-flash`. Dodano też algorytm "Exponential Backoff", dzięki czemu w razie darmowych limitów (rate-limit) skrypt bezpiecznie zaczeka i ponowi próbę bez wywalania błędu (brak błędu 404/429).
- **Zadanie dla zespołu:** Uruchomić ten skrypt (`python 03_evaluate_metrics.py`). Skrypt oceni odpowiedzi w chmurze (Zero obciążenia dla komputera) i zrzuci wynik do `data/evaluated_responses.json`.
- **⏱️ Estymacja czasu:** Z uwagi na limity darmowego API 15 zapytań/minutę, wykonanie ok. 3400 ocen zajmie około **3-4 godziny** pracy w tle. Skrypt posiada wznawianie (checkpointing).

## 🔴 Etap 4: Klasyfikacja Błędów (CZEKA)
- **Skrypt:** `04_classify_errors.py`
- Każdą ocenioną błędną odpowiedź (przez sędziego z Etapu 3) kategoryzuje do szufladki 1-5 oraz przypisuje metkę (błąd systematyczny/stochastyczny). Plik zrzucony do `data/classified_errors.json`. Wznawialny.
- **⏱️ Estymacja czasu:** Około **45 - 60 minut**. Ten skrypt analizuje *tylko* błędne odpowiedzi, więc API wykona znacznie mniej zapytań.

## 🔴 Etap 5: Wizualizacja i Analiza (CZEKA)
- **Skrypt:** `05_analyze_results.py`
- Rysuje świetne wykresy (kołowe, słupkowe) dla prowadzącego i tworzy gotowe statystyki do prezentacji zaliczeniowej.
- **⏱️ Estymacja czasu:** **5 sekund**. Wykresy wyskoczą niemal natychmiast.

## 🔴 Etap 6: Walidacja Ludzka (CZEKA)
- **Skrypt:** `06_prepare_manual_annotation.py`
- Pobiera pliki z Etapu 4 i generuje czysty plik Excel (`data/manual_annotation/adnotacja_reczna.csv`) z próbką 100 błędów do weryfikacji ręcznej w celu obliczenia Cohen's Kappa.
- **⏱️ Estymacja czasu:** Wygenerowanie pliku **1 sekunda**. Ręczne ocenienie 100 pytań w Excelu przez wyznaczoną osobę zajmie **około 15-30 minut**.
