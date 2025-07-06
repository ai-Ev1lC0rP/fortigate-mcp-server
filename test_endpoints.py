#!/usr/bin/env python3
"""
FortiGate MCP Server Endpoint Testing Script
Tests all major functionality with real FortiGate device
"""

import sys
import json
import time
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

from fortigate.fortigate import FortigateAPI, FortigateManager

def test_device_connectivity(host, token):
    """Test basic device connectivity"""
    print("🔗 Testing Device Connectivity...")
    try:
        api = FortigateAPI(host, token)
        status = api.get_system_status()
        print("✅ Connection successful!")
        
        # Extract key information
        if 'results' in status:
            results = status['results']
            print(f"  📋 Hostname: {results.get('hostname', 'Unknown')}")
            print(f"  🔢 Version: {results.get('version', 'Unknown')}")
            print(f"  🆔 Serial: {results.get('serial', 'Unknown')}")
            print(f"  🎯 Model: {results.get('model', 'Unknown')}")
        
        return True, api
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False, None

def test_vdom_discovery(api):
    """Test VDOM discovery"""
    print("\n🏗️ Testing VDOM Discovery...")
    try:
        vdoms = api.get_vdoms()
        print(f"✅ Found {len(vdoms)} VDOMs:")
        for vdom in vdoms:
            print(f"  📁 {vdom.get('name', 'Unknown')}")
        return True
    except Exception as e:
        print(f"❌ VDOM discovery failed: {str(e)}")
        return False

def test_firewall_policies(api):
    """Test firewall policy management"""
    print("\n🛡️ Testing Firewall Policies...")
    try:
        policies = api.get_firewall_policies()
        print(f"✅ Found {len(policies)} firewall policies")
        
        if policies:
            # Show first policy details
            first_policy = policies[0]
            print(f"  📋 Sample Policy: {first_policy.get('name', 'Unnamed')}")
            print(f"    🎯 Action: {first_policy.get('action', 'Unknown')}")
            print(f"    📊 Status: {first_policy.get('status', 'Unknown')}")
        
        return True
    except Exception as e:
        print(f"❌ Policy retrieval failed: {str(e)}")
        return False

def test_network_objects(api):
    """Test network objects"""
    print("\n🌐 Testing Network Objects...")
    try:
        # Test address objects
        addresses = api.get_address_objects()
        print(f"✅ Found {len(addresses)} address objects")
        
        # Test service objects
        services = api.get_service_objects()
        print(f"✅ Found {len(services)} service objects")
        
        return True
    except Exception as e:
        print(f"❌ Network objects test failed: {str(e)}")
        return False

def test_security_profiles(api):
    """Test security profiles"""
    print("\n🛡️ Testing Security Profiles...")
    try:
        # Test AV profiles
        av_profiles = api.get_av_profiles()
        print(f"✅ Found {len(av_profiles)} antivirus profiles")
        
        # Test Web Filter profiles  
        web_profiles = api.get_webfilter_profiles()
        print(f"✅ Found {len(web_profiles)} web filter profiles")
        
        # Test IPS sensors
        ips_sensors = api.get_ips_sensors()
        print(f"✅ Found {len(ips_sensors)} IPS sensors")
        
        return True
    except Exception as e:
        print(f"❌ Security profiles test failed: {str(e)}")
        return False

def test_user_management(api):
    """Test user management"""
    print("\n👥 Testing User Management...")
    try:
        # Test local users
        users = api.get_local_users()
        print(f"✅ Found {len(users)} local users")
        
        # Test user groups
        groups = api.get_user_groups()
        print(f"✅ Found {len(groups)} user groups")
        
        return True
    except Exception as e:
        print(f"❌ User management test failed: {str(e)}")
        return False

def test_vpn_management(api):
    """Test VPN management"""
    print("\n🔐 Testing VPN Management...")
    try:
        # Test IPSec Phase 1
        phase1 = api.get_ipsec_phase1()
        print(f"✅ Found {len(phase1)} IPSec Phase 1 interfaces")
        
        # Test SSL VPN settings
        ssl_settings = api.get_ssl_vpn_settings()
        print("✅ Retrieved SSL VPN settings")
        
        return True
    except Exception as e:
        print(f"❌ VPN management test failed: {str(e)}")
        return False

def test_system_monitoring(api):
    """Test system monitoring"""
    print("\n📊 Testing System Monitoring...")
    try:
        # Test system performance
        performance = api.get_system_performance()
        print("✅ Retrieved system performance metrics")
        
        # Test license info
        license_info = api.get_license_info()
        print("✅ Retrieved license information")
        
        return True
    except Exception as e:
        print(f"❌ System monitoring test failed: {str(e)}")
        return False

def main():
    """Main testing function"""
    print("🚀 FortiGate MCP Server Endpoint Testing")
    print("=" * 50)
    
    # Configuration from environment or config file
    import os
    import yaml
    
    host = os.getenv('FORTIGATE_HOST')
    token = os.getenv('FORTIGATE_TOKEN')
    
    # Try loading from config file if env vars not set
    if not host or not token:
        try:
            with open('config.yaml', 'r') as f:
                config = yaml.safe_load(f)
                if config and 'devices' in config:
                    # Use first device in config
                    first_device = list(config['devices'].values())[0]
                    host = first_device.get('host')
                    token = first_device.get('token')
        except FileNotFoundError:
            pass
    
    if not host or not token:
        print("❌ No FortiGate credentials found!")
        print("Please set environment variables:")
        print("  export FORTIGATE_HOST='your-fortigate-ip:port'")
        print("  export FORTIGATE_TOKEN='your-api-token'")
        print("Or create a config.yaml file with device configuration.")
        return
    
    # Test basic connectivity
    success, api = test_device_connectivity(host, token)
    if not success:
        print("\n❌ Cannot proceed without device connectivity")
        print("\n🔧 Troubleshooting Tips:")
        print("1. Verify FortiGate is reachable on the network")
        print("2. Check management port (common: 443, 8443, 10443)")
        print("3. Ensure API access is enabled on the management interface")
        print("4. Verify API token is valid and has proper permissions")
        print("5. Check for VPN/network access requirements")
        return
    
    # Run all tests
    tests = [
        test_vdom_discovery,
        test_firewall_policies,
        test_network_objects,
        test_security_profiles,
        test_user_management,
        test_vpn_management,
        test_system_monitoring
    ]
    
    results = []
    for test_func in tests:
        try:
            success = test_func(api)
            results.append(success)
        except Exception as e:
            print(f"❌ Test {test_func.__name__} crashed: {str(e)}")
            results.append(False)
    
    # Summary
    passed = sum(results)
    total = len(results)
    print(f"\n📊 Test Summary: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! FortiGate MCP Server is working correctly.")
    else:
        print("⚠️  Some tests failed. Check FortiGate configuration and permissions.")

if __name__ == "__main__":
    main()