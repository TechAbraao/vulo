from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPBearer, HTTPAuthorizationCredentials
from src.vulo.configs import Configs
from fastapi import Depends, HTTPException, status
from secrets import compare_digest

http_basic = HTTPBasic()
http_bearer = HTTPBearer()
configs = Configs()

def basic_auth(credentials: HTTPBasicCredentials = Depends(http_basic)):
    
    correct_admin_username = compare_digest(credentials.username, configs.admin_username)
    correct_admin_password = compare_digest(credentials.password, configs.admin_password)

    if not (correct_admin_username and correct_admin_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credencial inválida, insira uma usuário ou senha válidos.",
            headers={"WWW-Authenticate": "Basic"}
        )

    return credentials

def bearer_auth(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    pass