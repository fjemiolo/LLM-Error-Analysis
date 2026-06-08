# Status Projektu: LLM Error Analysis

Ten plik ułatwi współpracę w zespole lub z kolejnymi agentami. Pokazuje on dokładnie, co zostało już zrobione, a co jest dopiero przed Wami.

## 🟢 Etap 1: Przygotowanie Danych (ZAKOŃCZONO)
- **Skrypt:** `01_prepare_dataset.py`
- **Status:** Wygenerowano plik `data/sampled_100_questions.json`.
- Mamy wylosowaną, zbalansowaną i "zamrożoną" próbkę 100 pytań HotpotQA (easy, medium, hard).

## 🟡 Etap 2: Generowanie Odpowiedzi (W TRAKCIE)
- **Skrypt:** `02_generate_responses.py`
- **Co teraz robi program:** To zadanie aktualnie mieli w tle na Twoim procesorze. Skrypt bierze każde z 100 pytań i zmusza Llama 3.1 8B do odpowiedzi na 7 różnych sposobów (część wariantów wielokrotnie, stąd w sumie ok. 3400 zapytań!).
- **Bezpieczeństwo:** Skrypt jest odseparowany. **On wyłącznie ZBIERA odpowiedzi** i nic z nimi więcej nie robi. Zrzuca je w locie co 5 pytań do pliku `data/raw_responses.json`. Jeśli byś go teraz zabił, stracisz progres niezapisanych pytań i musiałbyś go zacząć od nowa.
- **⏱️ Estymacja czasu:** Średnio jedno pytanie (z 34 próbkami) zajmuje Twojemu Macowi M5 około 3 minut i 15 sekund (niesamowicie szybko jak na odpalanie RAG-a i 8B modelu lokalnie). Wykonanie pozostałych ~90 pytań zajmie około **4,5 do 5 godzin**.

## 🔴 Etap 3: Ewaluacja Odpowiedzi (CZEKA)
- **Skrypt:** `03_evaluate_metrics.py`
- Ocenia odpowiedzi z Etapu 2 (Exact Match, F1, oraz LLM-as-a-judge za pomocą Google Gemini Pro).
- Skrypt został tak przebudowany, by posiadać funkcję wznawiania (checkpointing). Możesz go zabić w połowie, a następnym razem po prostu pominie sprawdzone odpowiedzi! Wynik trafi do `data/evaluated_responses.json`.
- **⏱️ Estymacja czasu:** Około **3-4 godzin**. Samo Gemini ocenia w sekundę, ALE darmowe konto AI Studio ma limit 15 zapytań na minutę. Przetworzenie ~3400 odpowiedzi będzie wymagało cierpliwości API.

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
