import os
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP(
    name="gw_ai4sm", 
    version="1.0.0",
    description="Greenwhales-based AI Tool for Smart Manufacturing"
)

async def getToken(id: str, password: str) -> object:
  async with httpx.AsyncClient() as client:
    data = {"userId":id, "password":password}
    response = await client.post("https://greenwhales.io/api/user-auth/login", json=data)

    return response.json()
  

@mcp.tool()
async def gw_login(id: str, password: str) -> object:
    """
    Test tool
    """
    test = await getToken(id, password)
    print(test) 
    return test

# if __name__ == "__main__":
#     mcp.run()