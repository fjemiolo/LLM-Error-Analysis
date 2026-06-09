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
## 🟢 Etap 3: Automatyczna Ewaluacja (GOTOWE - Zakończono używając lokalnego sędziego Gemma 2)
Skrypt: 03_evaluate_metrics.py
Oblicza EM, F1 oraz ocenę "LLM as a judge" (czy odpowiedź jest merytorycznie poprawna pomimo formy).

## 🟢 Etap 4: Klasyfikacja Błędów (GOTOWE - Użyto Gemma 2 do kategoryzacji lingwistycznej)
Skrypt: 04_classify_errors.py
Dla odpowiedzi z oceną "LLM-judge = 0", skrypt kategoryzuje błąd (halucynacja, błąd formatu, błąd rozumowania, itp.) oraz analizuje stochastyczność (czy błąd jest powtarzalny).

## 🟢 Etap 5: Analiza i Wykresy (GOTOWE - Zapisane w folderze data/)
Skrypt: 05_analyze_results.py
Generuje pliki graficzne (wykresy słupkowe, macierze) z wynikami do wklejenia w raporcie.

## 🟡 Etap 6: Walidacja Ludzka (W TRAKCIE - Wygenerowano próbkę, czeka na człowieka)
- **Skrypt:** `06_prepare_manual_annotation.py`
- Pobiera pliki z Etapu 4 i generuje czysty plik Excel (`data/manual_annotation/adnotacja_reczna.csv`) z próbką 100 błędów do weryfikacji ręcznej w celu obliczenia Cohen's Kappa.
- **⏱️ Estymacja czasu:** Wygenerowanie pliku **1 sekunda**. Ręczne ocenienie 100 pytań w Excelu przez wyznaczoną osobę zajmie **około 15-30 minut**.
