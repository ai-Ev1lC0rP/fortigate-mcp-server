import json
from typing import Dict, List, Optional, Any

from mcptool.base import mcp, fortigate_manager

# === HIGH AVAILABILITY ===

@mcp.tool()
def fortigate_get_ha_status(device_id: str) -> str:
    """
    Get High Availability status

    Args:
        device_id: Device ID

    Returns:
        HA cluster status and peer information
    """
    try:
        api = fortigate_manager.get_device(device_id)
        ha_status = api.get_ha_status()
        return json.dumps(ha_status, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_configure_ha(device_id: str, 
                         mode: str = "a-p",
                         group_id: int = 1,
                         group_name: Optional[str] = None,
                         password: Optional[str] = None,
                         hbdev: Optional[List[str]] = None,
                         session_pickup: str = "enable",
                         session_pickup_connectionless: str = "enable",
                         override: str = "disable",
                         priority: int = 128,
                         vdom: str = "root") -> str:
    """
    Configure High Availability settings

    Args:
        device_id: Device ID
        mode: HA mode (a-p, a-a, standalone)
        group_id: HA group ID
        group_name: HA group name (optional)
        password: HA authentication password (optional)
        hbdev: Heartbeat devices (optional)
        session_pickup: Session pickup (enable, disable)
        session_pickup_connectionless: Connectionless session pickup (enable, disable)
        override: Override (enable, disable)
        priority: HA priority (1-255)
        vdom: Target VDOM (default: root)

    Returns:
        Result of HA configuration
    """
    try:
        ha_data = {
            "mode": mode,
            "group-id": group_id,
            "session-pickup": session_pickup,
            "session-pickup-connectionless": session_pickup_connectionless,
            "override": override,
            "priority": priority
        }

        if group_name:
            ha_data["group-name"] = group_name
        if password:
            ha_data["password"] = password
        if hbdev:
            ha_data["hbdev"] = " ".join(hbdev)

        api = fortigate_manager.get_device(device_id)
        result = api.configure_ha(ha_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_ha_failover(device_id: str) -> str:
    """
    Trigger HA failover

    Args:
        device_id: Device ID

    Returns:
        Result of failover operation
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.ha_failover()
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === SD-WAN ===

@mcp.tool()
def fortigate_get_sdwan_zones(device_id: str, vdom: str = "root") -> str:
    """
    Get SD-WAN zones

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of SD-WAN zones
    """
    try:
        api = fortigate_manager.get_device(device_id)
        zones = api.get_sdwan_zones(vdom)
        return json.dumps(zones, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_create_sdwan_zone(device_id: str, name: str,
                               service_sla_tie_break: str = "zone",
                               minimum_sla_meet_members: int = 1,
                               comments: Optional[str] = None,
                               vdom: str = "root") -> str:
    """
    Create SD-WAN zone

    Args:
        device_id: Device ID
        name: Zone name
        service_sla_tie_break: SLA tie break method
        minimum_sla_meet_members: Minimum SLA meet members
        comments: Comments (optional)
        vdom: Target VDOM (default: root)

    Returns:
        Result of zone creation
    """
    try:
        zone_data = {
            "name": name,
            "service-sla-tie-break": service_sla_tie_break,
            "minimum-sla-meet-members": minimum_sla_meet_members
        }

        if comments:
            zone_data["comment"] = comments

        api = fortigate_manager.get_device(device_id)
        result = api.create_sdwan_zone(zone_data, vdom)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_sdwan_members(device_id: str, vdom: str = "root") -> str:
    """
    Get SD-WAN members

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        List of SD-WAN member interfaces
    """
    try:
        api = fortigate_manager.get_device(device_id)
        members = api.get_sdwan_members(vdom)
        return json.dumps(members, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_sdwan_performance(device_id: str, vdom: str = "root") -> str:
    """
    Get SD-WAN performance SLA statistics

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        SD-WAN performance and SLA metrics
    """
    try:
        api = fortigate_manager.get_device(device_id)
        performance = api.get_sdwan_performance(vdom)
        return json.dumps(performance, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_sdwan_health_check(device_id: str, vdom: str = "root") -> str:
    """
    Get SD-WAN health check status

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        SD-WAN health check status for all members
    """
    try:
        api = fortigate_manager.get_device(device_id)
        health_check = api.get_sdwan_health_check(vdom)
        return json.dumps(health_check, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === ADVANCED MONITORING ===

@mcp.tool()
def fortigate_get_fortiview_statistics(device_id: str, 
                                     chart_type: str = "top-sources",
                                     vdom: str = "root") -> str:
    """
    Get FortiView statistics

    Args:
        device_id: Device ID
        chart_type: Chart type (top-sources, top-destinations, top-applications, top-websites)
        vdom: Target VDOM (default: root)

    Returns:
        FortiView statistical data
    """
    try:
        api = fortigate_manager.get_device(device_id)
        statistics = api.get_fortiview_statistics(chart_type, vdom)
        return json.dumps(statistics, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_threat_dashboard(device_id: str, vdom: str = "root") -> str:
    """
    Get threat dashboard data

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        Security rating and threat intelligence data
    """
    try:
        api = fortigate_manager.get_device(device_id)
        threat_data = api.get_threat_dashboard(vdom)
        return json.dumps(threat_data, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_policy_usage(device_id: str, vdom: str = "root") -> str:
    """
    Get firewall policy usage statistics

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        Policy usage statistics (hit counts, last used)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        usage = api.get_policy_usage(vdom)
        return json.dumps(usage, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_application_statistics(device_id: str, vdom: str = "root") -> str:
    """
    Get application control statistics

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        Application usage and control statistics
    """
    try:
        api = fortigate_manager.get_device(device_id)
        app_stats = api.get_application_statistics(vdom)
        return json.dumps(app_stats, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"