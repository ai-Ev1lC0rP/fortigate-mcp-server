import json
from typing import Dict, List, Optional, Any
from mcptool.base import mcp, fortigate_manager

@mcp.tool()
def fortigate_get_static_routes(device_id: str, vdom: str = "root") -> str:
    """
    Gets configured static routes

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        routes = api.get_static_routes(vdom)
        return json.dumps(routes, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def fortigate_get_routing_table(device_id: str, vdom: str = "root") -> str:
    """
    Gets configured routing table

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        routes = api.get_routing_table(vdom)
        return json.dumps(routes, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def fortigate_get_bgp_peers(device_id: str, vdom: str = "root") -> str:
    """
    Get configured BGP peers

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        routes = api.bgp_peers(vdom)
        return json.dumps(routes, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"