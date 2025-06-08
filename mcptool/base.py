import json
from mcp.server import FastMCP
from typing import Dict, List, Optional, Any
from fortigate.fortigate import FortigateManager

# Initialize manager and FastMCP
fortigate_manager = FortigateManager()
mcp = FastMCP("Fortigate MCP Server")



@mcp.tool()
def fortigate_list_devices() -> str:
	"""List all configured Fortigate devices"""
	try:
		devices = fortigate_manager.list_devices()
		return json.dumps(devices, indent=2)
	except Exception as e:
		return f"Errore: {str(e)}"


@mcp.tool()
def fortigate_add_device(device_id: str, host: str, token: str, vdoms: List[str] = None) -> str:
	"""Adds a new Fortigate device

	Args:
	    device_id: Unique identifier of the device
	    host: IP address or hostname of the Fortigate
	    token: API token for authentication
	    vdoms: List of VDOMs (optional, default: ['root'])
	"""
	try:
		fortigate_manager.add_device(device_id, host, token, vdoms or ['root'])
		return f"Device {device_id} added successfully"
	except Exception as e:
		return f"Errore: {str(e)}"

