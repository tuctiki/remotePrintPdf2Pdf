from selenium import webdriver
import time

print("Test Execution Started")


options = webdriver.FirefoxOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

profile = webdriver.FirefoxProfile()
profile.set_preference("print.always_print_silent", True)
profile.set_preference("print_printer", "Save to PDF")
profile.set_preference("print.printer_Save_to_PDF.print_to_filename", '/home/seluser/result.pdf')
profile.set_preference("print.printer_Save_to_PDF.print_to_file", True)

options.profile = profile

driver = webdriver.Remote(
command_executor='http://localhost:4444',
options=options
)

try: 
    driver.maximize_window()
    driver.get("file:///home/seluser/source.pdf")
    time.sleep(5)
    driver.execute_script('window.print();')
    time.sleep(5)
    print("Open local printed")
    driver.get("file:///home/seluser/result.pdf")
    time.sleep(5)
except Exception as err:
    print("Exception: file transformaion error:", err)
finally:
    driver.quit()

print("Test Execution Successfully Completed!")