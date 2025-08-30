# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/debian-13"

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    # Update and upgrade packages
    sudo apt update && sudo apt upgrade -y

    # Install dependencies
    sudo apt install -y curl gnupg2

    # Install Docker
    curl -fsSL https://get.docker.com | sh -s

    sudo usermod -aG docker vagrant

    # Install Podman
    sudo apt install -y podman

    sudo apt install -y python3-venv
  SHELL

end
