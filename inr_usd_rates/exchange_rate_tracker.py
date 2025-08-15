import requests
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class ExchangeRateTracker:
    """Class to handle exchange rate fetching and tracking."""
    
    def __init__(self, base_currency: str = "USD", target_currency: str = "INR"):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    def get_exchange_rate(self) -> Optional[float]:
        """Get current exchange rate from base currency to target currency."""
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            rate = data['rates'][self.target_currency]
            logger.info(f"Successfully fetched exchange rate: 1 {self.base_currency} = {rate} {self.target_currency}")
            return rate
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching exchange rate: {e}")
            return None
        except KeyError as e:
            logger.error(f"Error parsing exchange rate data: {e}")
            return None