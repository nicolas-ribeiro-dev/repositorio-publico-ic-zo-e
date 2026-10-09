from datetime import datetime
from zoneinfo import ZoneInfo

def data_hoje():
    agora = datetime.now(ZoneInfo("America/Sao_Paulo"))
    return agora.strftime("%Y-%m-%d")
