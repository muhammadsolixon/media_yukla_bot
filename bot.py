from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = "5818585876:AAFtvmYx3xt81fRdEqYzig2OvNAiOvgonws"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def salomlash(xabar: types.Message):
    # print(xabar.from_user.id)
    await xabar.reply(f"Assalomu alaykum, {xabar.from_user.full_name}")

@dp.message_handler(commands=['help'])
async def yordam(xabar: types.Message):
    await xabar.answer("/start - buyrug'ini bosish orqali botni qayta ishga tushurish mumkin !")


@dp.message_handler()
async def media_down(xabar: types.Message):
    soat = await xabar.answer("⏳")
    try:
        if xabar.text.startswith("https://www.instagram.com/"):
            url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
            querystring = {"url": xabar.text}
            headers = {
                "X-RapidAPI-Key": "2f124f417amsh403faa005a2f2fdp171256jsneace865cbe92",
                "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
            }

            video_data = requests.request("GET", url, headers=headers, params=querystring).json()
            await xabar.answer_video(video=video_data['media'], caption=video_data['title'])

        elif xabar.text.startswith("https://vm.tiktok.com/"):
            url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
            querystring = {"url": xabar.text}
            headers = {
              "X-RapidAPI-Key": "eb59523282msh7afe13a2ccc53fdp181e6djsn7c4d816b692c",
              "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring).json()

            video = response['video'][0]
            music = response['music'][0]
            description = response['description'][0]

            await xabar.answer_video(video=video, caption=description)
            await xabar.answer_audio(audio=music, caption=description)

    except:
        await xabar.answer("Bu linkdan video yuklab bo'lmaydi !")

    await soat.delete()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
