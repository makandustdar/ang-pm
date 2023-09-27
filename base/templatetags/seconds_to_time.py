from django import template

register = template.Library()


@register.simple_tag()
def time_or_none(time):
    # hours = float(raw_seconds // 3600)
    # minutes = float((raw_seconds % 3600) // 60)
    # seconds = float((raw_seconds % 3600) % 60)
    print(time)
    if time is None:
        return 0
    else:
        return time
    # hours_string = f"{f'{hours} ساعت ' if hours!=0 else ''}"
    # minutes_string = f"{f'{minutes} دقیقه ' if minutes!=0 else ''}"
    # seconds_string = f"{f'{seconds} ثانیه ' if seconds!=0 else ''}"
    # output = hours_string + minutes_string + seconds_string
    # if output == '':
    #     output = 'فعالیتی پیدا نشد'
    # return output


@register.simple_tag
def seconds_to_time(raw_seconds):
    hours = float(raw_seconds // 3600)
    minutes = float((raw_seconds % 3600) // 60)
    seconds = float((raw_seconds % 3600) % 60)
    hours_string = f"{f'{hours} ساعت ' if hours!=0 else ''}"
    minutes_string = f"{f'{minutes} دقیقه ' if minutes!=0 else ''}"
    seconds_string = f"{f'{seconds} ثانیه ' if seconds!=0 else ''}"
    output = hours_string + minutes_string + seconds_string
    if output == '':
        output = 'فعالیتی پیدا نشد'
    return output