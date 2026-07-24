import secrets

def generate_slug() -> str:
    return secrets.token_urlsafe(6)