# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **FortiGate MCP Server** that provides a Model Context Protocol (MCP) interface for managing FortiGate firewalls. The server is built using FastMCP and provides tools for device management, firewall policies, network objects, and routing configuration.

## Development Commands

### Setup and Installation
```bash
# Install dependencies
uv sync

# Configure devices
cp config.yaml.example config.yaml
# Edit config.yaml with your FortiGate device details

# Start development server
uv run python server.py
```

### Docker Development
```bash
# Build and run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Testing and Validation
```bash
# Test individual components
uv run python -m pytest  # If tests are added

# Validate configuration
uv run python -c "from server import load_config; load_config()"
```

## Architecture Overview

### Core Components

#### FortiGate API Layer (`fortigate/fortigate.py`)
- **FortigateAPI**: Low-level REST API client for FortiGate devices
- **FortigateManager**: High-level manager for multiple devices and VDOMs
- Handles authentication, VDOM switching, and API request management

#### MCP Tool Modules (`mcptool/`)
- **base.py**: Device management tools (add_device, list_devices).
- **system.py**: System status and device information tools.
- **policy.py**: Firewall policy and network object management tools.
- **routing.py**: Routing and network interface tools (read-only).
- **security.py**: Security profile management (AV, Web Filter, IPS, etc.).
- **users.py**: User and authentication server management.
- **vpn.py**: IPSec and SSL VPN management.
- **sysadmin.py**: System administration tasks (backups, performance, logs).
- **advanced.py**: Advanced features like HA and SD-WAN.
- Each module registers tools with the FastMCP server using `@mcp.tool()` decorators.

#### Server Entry Point (`server.py`)
- Loads device configuration from `config.yaml`
- Initializes the FortiGate manager with configured devices
- Starts the FastMCP server on port 8456

### Device Management Architecture

The server supports multiple FortiGate devices with multiple VDOMs:
- Each device has a unique `device_id`
- Devices are configured with host, API token, and VDOM list
- API requests are automatically routed to the correct device and VDOM
- Configuration is loaded from YAML and stored in memory

### MCP Tool Pattern

All tools follow this pattern:
```python
@mcp.tool()
def tool_name(device_id: str, vdom: str = 'root', **kwargs) -> str:
    """Tool description"""
    try:
        # Get device API client
        api = fortigate_manager.get_device(device_id)
        # Make API call with VDOM
        result = api.some_method(vdom=vdom, **kwargs)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"
```

## Configuration Management

### Device Configuration (`config.yaml`)
```yaml
devices:
  "device-id":
    host: "192.168.1.1:10443"
    token: "API_TOKEN"
    vdoms: ["root", "vdom1"]
    description: "Device description"
```

### Environment Variables
- Server listens on `0.0.0.0:8456` by default
- SSL verification is disabled for FortiGate API calls
- Logging level set to DEBUG for development

## Security Considerations

- API tokens are stored in configuration files (not in code)
- SSL verification is disabled for FortiGate connections (common in enterprise environments)
- All API calls use Bearer token authentication
- VDOM isolation is enforced at the API level

## Development Patterns

### Adding New Tools
1. Create tool function in appropriate module (`mcptool/`)
2. Use `@mcp.tool()` decorator with clear documentation
3. Follow error handling pattern with try/except
4. Return JSON strings for structured data
5. Include `device_id` and `vdom` parameters

### API Integration
- Use `FortigateManager.get_device()` to get API client
- Pass `vdom` parameter to API methods
- Handle exceptions gracefully with user-friendly messages
- Log debug information for troubleshooting

### Testing New Features
- Test with real FortiGate devices when possible
- Validate VDOM switching functionality
- Check error handling for invalid devices/VDOMs
- Verify JSON serialization of complex objects