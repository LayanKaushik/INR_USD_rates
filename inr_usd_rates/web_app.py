from flask import Flask, render_template, jsonify
import threading
import time
from datetime import datetime
import pytz
from .exchange_rate_tracker import ExchangeRateTracker
from .email_notifier import EmailNotifier
from .scheduler import RateScheduler

app = Flask(__name__)
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
    notifier = EmailNotifier(
        email_address="layankaushik13@gmail.com",
        recipient_email="layankaushik13@gmail.com"
    )
    scheduler = RateScheduler(tracker, notifier)
    
    # Schedule for 9 AM PST (converted to UTC)
    pst = pytz.timezone('US/Pacific')
    utc = pytz.UTC
    
    # 9 AM PST is 17:00 UTC (PST is UTC-8) during standard time
    # 16:00 UTC during daylight saving time (PDT is UTC-7)
    # We'll use a more flexible approach
    scheduler.schedule_weekday_notifications("09:00", timezone="US/Pacific")
    
    # Run scheduler in background
    scheduler_thread = threading.Thread(target=scheduler.run, daemon=True)
    scheduler_thread.start()

if __name__ == '__main__':
    # Start the email scheduler
    start_scheduler()
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)