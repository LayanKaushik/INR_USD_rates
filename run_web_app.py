#!/usr/bin/env python3
"""
Launch script for the INR USD Rates web application.
This script starts both the web server and the email scheduler.
"""

import os
import sys
import logging
import threading
from inr_usd_rates.web_app import app, start_scheduler
from inr_usd_rates.config import WEB_HOST, WEB_PORT, DEBUG_MODE

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('currency_tracker.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main function to start the web application and scheduler."""
    logger.info("Starting INR USD Rates Web Application")
    
    # Check if email password is configured
    if not os.getenv('EMAIL_PASSWORD'):
        logger.warning("""
        ⚠️  EMAIL_PASSWORD environment variable not set!
        
        To enable email notifications, please:
        1. Go to your Google Account settings
        2. Enable 2-factor authentication
        3. Generate an app password for Gmail
        4. Set the environment variable:
           
           Windows: set EMAIL_PASSWORD=your_app_password
           Linux/Mac: export EMAIL_PASSWORD=your_app_password
        
        The web application will still work without email notifications.
        """)
    
    try:
        # Start the email scheduler in a background thread
        logger.info("Starting email scheduler thread...")
        scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
        scheduler_thread.start()
        
        # Start the Flask web application
        logger.info(f"Starting web server on http://{WEB_HOST}:{WEB_PORT}")
        logger.info("Press Ctrl+C to stop the application")
        
        app.run(
            host=WEB_HOST,
            port=WEB_PORT,
            debug=DEBUG_MODE,
            use_reloader=False  # Disable reloader to prevent scheduler from starting twice
        )
        
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
    except Exception as e:
        logger.error(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()