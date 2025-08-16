"""
Configuration file for INR USD Rates application
"""
import os

# Environment detection
ENV = os.getenv('ENVIRONMENT', 'development')
IS_PRODUCTION = ENV == 'production'

# Email Configuration
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', "layankaushik13@gmail.com")
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', EMAIL_ADDRESS)
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Scheduler Configuration
NOTIFICATION_TIME = os.getenv('NOTIFICATION_TIME', "09:00")  # 9:00 AM PST
TIMEZONE = os.getenv('TIMEZONE', "US/Pacific")

# Application Configuration
# (Web app configurations removed - package only)

# API Configuration
EXCHANGE_API_URL = os.getenv('EXCHANGE_API_URL', "https://api.exchangerate-api.com/v4/latest")
API_TIMEOUT = int(os.getenv('API_TIMEOUT', 10))

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO' if IS_PRODUCTION else 'DEBUG')

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

# Email scheduler always enabled for package usage
ENABLE_EMAIL_SCHEDULER = os.getenv('ENABLE_EMAIL_SCHEDULER', 'true').lower() == 'true'