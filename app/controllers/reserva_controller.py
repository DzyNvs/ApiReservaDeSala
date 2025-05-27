import requests

def validar_turma(turma_id):
    try:
        url = f"http://127.0.0.1:5000/api/turmas/{turma_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Erro ao validar turma: {e}")
        return False
