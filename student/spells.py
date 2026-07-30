import asyncio
from magic_stage import play_effect, say, add_button, fingers_now, set_background, set_behind, set_front, heard_word, run_loop

def setup():
    add_button("Rồng Lửa", "dragon")
    add_button("Phượng Hoàng", "phoenix")
    add_button("Hoa Anh Đào", "sakura")
    add_button("Mưa Giông", "rain")


def stage():
    set_background("rung")
    set_behind("rain")
    set_front("dragon")

    add_button("Rồng Lửa", "dragon")
    add_button("Phượng Hoàng", "phoenix")
    add_button("Hoa Anh Đào", "sakura")


def on_fingers(count):
    if count == 1:
        play_effect("dragon")
    elif count == 2:
        play_effect("phoenix")
    elif count == 3:
        play_effect("sakura")
    else:
        say("chưa gán phép cho số này")


def on_voice(word):
    fingers = fingers_now()
    if fingers == 1 and (word == "rồng" or word == "dragon"):
        play_effect("dragon")
    elif fingers == 2 and (word == "phượng" or word == "phoenix"):
        play_effect("phoenix")
    elif fingers == 3 and (word == "hoa" or word == "sakura"):
        play_effect("sakura")
    else:
        say("nghe " + word + " nhưng tay đang giơ " + str(fingers) + " ngón")


async def main_loop():
    while True:
        count = fingers_now()
        word = heard_word()
        if count == 1 and word in ("rồng", "dragon"):
            play_effect("dragon")
        elif count == 2 and word in ("phượng", "phoenix"):
            play_effect("phoenix")
        elif count == 3 and word in ("hoa", "sakura"):
            play_effect("sakura")
        await asyncio.sleep(0.15)

run_loop(main_loop)
