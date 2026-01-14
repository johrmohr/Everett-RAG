#!/bin/bash
# Everett RAG System - Deployment Script for Oracle Cloud
# Run this script on your Oracle Cloud VM

set -e

echo "🚀 Everett RAG Deployment Script"
echo "================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo -e "${RED}Please don't run as root. Use a regular user with sudo access.${NC}"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Step 1: Update system
echo -e "\n${YELLOW}Step 1: Updating system...${NC}"
sudo apt-get update && sudo apt-get upgrade -y

# Step 2: Install Docker
echo -e "\n${YELLOW}Step 2: Installing Docker...${NC}"
if command_exists docker; then
    echo "Docker already installed"
else
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    rm get-docker.sh
    echo -e "${GREEN}Docker installed. You may need to log out and back in.${NC}"
fi

# Step 3: Install Docker Compose
echo -e "\n${YELLOW}Step 3: Installing Docker Compose...${NC}"
if command_exists docker-compose; then
    echo "Docker Compose already installed"
else
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    echo -e "${GREEN}Docker Compose installed.${NC}"
fi

# Step 4: Create environment file
echo -e "\n${YELLOW}Step 4: Setting up environment...${NC}"
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << 'EOF'
# AWS Credentials for Bedrock
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
EOF
    echo -e "${YELLOW}⚠️  Please edit .env file with your AWS credentials!${NC}"
else
    echo ".env file already exists"
fi

# Step 5: Build and start containers
echo -e "\n${YELLOW}Step 5: Building Docker images...${NC}"
docker-compose build

echo -e "\n${YELLOW}Step 6: Starting services...${NC}"
docker-compose up -d backend

# Step 7: Wait for services to be healthy
echo -e "\n${YELLOW}Waiting for services to start...${NC}"
sleep 30

# Step 8: Check health
echo -e "\n${YELLOW}Checking service health...${NC}"
if curl -s http://localhost:8000/health | grep -q "healthy"; then
    echo -e "${GREEN}✅ Backend is healthy${NC}"
else
    echo -e "${RED}❌ Backend health check failed${NC}"
fi

# Get public IP
PUBLIC_IP=$(curl -s ifconfig.me 2>/dev/null || echo "unknown")

echo -e "\n${GREEN}=================================${NC}"
echo -e "${GREEN}🎉 Deployment Complete!${NC}"
echo -e "${GREEN}=================================${NC}"
echo ""
echo "Your Everett RAG API is now running:"
echo ""
echo "  API: http://${PUBLIC_IP}:8000"
echo "  Health: http://${PUBLIC_IP}:8000/health"
echo "  Docs: http://${PUBLIC_IP}:8000/docs"
echo ""
echo "To view logs:"
echo "  docker-compose logs -f backend"
echo ""
echo "To stop:"
echo "  docker-compose down"
echo ""
echo -e "${YELLOW}Note: Make sure port 8000 is open in Oracle Cloud security list!${NC}"

