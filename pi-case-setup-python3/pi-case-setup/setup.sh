
#install smart fan service
sudo cp ./pi-fan.py /usr/bin
sudo cp ./pi-case-fan.service /etc/systemd/system/
sudo systemctl enable pi-case-fan.service
sudo systemctl start pi-case-fan.service
#install power ctrl service
sudo cp ./restart.py /usr/bin
sudo cp /etc/rc.local /etc/rc.local.bakup
sudo cp ./rc.local /etc/rc.local
