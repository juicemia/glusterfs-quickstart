# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'socket'

# For the bridge network to work properly you need to set it up so that
# it's on the same subnet as the interface being used for the bridge.
# This is because the bridge is going to communicate over the interface's
# broadcast address.
iface = ENV['VAGRANT_BRIDGE_IFACE']
raise 'VAGRANT_BRIDGE_IFACE required' if iface.to_s == ''

sock = Socket.getifaddrs.select { |s| s.name == iface && s.addr.ipv4? }.first
raise "#{iface} not found in list of interfaces" if sock.nil?

slash24 = sock.addr.ip_address.split('.')[0...3].join('.')

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "base"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL

  

  [1, 2, 3].each do |id|
    file_to_disk = "./tmp/glusterfs-vol-#{id}.vdi"

    config.vm.define "vol#{id}" do |vol|
      vol.vm.box = "generic/fedora28"
      vol.vm.hostname = "vol#{id}"

      addr = "#{slash24}.1#{id}"
      puts "Configuring #{vol.vm.hostname} with IP address #{addr}"

      vol.vm.network :public_network, ip: addr, bridge: 'wlp1s0'

      unless File.exist? file_to_disk
        vol.vm.provider 'virtualbox' do |vbox|
          satactl = "satactl-#{id}"
          vbox.customize ["storagectl", :id, "--name", satactl, "--add", "sata"]
  
          vbox.customize ['createhd', '--filename', file_to_disk, '--size', 1 * 1024]
          vbox.customize ['storageattach', :id, '--storagectl', satactl, '--port', 1, '--device', 0, '--type', 'hdd', '--medium', file_to_disk]
        end
      end
    end
  end
end
