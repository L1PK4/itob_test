import asyncio
import aiohttp
from enum import Enum


class State(Enum):
    OFF = 0
    ON = 1
    BOILED = 2
    BOILING = 3


class Kettle:
    def __init__(self, boiling_time: float = 10., water_volume: float = 1.) -> None:
        self._boiling_time: float = boiling_time
        self._water_volume: float = water_volume
        self._temperature: float = 25.
        self._state: State = State.OFF

    def __str__(self) -> str:
        return f"Kettle is {self._state.name}" + \
            (f"\nTemperature: {self._temperature}" if self._state == State.BOILING else "")

    @property
    def state(self):
        return self._state

    @property
    def temperature(self):
        return self._temperature

    async def start(self):
        self._state = State.BOILING
        speed: float = 1. / self._water_volume
        while self._temperature < 100.:
            await asyncio.sleep(0.1)
            self._temperature += speed
        self._state = State.BOILED
        return True

    async def send_data(self, url: str, data: dict):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                response_data = await response.json()
        return response_data
    