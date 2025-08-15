#!/usr/bin/env python3
"""
Main entry point for the INR USD Rates package.
"""

import logging
from .scheduler import RateScheduler

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    """Main function to start the exchange rate scheduler."""
    scheduler = RateScheduler()
    scheduler.schedule_weekday_notifications()
    scheduler.run()


if __name__ == "__main__":
    main()