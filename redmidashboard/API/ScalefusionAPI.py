# import requests
#
# intune_api_url = 'https://api.scalefusion.com/api/v1/devices.json'
# bearer_token = '09bac36d5d054d838322aef82d5bc4cd'
# headers = {'Authorization': f'Token {bearer_token}'}
#
# response = requests.get(intune_api_url, headers=headers)
# if response.status_code == 200:
#     data = response.json()
#     devices = data.get('devices', [])
#     if devices:
#         device = devices[0].get('device', {})
#         device_info = {
#             'Name of the owner': device.get('name'),
#             'Enrollment_type': device.get('enrollment_method'),
#             'Model': device.get('model'),
#             'Make': device.get('make'),
#             'OS Type': device.get('os_type'),
#             'OS Version': device.get('os_version'),
#             'Battery Status': device.get('battery_status'),
#             'Battery temp': device.get('battery_temp_in_celsius'),
#             'RAM Usage': device.get('ram_usage'),
#             'Total RAM Size': device.get('total_ram_size'),
#         }
#     else:
#         device_info = {}
#     print("Device Info:", device_info)
# else:
#     print(f"Failed to fetch data from the API. Status code: {response.status_code}")

