# 🚀 Deployment Guide

This guide covers multiple deployment options for your House Price Prediction application.

## Quick Start (Local)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the complete pipeline
python run_pipeline.py

# 3. Launch the app
streamlit run app.py
```

The app will be available at: `http://localhost:8501`

---

## 🌐 Streamlit Community Cloud (Recommended)

**Free and easiest option!**

### Steps:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/house-price-prediction.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Select the repository and branch
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Configure**
   - The app will automatically run `generate_data.py` and `src/train_model.py` on first load
   - Your app will be live at: `https://yourusername-house-price-prediction-app-xxxxx.streamlit.app`

### Notes:
- Free tier includes: 1 GB storage, unlimited public apps
- Apps sleep after inactivity but wake up on visit
- Perfect for demos and portfolios

---

## 🐳 Docker Deployment

### Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Generate data and train model
RUN python generate_data.py && python src/train_model.py

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run

```bash
# Build image
docker build -t house-price-app .

# Run container
docker run -p 8501:8501 house-price-app

# Run in background
docker run -d -p 8501:8501 --name house-price house-price-app

# Stop container
docker stop house-price

# View logs
docker logs house-price
```

---

## ☁️ AWS Deployment

### Option 1: AWS EC2

1. **Launch EC2 Instance**
   - Ubuntu 22.04 LTS
   - t2.micro (free tier eligible)
   - Configure security group: Allow port 8501

2. **Connect and Setup**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   
   # Install Python and dependencies
   sudo apt update
   sudo apt install python3-pip
   
   # Clone repository
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   
   # Install requirements
   pip3 install -r requirements.txt
   
   # Run pipeline
   python3 run_pipeline.py
   
   # Run app (with nohup to keep running)
   nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &
   ```

3. **Access**
   - Visit: `http://your-ec2-ip:8501`

### Option 2: AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize**
   ```bash
   eb init -p python-3.9 house-price-app --region us-east-1
   ```

3. **Create environment**
   ```bash
   eb create house-price-env
   ```

4. **Deploy**
   ```bash
   eb deploy
   ```

---

## 🔷 Azure Deployment

### Azure Web Apps

1. **Install Azure CLI**
   ```bash
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   ```

2. **Login**
   ```bash
   az login
   ```

3. **Create Resource Group**
   ```bash
   az group create --name house-price-rg --location eastus
   ```

4. **Create App Service Plan**
   ```bash
   az appservice plan create --name house-price-plan \
     --resource-group house-price-rg \
     --sku B1 --is-linux
   ```

5. **Create Web App**
   ```bash
   az webapp create --resource-group house-price-rg \
     --plan house-price-plan \
     --name house-price-app \
     --runtime "PYTHON:3.9"
   ```

6. **Deploy**
   ```bash
   az webapp up --name house-price-app \
     --resource-group house-price-rg
   ```

---

## 🟢 Heroku Deployment

1. **Create Procfile**
   ```bash
   echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   ```

2. **Create setup.sh**
   ```bash
   cat > setup.sh << 'EOF'
   mkdir -p ~/.streamlit/
   
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   EOF
   ```

3. **Deploy**
   ```bash
   # Login
   heroku login
   
   # Create app
   heroku create house-price-app
   
   # Push
   git push heroku main
   
   # Open
   heroku open
   ```

---

## 🔧 Google Cloud Platform

### Cloud Run

1. **Install gcloud CLI**
   ```bash
   curl https://sdk.cloud.google.com | bash
   ```

2. **Initialize**
   ```bash
   gcloud init
   ```

3. **Build and Deploy**
   ```bash
   # Build
   gcloud builds submit --tag gcr.io/PROJECT_ID/house-price-app
   
   # Deploy
   gcloud run deploy house-price-app \
     --image gcr.io/PROJECT_ID/house-price-app \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

---

## 🔒 Production Considerations

### Security
- Use environment variables for sensitive data
- Implement authentication if needed
- Use HTTPS (SSL certificate)
- Regular security updates

### Performance
- Enable caching with `@st.cache_resource` and `@st.cache_data`
- Use CDN for static assets
- Implement request rate limiting
- Monitor application performance

### Monitoring
- Set up application logging
- Use monitoring tools (Datadog, New Relic, etc.)
- Track error rates
- Monitor resource usage

### Backup
- Regular model backups
- Database backups (if applicable)
- Configuration backups

---

## 📊 Cost Comparison

| Platform | Free Tier | Paid Plans | Best For |
|----------|-----------|------------|----------|
| Streamlit Cloud | ✅ Yes | From $0/month | Demos, Portfolios |
| Heroku | ⚠️ Limited | From $7/month | Small apps |
| AWS EC2 | ✅ 12 months | From $5/month | Full control |
| Google Cloud Run | ✅ Generous | Pay per use | Scalable apps |
| Azure | ✅ Limited | From $13/month | Enterprise |
| Docker + VPS | N/A | From $5/month | Full control |

---

## 🆘 Troubleshooting

### Issue: "Model not found"
**Solution:** Run `python src/train_model.py` first

### Issue: Port already in use
**Solution:** 
```bash
# Find process
lsof -i :8501
# Kill process
kill -9 PID
```

### Issue: Memory error
**Solution:** Reduce dataset size in `config.py`

### Issue: Dependencies error
**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Docker Documentation](https://docs.docker.com)
- [AWS Documentation](https://docs.aws.amazon.com)
- [Heroku Documentation](https://devcenter.heroku.com)

---

## 💡 Tips

1. **Start with Streamlit Cloud** - It's free and easiest
2. **Use Docker** for consistency across environments
3. **Monitor costs** on cloud platforms
4. **Implement CI/CD** for automated deployments
5. **Test locally** before deploying

---

Need help? Create an issue on GitHub or contact support!
