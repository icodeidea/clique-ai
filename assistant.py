import os
import chainlit as cl
from app.pipelines.supervisor_agent_pipeline import run_agent_pipeline

@cl.on_chat_start
async def start():
    is_dev_mode = bool(os.getenv("DEV_MODE"))

    # Set the pipeline
    cl.user_session.set("pipeline", run_agent_pipeline)

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")

    # Retrieve the assistant from the user session
    pipeline = cl.user_session.get("pipeline")

    # Process the user message using the pipeline
    try:
        response_generator = pipeline(
            message=message.content,
            thread_id=cl.user_session.get("id")
        )
        for delta in response_generator:
            await msg.stream_token(str(delta))
    except TypeError as e:
        # Handle specific TypeError and log or print additional information for debugging
        print(f"Error occurred: {e}")
        await msg.stream_token(f"\n\n I encountetrd an error, please try again later.")

    await msg.send()

# Run the Chainlit application
if __name__ == "__main__":
    cl.run_sync()

    # source.venv / bin / activate


