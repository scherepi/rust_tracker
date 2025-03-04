import a2s
import time
import I2C_LCD_driver as driver
# access and clear our LCD!
mylcd = driver.lcd()
mylcd.lcd_clear()
# print startup message:
mylcd.lcd_display_string("Started!", 1)
 
# define our server address and port
# TODO: use a config file for this
address = ("205.178.168.41", 28010)
while True:
    try:
        # get the server info and display it!
        info = a2s.info(address)
        mylcd.lcd_display_string(info.server_name[0:16], 1)
        mylcd.lcd_display_string("Active: " + str(info.player_count),2)
    except Exception as e:
        # if something happens, print the error and quit
        print(e)
        exit(1)
      # re-query every minute
      # TODO: add this value to the config file too
        time.sleep(60)
