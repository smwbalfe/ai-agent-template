from src.mcp.mcp import run_mcp_client
from src.agent.agent import run_agent
from src.langgraph.graph import run_graph
import asyncio
import argparse


def main():
    parser = argparse.ArgumentParser(description='AI Agent Template')
    parser.add_argument('--mode', choices=['agent', 'mcp', 'graph'], default='mcp', 
                       help='Run mode: agent, mcp client, or graph (default: mcp)')
    
    args = parser.parse_args()
    
    if args.mode == 'agent':
        run_agent()
    elif args.mode == 'graph':
        run_graph()
    else:
        # has a mcp server script built in
        asyncio.run(run_mcp_client())
    
if __name__ == "__main__":
    main()
