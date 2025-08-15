import schedule
import time
import logging
from .exchange_rate_tracker import ExchangeRateTracker
from .email_notifier import EmailNotifier

logger = logging.getLogger(__name__)


class RateScheduler:
    """Class to handle scheduling of exchange rate notifications."""
    
    def __init__(self, tracker: ExchangeRateTracker = None, notifier: EmailNotifier = None):
        self.tracker = tracker or ExchangeRateTracker()
        self.notifier = notifier or EmailNotifier()
    
    def job(self):
        """Main job function to get rate and send email."""
        logger.info("Starting daily exchange rate job")
        rate = self.tracker.get_exchange_rate()
        
        if rate is not None:
            success = self.notifier.send_rate_notification(
                rate, 
                self.tracker.base_currency, 
                self.tracker.target_currency
            )
            if success:
                logger.info("Daily exchange rate job completed successfully")
            else:
                logger.error("Failed to send email")
        else:
            logger.error("Failed to fetch exchange rate")
    
    def schedule_weekday_notifications(self, time_str: str = "08:00"):
        """Schedule notifications for weekdays at specified time."""
        schedule.every().monday.at(time_str).do(self.job)
        schedule.every().tuesday.at(time_str).do(self.job)
        schedule.every().wednesday.at(time_str).do(self.job)
        schedule.every().thursday.at(time_str).do(self.job)
        schedule.every().friday.at(time_str).do(self.job)
        
        logger.info(f"Exchange rate scheduler started. Will send emails on weekdays at {time_str}")
    
    def run(self):
        """Run the scheduler main loop."""
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            logger.info("Scheduler stopped by user")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")