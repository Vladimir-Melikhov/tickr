from fastapi import APIRouter


router = APIRouter()

@router.get('/helth')
async def main():
    return {'status': 'ok'}