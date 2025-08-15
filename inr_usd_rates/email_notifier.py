import smtplib
import os
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)


class EmailNotifier:
    """Class to handle email notifications for exchange rates."""
    
    def __init__(self, email_address: Optional[str] = None, email_password: Optional[str] = None, 
                 recipient_email: Optional[str] = None):
        self.email_address = email_address or os.getenv('EMAIL_ADDRESS')
        self.email_password = email_password or os.getenv('EMAIL_PASSWORD')
        self.recipient_email = recipient_email or os.getenv('RECIPIENT_EMAIL', self.email_address)
        
        if not self.email_address or not self.email_password:
            logger.warning("Email credentials not provided. Set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
    
    def send_rate_notification(self, rate: float, base_currency: str = "USD", 
                             target_currency: str = "INR") -> bool:
        """Send email notification with current exchange rate."""
        if not self.email_address or not self.email_password:
            logger.error("Email credentials not available")
            return False
            
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = self.recipient_email
            msg['Subject'] = f'Daily {base_currency} to {target_currency} Exchange Rate - {datetime.now().strftime("%Y-%m-%d")}'
            
            body = self._create_email_body(rate, base_currency, target_currency)
            msg.attach(MIMEText(body, 'html'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.send_message(msg)
            server.quit()
            
            logger.info(f"Email sent successfully to {self.recipient_email}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return False
    
    def _create_email_body(self, rate: float, base_currency: str, target_currency: str) -> str:
        """Create HTML email body with exchange rate information."""
        return f"""
        <html>
        <body>
        <h2>Daily Exchange Rate Update</h2>
        <p>Hello,</p>
        <p>Here's today's exchange rate:</p>
        <div style="background-color: #f0f8ff; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h3 style="color: #2c5aa0;">1 {base_currency} = {rate:.4f} {target_currency}</h3>
        </div>
        <p>Date: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}</p>
        <p>This is an automated email from your currency tracker.</p>
        </body>
        </html>
        """