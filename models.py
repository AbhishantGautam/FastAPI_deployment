from pydantic import BaseModel


class MInput(BaseModel):
    temp : float
    feelslike : float
    humidity : float
    precip : float
    windspeed : float
    winddir : float
    sealevelpressure : float
    visibility : float