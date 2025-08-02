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
def fortigate_create_static_route(device_id: str,
    dst: str,
    gateway: str,
    device: str,
    comment: Optional[str] = None,
    vdom: str = "root") -> str:
    """
    Creates a new static route.

    Args:
        device_id: The ID of the FortiGate device.
        dst: The destination network.
        gateway: The gateway for the route.
        device: The device to use for the route.
        comment: A comment for the route.
        vdom: The VDOM to create the route in.

    Returns:
        The result of the route creation.
    """
    try:
        api = fortigate_manager.get_device(device_id)
        data = {
            "dst": dst,
            "gateway": gateway,
            "device": device,
        }
        if comment:
            data["comment"] = comment
        result = api.create_static_route(data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_delete_static_route(device_id: str, route_id: int, vdom: str = "root") -> str:
    """
    Deletes a static route.

    Args:
        device_id: The ID of the FortiGate device.
        route_id: The ID of the route to delete.
        vdom: The VDOM to delete the route from.

    Returns:
        The result of the route deletion.
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_static_route(route_id, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_update_static_route(device_id: str,
    route_id: int,
    dst: Optional[str] = None,
    gateway: Optional[str] = None,
    device: Optional[str] = None,
    comment: Optional[str] = None,
    vdom: str = "root") -> str:
    """
    Updates a static route.

    Args:
        device_id: The ID of the FortiGate device.
        route_id: The ID of the route to update.
        dst: The destination network.
        gateway: The gateway for the route.
        device: The device to use for the route.
        comment: A comment for the route.
        vdom: The VDOM to update the route in.

    Returns:
        The result of the route update.
    """
    try:
        api = fortigate_manager.get_device(device_id)
        data = {}
        if dst:
            data["dst"] = dst
        if gateway:
            data["gateway"] = gateway
        if device:
            data["device"] = device
        if comment:
            data["comment"] = comment

        if not data:
            return "Error: No fields provided for update."

        result = api.update_static_route(route_id, data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_policy_routes(device_id: str, vdom: str = "root") -> str:
    """
    Gets configured policy routes.

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        routes = api.get_policy_routes(vdom)
        return json.dumps(routes, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_policy_route(device_id: str,
    input_device: str,
    src: str,
    dst: str,
    protocol: str,
    output_device: str,
    gateway: str,
    comment: Optional[str] = None,
    vdom: str = "root") -> str:
    """
    Creates a new policy route.

    Args:
        device_id: The ID of the FortiGate device.
        input_device: The input device for the route.
        src: The source network.
        dst: The destination network.
        protocol: The protocol for the route.
        output_device: The output device for the route.
        gateway: The gateway for the route.
        comment: A comment for the route.
        vdom: The VDOM to create the route in.

    Returns:
        The result of the route creation.
    """
    try:
        api = fortigate_manager.get_device(device_id)
        data = {
            "input-device": input_device,
            "src": src,
            "dst": dst,
            "protocol": protocol,
            "output-device": output_device,
            "gateway": gateway,
        }
        if comment:
            data["comment"] = comment
        result = api.create_policy_route(data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_route_lookup(device_id: str, destination: str, vdom: str = "root") -> str:
    """
    Looks up a route in the routing table.

    Args:
        device_id: The ID of the FortiGate device.
        destination: The destination to look up.
        vdom: The VDOM to look up the route in.

    Returns:
        The result of the route lookup.
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.route_lookup(destination, vdom)
        return json.dumps(result, indent=2)
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
        routes = api.get_bgp_peers(vdom)
        return json.dumps(routes, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"