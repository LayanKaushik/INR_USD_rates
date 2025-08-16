# INR USD Rates

A Python package for automated USD to INR exchange rate tracking and email notifications.

## Features

- Automated daily email notifications with current exchange rates
- Configurable currency pairs (default: USD to INR)
- Scheduled weekday notifications
- Modular design with separate components for tracking, notifications, and scheduling
- Easy to extend for other currency pairs

## Installation

### From PyPI (when published)
```bash
pip install inr-usd-rates
```

### From Source
```bash
git clone https://github.com/LayanKaushik/INR_USD_rates.git
cd INR_USD_rates
pip install -e .
```

## Quick Start

### Environment Variables
Set up the following environment variables:
```bash
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
export RECIPIENT_EMAIL="recipient@example.com"  # Optional, defaults to EMAIL_ADDRESS
```

### Run the Scheduler
```bash
# Using the installed command
inr-usd-rates

# Or using Python module
python -m inr_usd_rates.main
```

## Usage

### Basic Usage
```python
from inr_usd_rates import ExchangeRateTracker, EmailNotifier, RateScheduler

# Create components
tracker = ExchangeRateTracker()
notifier = EmailNotifier()
scheduler = RateScheduler(tracker, notifier)

# Schedule weekday notifications at 8:00 AM
scheduler.schedule_weekday_notifications("08:00")

# Run the scheduler
scheduler.run()
```

### Custom Currency Pair
```python
from inr_usd_rates import ExchangeRateTracker

# Track EUR to USD
tracker = ExchangeRateTracker("EUR", "USD")
rate = tracker.get_exchange_rate()
print(f"1 EUR = {rate} USD")
```

### Manual Email Notification
```python
from inr_usd_rates import EmailNotifier

notifier = EmailNotifier()
notifier.send_rate_notification(75.25, "USD", "INR")
```

## Configuration

### Email Setup
For Gmail, you'll need to:
1. Enable 2-factor authentication
2. Generate an app password
3. Use the app password as EMAIL_PASSWORD

### Scheduling
The default schedule sends emails on weekdays at 8:00 AM. You can customize this:

```python
scheduler = RateScheduler()
scheduler.schedule_weekday_notifications("09:30")  # 9:30 AM
```

### Environment Variables
```bash
# Email Configuration
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-gmail-app-password
RECIPIENT_EMAIL=recipient@example.com

# Scheduler Configuration  
NOTIFICATION_TIME=09:00
TIMEZONE=US/Pacific
ENABLE_EMAIL_SCHEDULER=true

# API Configuration
EXCHANGE_API_URL=https://api.exchangerate-api.com/v4/latest
API_TIMEOUT=10
```

## Development

### Setup Development Environment
```bash
git clone https://github.com/LayanKaushik/INR_USD_rates.git
cd INR_USD_rates
pip install -e .
pip install pytest black flake8  # Optional dev dependencies
```

### Run Tests
```bash
pytest
```

### Code Formatting
```bash
black inr_usd_rates/
```

## Requirements

- Python 3.7+
- requests>=2.25.0
- schedule>=1.1.0
- pytz>=2021.1

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Future Enhancements

- Support for more currency pairs
- Historical rate tracking
- Rate change alerts and thresholds
- Integration with other notification channels (SMS, Slack, etc.)
