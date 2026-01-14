# Oracle Cloud Deployment Guide

Deploy the Everett RAG system to Oracle Cloud Always Free Tier for **free, 24/7 hosting with no cold starts**.

## What You Get (Free Forever)

| Resource | Allocation |
|----------|------------|
| **ARM VMs** | 4 OCPUs + 24 GB RAM total |
| **Storage** | 200 GB block storage |
| **Bandwidth** | 10 TB/month outbound |

This is more than enough for the Everett RAG system.

---

## Prerequisites

1. **Oracle Cloud Account** - [Sign up here](https://www.oracle.com/cloud/free/)
2. **AWS Credentials** - For Bedrock API (embedding + LLM)
3. **SSH Key Pair** - For VM access

---

## Step 1: Create Oracle Cloud Account

1. Go to [oracle.com/cloud/free](https://www.oracle.com/cloud/free/)
2. Sign up with your email
3. Add a credit card (won't be charged for Always Free resources)
4. Wait for account approval (can take a few hours)

> ⚠️ **Tip**: If your account is rejected, try using a different email or card.

---

## Step 2: Create a VM Instance

1. Log into Oracle Cloud Console
2. Go to **Compute → Instances → Create Instance**

### Instance Configuration:

| Setting | Value |
|---------|-------|
| **Name** | `everett-rag` |
| **Image** | Oracle Linux 8 or Ubuntu 22.04 |
| **Shape** | VM.Standard.A1.Flex (ARM) |
| **OCPUs** | 2 (free tier allows up to 4) |
| **Memory** | 12 GB (free tier allows up to 24) |
| **Boot Volume** | 50 GB |

### Networking:
- Create new VCN or use existing
- Assign public IP address
- **Add SSH key** for access

3. Click **Create** and wait for the instance to be running

---

## Step 3: Configure Security List (Firewall)

1. Go to **Networking → Virtual Cloud Networks**
2. Click your VCN → **Security Lists** → Default Security List
3. Add **Ingress Rules**:

| Source CIDR | Protocol | Port | Description |
|-------------|----------|------|-------------|
| `0.0.0.0/0` | TCP | 80 | HTTP |
| `0.0.0.0/0` | TCP | 443 | HTTPS |
| `0.0.0.0/0` | TCP | 8501 | Streamlit (temporary) |
| `0.0.0.0/0` | TCP | 8000 | API (temporary) |

---

## Step 4: Connect to Your VM

```bash
# Replace with your VM's public IP
ssh -i ~/.ssh/your-key ubuntu@YOUR_VM_IP
```

---

## Step 5: Initial Server Setup

```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install Git
sudo apt-get install -y git

# Clone your repository
git clone https://github.com/YOUR_USERNAME/Everett-RAG.git
cd Everett-RAG
```

---

## Step 6: Run the Deployment Script

```bash
# Make script executable
chmod +x deploy.sh

# Run deployment
./deploy.sh
```

The script will:
1. Install Docker and Docker Compose
2. Create environment file
3. Build Docker images
4. Start the services

---

## Step 7: Configure AWS Credentials

Edit the `.env` file with your AWS credentials:

```bash
nano .env
```

```env
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_actual_access_key
AWS_SECRET_ACCESS_KEY=your_actual_secret_key
```

Then restart:

```bash
docker-compose down
docker-compose up -d
```

---

## Step 8: Verify Deployment

```bash
# Check containers are running
docker-compose ps

# Check backend health
curl http://localhost:8000/health

# View logs
docker-compose logs -f
```

Access your app at: `http://YOUR_VM_IP:8501`

---

## Optional: Set Up Custom Domain with HTTPS

### 1. Point Domain to VM

Add an A record in your DNS:
- **Type**: A
- **Name**: @ (or subdomain like `everett`)
- **Value**: Your VM's public IP

### 2. Install Certbot for SSL

```bash
sudo apt-get install -y certbot

# Get certificate (standalone mode)
docker-compose down
sudo certbot certonly --standalone -d yourdomain.com
```

### 3. Copy Certificates

```bash
sudo mkdir -p nginx/ssl
sudo cp /etc/letsencrypt/live/yourdomain.com/fullchain.pem nginx/ssl/
sudo cp /etc/letsencrypt/live/yourdomain.com/privkey.pem nginx/ssl/
sudo chown -R $USER:$USER nginx/ssl
```

### 4. Update Nginx Config

Edit `nginx/nginx.conf`:
- Replace `server_name _` with your domain
- Uncomment the HTTPS server block
- Uncomment the HTTP → HTTPS redirect

### 5. Start with Nginx

```bash
docker-compose --profile with-nginx up -d
```

---

## Useful Commands

```bash
# View logs
docker-compose logs -f

# Restart services
docker-compose restart

# Stop everything
docker-compose down

# Rebuild after code changes
docker-compose build --no-cache
docker-compose up -d

# Check resource usage
docker stats
```

---

## Troubleshooting

### Container won't start
```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend
```

### Out of memory
- Reduce the number of OCPUs/RAM allocated to other services
- Consider using swap:
```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Port already in use
```bash
# Find what's using the port
sudo lsof -i :8000
# Kill it
sudo kill -9 PID
```

### AWS Bedrock errors
- Verify your AWS credentials are correct
- Check that Bedrock is enabled in your AWS account
- Ensure your IAM user has `bedrock:InvokeModel` permission

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│              Oracle Cloud VM                     │
│  ┌─────────────┐      ┌─────────────────────┐   │
│  │   Nginx     │◄────►│   Streamlit (8501)  │   │
│  │  (80/443)   │      └─────────────────────┘   │
│  └─────────────┘               │                │
│         │                      ▼                │
│         │              ┌─────────────────────┐  │
│         └─────────────►│   FastAPI (8000)    │  │
│                        │   + FAISS Index     │  │
│                        └─────────────────────┘  │
│                                │                │
└────────────────────────────────┼────────────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │   AWS Bedrock   │
                        │  (Claude Haiku) │
                        └─────────────────┘
```

---

## Cost Breakdown

| Resource | Cost |
|----------|------|
| Oracle Cloud VM | **$0** (Always Free) |
| Oracle Storage | **$0** (200 GB free) |
| Oracle Bandwidth | **$0** (10 TB free) |
| AWS Bedrock | ~$0.001-0.01 per query |
| **Total** | **< $1/month** for typical usage |

---

## Security Recommendations

1. **Remove temporary ports** (8000, 8501) from security list after setting up Nginx
2. **Use HTTPS** with Let's Encrypt
3. **Set up fail2ban** for SSH protection:
   ```bash
   sudo apt-get install fail2ban
   sudo systemctl enable fail2ban
   ```
4. **Keep system updated**:
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```

