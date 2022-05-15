print("Not: Hocam teknofest'den dolayı tüm projelere vakitim kalmadı.")

elektrik= 500
doğalgaz= 300
su= 400
aidat= 125
internet= 150
print("Hey selam. Mayıs ayında ödediğin faturaları görmek ister misin?\nNot: Küçük harflerle yazınız.")
print(100*"*")
a= str(input("Hangi faturanızı görmek istersiniz: "))
if a=="elektrik":
  print("Bu ayın elektrik faturası:",elektrik)
if a=="doğalgaz":
  print("Bu ayın doğalgaz faturası:",doğalgaz)
if a=="su":
  print("Bu ayın su faturası:",su)
if a=="aidat":
  print("Bu ayın aidat faturası:",aidat)
if a=="internet":
  print("Bu ayın internet faturası:",internet)
else:
  print("Geçerli kelime gir (Yazımına dikkat et)")