import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score
import os

def map_human_label(val):
    val = str(val).strip()
    if val == "1" or val == "1.0": return "Hallucination"
    if val == "2" or val == "2.0": return "Multi-hop reasoning error"
    if val == "3" or val == "3.0": return "Format error"
    if val == "4" or val == "4.0": return "Negation error"
    if val == "5" or val == "5.0": return "Entity confusion"
    return "Unknown"

def main():
    human_file = "data/manual_annotation/adnotacja_reczna.csv"
    key_file = "data/manual_annotation/KLUCZ_adnotacja_reczna.csv"
    
    if not os.path.exists(human_file) or not os.path.exists(key_file):
        print(f"Błąd: Nie znaleziono plików adnotacji w folderze data/manual_annotation/.")
        return
        
    df_human = pd.pd.read_csv(human_file)
    df_key = pd.read_csv(key_file)
    
    human_col = 'Twoja Klasyfikacja (wpisz 1-5)'
    ai_col = 'Klasyfikacja Gemini (UKRYTE przed adnotatorem)'
    
    if df_human[human_col].isnull().any() or df_human[human_col].eq("").any():
        print("UWAGA: Plik adnotacja_reczna.csv nie został jeszcze w pełni wypełniony!")
        print("Wypełnij wszystkie 100 wierszy cyframi 1-5 i uruchom ten skrypt ponownie.")
        return
        
    human_labels = df_human[human_col].apply(map_human_label)
    ai_labels = df_key[ai_col]
    
    # Czyszczenie i przygotowanie list do ewaluacji
    y_human = human_labels.tolist()
    y_ai = ai_labels.tolist()
    
    # Obliczanie Cohen's Kappa
    kappa = cohen_kappa_score(y_human, y_ai)
    
    # Zwykła zgodność procentowa
    matches = sum([1 for h, a in zip(y_human, y_ai) if h == a])
    accuracy = matches / len(y_human)
    
    print("\n" + "="*50)
    print("WYNIKI WALIDACJI LUDZKIEJ (INTER-RATER RELIABILITY)")
    print("="*50)
    print(f"Przeanalizowanych próbek: {len(y_human)}")
    print(f"Dokładna zgodność (Accuracy): {accuracy*100:.1f}%")
    print(f"Cohen's Kappa Score: {kappa:.3f}")
    
    print("\nInterpretacja wyniku Kappa:")
    if kappa < 0: print("- Mniej niż 0: Zgodność gorsza niż losowa (Bardzo źle)")
    elif kappa <= 0.20: print("- 0.01 - 0.20: Znikoma zgodność")
    elif kappa <= 0.40: print("- 0.21 - 0.40: Słaba zgodność")
    elif kappa <= 0.60: print("- 0.41 - 0.60: Umiarkowana zgodność")
    elif kappa <= 0.80: print("- 0.61 - 0.80: Znaczna zgodność (Dobry wynik badawczy!)")
    else: print("- 0.81 - 1.00: Prawie idealna zgodność (Wybitny wynik badawczy!)")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
