from fastmcp import Client
import asyncio


# Local Python script
#The client automatically infers the appropriate transport based on the input: File path ending in .py → Python Stdio transport
client = Client("D:\\ia_projects\\fastmcp_lab\\mcp_servers\\api_mcp.py")

async def main():
    async with client:
        # Basic server interaction
        await client.ping() # It use ping() to verify the server is reachable:
        
        # List available operations
        tools = await client.list_tools()
        print('Tools:', tools)
        
        
        # Execute operations
        # Call the read_root tool with parameters
        # It uses the call_tool method to invoke the read_root function without parameters.
        result_read_root = await client.call_tool("read_root", {})
        print(f"Result of read_root: {result_read_root.data}")  

        # Call the read_item tool with parameters
        result_read_item = await client.call_tool("read_item_items", {"item_id": 42, "q": "example"})
        print(f"Result of read_item: {result_read_item.data}")


asyncio.run(main())