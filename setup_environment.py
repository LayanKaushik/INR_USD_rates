#!/usr/bin/env python3
"""
Environment setup script for INR USD Rates application.
This script helps users configure their environment variables.
"""

import os
import getpass
import sys
import platform

def setup_email_config():
    """Interactive setup for email configuration."""
    print("🔧 Email Configuration Setup")
    print("=" * 50)
    
    print("\nTo receive automated email notifications, you'll need:")
    print("1. A Gmail account with 2-factor authentication enabled")
    print("2. An app password generated for this application")
    print("\nHow to generate an app password:")
    print("1. Go to https://myaccount.google.com/security")
    print("2. Enable 2-Step Verification if not already enabled")
    print("3. Go to App passwords section")
    print("4. Generate a new app password for 'Mail'")
    print("5. Copy the 16-character password")
    
    choice = input("\nDo you want to set up email configuration now? (y/n): ").lower()
    
    if choice == 'y':
        app_password = getpass.getpass("Enter your Gmail app password (16 characters): ")
        
        if len(app_password) == 16 and app_password.replace(' ', '').isalnum():
            # Set environment variable for current session
            os.environ['EMAIL_PASSWORD'] = app_password
            
            # Create a .env file for future sessions
            with open('.env', 'w') as f:
                f.write(f"EMAIL_PASSWORD={app_password}\n")
            
            print("✅ Email configuration saved!")
            print("📧 Email notifications will be sent to: layankaushik13@gmail.com")
            print("⏰ Scheduled for weekdays at 9:00 AM PST")
            
            return True
        else:
            print("❌ Invalid app password format. Please check and try again.")
            return False
    
    return False

def create_run_script():
    """Create a convenient run script for the application."""
    if platform.system() == "Windows":
        script_content = """@echo off
echo Starting INR USD Rates Web Application...
if exist .env (
    for /f "tokens=1,2 delims==" %%a in (.env) do set %%a=%%b
)
python run_web_app.py
pause
"""
        with open('run_app.bat', 'w') as f:
            f.write(script_content)
        print("✅ Created run_app.bat - double-click to start the application")
    
    else:  # Linux/Mac
        script_content = """#!/bin/bash
echo "Starting INR USD Rates Web Application..."
if [ -f .env ]; then
    export $(cat .env | xargs)
fi
python3 run_web_app.py
"""
        with open('run_app.sh', 'w') as f:
            f.write(script_content)
        os.chmod('run_app.sh', 0o755)
        print("✅ Created run_app.sh - run with ./run_app.sh")

def main():
    """Main setup function."""
    print("🚀 INR USD Rates Application Setup")
    print("=" * 50)
    
    print("\nThis application provides:")
    print("• 🌐 Web interface for live exchange rates")
    print("• 📧 Daily email notifications at 9 AM PST")
    print("• 💱 Currency converter")
    print("• 📱 Mobile-friendly design")
    
    # Setup email configuration
    email_configured = setup_email_config()
    
    # Create run scripts
    print("\n🔧 Creating run scripts...")
    create_run_script()
    
    print("\n" + "=" * 50)
    print("🎉 Setup Complete!")
    print("\nTo start the application:")
    
    if platform.system() == "Windows":
        print("  Option 1: Double-click run_app.bat")
        print("  Option 2: python run_web_app.py")
    else:
        print("  Option 1: ./run_app.sh")
        print("  Option 2: python3 run_web_app.py")
    
    print("\n📱 Access the web interface at: http://localhost:5000")
    
    if not email_configured:
        print("\n⚠️  Email notifications are disabled until you configure EMAIL_PASSWORD")
        print("   Run this setup script again or manually set the environment variable")
    
    print("\n💡 Tip: Keep the application running to receive daily email notifications!")

if __name__ == "__main__":
    main()