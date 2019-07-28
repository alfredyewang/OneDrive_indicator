
#!/usr/bin/python
import os
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator
from gi.repository import Notify as notify

def main():
  indicator = appindicator.Indicator.new("Onedrive", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  notify.init('Onedrive')
  gtk.main()

def menu():
  menu = gtk.Menu()
  command_open_folder = gtk.MenuItem('Open OneDrive Folder')
  command_open_folder.connect('activate', open_folder)
  menu.append(command_open_folder)

  command_start_syncing = gtk.MenuItem('Start Syncing')
  command_start_syncing.connect('activate', start_syncing )
  menu.append(command_start_syncing)

  command_quit = gtk.MenuItem('Quit')
  command_quit.connect('activate', quit)
  menu.append(command_quit)

  # command_monitor = gtk.MenuItem('Monitor')
  # command_monitor.connect('activate', monitor)
  # menu.append(command_monitor)

  menu.show_all()
  return menu

def open_folder(_):
  os.system("nautilus $HOME/OneDrive")

def monitor(_):
  import subprocess
  message = subprocess.check_output("onedrive -m", shell=True)
  print(message)
  message = str(message)
  notify.Notification.new("Status", message, None).show()


def start_syncing(_):
  import subprocess
  message = subprocess.check_output("onedrive", shell=True)
  message = str(message)[2:-1]
  if len(message) == 0:
    notify.Notification.new("Status", 'Synced', None).show()

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()
