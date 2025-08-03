from fastmcp import FastMCP
from fastmcp.prompts.prompt import PromptMessage, TextContent

#------------------1. CREATE A BASIC MCP SERVER------------------
# Create a server instance with a descriptive name
mcp = FastMCP(name="My First MCP Server")

#------------------2. ADD TOOLS TO MCP SERVER------------------
# Tools are functions that can be called by the LLM.
@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

#------------------3.EXPOSE DATA WITH RESOURCES TO MCP SERVER------------------
# Resources provide read-only data to the LLM. You can define a resource decorating a function with the `@mcp.resource`, which provides a unique URI for the resource.
# It exposes a simple dicctionary of configuration as a resource.
# When a client solicitate the URI `resource://config`, FastMCP run the `get_config` function and the server returns the output(serialized as a JSON). 
# The `get_config` function is only called when the client requests the resource.
@mcp.resource("resource://config")
def get_config() -> dict:
    """Provides the application's configuration."""
    return {"version": "1.0", "author": "MyTeam"}

#------------------4.GENERATE DINAMIC CONTENT WITH RESOURCES TEMPLATES TO MCP SERVER------------------
# Sometimes, you need to generate resources based on parameters. This is what Resource Templates are for. 
# You define them using the same @mcp.resource decorator but with placeholders in the URI.
# In this example, we create a template that provides a personalized greeting.
# Example (greetings://Ford will call personalized_greeting(name="Ford"))
# FastMCP automatically maps the {name} placeholder in the URI to the name parameter in your function.
@mcp.resource("greetings://{name}")
def personalized_greeting(name: str) -> str:
    """Generates a personalized greeting for the given name."""
    return f"Hello, {name}! Welcome to the MCP server."


#------------------4.1 GENERATE PROMPTS TO MCP SERVER------------------
# Basic prompt returning a string (converted to user message automatically)
@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"

# Prompt returning a specific message type
@mcp.prompt
def generate_code_request(language: str, task_description: str) -> PromptMessage:
    """Generates a user message requesting code generation."""
    content = f"Write a {language} function that performs the following task: {task_description}"
    return PromptMessage(role="user", content=TextContent(type="text", text=content))



#------------------5. RUN MCP SERVER------------------
# To make your server executable, add a __main__ block to your script that calls mcp.run().
# To run the server, execute the script in your terminal: python my_server_mcp.py
# This starts the server using the default STDIO transport, which is how clients communicate with local servers.
# Note: FastMCP also provides a command-line interface for running servers without modifying the source code:
# > fastmcp run server.py
# > fastmcp run server.py --transport sse --port 9000
# Note 2: For development and testing, you can use the dev command to run your server with the MCP Inspector: 
# > fastmcp dev my_server_mcp.py
if __name__ == "__main__":
    mcp.run() 