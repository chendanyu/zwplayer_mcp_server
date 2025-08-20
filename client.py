import sys
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

# python streamable_client.py http://127.0.0.1:8000/mcp

"""
from mcp.shared.metadata_utils import get_display_name


async def display_tools(session: ClientSession):
    "Display available tools with human-readable names
    tools_response = await session.list_tools()

    for tool in tools_response.tools:
        # get_display_name() returns the title if available, otherwise the name
        display_name = get_display_name(tool)
        print(f"Tool: {display_name}")
        if tool.description:
            print(f"   {tool.description}")


async def display_resources(session: ClientSession):
    "Display available resources with human-readable names
    resources_response = await session.list_resources()

    for resource in resources_response.resources:
        display_name = get_display_name(resource)
        print(f"Resource: {display_name} ({resource.uri})")
"""

async def main():
    # 确保提供了URL参数
    if len(sys.argv) < 2:
        print("Usage: python script.py <server_url>")
        return
    
    url = sys.argv[1]
    
    try:
        # 连接到流式HTTP服务器
        async with streamablehttp_client(url) as (read_stream, write_stream, _):
            # 使用客户端流创建会话
            async with ClientSession(read_stream, write_stream) as session:
                # 初始化连接
                await session.initialize()
                
                """
                # 显示服务器上面的所有工具
                await display_tools(session)
                """
                    
                # 调用工具（示例：调用名为"zwplayer_indroduce"的工具）
                tool_result = await session.call_tool("zwplayer_indroduce", {})
                print(f"Tool result:{type(tool_result)},{tool_result}")
                print(tool_result.content[0].text)
    
    except Exception as e:
        print(f"Error occurred: {e}")

# 确保在异步环境中运行
if __name__ == "__main__":
    asyncio.run(main())