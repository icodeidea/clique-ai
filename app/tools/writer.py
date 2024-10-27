from typing import Annotated, List, Tuple, Union
from langchain_core.tools import tool

@tool
def repurpose_content_to_tweets(
        article_content: str,
        # output_dir: Annotated[Path, "output directory of the draft"],
) -> List[str]:
    """Repurpose the content of the article into an array tweets returned in JSON format."""
    print(f"REPUPPOSE CONTENT TO TWEETS: ===============")

    user_prompt = f"""
        Please repurpose the content of the article into an array tweets returned in JSON format.
        # ARTICLE:
        {article_content}
        # END OF ARTICLE
        ---
        The format should be like this:
        {{
        "tweets": [<tweet1>, <tweet2>, <tweet3>],
        }}
    """
    formatted_message = {"role": "user", "content": user_prompt}
    print(f"USER PROMPT: {formatted_message}")
    response = openai_client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_format={"type": "json_object"},
        messages=[formatted_message],
    )
    tweets_path = WORKING_DIRECTORY / "tweets.json"
    # Logic to generate tweets...
    tweets = response.choices[0].message.content
    with tweets_path.open("w") as file:
        json.dump({"tweets": tweets}, file)
    return {
        "status": "Successfully repurposed tweets. Done.",
        "repurposed_tweets": response.choices[0].message.model_dump_json(),
        "tweets_path": tweets_path,
    }


@tool
def write_draft(
        topic: Annotated[str, "topic of the article"],
        research_results: Annotated[str, "research results of the topic"],
        # output_dir: Annotated[Path, "output directory of the draft"],
) -> str:
    """Use this to write a draft of the article."""
    print(f"WRITE DRAFT: ===============")
    user_prompt = f"""
    Please write a draft of the article based on the topic and research results.
    # TOPIC:
    {topic}
    # END OF TOPIC
    # RESEARCH RESULTS:
    {research_results}
    # END OF RESEARCH RESULTS
    ---
    Only write the article draft and nothing else. Begin!
    """
    formatted_message = {"role": "user", "content": user_prompt}
    print(f"USER PROMPT: {formatted_message}")
    response = openai_client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[formatted_message],
    )
    draft_path = WORKING_DIRECTORY / "newsletter_draft.json"
    # Logic to generate the draft...
    draft = response.choices[0].message.content
    with draft_path.open("w") as file:
        json.dump({"draft": draft}, file)
    return {
        "newsletter_draft": response.choices[0].message.content,
        "status": "Newsletter draft completed. Done.",
        "draft_path": draft_path,
    }


@tool
def critique_content(content: str) -> str:
    """Use this to critique the content of the article."""
    print(f"CRITIQUE CONTENT: ===============")
    user_prompt = f"""
    Please critique the content of the article on a scale of 1-5 for each of the following aspects:
    1. Coherence
    2. Grammar
    3. Style
    ---
    Please find the content of the article below:
    # ARTICLE:
    {content}
    # END OF ARTICLE
    ---
    Return your critique in the JSON format:
    {{
    "critiques": {{
        "coherence": <int>,
        "grammar": <int>,
        "style": <string>,
        }}
    }}

]
    """
    formatted_message = {"role": "user", "content": user_prompt}
    print(f"USER PROMPT: {formatted_message}")
    response = openai_client.chat.completions.create(
        model="gpt-4-turbo-preview",
        response_format={"type": "json_object"},
        messages=[formatted_message],
    )
    json_response = response.choices[0].message.model_dump_json()
    print(f"JSON RESPONSE: {json_response}")
    return json_response
