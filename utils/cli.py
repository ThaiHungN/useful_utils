"""
Command-line interface for useful_utils.
"""

import sys
import argparse
from . import help, set_debug
from loguru import logger


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Useful Utils - A collection of reusable code snippets and utilities"
    )
    parser.add_argument(
        "--version", action="version", version="useful-utils 1.0.0"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Help command
    help_parser = subparsers.add_parser("help", help="Show help information")
    help_parser.add_argument("subcommand", nargs="?", choices=["list", "detail", "search"])
    help_parser.add_argument("function_name", nargs="?")
    help_parser.add_argument("query", nargs="?")
    
    # Logging command
    logging_parser = subparsers.add_parser("logging", help="Configure logging")
    logging_parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    logging_parser.add_argument("--message", "-m", help="Log message to display")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == "help":
        if args.subcommand == "list":
            print(help("list"))
        elif args.subcommand == "detail" and args.function_name:
            print(help("detail", args.function_name))
        elif args.subcommand == "search" and args.query:
            print(help("search", args.query))
        else:
            print(help())
    
    elif args.command == "logging":
        set_debug(debug_mode=args.debug)
        if args.message:
            logger.info(args.message)
        else:
            logger.info("Logging configured successfully")


if __name__ == "__main__":
    main() 