import enum
import logging

from livekit.agents import Agent, function_tool

logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)


class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"


class TemperatureAssistant(Agent):
    def __init__(self) -> None:
        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 20,
            Zone.OFFICE: 25,
        }

        super().__init__(
            instructions=(
                "You are a virtual assistant created with LiveKit. "
                "Your interface with users is voice-based. "
                "Use an explanatory and assertive tone, and do not present "
                "unverified information as fact. "
                "You can read and change the temperature of the available rooms."
            )
        )

    @function_tool(description="Get the temperature in a specific room.")
    async def get_temperature(self, zone: Zone) -> str:
        """Return the current temperature for a room.

        Args:
            zone: Room whose temperature should be checked.
        """
        logger.info("get temperature - zone=%s", zone.value)
        temp = self._temperature[zone]
        return f"The temperature in {zone.value} is {temp}°C."

    @function_tool(description="Set the temperature in a specific room.")
    async def set_temperature(self, zone: Zone, temp: int) -> str:
        """Set the temperature for a room.

        Args:
            zone: Room whose temperature should be changed.
            temp: New temperature in degrees Celsius.
        """
        logger.info("set temperature - zone=%s temp=%s", zone.value, temp)
        self._temperature[zone] = temp
        return f"The temperature in {zone.value} is now {temp}°C."
