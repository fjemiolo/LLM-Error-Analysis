# Instrukcja / Prompt dla nowego Agenta AI

Jeśli sklonowałeś to repozytorium na nowy komputer (lub otworzyłeś nową sesję) i chcesz kontynuować pracę, po prostu skopiuj poniższy tekst i wyślij go swojemu nowemu asystentowi AI.

---
**SKOPIUJ PONIŻSZY TEKST I WYŚLIJ DO AGENTA:**

```text
Cześć! Przejęliśmy projekt "LLM Error Analysis". 
Jesteśmy po Etapie 1 i 2. W folderze `data/` znajduje się ogromny plik `raw_responses.json` z odpowiedziami wygenerowanymi przez Llamę 3.1 8B. Nie musisz już niczego generować lokalnie.

Twoim zadaniem na teraz jest poprowadzenie mnie przez Etap 3 (Ewaluacja) i Etap 4 (Klasyfikacja błędów).
Oto co musimy zrobić krok po kroku:
1. Upewnij się, że w głównym folderze znajduje się plik `.env` z wpisanym `GEMINI_API_KEY=...` (jeśli nie, poproś mnie o utworzenie go). 
*(Uwaga dla Agenta: skrypty 03 i 04 są domyślnie napisane pod Google GenAI. Jeśli użytkownik powie Ci, że chce użyć modelu Claude, Twoim pierwszym zadaniem przed uruchomieniem kodu będzie podmienienie w skryptach `03` i `04` biblioteki `google-genai` na `anthropic`, instalacja paczki `anthropic` i dostosowanie wywołań API do Claude 3.5 Sonnet).*
2. Uruchom skrypt `03_evaluate_metrics.py`. Używa on Gemini 1.5 Pro jako sędziego. Pamiętaj, że skrypt ma wbudowany checkpointing – jeśli padnie z powodu limitu zapytań (Rate Limit Google to 15 zapytań/minutę), po prostu uruchom go ponownie, a on wznowi pracę.
3. Gdy skończymy 03, uruchom skrypt `04_classify_errors.py`, który poklasyfikuje znalezione błędy.
4. Zaktualizuj plik `CURRENT_PROGRESS.md` zaznaczając Etapy 3 i 4 jako 🟢 ZAKOŃCZONO.

Zacznijmy od zestawienia środowiska! Ponieważ folder `venv/` nie został pobrany z GitHuba, zrób to w ten sposób:
1. Utwórz nowe środowisko wirtualne (`python3 -m venv venv`).
2. Aktywuj je (`source venv/bin/activate` na Mac/Linux lub `venv\Scripts\activate` na Windows).
3. Zainstaluj wymagane paczki (`pip install -r requirements.txt`).

Gdy to będzie gotowe, odpal skrypt 03. Daj mi znać, gdy będziesz gotowy!
```
---
