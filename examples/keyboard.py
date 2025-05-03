"""Example usage of the KeyboardController."""

import asyncio
import logging

from maa import KeyboardController

logger = logging.getLogger(__name__)


class KeyState:
    def __init__(self) -> None:
        self.value = 0

    async def update(self, key: str) -> None:
        if key == "a":
            self.value += 1
        elif key == "b":
            self.value -= 1


async def main() -> None:
    key_state = KeyState()

    async def key_handler(key: str) -> None:
        await key_state.update(key)

    controller = KeyboardController(key_handler=key_state.update, timeout=0.001)
    await controller.start()

    try:
        while True:
            logger.info(key_state.value)
            await asyncio.sleep(0.1)
    finally:
        await controller.stop()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(main())
