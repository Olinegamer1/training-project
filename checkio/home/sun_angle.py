from datetime import datetime
from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    time_pattern = "%H:%M"
    time = datetime.strptime(time, time_pattern)
    angel = ((time.hour - 6) * 60 + time.minute) * 0.25
    return angel if 0 <= angel <= 180 else "I don't see the sun!"


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")
