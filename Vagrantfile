# -*- mode: ruby -*-
# vi: set ft=ruby :

if ARGV.include?('up') || ARGV.include?('reload')
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
end

Vagrant.configure("2") do |config|
  [1, 2, 3].each do |id|
    config.vm.define "vol#{id}" do |vol|
      vol.vm.box = "hashicorp/bionic64"
      vol.vm.hostname = "vol#{id}"

      addr = "#{slash24}.1#{id}"
      vol.vm.network :public_network, ip: addr, bridge: ''
    end
  end
end
