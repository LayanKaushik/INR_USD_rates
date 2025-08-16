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

# Web App Configuration
WEB_HOST = os.getenv('HOST', '0.0.0.0')
WEB_PORT = int(os.getenv('PORT', 5000))
DEBUG_MODE = not IS_PRODUCTION

# Security Configuration
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

# API Configuration
EXCHANGE_API_URL = os.getenv('EXCHANGE_API_URL', "https://api.exchangerate-api.com/v4/latest")
API_TIMEOUT = int(os.getenv('API_TIMEOUT', 10))

# Database Configuration (for future use)
DATABASE_URL = os.getenv('DATABASE_URL')

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO' if IS_PRODUCTION else 'DEBUG')

# Rate Limiting
RATE_LIMIT_PER_MINUTE = int(os.getenv('RATE_LIMIT_PER_MINUTE', 60))

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

# Production specific settings
if IS_PRODUCTION:
    # Disable email scheduler in production (use external cron job instead)
    ENABLE_EMAIL_SCHEDULER = os.getenv('ENABLE_EMAIL_SCHEDULER', 'false').lower() == 'true'
else:
    ENABLE_EMAIL_SCHEDULER = True