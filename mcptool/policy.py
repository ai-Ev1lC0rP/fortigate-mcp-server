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
def fortigate_update_firewall_policy(device_id: str, policy_id: int, 
                                   name: Optional[str] = None,
                                   srcintf: Optional[List[str]] = None, 
                                   dstintf: Optional[List[str]] = None,
                                   srcaddr: Optional[List[str]] = None, 
                                   dstaddr: Optional[List[str]] = None, 
                                   service: Optional[List[str]] = None,
                                   action: Optional[str] = None, 
                                   schedule: Optional[str] = None,
                                   comments: Optional[str] = None, 
                                   status: Optional[str] = None,
                                   vdom: str = "root") -> str:
    """
    Updates existing firewall policy

    Args:
        device_id: Device ID
        policy_id: Policy ID to update
        name: Policy name (optional)
        srcintf: List of source interfaces (optional)
        dstintf: List of destination interfaces (optional)
        srcaddr: List of source addresses (optional)
        dstaddr: List of destination addresses (optional)
        service: List of services (optional)
        action: Action to be performed (accept, deny) (optional)
        schedule: Schedule (optional)
        comments: Comments (optional)
        status: Policy status (enable, disable) (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Updated firewall policy result
    """
    try:
        # Build update data with only provided fields
        policy_data = {}
        
        if name is not None:
            policy_data["name"] = name
        if srcintf is not None:
            policy_data["srcintf"] = [{"name": intf} for intf in srcintf]
        if dstintf is not None:
            policy_data["dstintf"] = [{"name": intf} for intf in dstintf]
        if srcaddr is not None:
            policy_data["srcaddr"] = [{"name": addr} for addr in srcaddr]
        if dstaddr is not None:
            policy_data["dstaddr"] = [{"name": addr} for addr in dstaddr]
        if service is not None:
            policy_data["service"] = [{"name": svc} for svc in service]
        if action is not None:
            policy_data["action"] = action
        if schedule is not None:
            policy_data["schedule"] = schedule
        if comments is not None:
            policy_data["comments"] = comments
        if status is not None:
            policy_data["status"] = status

        if not policy_data:
            return "Error: No fields provided to update"

        api = fortigate_manager.get_device(device_id)
        result = api.update_firewall_policy(policy_id, policy_data, vdom)
        return json.dumps(result, indent=2)

    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_validate_firewall_policy(device_id: str, srcintf: str, source_ip: str, 
                                     protocol: str, dest: str, source_port: int = 0, 
                                     dest_port: int = 0, vdom: str = "root") -> str:
    """
    Validates firewall policy by simulating packet flow and checking which policy would match

    Args:
        device_id: Device ID
        srcintf: Source interface name
        source_ip: Source IP address
        protocol: Protocol (tcp, udp, icmp, etc.)
        dest: Destination IP address
        source_port: Source port number (default: 0)
        dest_port: Destination port number (default: 0)
        vdom: Target VDOM (default: root)

    Returns:
        Policy lookup result showing which policy would match this traffic
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.lookup_firewall_policy(
            srcintf=srcintf,
            source_ip=source_ip,
            protocol=protocol,
            dest=dest,
            source_port=source_port,
            dest_port=dest_port,
            vdom=vdom
        )
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_firewall_policy(device_id: str, name: str,
                                    srcintf: List[str], dstintf: List[str],
                                    srcaddr: List[str], dstaddr: List[str], service: List[str],
                                    action: str, schedule: str = "always",
                                    comments: Optional[str] = None, 
                                    logtraffic: str = "utm",
                                    nat: str = "disable",
                                    status: str = "enable",
                                    users: Optional[List[str]] = None,
                                    groups: Optional[List[str]] = None,
                                    poolname: Optional[str] = None,
                                    utm_status: str = "disable",
                                    av_profile: Optional[str] = None,
                                    webfilter_profile: Optional[str] = None,
                                    dnsfilter_profile: Optional[str] = None,
                                    application_list: Optional[str] = None,
                                    ips_sensor: Optional[str] = None,
                                    ssl_ssh_profile: Optional[str] = None,
                                    vdom: str = "root") -> str:
    """
    Creates comprehensive firewall policy with all common fields

    Args:
        device_id: Device ID
        name: Policy name
        srcintf: List of source interfaces
        dstintf: List of destination interfaces
        srcaddr: List of source addresses
        dstaddr: List of destination addresses
        service: List of services
        action: Action to be performed (accept, deny)
        schedule: Schedule (default: always)
        comments: Comments (optional)
        logtraffic: Log traffic setting (disable, all, utm) (default: utm)
        nat: NAT setting (enable, disable) (default: disable)
        status: Policy status (enable, disable) (default: enable)
        users: List of users (optional)
        groups: List of user groups (optional)
        poolname: NAT pool name (optional)
        utm_status: UTM status (enable, disable) (default: disable)
        av_profile: Antivirus profile name (optional)
        webfilter_profile: Web filter profile name (optional)
        dnsfilter_profile: DNS filter profile name (optional)
        application_list: Application control list name (optional)
        ips_sensor: IPS sensor name (optional)
        ssl_ssh_profile: SSL/SSH inspection profile name (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Resulting firewall policy
    """
    try:
        # Prepare policy data
        policy_data = {
            "name": name,
            "srcintf": [{"name": intf} for intf in srcintf],
            "dstintf": [{"name": intf} for intf in dstintf],
            "srcaddr": [{"name": addr} for addr in srcaddr],
            "dstaddr": [{"name": addr} for addr in dstaddr],
            "service": [{"name": svc} for svc in service],
            "action": action,
            "status": status,
            "schedule": schedule,
            "logtraffic": logtraffic,
            "nat": nat,
            "utm-status": utm_status
        }

        # Add optional fields
        if comments:
            policy_data["comments"] = comments
        if users:
            policy_data["users"] = [{"name": user} for user in users]
        if groups:
            policy_data["groups"] = [{"name": group} for group in groups]
        if poolname:
            policy_data["poolname"] = poolname
        if av_profile:
            policy_data["av-profile"] = av_profile
        if webfilter_profile:
            policy_data["webfilter-profile"] = webfilter_profile
        if dnsfilter_profile:
            policy_data["dnsfilter-profile"] = dnsfilter_profile
        if application_list:
            policy_data["application-list"] = application_list
        if ips_sensor:
            policy_data["ips-sensor"] = ips_sensor
        if ssl_ssh_profile:
            policy_data["ssl-ssh-profile"] = ssl_ssh_profile

        api = fortigate_manager.get_device(device_id)
        result = api.create_firewall_policy(policy_data=policy_data, vdom=vdom)
        return json.dumps(result, indent=2)

    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_search_firewall_policies(device_id: str, 
                                     name_filter: Optional[str] = None,
                                     action_filter: Optional[str] = None,
                                     status_filter: Optional[str] = None,
                                     srcaddr_filter: Optional[str] = None,
                                     dstaddr_filter: Optional[str] = None,
                                     service_filter: Optional[str] = None,
                                     vdom: str = "root") -> str:
    """
    Search and filter firewall policies based on various criteria

    Args:
        device_id: Device ID
        name_filter: Filter by policy name (partial match)
        action_filter: Filter by action (accept, deny)
        status_filter: Filter by status (enable, disable)
        srcaddr_filter: Filter by source address (partial match)
        dstaddr_filter: Filter by destination address (partial match)
        service_filter: Filter by service (partial match)
        vdom: Target VDOM (default: root)

    Returns:
        Filtered list of firewall policies
    """
    try:
        api = fortigate_manager.get_device(device_id)
        policies = api.get_firewall_policies(vdom)
        
        # Apply filters
        filtered_policies = []
        for policy in policies:
            # Apply name filter
            if name_filter and name_filter.lower() not in policy.get('name', '').lower():
                continue
            
            # Apply action filter
            if action_filter and policy.get('action') != action_filter:
                continue
            
            # Apply status filter
            if status_filter and policy.get('status') != status_filter:
                continue
            
            # Apply source address filter
            if srcaddr_filter:
                srcaddr_names = [addr.get('name', '') for addr in policy.get('srcaddr', [])]
                if not any(srcaddr_filter.lower() in name.lower() for name in srcaddr_names):
                    continue
            
            # Apply destination address filter
            if dstaddr_filter:
                dstaddr_names = [addr.get('name', '') for addr in policy.get('dstaddr', [])]
                if not any(dstaddr_filter.lower() in name.lower() for name in dstaddr_names):
                    continue
            
            # Apply service filter
            if service_filter:
                service_names = [svc.get('name', '') for svc in policy.get('service', [])]
                if not any(service_filter.lower() in name.lower() for name in service_names):
                    continue
            
            filtered_policies.append(policy)
        
        return json.dumps({
            "total_policies": len(policies),
            "filtered_policies": len(filtered_policies),
            "policies": filtered_policies
        }, indent=2)
        
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_policy_statistics(device_id: str, vdom: str = "root") -> str:
    """
    Get statistics and summary of firewall policies

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        Policy statistics including counts by action, status, and other metrics
    """
    try:
        api = fortigate_manager.get_device(device_id)
        policies = api.get_firewall_policies(vdom)
        
        # Calculate statistics
        stats = {
            "total_policies": len(policies),
            "by_action": {},
            "by_status": {},
            "by_nat": {},
            "by_logtraffic": {},
            "with_utm": 0,
            "with_users": 0,
            "with_comments": 0
        }
        
        for policy in policies:
            # Count by action
            action = policy.get('action', 'unknown')
            stats["by_action"][action] = stats["by_action"].get(action, 0) + 1
            
            # Count by status
            status = policy.get('status', 'unknown')
            stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
            
            # Count by NAT
            nat = policy.get('nat', 'unknown')
            stats["by_nat"][nat] = stats["by_nat"].get(nat, 0) + 1
            
            # Count by log traffic
            logtraffic = policy.get('logtraffic', 'unknown')
            stats["by_logtraffic"][logtraffic] = stats["by_logtraffic"].get(logtraffic, 0) + 1
            
            # Count UTM enabled policies
            if policy.get('utm-status') == 'enable':
                stats["with_utm"] += 1
            
            # Count policies with users
            if policy.get('users') or policy.get('groups'):
                stats["with_users"] += 1
            
            # Count policies with comments
            if policy.get('comments'):
                stats["with_comments"] += 1
        
        return json.dumps(stats, indent=2)
        
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_firewall_address(device_id: str,
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