# Django_dashboard_DHT11
Display DHT11 value to show on dashboard from Django on Raspberry pi

When run just type "python manage.py runserver 192.168.210.9:8000" or "python3 manage.py runserver 0.0.0.0:8000"
If we use 0.0.0.0 is just calls itself.
=======================================================
In case we want to set up Rpi to autorun the server, so need to add this command these step.
1. Open terminal
2. Type "sudo nano /etc/rc.local"
3. Tpye "python3 /home/pi/Desktop/DHT-dashboard/myenv/relay/manage.py runserver 0.0.0.0:8000" 
4. Ctrl+x, Yes , to save this command.
5. Add this command in manage.py
def main():
    	os.chdir("/home/pi/Desktop/DHT-dashboard/myenv/relay/")  # this command to set the current workding directory" (very important).
 	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relay.settings')
 try:
	from django.core.management import execute_from_command_line
	except ImportError as exc:
      


