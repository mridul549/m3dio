import os, requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def token(request):
    if not "Authorization" in request.headers:
        return None, ("Missing token", 401)
    
    token = request.headers["Authorization"]

    if not token:
        return None, ("Missing token", 401)
    
    print(f"{'AUTH_SVC_ADDRESS'}")
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers={"Authorization": token},
    )

    if response.status_code == 200:
        return response.text, None
    else: 
        return None, (response.text, response.status_code)