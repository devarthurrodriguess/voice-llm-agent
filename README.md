# Real-Time Voice AI Agent

Early prototype of a real-time voice assistant built with Python, LiveKit Agents, and OpenAI.

The agent uses a classic voice pipeline (`VAD -> STT -> LLM -> TTS`) and exposes basic function tools that can read and update room temperatures.

## Features

- Real-time voice interaction with LiveKit
- Silero voice activity detection (VAD)
- OpenAI speech-to-text (STT)
- OpenAI LLM responses
- OpenAI text-to-speech (TTS)
- Basic LLM tool calling
- In-memory temperature state for multiple rooms

## Project status

**v0.1.0 — Initial prototype**

This version is intentionally small and serves as the baseline for future improvements such as external APIs, persistent state, automated evaluations, observability, tests, and deployment.

## Requirements

- Python 3.10+
- A LiveKit project
- An OpenAI API key

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy the environment template:

Windows:

```bash
copy .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

Fill in the variables in `.env`:

```env
LIVEKIT_URL=
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=
OPENAI_API_KEY=
```

## Run

For local development with LiveKit Agents:

```bash
python main.py dev
```

## Repository hygiene

The local `.env` file and virtual environments are ignored by Git. Only `.env.example` should be committed.
