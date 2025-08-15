"""
INR USD Rates Package

A Python package for automated USD to INR exchange rate tracking and email notifications.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .exchange_rate_tracker import ExchangeRateTracker
from .email_notifier import EmailNotifier
from .scheduler import RateScheduler

__all__ = ["ExchangeRateTracker", "EmailNotifier", "RateScheduler"]