from dotenv import load_dotenv
from livekit.agents import AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import openai, silero

from api import TemperatureAssistant

load_dotenv()


async def entrypoint(ctx: JobContext) -> None:
    session = AgentSession(
        vad=silero.VAD.load(),
        stt=openai.STT(language="en"),
        llm=openai.LLM(),
        tts=openai.TTS(),
    )

    await session.start(
        room=ctx.room,
        agent=TemperatureAssistant(),
    )

    await session.generate_reply(
        instructions="Greet the user in English and ask how you can help."
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
