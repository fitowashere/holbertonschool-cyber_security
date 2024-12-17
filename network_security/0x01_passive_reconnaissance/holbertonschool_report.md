# Holberton School Domain Analysis Report
*Date: December 17, 2024*

## 1. IP Ranges

### Primary IP Addresses
- 99.83.190.102 (AWS)
- 75.2.70.75 (AWS)

### Additional IP Ranges (Associated with Subdomains)
- 13.36.10.99 (apply.holbertonschool.com)
- 13.37.98.87 (read.holbertonschool.com)
- 13.38.122.220 (staging-apply-forum.holbertonschool.com)
- 52.85.96.82 (rails-assets.holbertonschool.com)
- 63.35.51.142 (www.holbertonschool.com)
- 104.16.53.111 (support.holbertonschool.com)

## 2. Technologies & Frameworks

### Web Servers
- Amazon CloudFront
- Nginx
- Apache

### Cloud Services
- Amazon Web Services (AWS)
- Cloudflare CDN
- AWS Route 53 (DNS)

### Frontend Technologies
- React
- Ruby on Rails
- JavaScript
- jQuery
- Bootstrap

### Backend Technologies
- Ruby
- Node.js
- PostgreSQL

### Security & Infrastructure
- SSL/TLS (Let's Encrypt)
- AWS WAF
- CloudFront Distribution
- AWS Load Balancer

### Content Management
- Discourse (Forums)
- Custom CMS

### Additional Services
- Google Workspace (Email)
- Zendesk (Support)
- Mailgun
- Dropbox Business

## 3. Notable Findings

### Security Measures
- SPF records implemented
- Multiple domain verification records
- WAF protection
- SSL/TLS on all subdomains

### Infrastructure
- Primary hosting on AWS
- Multiple staging environments
- Distributed CDN setup
- Load-balanced application servers

### Service Distribution
- Main website: AWS CloudFront
- Support system: Cloudflare
- Learning platform: Custom AWS setup
- Application system: Dedicated AWS instances

## 4. Observations

1. The infrastructure is primarily AWS-based with some services distributed across other providers
2. Multiple staging and production environments suggest active development
3. Strong emphasis on security with multiple layers of protection
4. Extensive use of modern web technologies and frameworks
5. Well-structured email delivery system with multiple providers

*Note: This information was gathered through passive reconnaissance using Shodan and should be verified for accuracy.*