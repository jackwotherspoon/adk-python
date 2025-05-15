# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

from toolbox_core import ToolboxClient
from toolbox_core.tool import ToolboxTool as MCPToolboxTool


class ToolboxTool:
    """A class that provides access to toolbox tools.

    Example:
    ```python
    toolbox = ToolboxTool("http://127.0.0.1:5000")
    tool = await toolbox.get_tool("tool_name")
    toolset = await toolbox.get_toolset("toolset_name")
    ```
    """

    toolbox_client: Any
    """The toolbox client."""

    def __init__(self, url: str):
        self.toolbox_client = ToolboxClient(url)

    async def get_tool(self, tool_name: str) -> MCPToolboxTool:
        return await self.toolbox_client.load_tool(tool_name)

    async def get_toolset(self, toolset_name: str) -> list[MCPToolboxTool]:
        return await self.toolbox_client.load_toolset(toolset_name)
