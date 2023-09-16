#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = "8440502"
    API_HASH = "e77474ae3075f4000d3418c5a5a3a112"
    BOT_TOKEN = "5521953154:AAETsXLlh354SXv6gpHbR47Jjx97-wHoRk4"
    DEV = "1315975369 , 5480563272"
    OWNER = "1315975369"
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By TGVid-Comp (https://github.com/Zylern/TGVid-Comp)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = "https://graph.org/file/a0185fe78369f993a8e97.jpg"
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
