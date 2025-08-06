# ansible_note_taking

## Note-Taking App with Ansible Deployment

This project is a simple Python Flask web application for note-taking, deployed on an AWS EC2 instance using Ansible automation.

---

## Project Structure

- `app.py` — The main Flask application file.
- `templates/index.html` — The HTML template rendered by Flask.
- `roles/` — Ansible roles containing tasks, files, and templates for deployment.
- `site.yml` — The main Ansible playbook to configure the EC2 instance and deploy the app.
- `.gitignore` — Specifies files to ignore in Git.
- `README.md` — This file.

---

## Prerequisites

- AWS EC2 instance with Amazon Linux or similar
- Python 3 installed on the EC2 instance
- Ansible installed on your control machine
- Access to AWS security group allowing port 80 inbound traffic
- Git installed (optional for cloning this repo)

---

## Setup Instructions

1. **Clone the repository**


     git clone https://github.com/your-username/your-repo-name.git
     cd your-repo-name

2. **Run the Ansible playbook**

This will configure your EC2 instance, install dependencies, and deploy the app files.

    ansible-playbook -i hosts site.yml

3. **Start the Flask app on the EC2 instance**

SSH into your EC2:

     ssh -i your-key.pem ec2-user@your-ec2-ip

     python3 /home/ec2-user/app.py
    
4. **Access the app**

Open your browser and visit:

     http://your-ec2-public-ip:80



