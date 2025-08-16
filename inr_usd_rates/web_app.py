from flask import Flask, render_template, jsonify
import threading
import time
import logging
from datetime import datetime
import pytz
from .exchange_rate_tracker import ExchangeRateTracker
from .email_notifier import EmailNotifier
from .scheduler import RateScheduler
from . import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

# Set up logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

tracker = ExchangeRateTracker()

@app.route('/')
def index():
    """Main page displaying current exchange rates"""
    return render_template('index.html')

@app.route('/api/rates')
def get_rates():
    """API endpoint to get current exchange rates"""
    try:
        usd_to_inr = tracker.get_exchange_rate()
        
        # Get rates for other popular currencies
        eur_tracker = ExchangeRateTracker("EUR", "INR")
        eur_to_inr = eur_tracker.get_exchange_rate()
        
        gbp_tracker = ExchangeRateTracker("GBP", "INR") 
        gbp_to_inr = gbp_tracker.get_exchange_rate()
        
        return jsonify({
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'rates': {
                'USD_to_INR': usd_to_inr,
                'EUR_to_INR': eur_to_inr,
                'GBP_to_INR': gbp_to_inr
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/rate/<from_currency>/<to_currency>')
def get_specific_rate(from_currency, to_currency):
    """Get exchange rate for specific currency pair"""
    try:
        custom_tracker = ExchangeRateTracker(from_currency.upper(), to_currency.upper())
        rate = custom_tracker.get_exchange_rate()
        
        return jsonify({
            'success': True,
            'from_currency': from_currency.upper(),
            'to_currency': to_currency.upper(),
            'rate': rate,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

def start_scheduler():
    """Start the email scheduler in a separate thread"""
    if not config.ENABLE_EMAIL_SCHEDULER:
        logger.info("Email scheduler disabled in production mode")
        return
    
    if not config.EMAIL_PASSWORD:
        logger.warning("EMAIL_PASSWORD not set - email notifications disabled")
        return
    
    logger.info("Starting email scheduler...")
    notifier = EmailNotifier(
        email_address=config.EMAIL_ADDRESS,
        recipient_email=config.RECIPIENT_EMAIL
    )
    scheduler = RateScheduler(tracker, notifier)
    
    # Schedule notifications
    scheduler.schedule_weekday_notifications(config.NOTIFICATION_TIME, timezone=config.TIMEZONE)
    
    # Run scheduler in background
    scheduler_thread = threading.Thread(target=scheduler.run, daemon=True)
    scheduler_thread.start()
    logger.info("Email scheduler started successfully")

@app.route('/health')
def health_check():
    """Health check endpoint for production monitoring"""
    try:
        # Test API connectivity
        test_rate = tracker.get_exchange_rate()
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'api_connected': test_rate is not None,
            'environment': config.ENV
        })
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

if __name__ == '__main__':
    # Start the email scheduler only in development
    if not config.IS_PRODUCTION:
        start_scheduler()
    
    # Run the Flask app
    app.run(
        debug=config.DEBUG_MODE, 
        host=config.WEB_HOST, 
        port=config.WEB_PORT
    )