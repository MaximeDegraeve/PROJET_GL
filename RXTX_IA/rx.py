import requests

# URL de ton serveur
URL = "http://localhost:8000/train"

def test_cas(nom, data):
    """Fonction pour tester différents cas"""
    print(f"\n{'='*60}")
    print(f" TEST : {nom}")
    print(f"{'='*60}")
    print(f" Envoi : {data}")
    
    try:
        response = requests.post(URL, json=data)
        print(f" Status : {response.status_code}")
        print(f" Réponse : {response.json()}")
    except Exception as e:
        print(f" Erreur : {e}")


# ========================================
# Lance les tests
# ========================================

print("\n🚀 DÉBUT DES TESTS")

# Test 1 : Données valides 
test_cas(
    "Données valides",
    {
        "action": "start",
        "model_name": "lstm",
        "horizon": 24
    }
)

# Test 2 : Champ manquant 
test_cas(
    "Champ manquant (pas de horizon)",
    {
        "action": "start",
        "model_name": "lstm"
    }
)

# Test 3 : Mauvais type 
test_cas(
    "Mauvais type (horizon = string)",
    {
        "action": "start",
        "model_name": "lstm",
        "horizon": "vingt-quatre"
    }
)

# Test 4 : Conversion automatique 
test_cas(
    "Conversion automatique (horizon = '24')",
    {
        "action": "start",
        "model_name": "lstm",
        "horizon": "24"  # String mais convertible en int
    }
)

# Test 5 : Horizon négatif  (si tu as ajouté Field(gt=0))
test_cas(
    "Horizon négatif",
    {
        "action": "start",
        "model_name": "lstm",
        "horizon": -5
    }
)

# Test 6 : Champ en trop 
test_cas(
    "Champ supplémentaire (ignoré)",
    {
        "action": "start",
        "model_name": "lstm",
        "horizon": 24,
        "champ_inconnu": "je suis en trop"
    }
)

print("\n" + "="*60)
print("TESTS TERMINÉS")
print("="*60 + "\n")