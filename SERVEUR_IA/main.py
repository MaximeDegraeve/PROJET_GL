from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# NOUVEAU : Définir la structure des données attendues
class Hyperparameters(BaseModel):
    batch_size: int = Field(ge=1, description="Taille du batch (>= 1)")


@app.get("/")
def accueil():
    return {"message": "Serveur IA actif !"}


@app.post("/train")
def recevoir_donnees(config: ConfigSimple):  # ← Changé : dict → ConfigSimple
    """
    Maintenant les données sont validées automatiquement !
    """
    print(" Config reçue :", config)
    print(" Action :", config.action)
    print(" Modèle :", config.model_name)
    print(" Horizon :", config.horizon)
    
    return {
        "status": "configuration valide",
        "action": config.action,
        "model": config.model_name,
        "horizon": config.horizon
    }