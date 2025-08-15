"""
Configuration file for INR USD Rates application
"""
import os

# Email Configuration
EMAIL_ADDRESS = "layankaushik13@gmail.com"
RECIPIENT_EMAIL = "layankaushik13@gmail.com"

# You need to set this environment variable with your app password
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Scheduler Configuration
NOTIFICATION_TIME = "09:00"  # 9:00 AM PST
TIMEZONE = "US/Pacific"

# Web App Configuration
WEB_HOST = "0.0.0.0"
WEB_PORT = 5000
DEBUG_MODE = True

# API Configuration
EXCHANGE_API_URL = "https://api.exchangerate-api.com/v4/latest"
API_TIMEOUT = 10

# Supported Currency Pairs
SUPPORTED_CURRENCIES = {
    'USD': 'US Dollar',
    'EUR': 'Euro', 
    'GBP': 'British Pound',
    'CAD': 'Canadian Dollar',
    'AUD': 'Australian Dollar',
    'JPY': 'Japanese Yen',
    'CHF': 'Swiss Franc',
    'CNY': 'Chinese Yuan'
}