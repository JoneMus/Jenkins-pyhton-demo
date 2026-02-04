# Using Jenkinsin LTS (Long Term Support)
FROM jenkins/jenkins:lts

# Change to root user to install packages
USER root

# Update package lists and install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Change back to jenkins user
USER jenkins