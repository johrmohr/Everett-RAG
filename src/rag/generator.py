"""
LLM generation using AWS Bedrock Claude
"""
import json
from pathlib import Path
from typing import List, Optional, Dict, Any

import boto3
from botocore.config import Config

import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config import AWS_REGION, LLM_MODEL_ID, MAX_TOKENS, TEMPERATURE, SYSTEM_PROMPT


class EverettGenerator:
    """Handles text generation using AWS Bedrock Claude"""

    def __init__(
        self,
        region: str = AWS_REGION,
        model_id: str = LLM_MODEL_ID
    ):
        """Initialize the Bedrock client for Claude"""
        config = Config(
            region_name=region,
            retries={"max_attempts": 3, "mode": "adaptive"}
        )

        self.client = boto3.client(
            service_name="bedrock-runtime",
            config=config
        )
        self.model_id = model_id

    @property
    def system_prompt(self):
        """Always read fresh from config"""
        import importlib
        import config
        importlib.reload(config)
        return config.SYSTEM_PROMPT
        
    def generate(
        self,
        query: str,
        context: str,
        conversation_history: Optional[List[Dict[str, str]]] = None,
        max_tokens: int = MAX_TOKENS,
        temperature: float = TEMPERATURE,
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Generate a response using Claude with RAG context.
        
        Args:
            query: The user's question
            context: Retrieved context from manuscripts
            conversation_history: Previous messages in the conversation
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated response text
        """
        # Build the messages
        messages = []
        
        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history)
        
        # Build the user message with context
        # Use different template depending on whether we have relevant context
        if context and context.strip() and "No relevant" not in context:
            user_message = f"""Based on the following excerpts from Hugh Everett III's manuscripts, please answer the question.

## Relevant Manuscript Excerpts:
{context}

## Question:
{query}

Please provide a thoughtful answer based on the manuscript content. Cite specific sources when possible."""
        else:
            # No relevant excerpts found - let the system prompt guide the response
            user_message = f"""{query}"""
        
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Prepare the request body for Claude
        # Use custom system prompt if provided, otherwise use default
        effective_system_prompt = system_prompt if system_prompt else self.system_prompt
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "temperature": temperature,
            "system": effective_system_prompt,
            "messages": messages
        }
        
        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json"
        )
        
        response_body = json.loads(response["body"].read())
        
        # Extract the text from Claude's response
        return response_body["content"][0]["text"]
    
    def generate_streaming(
        self,
        query: str,
        context: str,
        conversation_history: Optional[List[Dict[str, str]]] = None,
        max_tokens: int = MAX_TOKENS,
        temperature: float = TEMPERATURE
    ):
        """
        Generate a streaming response using Claude.
        
        Yields:
            Chunks of generated text
        """
        messages = []

        if conversation_history:
            messages.extend(conversation_history)

        # Use different template depending on whether we have relevant context
        if context and context.strip() and "No relevant" not in context:
            user_message = f"""Based on the following excerpts from Hugh Everett III's manuscripts, please answer the question.

## Relevant Manuscript Excerpts:
{context}

## Question:
{query}

Please provide a thoughtful answer based on the manuscript content. Cite specific sources when possible."""
        else:
            # No relevant excerpts found - let the system prompt guide the response
            user_message = f"""{query}"""

        messages.append({
            "role": "user",
            "content": user_message
        })

        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "temperature": temperature,
            "system": self.system_prompt,
            "messages": messages
        }
        
        response = self.client.invoke_model_with_response_stream(
            modelId=self.model_id,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json"
        )
        
        for event in response["body"]:
            chunk = json.loads(event["chunk"]["bytes"])
            if chunk["type"] == "content_block_delta":
                yield chunk["delta"].get("text", "")


if __name__ == "__main__":
    # Test the generator
    generator = EverettGenerator()
    
    test_context = """
    **Source 1:** Everett Handwritten Draft -- I Introduction circa 1955
    The question of the consistency of these schemes arises if one contemplates regarding
    the observer and his object-system as a single (composite) physical system.
    """
    
    response = generator.generate(
        query="What was Everett's key insight about observers?",
        context=test_context
    )
    
    print(response)

