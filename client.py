from fastmcp import Client
import asyncio


# Local Python script
#The client automatically infers the appropriate transport based on the input: File path ending in .py → Python Stdio transport
client = Client("my_server_mcp.py")

async def main():
    async with client:
        # Basic server interaction
        await client.ping() # It use ping() to verify the server is reachable:
        
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()
        
        print('Tools:', tools)
        print('Resources:', resources)
        print('Prompts:', prompts)
        
        # Execute operations
        # Call the add tool with parameters
        # It uses the call_tool method to invoke the add function with parameters a=3 and b=2.
        result_add = await client.call_tool("add", {"a": 3, "b": 2})
        print(f"Result of add: {result_add.data}")  # Output: 5

        # Access a resource
        # It uses the get_resource method to fetch the configuration data from the server.
        config = await client.read_resource("resource://config")
        print(f"Config: {config[0].text}") # Output: {'version': '1.0', 'author': 'MyTeam'}

asyncio.run(main())