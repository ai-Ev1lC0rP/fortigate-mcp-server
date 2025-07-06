# README.md
# Fortigate MCP Server

An MCP (Model Context Protocol) server for managing Fortigate devices using FastMCP.

## Features

### Device Management
- ✅ Add / remove devices
- ✅ List configured devices
- ✅ System status and device info
- ✅ VDOMs discovery

### Firewall Policy Management
- ✅ List existing policies
- ✅ Create new policies
- ✅ Modify existing policies
- ✅ Delete policies
- ✅ Policy validation
- ✅ Policy search and filtering
- ✅ Policy statistics

### Network Objects Management
- ✅ Address objects (IP, range, FQDN)
- ✅ Service objects (TCP / UDP)
- 🔄 Create / modify objects TBD

### Routing Management
- ✅ Static routes
- ✅ Routing table
- ✅ Policy routing
- ✅ Interface list

## Installation

1. **Clone repository**
```bash
git clone https://github.com/Filippo125/fortigate-mcp-server.git
cd fortigate-mcp-server
```

2. **Install dependencies**
```bash
uv sync
```

3. **Configure devices**
```bash
cp config.yaml.example config.yaml
```

4. **Start server**
```bash
uv run python server.py
```