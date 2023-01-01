Vagrant.configure(2) do |config|
  config.vm.box = "vshn/centos7"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.synced_folder "ssl", "/etc/ssl/certs/server.crt"
  config.vm.synced_folder "ssl", "/etc/ssl/private/server.key"
  config.vm.network "forwarded_port", guest: 80, host: 8080, id: "nginx"
  config.vm.network "forwarded_port", guest: 443, host: 444, id: "nginx"
  config.vm.synced_folder "src", "/srv/src"
  config.vm.provision "shell", path: "provision.sh"
 # config.vm.provision "shell", inline: <<-SHELL
 #     cd /srv/src
 #     python3 app.py &
 #   SHELL
end
