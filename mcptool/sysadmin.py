import json
from typing import Dict, List, Optional, Any

from mcptool.base import mcp, fortigate_manager

# === CONFIGURATION MANAGEMENT ===

@mcp.tool()
def fortigate_backup_config(device_id: str, scope: str = "global") -> str:
    """
    Backup FortiGate configuration

    Args:
        device_id: Device ID
        scope: Backup scope (global, vdom)

    Returns:
        Configuration backup data
    """
    try:
        api = fortigate_manager.get_device(device_id)
        backup = api.backup_config(scope)
        return json.dumps(backup, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_restore_config(device_id: str, config_data: str) -> str:
    """
    Restore FortiGate configuration

    Args:
        device_id: Device ID
        config_data: Configuration data to restore

    Returns:
        Result of configuration restore
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.restore_config(config_data)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === SYSTEM MONITORING ===

@mcp.tool()
def fortigate_get_system_performance(device_id: str, vdom: str = "root") -> str:
    """
    Get system performance metrics

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        System performance data (CPU, memory, disk usage)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        performance = api.get_system_performance(vdom)
        return json.dumps(performance, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_bandwidth_usage(device_id: str, vdom: str = "root") -> str:
    """
    Get bandwidth usage statistics

    Args:
        device_id: Device ID
        vdom: Target VDOM (default: root)

    Returns:
        Bandwidth usage statistics by interface
    """
    try:
        api = fortigate_manager.get_device(device_id)
        bandwidth = api.get_bandwidth_usage(vdom)
        return json.dumps(bandwidth, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_session_table(device_id: str, count: int = 100, vdom: str = "root") -> str:
    """
    Get active session table

    Args:
        device_id: Device ID
        count: Number of sessions to retrieve (default: 100)
        vdom: Target VDOM (default: root)

    Returns:
        Active firewall sessions
    """
    try:
        api = fortigate_manager.get_device(device_id)
        sessions = api.get_session_table(count, vdom)
        return json.dumps(sessions, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_disk_usage(device_id: str) -> str:
    """
    Get disk usage information

    Args:
        device_id: Device ID

    Returns:
        Disk usage statistics
    """
    try:
        api = fortigate_manager.get_device(device_id)
        disk_usage = api.get_disk_usage()
        return json.dumps(disk_usage, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === LICENSE AND FIRMWARE ===

@mcp.tool()
def fortigate_get_license_info(device_id: str) -> str:
    """
    Get license information

    Args:
        device_id: Device ID

    Returns:
        License status and details
    """
    try:
        api = fortigate_manager.get_device(device_id)
        license_info = api.get_license_info()
        return json.dumps(license_info, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_firmware_info(device_id: str) -> str:
    """
    Get firmware information

    Args:
        device_id: Device ID

    Returns:
        Current firmware version and build information
    """
    try:
        api = fortigate_manager.get_device(device_id)
        firmware_info = api.get_firmware_info()
        return json.dumps(firmware_info, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === LOGGING ===

@mcp.tool()
def fortigate_get_system_logs(device_id: str, lines: int = 100, 
                            level: str = "information") -> str:
    """
    Get system logs

    Args:
        device_id: Device ID
        lines: Number of log lines to retrieve (default: 100)
        level: Log level (emergency, alert, critical, error, warning, notice, information, debug)

    Returns:
        System log entries
    """
    try:
        api = fortigate_manager.get_device(device_id)
        logs = api.get_system_logs(lines, level)
        return json.dumps(logs, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_traffic_logs(device_id: str, count: int = 100, vdom: str = "root") -> str:
    """
    Get traffic logs

    Args:
        device_id: Device ID
        count: Number of log entries to retrieve (default: 100)
        vdom: Target VDOM (default: root)

    Returns:
        Traffic log entries
    """
    try:
        api = fortigate_manager.get_device(device_id)
        logs = api.get_traffic_logs(count, vdom)
        return json.dumps(logs, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_get_security_logs(device_id: str, count: int = 100, vdom: str = "root") -> str:
    """
    Get security/attack logs

    Args:
        device_id: Device ID
        count: Number of log entries to retrieve (default: 100)
        vdom: Target VDOM (default: root)

    Returns:
        Security log entries (attacks, intrusions, malware)
    """
    try:
        api = fortigate_manager.get_device(device_id)
        logs = api.get_security_logs(count, vdom)
        return json.dumps(logs, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


# === SYSTEM OPERATIONS ===

@mcp.tool()
def fortigate_reboot_system(device_id: str, 
                          event_log_message: str = "System reboot via API") -> str:
    """
    Reboot FortiGate system

    Args:
        device_id: Device ID
        event_log_message: Message to log for the reboot event

    Returns:
        Result of reboot operation
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.reboot_system(event_log_message)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
def fortigate_shutdown_system(device_id: str,
                            event_log_message: str = "System shutdown via API") -> str:
    """
    Shutdown FortiGate system

    Args:
        device_id: Device ID
        event_log_message: Message to log for the shutdown event

    Returns:
        Result of shutdown operation
    """
    try:
        api = fortigate_manager.get_device(device_id)
        result = api.shutdown_system(event_log_message)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"