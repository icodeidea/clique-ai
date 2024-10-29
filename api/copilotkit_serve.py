# """Demo"""
#
# import os
# from dotenv import load_dotenv
# load_dotenv()
#
# from fastapi import FastAPI
# import uvicorn
# from copilotkit.integrations.fastapi import add_fastapi_endpoint
# from copilotkit import CopilotKitSDK, LangGraphAgent
# from app.pipelines.supervisor_agent_pipeline import run_agent_pipeline, super_graph
#
# app = FastAPI()
# sdk = CopilotKitSDK(
#     agents=[
#         LangGraphAgent(
#             name="genesis_agent",
#             description="operation agent.",
#             agent=super_graph,
#         )
#     ],
# )
#
# add_fastapi_endpoint(app, sdk, "/copilotkit")
#
# # add new route for health check
# @app.get("/health")
# def health():
#     """Health check."""
#     return {"status": "ok"}
#
#
# def main():
#     """Run the uvicorn server."""
#     port = int(os.getenv("PORT", "8000"))
#     uvicorn.run("clique_ai.demo:app", host="0.0.0.0", port=port, reload=True)
#