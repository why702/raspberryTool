import sys
import os.path
from datetime import date
import argparse
import glob

from linebot import LineBotApi
from linebot.models import ImageSendMessage

line_bot_api = LineBotApi('kGtIfERt9Z0Ms9RJrw1y6+HDn4cSppu7vebBRv8m9RepJuy+a3LOAAxt1GCRzV4E/wFvq/oWE5b9gtyJ/lx8TwQEAaP3uL5UyrKcGPz9yA+tiV+HdjNjotiyWjQtcRzGYFQ54XCi5Y7v3BfAJ9v9AwdB04t89/1O/w1cDnyilFU=')

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

client_id = 'bd1be1c19619665'
client_secret = 'f8a92ea372383252971aaf35ad0b86fff5f98190'
access_token = 'c538cf5311ec8b3028694d308ca8907f1b945345'
refresh_token = '3b81c891048e4a1d4def4e7c0a60b357174f0594'

client = ImgurClient(client_id, client_secret, access_token, refresh_token)
# client.set_user_auth(access_token, refresh_token)

today = date.today()

def update_line(imgurl):
    line_bot_api.push_message('U485d701a822e415d69778f7e8bfe4c36',
                              ImageSendMessage(
                                  original_content_url=imgurl,
                                  preview_image_url=imgurl))

def update_imgur(imgPath):
    album = ''
    imgurl = ''
    try:
        config = {
            'album': album,
            'name': os.path.basename(imgPath),
            'title': str(today) + os.path.basename(imgPath),
            'description': 'upload AIY images'
        }
        if os.path.exists(imgPath) == True:
            image = client.upload_from_path(imgPath, config=config, anon=False)
            imgurl = 'https://i.imgur.com/{}.png'.format(image.get('id'))
    except ImgurClientError as e:
        print(e.error_message)
        print(e.status_code)

    return imgurl
  
def main(args):
    for imgPath in args.images:
        imgurl = update_imgur(imgPath)
        print(imgurl)
        update_line(imgurl)

    if os.path.exists(args.dir):
        for imgPath in glob.glob(os.path.join(args.dir, '*.jpg')):
            imgurl = update_imgur(imgPath)
            print(imgurl)
            update_line(imgurl)
        for imgPath in glob.glob(os.path.join(args.dir, '*.jpeg')):
            imgurl = update_imgur(imgPath)
            print(imgurl)
            update_line(imgurl)
        for imgPath in glob.glob(os.path.join(args.dir, '*.png')):
            imgurl = update_imgur(imgPath)
            print(imgurl)
            update_line(imgurl)
        for imgPath in glob.glob(os.path.join(args.dir, '*.bmp')):
            imgurl = update_imgur(imgPath)
            print(imgurl)
            update_line(imgurl)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--images', type=str, default='', nargs='+', help='Path(s) of the image(s)')
    parser.add_argument('--dir', type=str, default='', help='Get the models.')
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
