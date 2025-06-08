import json
from typing import Dict, List, Optional, Any

from mcptool.base import mcp, fortigate_manager

# === FIREWALL OBJECTS ===
@mcp.tool()
def fortigate_get_firewall_policies(device_id: str, vdom: str = "root") -> str:
    """
    Gets list of firewall policies

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        policies = api.get_firewall_policies(vdom)
        return json.dumps(policies, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_policy_by_id(device_id: str, policy_id: int, vdom: str = "root") -> str:
    """
    Gets specific firewall policy by ID

    Args:
        device_id: Device ID
        policy_id: Policy ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        policy = api.get_policy_by_id(policy_id, vdom)
        return json.dumps(policy, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_firewall_policy(device_id: str, policy_id: int, vdom: str = "root") -> str:
    """
    Deletes firewall policy

    Args:
        device_id: Device ID
        policy_id: Policy ID to be deleted
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_firewall_policy(policy_id, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === ADDRESS OBJECTS ===
@mcp.tool()
def fortigate_get_address_objects(device_id: str, vdom: str = "root") -> str:
    """
    Gets configured address objects

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        addresses = api.get_address_objects(vdom)
        return json.dumps(addresses, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

