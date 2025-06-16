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


@mcp.tool()
def create_firewall_policy(device_id: str, name: str,
                                 srcintf: List[str], dstintf: List[str],
                                 srcaddr: List[str], dstaddr: List[str], service: List[str],
                                 action: str, schedule: str = "always",
                                 comments: Optional[str] = None, vdom:str = "root") -> str:
    """
    Creates firewall policy

    Args:
        name: Policy name
        srcintf: List of source interface
        dstintf: List of destination interface
        srcaddr: List of source address
        dstaddr: List of destination address
        service: List of service
        action: Action to be performed (accept, deny)
        schedule: Schedule (default: always)
        comments: Comments (default: None)
        vdom: Target VDOM (default: root)

    Returns:
        Resulting firewall policy
    """
    try:
        # Prepara i dati per la policy
        policy_data = {
        "name": name,
        "srcintf": [{"name": intf} for intf in srcintf],
        "dstintf": [{"name": intf} for intf in dstintf],
        "srcaddr": [{"name": addr} for addr in srcaddr],
        "dstaddr": [{"name": addr} for addr in dstaddr],
            "users"
        "service": [{"name": svc} for svc in service],
        "action": action,
        "status": "enable"
        }

        if comments:
            policy_data["comments"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_firewall_policy(policy_data=policy_data, vdom=vdom)
        return json.dumps(result, indent=2)

    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def create_firewall_address(device_id: str,
    name: str,
    type: str,
    subnet: Optional[str] = None,
    start_ip: Optional[str] = None,
    end_ip: Optional[str] = None,
    fqdn: Optional[str] = None,
    country: Optional[str] = None,
    interface: Optional[str] = None,
    comments: Optional[str] = None,
    vdom: str = "root") -> str:
    """
    Create a new address object on FortiGate

    Args:
        device_id: Device identifier
        name: Address object name
        type: Address type (ipmask, iprange, fqdn, geography, interface-subnet)
        subnet: Subnet in CIDR format (for type=ipmask), e.g. "192.168.1.0/24"
        start_ip: Start IP address (for type=iprange)
        end_ip: End IP address (for type=iprange)
        fqdn: Fully qualified domain name (for type=fqdn)
        country: Country code (for type=geography)
        interface: Interface name (for type=interface-subnet)
        comments: Optional comments
        vdom: Target VDOM (default: root)

    Returns:
        Result of address object creation
    """
    try:
        # Prepare address object data
        address_data = {
            "name": name,
            "type": type
        }

        # Add type-specific parameters
        if type == "ipmask" and subnet:
            address_data["subnet"] = subnet
        elif type == "iprange" and start_ip and end_ip:
            address_data["start-ip"] = start_ip
            address_data["end-ip"] = end_ip
        elif type == "fqdn" and fqdn:
            address_data["fqdn"] = fqdn
        elif type == "geography" and country:
            address_data["country"] = country
        elif type == "interface-subnet" and interface:
            address_data["interface"] = interface
        else:
            return f"Error: missing or invalid parameters for type '{type}'"

        # Add comments if specified
        if comments:
            address_data["comment"] = comments
        api = fortigate_manager.get_device(device_id)
        result = api.create_address_object(address_data)

        return json.dumps(result, indent=2)

    except Exception as e:
        return f"Error: {str(e)}"

# === ADDRESS OBJECTS ===
@mcp.tool()
def fortigate_get_vip_objects(device_id: str,vdom: str = "root") -> str:
    """Gets configured vip objects """
    try:
        api = fortigate_manager.get_device(device_id)
        policies = api.get_vip_addresses(vdom)
        return json.dumps(policies, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def fortigate_delete_vip_object(device_id: str, vip_name: str, vdom: str = "root") -> str:
    """ Deletes vip object by name"""
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.delete_vip_address(vip_name, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"