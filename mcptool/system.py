import json
from typing import Dict, List, Optional, Any

from mcptool.base import mcp, fortigate_manager

# === DEVICE MANAGEMENT ===

@mcp.tool()
def fortigate_get_system_status(device_id: str) -> str:
    """
    Gets Fortigate system status

    Args:
        device_id: Device ID
    """
    try:
        api = fortigate_manager.get_device(device_id)
        status = api.get_system_status()
        return json.dumps(status, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_vdoms(device_id: str) -> str:
    """
    Lists all VDOMs of a device

    Args:
        device_id: Device ID
    """
    try:
        api = fortigate_manager.get_device(device_id)
        vdoms = api.get_vdoms()
        return json.dumps(vdoms, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === SERVICE MANAGEMENT ===

@mcp.tool()
def fortigate_get_service_objects(device_id: str, vdom: str = "root") -> str:
    """
    Gets configured service objects

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        services = api.get_service_objects(vdom)
        return json.dumps(services, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_interfaces(device_id: str, vdom: str = "root") -> str:
    """
    Gets configured interfaces

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        interfaces = api.get_interfaces(vdom)
        return json.dumps(interfaces, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === UTILITY FUNCTIONS ===

@mcp.tool()
def fortigate_validate_policy(name: str, srcintf: List[str], dstintf: List[str],
                             srcaddr: List[str], dstaddr: List[str],
                             service: List[str], action: str) -> str:
    """
    Validates the parameters of a policy before creation

    Args:
        name: Policy name
        srcintf: List of source interfaces
        dstintf: List of destination interfaces
        srcaddr: List of source addresses
        dstaddr: List of destination addresses
        service: List of services
        action: Action (accept/deny)
    """
    errors = []

    if not name or len(name) < 1:
        errors.append("Policy name required")

    if not srcintf or len(srcintf) == 0:
        errors.append("At least one source interface required")

    if not dstintf or len(dstintf) == 0:
        errors.append("At least one destination interface required")

    if not srcaddr or len(srcaddr) == 0:
        errors.append("At least one source address required")

    if not dstaddr or len(dstaddr) == 0:
        errors.append("At least one destination address required")

    if not service or len(service) == 0:
        errors.append("At least one service required")

    if action not in ["accept", "deny"]:
        errors.append("Action must be 'accept' or 'deny'")

    if errors:
        return f"Validation errors:\n- " + "\n- ".join(errors)
    else:
        return "Policy valid - can be created"


if __name__ == "__main__":
    # Initial example configuration
    # fortigate_manager.add_device("fw-hq", "192.168.1.1", "your-token", ["root", "dmz"])
    # fortigate_manager.add_device("fw-branch", "192.168.10.1", "your-token")

    mcp.run()