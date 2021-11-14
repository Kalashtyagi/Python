import speedtest
speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = speed.upload()
print(f'The downlaod speed is {download_speed}')
print(f'The upload speed is {upload_speed}')