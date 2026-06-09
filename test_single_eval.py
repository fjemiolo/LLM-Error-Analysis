import json
import sys

# Podpinamy moduł ewaluacji
import importlib.util
spec = importlib.util.spec_from_file_location("metrics", "03_evaluate_metrics.py")
metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrics)

def run_quick_test():
    with open('data/raw_responses.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Bierzemy pierwsze pytanie z brzegu
    item = data[0]
    question = item['question']
    truth = item['true_answer']
    
    # Bierzemy pierwszą odpowiedź modelu (konfiguracja C1)
    pred = item['responses']['C1'][0]
    
    print("--- SZYBKI TEST DZIAŁANIA SĘDZIEGO ---")
    print(f"Pytanie: {question}")
    print(f"Poprawna odpowiedź: {truth}")
    print(f"Odpowiedź Llama 3.1: {pred}")
    print("-" * 40)
    
    em = metrics.exact_match_score(pred, truth)
    f1 = metrics.f1_score(pred, truth)
    
    print("Wysyłam zapytanie do API Gemini-2.5-flash...")
    judge = metrics.llm_as_judge(question, pred, truth)
    
    print("-" * 40)
    print("WYNIKI METRYK:")
    print(f"Exact Match (EM): {em}")
    print(f"F1 Score: {f1:.2f}")
    print(f"LLM-as-a-Judge: {'ZALICZONE (True)' if judge else 'NIEZALICZONE (False)'}")

if __name__ == '__main__':
    run_quick_test()
