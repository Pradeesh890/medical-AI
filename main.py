import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Medical AI Platform - Choose how to run the application")
    parser.add_argument('--api', action='store_true', help='Run the FastAPI server')
    parser.add_argument('--mcp', action='store_true', help='Run as MCP tool')
    
    args = parser.parse_args()
    
    if args.api:
        print("Starting Medical AI API server...")
        # Execute fastapi_app.py
        os.system(f"{sys.executable} fastapi_app.py")
    elif args.mcp:
        print("Starting Medical AI as MCP tool...")
        # Execute mcp_tools.py
        os.system(f"{sys.executable} mcp_tools.py")
    else:
        print("Welcome to Medical AI!")
        print("Usage options:")
        print("  --api: Start the FastAPI server")
        print("  --mcp: Run as MCP tool")
        print("\nExample: python main.py --api")


if __name__ == "__main__":
    main()
