# 🚀 Deployment Guide

This guide covers multiple deployment options for the INR USD Rates application.

## 🌐 Quick Deploy Options

### 1. **Render (Recommended - Free Tier Available)**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

**Steps:**
1. Fork this repository
2. Connect your GitHub account to Render
3. Create a new Web Service from your forked repository
4. Render will automatically detect the `render.yaml` configuration
5. Set environment variables (especially `EMAIL_PASSWORD`)
6. Deploy!

**Live URL:** Your app will be available at `https://your-app-name.onrender.com`

### 2. **Heroku (Easy One-Click Deploy)**

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/LayanKaushik/INR_USD_rates)

**Steps:**
1. Click the "Deploy to Heroku" button above
2. Fill in the app name and environment variables
3. Set `EMAIL_PASSWORD` with your Gmail app password
4. Click "Deploy app"
5. Enable Heroku Scheduler for daily emails

**Live URL:** Your app will be available at `https://your-app-name.herokuapp.com`

### 3. **Railway**

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

**Steps:**
1. Connect your GitHub repository to Railway
2. Configure environment variables
3. Deploy automatically

---

## ⚙️ Environment Variables

### **Required for Email Notifications:**
- `EMAIL_PASSWORD`: Gmail app password (16 characters)

### **Optional (with defaults):**
```env
ENVIRONMENT=production
EMAIL_ADDRESS=layankaushik13@gmail.com
RECIPIENT_EMAIL=layankaushik13@gmail.com
NOTIFICATION_TIME=09:00
TIMEZONE=US/Pacific
SECRET_KEY=auto-generated
```

---

## 🔧 Manual Deployment Options

### **Docker Deployment**

```bash
# Clone repository
git clone https://github.com/LayanKaushik/INR_USD_rates.git
cd INR_USD_rates

# Create environment file
cp .env.example .env
# Edit .env with your EMAIL_PASSWORD

# Build and run with Docker Compose
docker-compose up -d

# Access application
open http://localhost:5000
```

### **VPS/Server Deployment**

```bash
# Install Python 3.9+
sudo apt update
sudo apt install python3.9 python3-pip nginx

# Clone and setup
git clone https://github.com/LayanKaushik/INR_USD_rates.git
cd INR_USD_rates
pip install -r requirements.txt

# Set environment variables
export EMAIL_PASSWORD="your_app_password"
export ENVIRONMENT="production"

# Run with Gunicorn
gunicorn --bind 0.0.0.0:5000 inr_usd_rates.web_app:app

# Setup Nginx proxy (optional)
# Configure systemd service for auto-restart
```

---

## 📧 Email Setup Guide

### **1. Enable 2-Factor Authentication**
- Go to [Google Account Security](https://myaccount.google.com/security)
- Turn on 2-Step Verification

### **2. Generate App Password**
- In Security settings, find "App passwords"
- Select "Mail" as the app
- Copy the 16-character password
- Use this as your `EMAIL_PASSWORD` environment variable

### **3. Test Email Configuration**
```bash
# Test email functionality
python -c "
from inr_usd_rates import EmailNotifier
notifier = EmailNotifier()
success = notifier.send_rate_notification(75.25, 'USD', 'INR')
print('✅ Email sent!' if success else '❌ Email failed')
"
```

---

## 🔄 Automated Daily Emails

### **Cloud Platforms (Render/Heroku):**
- Use built-in cron jobs or scheduler add-ons
- Render: Configured in `render.yaml`
- Heroku: Use Heroku Scheduler add-on

### **Self-Hosted:**
```bash
# Add to crontab for 9 AM PST (5 PM UTC) weekdays
0 17 * * 1-5 cd /path/to/app && python -c "
from inr_usd_rates import ExchangeRateTracker, EmailNotifier
import os
os.environ['EMAIL_PASSWORD'] = 'your_password'
tracker = ExchangeRateTracker()
notifier = EmailNotifier()
rate = tracker.get_exchange_rate()
if rate: notifier.send_rate_notification(rate, 'USD', 'INR')
"
```

---

## 🏥 Health Monitoring

### **Health Check Endpoint:**
```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-16T10:30:00",
  "api_connected": true,
  "environment": "production"
}
```

### **Monitoring Setup:**
- **Uptime monitoring:** Use UptimeRobot, Pingdom, or StatusCake
- **Logs:** Check platform-specific logging (Render logs, Heroku logs)
- **Alerts:** Set up email alerts for downtime

---

## 🔒 Security Considerations

### **Production Checklist:**
- ✅ Set strong `SECRET_KEY`
- ✅ Use environment variables for sensitive data
- ✅ Enable HTTPS (automatic on Render/Heroku)
- ✅ Monitor application logs
- ✅ Regular dependency updates
- ✅ Use app passwords, not account passwords

### **Rate Limiting:**
- Built-in API rate limiting
- Configurable via `RATE_LIMIT_PER_MINUTE`

---

## 🐛 Troubleshooting

### **Common Issues:**

**1. Email not sending:**
```bash
# Check EMAIL_PASSWORD is set correctly
echo $EMAIL_PASSWORD

# Verify 2FA is enabled on Gmail
# Ensure app password is exactly 16 characters
```

**2. Application won't start:**
```bash
# Check logs for errors
heroku logs --tail  # Heroku
render logs         # Render

# Verify environment variables are set
```

**3. API not responding:**
```bash
# Test API connectivity
curl https://your-app.com/health

# Check exchange rate API
curl https://api.exchangerate-api.com/v4/latest/USD
```

---

## 📊 Performance Optimization

### **Caching:**
- API responses cached for 1 minute
- Static assets served with CDN on cloud platforms

### **Scaling:**
- Horizontal scaling available on all cloud platforms
- Database can be added for historical data storage

---

## 🆕 Updates and Maintenance

### **Automatic Updates:**
- GitHub Actions CI/CD pipeline included
- Automatic deployment on `main` branch push
- Health checks and testing before deployment

### **Manual Updates:**
```bash
git pull origin main
pip install -r requirements.txt
# Restart application service
```

---

## 💡 Features Available

✅ **Live Exchange Rates**: USD, EUR, GBP to INR  
✅ **Currency Converter**: Interactive real-time conversion  
✅ **Dark/Light Mode**: Automatic theme switching  
✅ **Mobile Responsive**: Works on all devices  
✅ **Daily Email Notifications**: Automated at 9 AM PST  
✅ **API Endpoints**: RESTful API for programmatic access  
✅ **Health Monitoring**: Built-in health checks  
✅ **Production Ready**: Optimized for cloud deployment  

---

## 🎯 Next Steps After Deployment

1. **Test the live application** at your deployment URL
2. **Set up monitoring** with your preferred service
3. **Configure email notifications** with your Gmail app password
4. **Share the URL** with others who need currency rates
5. **Monitor logs** for any issues during the first week

**Your application will be accessible worldwide at your deployment URL! 🌍**